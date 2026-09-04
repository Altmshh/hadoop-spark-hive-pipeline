#!/bin/bash
# Wells Fargo - Daily MySQL Bronze Ingestion

sqoop import \
  --connect jdbc:mysql://mysql-server:3306/banking_db \
  --username admin \
  --password-file /user/hadoop/pwd.file \
  --table customers \
  --target-dir /warehouse/bronze/mysql/customers \
  --incremental append \
  --check-column customer_id \
  --last-value 10500 \
  --as-parquetfile \
  -m 4