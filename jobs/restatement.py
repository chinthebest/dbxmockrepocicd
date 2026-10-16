"""Entry point: reprocess an entity for a date range (restatement)."""
import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from pyspark.sql import SparkSession  # noqa: E402

from common.args import build_parser  # noqa: E402
from common.logger import get_logger  # noqa: E402
from entities import ENTITIES  # noqa: E402

log = get_logger("restatement")


def main():
    args = build_parser(restatement=True).parse_args()
    if args.entity not in ENTITIES:
        raise ValueError(f"Unknown entity '{args.entity}'. Valid: {sorted(ENTITIES)}")

    spark = SparkSession.builder.getOrCreate()
    log.info("Restating entity=%s from %s to %s", args.entity, args.start_date, args.end_date)
    ENTITIES[args.entity](
        spark, args.catalog, args.schema,
        start_date=args.start_date, end_date=args.end_date,
    )
    log.info("Restatement complete")


if __name__ == "__main__":
    main()
