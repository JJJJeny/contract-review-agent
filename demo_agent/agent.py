"""ADK web demo for the contract-review agent.

All agent code lives in a notebook: 07_agent_v2_and_scoring.ipynb by default (set
DEMO_NOTEBOOK=02_agent_adk.ipynb for the earlier version). This file runs its Part A code cells
(sections 1-14, without the cells that call the API), then wraps one review in a
root_agent so `adk web` shows the input, every tool call the verifier makes, and the
final findings with their quotes, revision plan and human-review list.

    cd contract-review-agent
    export OPENAI_API_KEY=...        # the Portkey key; DEMO_FAKE=1 runs the scripted fake model instead
    adk web .                        # open http://127.0.0.1:8000, pick demo_agent, type "C05 termination"
"""
import asyncio, json, os, re, sys
from pathlib import Path

from google.adk.agents import BaseAgent
from google.adk.events import Event
from google.genai import types

REPO = Path(os.environ.get("REPO_DIR", Path(__file__).resolve().parents[1]))


FAKE = bool(os.environ.get("DEMO_FAKE"))


NOTEBOOK = os.environ.get("DEMO_NOTEBOOK", "07_agent_v2_and_scoring.ipynb")


def _run_notebook():
    nb = json.loads((REPO / NOTEBOOK).read_text())
    g = {"__name__": "agent_notebook", "IN_COLAB": False, "DATA_DIR": REPO, "os": os, "sys": sys, "Path": Path,
         "EMBEDDER": None}
    on = False
    for i, cell in enumerate(nb["cells"]):
        src = "".join(cell["source"])
        if cell["cell_type"] == "markdown":
            on = on or src.startswith("## 1. Model")
            if src.startswith("## 16.") or src.startswith("# Part B"):
                break
        elif on and not re.search(r"^\S.*\bawait\b", src, re.M):   # skip cells that run the agent
            if FAKE and "make_embedder()" in src:
                continue                                              # no key needed for the fake model
            exec(compile(src, f"<{NOTEBOOK} cell {i}>", "exec"), g)
    if FAKE and "FakeAdkLlm" not in g:                                # the scripted fake model lives in 02
        for cell in json.loads((REPO / "02_agent_adk.ipynb").read_text())["cells"]:
            if cell["cell_type"] == "code" and "class FakeAdkLlm" in "".join(cell["source"]):
                exec(compile("".join(cell["source"]), "<02_agent_adk.ipynb FakeAdkLlm>", "exec"), g)
    return g


NB = _run_notebook()
MODEL = NB["FakeAdkLlm"]() if FAKE else NB["ADK_MODEL"]
EMBEDDER = NB["EMBEDDER"]


def say(ctx, text, author="contract_reviewer"):
    return Event(invocation_id=ctx.invocation_id, author=author,
                 content=types.Content(role="model", parts=[types.Part(text=text)]))


def report(cid, r, only):
    lines = [f"## {cid}: findings", "", "| family | verdict | severity | how decided | evidence |", "|---|---|---|---|---|"]
    for fam, f in r["results"].items():
        how = f["path"] if f.get("path") in ("prepass", "rag") else f"loop, {f.get('steps', 0)} steps"
        if str(f.get("path", "")).startswith("forced"):
            how = f["path"]
        quote = (f.get("evidence_text") or "none found")[:160].replace("|", "/")
        mark = "**" if fam in only else ""
        lines.append(f"| {mark}{fam}{mark} | {f.get('verdict')} | {f.get('severity')} | {how} | {f.get('section_ref', '')} \"{quote}\" |")
    lines += ["", "## Revision plan (most important first)"]
    lines += [f"{p['id']}. **{p['family']}** ({p['severity']}): {p.get('ask') or p.get('notes', '')}"
              + (f"  \n   if they refuse: {p['fallback']}" if p.get("fallback") else "") for p in r["plan"]] or ["nothing to change"]
    lines += ["", "## For human review"]
    lines += [f"- {q['family']}: {q['question']}" for q in r["human_queue"]] or ["- nothing queued"]
    s = r["summary"]
    lines += ["", f"_{s['llm_calls']} model calls, {s['tool_calls']} tool calls, ${s['cost_usd']}, {s['elapsed_s']} s_"]
    return "\n".join(lines)


class ContractReviewer(BaseAgent):
    async def _run_async_impl(self, ctx):
        text = "".join(p.text or "" for p in (ctx.user_content.parts if ctx.user_content else []))
        m = re.search(r"\bC\s?(\d{1,2})\b", text, re.I)
        if not m or not (REPO / "data" / "contracts" / f"C{int(m.group(1)):02d}.txt").exists():
            yield say(ctx, "Type a contract id from C01 to C15, optionally with a clause family, e.g. `C05 termination`.")
            return
        cid = f"C{int(m.group(1)):02d}"
        only = [f for f in NB["FAMILIES"] if f.split("_")[0] in text.lower()] or NB["FAMILIES"]
        meta = NB["load_meta"]()[cid]
        yield say(ctx, f"Reviewing **{cid} {meta['short_name']}** ({meta['split']} set). Pre-pass over all six "
                       f"families, then the follow-up loop for the families whose triggers fire. Showing the steps for: "
                       f"{', '.join(only)}.")
        queue, shown = asyncio.Queue(), None
        NB["EVENT_SINK"] = lambda fam, ev: queue.put_nowait((fam, ev))
        contract = NB["Contract"].load(REPO / "data" / "contracts" / f"{cid}.txt", meta)
        task = asyncio.create_task(NB["review_contract"](contract, MODEL, EMBEDDER, "adaptive"))
        try:
            while not (task.done() and queue.empty()):
                try:
                    fam, ev = await asyncio.wait_for(queue.get(), 0.5)
                except asyncio.TimeoutError:
                    continue
                if ev.author != "clause_verifier" or fam not in only or not (ev.content and ev.content.parts):
                    continue
                if all(p.text == "stopped" for p in ev.content.parts):     # placeholder reply after a forced stop
                    continue
                if fam != shown:
                    shown = fam
                    yield say(ctx, f"**{fam}**: triggers fired, checking further")
                yield Event(invocation_id=ctx.invocation_id, author=self.name, content=ev.content)
            r = task.result()
        finally:
            NB["EVENT_SINK"] = None
        yield say(ctx, report(cid, r, only))


# the sub-agents are listed only so the web UI can draw the graph; each review builds its own copies
root_agent = ContractReviewer(name="contract_reviewer",
                              description="Reviews a vendor service agreement against our rubric.",
                              sub_agents=list(NB["make_agents"](MODEL)[:3]))
