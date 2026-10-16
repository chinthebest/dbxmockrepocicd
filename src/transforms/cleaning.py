from pyspark.sql import DataFrame, Window
from pyspark.sql import functions as F


def clean_customers(df: DataFrame) -> DataFrame:
    """Trim names, lower-case emails, drop null ids, keep latest row per customer."""
    w = Window.partitionBy("customer_id").orderBy(F.col("updated_at").desc())
    return (
        df.filter(F.col("customer_id").isNotNull())
        .withColumn("customer_name", F.trim("customer_name"))
        .withColumn("email", F.lower(F.trim("email")))
        .withColumn("_rn", F.row_number().over(w))
        .filter("_rn = 1")
        .drop("_rn")
    )


def clean_orders(df: DataFrame) -> DataFrame:
    """Drop non-positive amounts and duplicate order ids."""
    return df.filter(F.col("amount") > 0).dropDuplicates(["order_id"])
