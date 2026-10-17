from transforms.cleaning import clean_orders


def run(spark, catalog, schema, start_date=None, end_date=None):
    raw = spark.table(f"{catalog}.{schema}.raw_orders")
    target = f"{catalog}.{schema}.curated_orders"

    if start_date and end_date:
        # Restatement: replace only the requested date range
        spark.sql(
            f"DELETE FROM {target} WHERE order_date BETWEEN '{start_date}' AND '{end_date}'"
        )
        df = clean_orders(raw.filter(f"order_date BETWEEN '{start_date}' AND '{end_date}'"))
        df.write.mode("append").saveAsTable(target)
    else:
        clean_orders(raw).write.mode("overwrite").saveAsTable(target)
