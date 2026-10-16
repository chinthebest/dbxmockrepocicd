from transforms.cleaning import clean_customers


def run(spark, catalog, schema, start_date=None, end_date=None):
    raw = spark.table(f"{catalog}.{schema}.raw_customers")
    clean_customers(raw).write.mode("overwrite").saveAsTable(
        f"{catalog}.{schema}.curated_customers"
    )
