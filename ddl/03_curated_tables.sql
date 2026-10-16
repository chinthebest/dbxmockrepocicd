CREATE TABLE IF NOT EXISTS {{catalog}}.{{schema}}.curated_customers (
  customer_id   BIGINT,
  customer_name STRING,
  email         STRING,
  updated_at    TIMESTAMP
);

CREATE TABLE IF NOT EXISTS {{catalog}}.{{schema}}.curated_orders (
  order_id    BIGINT,
  customer_id BIGINT,
  amount      DECIMAL(10,2),
  order_date  DATE
);
