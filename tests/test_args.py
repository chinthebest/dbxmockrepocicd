import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from common.args import build_parser  # noqa: E402


def test_entity_args():
    a = build_parser().parse_args(["--entity", "customer", "--catalog", "c", "--schema", "s"])
    assert a.entity == "customer" and a.catalog == "c" and a.schema == "s"


def test_restatement_args():
    a = build_parser(restatement=True).parse_args(
        ["--entity", "order", "--catalog", "c", "--schema", "s",
         "--start-date", "2024-01-01", "--end-date", "2024-01-31"]
    )
    assert a.start_date == "2024-01-01" and a.end_date == "2024-01-31"
