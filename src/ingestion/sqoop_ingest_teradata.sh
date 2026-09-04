#!/bin/bash
# Wells Fargo - Daily Teradata Bronze Ingestion

sqoop import \
  --connect jdbc:teradata://teradata-server/banking_warehouse \
  --username dba \
  --password secret \
  --table daily_gl_ledger \
  --target-dir /warehouse/bronze/teradata/gl_ledger \
  --incremental append \
  --check-column load_date \
  --last-value '2026-04-01' \
  --as-parquetfile \
  -m 6