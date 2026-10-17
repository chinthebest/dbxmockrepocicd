INSERT INTO {{catalog}}.{{schema}}.raw_customers VALUES
  (1, '  Alice Smith ', 'ALICE@Example.com', TIMESTAMP'2024-01-01 10:00:00'),
  (1, 'Alice Smith',    'alice@example.com', TIMESTAMP'2024-01-05 10:00:00'),
  (2, 'Bob Jones',      'Bob@Example.com',   TIMESTAMP'2024-01-02 09:00:00'),
  (NULL, 'Ghost',       'ghost@example.com', TIMESTAMP'2024-01-03 09:00:00');
