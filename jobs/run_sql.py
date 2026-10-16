"""Run every .sql file in a folder (ddl or seed), in filename order.

SQL files may use {{catalog}} and {{schema}} placeholders.
"""
import argparse
import pathlib

from pyspark.sql import SparkSession


def split_statements(text: str):
    return [s.strip() for s in text.split(";") if s.strip()]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", required=True, choices=["ddl", "seed"])
    parser.add_argument("--catalog", required=True)
    parser.add_argument("--schema", required=True)
    args = parser.parse_args()

    spark = SparkSession.builder.getOrCreate()
    root = pathlib.Path(__file__).resolve().parents[1]

    files = sorted((root / args.folder).glob("*.sql"))
    if not files:
        raise FileNotFoundError(f"No .sql files found in {root / args.folder}")

    for f in files:
        text = (
            f.read_text()
            .replace("{{catalog}}", args.catalog)
            .replace("{{schema}}", args.schema)
        )
        for stmt in split_statements(text):
            print(f"[{f.name}] {stmt.splitlines()[0][:80]} ...")
            spark.sql(stmt)


if __name__ == "__main__":
    main()
