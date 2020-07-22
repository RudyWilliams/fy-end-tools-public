import pandas as pd
import pytest

from fy_end_tools.processing.fetch import MergeData
from fy_end_tools.statistics.riskfactors import RiskFactorStatistics


@pytest.fixture
def rfs_obj1():
    df = pd.read_csv("tests/test-data/riskfactor_1.csv")
    rfs = RiskFactorStatistics(df=df)
    return rfs


@pytest.fixture
def mergedata_obj1():
    md_obj = MergeData(
        log_fpath="tests/test-data/merges/l1.csv",
        rf_fpath="tests/test-data/merges/rf1.csv",
        progs_fpath="tests/test-data/merges/p1.csv",
    )
    return md_obj


@pytest.fixture
def merge_truth1_served():
    truth = pd.read_csv(
        "tests/test-data/merges/truth1-served.csv", parse_dates=["intake", "exit"]
    )
    return truth


@pytest.fixture
def merge_truth1_intake():
    truth = pd.read_csv(
        "tests/test-data/merges/truth1-intake.csv", parse_dates=["intake", "exit"]
    )
    return truth


@pytest.fixture
def merge_truth1_exit():
    truth = pd.read_csv(
        "tests/test-data/merges/truth1-exit.csv", parse_dates=["intake", "exit"]
    )
    return truth


@pytest.fixture
def merge_truth1_served_prog1_only():
    truth = pd.read_csv(
        "tests/test-data/merges/truth1-served-prog1.csv", parse_dates=["intake", "exit"]
    )
    return truth


@pytest.fixture
def merge_truth1_intake_prog1_and_prog3_only():
    truth = pd.read_csv(
        "tests/test-data/merges/truth1-intake-prog1prog3.csv",
        parse_dates=["intake", "exit"],
    )
    return truth
