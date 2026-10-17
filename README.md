# dab-poc

Mock repo showing PySpark deployment to Databricks (AWS) using Databricks Asset Bundles (DABs) and GitHub Actions.

## Layout
| Path | Purpose | Deployed? |
|---|---|---|
| `databricks.yml` | Bundle definition and targets | n/a |
| `resources/jobs.yml` | Job definitions (serverless, cluster variant commented) | n/a |
| `jobs/` | Entry points: `run_sql.py`, `run_entity.py`, `restatement.py` | yes |
| `src/` | ETL code (`common`, `transforms`, `entities`) | yes |
| `ddl/`, `seed/` | `.sql` files with `{{catalog}}` / `{{schema}}` placeholders | yes |
| `requirements-cluster.txt` | Third-party libs for compute | yes |
| `tests/`, `app/`, `deploy.py` | Tests, docs, legacy script | no |

## Local quick start
```bash
databricks auth login --host <workspace-url>
databricks bundle validate -t dev
databricks bundle deploy -t dev
databricks bundle run setup_serverless -t dev      # DDL then seed
databricks bundle run entity_serverless -t dev     # customer then order
databricks bundle run restatement_serverless -t dev
```

## GitHub secrets (Settings > Secrets and variables > Actions)
`DATABRICKS_HOST`, `DATABRICKS_CLIENT_ID`, `DATABRICKS_CLIENT_SECRET`

## Workflows
- `ci.yml`: PR checks (lint, tests, bundle validate)
- `cd.yml`: deploy to dev on push to `main` / `poc-dab`
- `run-job.yml`: manually trigger a job from GitHub

## Before you run
Replace the host, catalog and schema in `databricks.yml`.
