import argparse


def build_parser(restatement: bool = False) -> argparse.ArgumentParser:
    p = argparse.ArgumentParser()
    p.add_argument("--entity", required=True)
    p.add_argument("--catalog", required=True)
    p.add_argument("--schema", required=True)
    if restatement:
        p.add_argument("--start-date", required=True, help="YYYY-MM-DD")
        p.add_argument("--end-date", required=True, help="YYYY-MM-DD")
    return p
