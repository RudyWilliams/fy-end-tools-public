import argparse
from pathlib import Path
import pandas as pd

import fy_end_tools.cli.config as config


def _generate_riskfactor_plots(cfg, start, end, subset, program):

    from fy_end_tools.processing.fetch import MergeData
    from fy_end_tools.statistics.riskfactors import RiskFactorStatistics
    import fy_end_tools.plotting.riskfactors as plotrf

    try:
        prog_ids = cfg.PROG_NAME_ID_MAP[program] if program else None
    except KeyError:
        raise KeyError(f"Could not locate {program} in config->prog_name_id_map keys.")

    md = MergeData(
        log_fpath=cfg.LOG_FPATH, rf_fpath=cfg.RF_FPATH, progs_fpath=cfg.PROGS_FPATH
    )

    data_df = md.merge_data(
        log_rf_on=cfg.LOG_RF_ON_COLUMN,
        log_progs_on=cfg.LOG_PROGS_ON_COLUMN,
        start=start,
        end=end,
        intake_column=cfg.INTAKE_COLUMN,
        exit_column=cfg.EXIT_COLUMN,
        prog_id_column=cfg.PROG_ID_COLUMN,
        log_columns=cfg.LOG_COLUMNS,
        rf_columns=cfg.RF_COLUMNS,
        progs_columns=cfg.PROGS_COLUMNS,
        subset=subset,
        prog_ids=prog_ids,
    )

    rfs = RiskFactorStatistics(df=data_df)
    bar_data = rfs.create_column_stats_df(columns=cfg.RF_TYPE_COLUMNS)
    stacked_bar_data = rfs.create_n_domain_stats_df(rf_type_columns=cfg.RF_TYPE_COLUMNS)
    distr_data = rfs.create_cumulative_distr_df(rf_columns=cfg.FACTOR_COLUMNS)

    bar_plot = plotrf.make_column_stats_bar_plot(data=bar_data)
    stacked_bar_plots = plotrf.make_n_domain_stacked_bar_plot(data=stacked_bar_data)
    distr_plot = plotrf.make_distr_plot(data=distr_data)
    cum_distr_plot = plotrf.make_cumulative_distr_plot(data=distr_data)

    subplot = plotrf.organize_all_plots(
        bar_plot=bar_plot,
        stacked_bar_plots=stacked_bar_plots,
        distr_plot=distr_plot,
        cum_distr_plot=cum_distr_plot,
    )
    subplot.update_layout(
        title={
            "text": f"Risk Factor Analysis :: Program:{program} :: Subset:{subset}",
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
        }
    )
    return subplot


def run_cli():
    parser = argparse.ArgumentParser(
        description="Fetch & merge data. Calculate and plot statistics."
    )

    accepted_analysis = {"riskfactor"}
    accepted_subset = {"served", "intake", "exit"}

    parser.add_argument("start", type=lambda x: pd.Timestamp(x))
    parser.add_argument("end", type=lambda x: pd.Timestamp(x))
    parser.add_argument(
        "analysis", type=str, help=f"Must be one of {accepted_analysis}"
    )
    parser.add_argument("subset", type=str, help=f"Must be one of {accepted_subset}")
    parser.add_argument(
        "--program",
        type=str,
        default=None,
        help="Specify a program to subset further. Can be any key from prog_name_id_map in configuration. The default is None s.t. no further subset by program will be performed.",
    )
    parser.add_argument(
        "--save",
        type=str,
        default=None,
        help="Specify a path to save resulting plot at (e.g. results/plots/).",
    )
    parser.add_argument(
        "--testing",
        action="store_true",
        help="When flagged, use test dir/data to run cli",
    )
    args = parser.parse_args()

    start = args.start
    end = args.end
    analysis = args.analysis
    subset = args.subset
    program = args.program
    save = args.save
    testing = args.testing

    if analysis not in accepted_analysis:
        raise ValueError(f"analysis arg must be one of {accepted_analysis}")
    if subset not in accepted_subset:
        raise ValueError(f"subset arg must be one of {accepted_subset}")

    # use config based on platform (production or testing)
    if testing:
        cfg = config.TestingConfig
    else:
        cfg = config.Config

    if analysis == "riskfactor":
        rf_subplots = _generate_riskfactor_plots(
            cfg=cfg, start=start, end=end, subset=subset, program=program
        )
        rf_subplots.show()
        if save:
            rf_subplots.write_html(save)

