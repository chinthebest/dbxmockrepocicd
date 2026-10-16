"""Entry point: run the ETL pipeline for one entity."""
import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from pyspark.sql import SparkSession  # noqa: E402

from common.args import build_parser  # noqa: E402
from common.logger import get_logger  # noqa: E402
from entities import ENTITIES  # noqa: E402

log = get_logger("run_entity")


def main():
    args = build_parser().parse_args()
    if args.entity not in ENTITIES:
        raise ValueError(f"Unknown entity '{args.entity}'. Valid: {sorted(ENTITIES)}")

    spark = SparkSession.builder.getOrCreate()
    log.info("Running entity=%s into %s.%s", args.entity, args.catalog, args.schema)
    ENTITIES[args.entity](spark, args.catalog, args.schema)
    log.info("Done entity=%s", args.entity)


if __name__ == "__main__":
    main()
