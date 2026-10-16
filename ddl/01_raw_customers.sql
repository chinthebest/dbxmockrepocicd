CREATE TABLE IF NOT EXISTS {{catalog}}.{{schema}}.raw_customers (
  customer_id   BIGINT,
  customer_name STRING,
  email         STRING,
  updated_at    TIMESTAMP
);
