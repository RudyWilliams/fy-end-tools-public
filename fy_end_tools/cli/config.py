from pathlib import Path
import yaml


class Config:

    with open("fy_end_tools/config.yml", "r") as f:
        CONFIG = yaml.safe_load(f)

    DIR_PATH = Path(CONFIG["dirs"]["csv_files"])
    LOG = CONFIG["files"]["log"]["name"]
    RF = CONFIG["files"]["riskfactors"]["name"]
    PROGS = CONFIG["files"]["progs"]["name"]

    LOG_FPATH = DIR_PATH / LOG
    RF_FPATH = DIR_PATH / RF
    PROGS_FPATH = DIR_PATH / PROGS

    INTAKE_COLUMN = CONFIG["files"]["log"]["intake_column"]
    EXIT_COLUMN = CONFIG["files"]["log"]["exit_column"]
    PROG_ID_COLUMN = CONFIG["files"]["log"]["prog_id_column"]
    LOG_RF_ON_COLUMN = CONFIG["merge-on"]["log_rf"]
    LOG_PROGS_ON_COLUMN = CONFIG["merge-on"]["log_progs"]

    LOG_COLUMNS = (
        [INTAKE_COLUMN, EXIT_COLUMN] + [LOG_RF_ON_COLUMN] + [LOG_PROGS_ON_COLUMN]
    )

    FACTOR_COLUMNS = CONFIG["files"]["riskfactors"]["factor_columns"]
    RF_TYPE_COLUMNS = CONFIG["files"]["riskfactors"]["rf_type_columns"]

    RF_COLUMNS = FACTOR_COLUMNS + RF_TYPE_COLUMNS + [LOG_RF_ON_COLUMN]
    PROGS_COLUMNS = CONFIG["files"]["progs"]["addn_columns"] + [LOG_PROGS_ON_COLUMN]

    PROG_NAME_ID_MAP = CONFIG["prog_name_id_map"]


class TestingConfig:

    with open("tests/config.yml", "r") as f:
        CONFIG = yaml.safe_load(f)

    DIR_PATH = Path(CONFIG["dirs"]["csv_files"])
    LOG = CONFIG["files"]["log"]["name"]
    RF = CONFIG["files"]["riskfactors"]["name"]
    PROGS = CONFIG["files"]["progs"]["name"]

    LOG_FPATH = DIR_PATH / LOG
    RF_FPATH = DIR_PATH / RF
    PROGS_FPATH = DIR_PATH / PROGS

    INTAKE_COLUMN = CONFIG["files"]["log"]["intake_column"]
    EXIT_COLUMN = CONFIG["files"]["log"]["exit_column"]
    PROG_ID_COLUMN = CONFIG["files"]["log"]["prog_id_column"]
    LOG_RF_ON_COLUMN = CONFIG["merge-on"]["log_rf"]
    LOG_PROGS_ON_COLUMN = CONFIG["merge-on"]["log_progs"]

    LOG_COLUMNS = (
        [INTAKE_COLUMN, EXIT_COLUMN] + [LOG_RF_ON_COLUMN] + [LOG_PROGS_ON_COLUMN]
    )

    FACTOR_COLUMNS = CONFIG["files"]["riskfactors"]["factor_columns"]
    RF_TYPE_COLUMNS = CONFIG["files"]["riskfactors"]["rf_type_columns"]

    RF_COLUMNS = FACTOR_COLUMNS + RF_TYPE_COLUMNS + [LOG_RF_ON_COLUMN]
    PROGS_COLUMNS = CONFIG["files"]["progs"]["addn_columns"] + [LOG_PROGS_ON_COLUMN]

    PROG_NAME_ID_MAP = CONFIG["prog_name_id_map"]
