import sys
from pathlib import Path

import pytest

pytest.importorskip("pyspark")
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from pyspark.sql import SparkSession  # noqa: E402

from transforms.cleaning import clean_orders  # noqa: E402


@pytest.fixture(scope="module")
def spark():
    return SparkSession.builder.master("local[1]").appName("tests").getOrCreate()


def test_clean_orders_drops_negative_and_duplicates(spark):
    df = spark.createDataFrame(
        [(1, 10.0), (1, 10.0), (2, -1.0)], ["order_id", "amount"]
    )
    out = clean_orders(df).collect()
    assert [r.order_id for r in out] == [1]
