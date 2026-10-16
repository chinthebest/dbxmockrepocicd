CREATE TABLE IF NOT EXISTS {{catalog}}.{{schema}}.raw_orders (
  order_id    BIGINT,
  customer_id BIGINT,
  amount      DECIMAL(10,2),
  order_date  DATE
);
