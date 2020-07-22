import pandas as pd


def test_merge_log_rf_served(mergedata_obj1, merge_truth1_served):
    """
    test the internal method works as planed:
    trim to served/intake/exit and merge log with rf
    """
    md = mergedata_obj1
    md._merge_log_rf(
        on=["iid"],
        start=pd.Timestamp("7/1/2019"),
        end=pd.Timestamp("7/31/2019"),
        intake_column="intake",
        exit_column="exit",
        prog_id_column=None,
        log_columns=["intake", "exit", "iid", "pid"],
        rf_columns=["iid", "rf1", "rf2", "rf3", "rf4", "type1", "type2"],
        subset="served",
        prog_ids=None,
    )
    # have to trim column of truth
    truth = merge_truth1_served.drop(columns="pname")
    check = md._merged_log_rf_df.loc[
        :, truth.columns
    ]  # need to have columns in same order
    assert check.equals(truth)


def test_merge_log_rf_intake(mergedata_obj1, merge_truth1_intake):
    """
    test the internal method works as planed:
    trim to served/intake/exit and merge log with rf
    """
    md = mergedata_obj1
    md._merge_log_rf(
        on=["iid"],
        start=pd.Timestamp("7/1/2019"),
        end=pd.Timestamp("7/31/2019"),
        intake_column="intake",
        exit_column="exit",
        prog_id_column=None,
        log_columns=["intake", "exit", "iid", "pid"],
        rf_columns=["iid", "rf1", "rf2", "rf3", "rf4", "type1", "type2"],
        subset="intake",
        prog_ids=None,
    )
    # have to trim column of truth
    truth = merge_truth1_intake.drop(columns="pname")
    check = md._merged_log_rf_df.loc[
        :, truth.columns
    ]  # need to have columns in same order
    assert check.equals(truth)


def test_merge_log_rf_exit(mergedata_obj1, merge_truth1_exit):
    """
    test the internal method works as planed:
    trim to served/intake/exit and merge log with rf
    """
    md = mergedata_obj1
    md._merge_log_rf(
        on=["iid"],
        start=pd.Timestamp("7/1/2019"),
        end=pd.Timestamp("7/31/2019"),
        intake_column="intake",
        exit_column="exit",
        prog_id_column=None,
        log_columns=["intake", "exit", "iid", "pid"],
        rf_columns=["iid", "rf1", "rf2", "rf3", "rf4", "type1", "type2"],
        subset="exit",
        prog_ids=None,
    )
    # have to trim column of truth
    truth = merge_truth1_exit.drop(columns="pname")
    check = md._merged_log_rf_df.loc[
        :, truth.columns
    ]  # need to have columns in same order
    assert check.equals(truth)


def test_merge_all_served(mergedata_obj1, merge_truth1_served):
    md = mergedata_obj1
    check = md.merge_data(
        log_rf_on=["iid"],
        log_progs_on=["pid"],
        start=pd.Timestamp("7/1/2019"),
        end=pd.Timestamp("7/31/2019"),
        intake_column="intake",
        exit_column="exit",
        prog_id_column=None,
        log_columns=["iid", "pid", "intake", "exit"],
        rf_columns=["iid", "rf1", "rf2", "rf3", "rf4", "type1", "type2"],
        progs_columns=["pid", "pname"],
        subset="served",
        prog_ids=None,
    ).sort_values(by=["intake"], ascending=True, ignore_index=True)
    truth = merge_truth1_served.sort_values(
        by=["intake"], ascending=True, ignore_index=True
    )
    assert check.equals(truth)


def test_merge_all_intake(mergedata_obj1, merge_truth1_intake):
    md = mergedata_obj1
    check = md.merge_data(
        log_rf_on=["iid"],
        log_progs_on=["pid"],
        start=pd.Timestamp("7/1/2019"),
        end=pd.Timestamp("7/31/2019"),
        intake_column="intake",
        exit_column="exit",
        prog_id_column=None,
        log_columns=["iid", "pid", "intake", "exit"],
        rf_columns=["iid", "rf1", "rf2", "rf3", "rf4", "type1", "type2"],
        progs_columns=["pid", "pname"],
        subset="intake",
        prog_ids=None,
    ).sort_values(by=["intake"], ascending=True, ignore_index=True)
    truth = merge_truth1_intake.sort_values(
        by=["intake"], ascending=True, ignore_index=True
    )
    assert check.equals(truth)


def test_merge_all_exit(mergedata_obj1, merge_truth1_exit):
    md = mergedata_obj1
    check = md.merge_data(
        log_rf_on=["iid"],
        log_progs_on=["pid"],
        start=pd.Timestamp("7/1/2019"),
        end=pd.Timestamp("7/31/2019"),
        intake_column="intake",
        exit_column="exit",
        prog_id_column=None,
        log_columns=["iid", "pid", "intake", "exit"],
        rf_columns=["iid", "rf1", "rf2", "rf3", "rf4", "type1", "type2"],
        progs_columns=["pid", "pname"],
        subset="exit",
        prog_ids=None,
    ).sort_values(by=["intake"], ascending=True, ignore_index=True)
    truth = merge_truth1_exit.sort_values(
        by=["intake"], ascending=True, ignore_index=True
    )
    assert check.equals(truth)


def test_merge_all_served_prog1_only(mergedata_obj1, merge_truth1_served_prog1_only):
    md = mergedata_obj1
    check = md.merge_data(
        log_rf_on=["iid"],
        log_progs_on=["pid"],
        start=pd.Timestamp("7/1/2019"),
        end=pd.Timestamp("7/31/2019"),
        intake_column="intake",
        exit_column="exit",
        prog_id_column="pid",
        log_columns=["iid", "pid", "intake", "exit"],
        rf_columns=["iid", "rf1", "rf2", "rf3", "rf4", "type1", "type2"],
        progs_columns=["pid", "pname"],
        subset="served",
        prog_ids=[1],
    ).sort_values(by=["intake"], ascending=True, ignore_index=True)
    truth = merge_truth1_served_prog1_only.sort_values(
        by=["intake"], ascending=True, ignore_index=True
    )
    assert check.equals(truth)


def test_merge_all_intake_prog1_and_prog3_only(
    mergedata_obj1, merge_truth1_intake_prog1_and_prog3_only
):
    md = mergedata_obj1
    check = md.merge_data(
        log_rf_on=["iid"],
        log_progs_on=["pid"],
        start=pd.Timestamp("7/1/2019"),
        end=pd.Timestamp("7/31/2019"),
        intake_column="intake",
        exit_column="exit",
        prog_id_column="pid",
        log_columns=["iid", "pid", "intake", "exit"],
        rf_columns=["iid", "rf1", "rf2", "rf3", "rf4", "type1", "type2"],
        progs_columns=["pid", "pname"],
        subset="intake",
        prog_ids=[1, 3],
    ).sort_values(by=["intake"], ascending=True, ignore_index=True)
    truth = merge_truth1_intake_prog1_and_prog3_only.sort_values(
        by=["intake"], ascending=True, ignore_index=True
    )
    assert check.equals(truth)
