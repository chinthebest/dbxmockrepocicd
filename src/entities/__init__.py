from entities import customer, order

# entity name -> run(spark, catalog, schema, start_date=None, end_date=None)
ENTITIES = {
    "customer": customer.run,
    "order": order.run,
}
