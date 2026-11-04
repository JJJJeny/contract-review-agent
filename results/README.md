# Results

Executed runs and score files, grouped by split. Notebooks stay at the repo root so Colab paths keep working.

| Folder | What is inside |
|---|---|
| `dev/` | Dev split (C01, C02, C11, C12): executed notebooks `05_dev_run`, `06_baseline_devrun`, `07_dev_run`, and `results_dev_v2.zip` (07 runs + scores). |
| `test/` | Test split (the other 11 contracts): executed `07_test_run`, `06_baseline_testrun`, `results_test_v2.zip` (07 runs + scores), and `baseline_scores_test.zip` (RAG baseline runs + scores). |

Final test numbers (66 rows): RAG baseline accuracy 0.50, single pass 0.59, agent loop 0.70.
