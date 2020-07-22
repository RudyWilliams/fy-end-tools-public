def test_n_obs(rfs_obj1):
    assert rfs_obj1.n_obs == 6


def test_full_rf_column_statistics_counts(rfs_obj1):
    columns = ["rf1", "rf2", "rf3", "rf4", "rf5", "rf6", "rf7", "rf8"]
    result = rfs_obj1.create_column_stats_df(columns=columns)
    assert result.loc["rf1", "count"] == 3
    assert result.loc["rf2", "count"] == 2
    assert result.loc["rf3", "count"] == 4
    assert result.loc["rf4", "count"] == 2
    assert result.loc["rf5", "count"] == 2
    assert result.loc["rf6", "count"] == 2
    assert result.loc["rf7", "count"] == 2
    assert result.loc["rf8", "count"] == 1


def test_full_rf_column_statistics_percents(rfs_obj1):
    columns = ["rf1", "rf2", "rf3", "rf4", "rf5", "rf6", "rf7", "rf8"]
    result = rfs_obj1.create_column_stats_df(columns=columns)
    assert result.loc["rf1", "percent"] == 3 / 6
    assert result.loc["rf2", "percent"] == 2 / 6
    assert result.loc["rf3", "percent"] == 4 / 6
    assert result.loc["rf4", "percent"] == 2 / 6
    assert result.loc["rf5", "percent"] == 2 / 6
    assert result.loc["rf6", "percent"] == 2 / 6
    assert result.loc["rf7", "percent"] == 2 / 6
    assert result.loc["rf8", "percent"] == 1 / 6


def test_type_column_statistics_counts(rfs_obj1):
    type_columns = ["type1", "type2", "type3", "type4"]
    result = rfs_obj1.create_column_stats_df(columns=type_columns)
    assert result.loc["type1", "count"] == 5
    assert result.loc["type2", "count"] == 5
    assert result.loc["type3", "count"] == 4
    assert result.loc["type4", "count"] == 3


def test_type_column_statistics_percents(rfs_obj1):
    type_columns = ["type1", "type2", "type3", "type4"]
    result = rfs_obj1.create_column_stats_df(columns=type_columns)
    assert result.loc["type1", "percent"] == 5 / 6
    assert result.loc["type2", "percent"] == 5 / 6
    assert result.loc["type3", "percent"] == 4 / 6
    assert result.loc["type4", "percent"] == 3 / 6


def test_n_domain_statistics_counts(rfs_obj1):
    type_columns = ["type1", "type2", "type3", "type4"]
    result = rfs_obj1.create_n_domain_stats_df(rf_type_columns=type_columns)
    assert result.loc[0, "count"] == 1
    assert result.loc[3, "count"] == 3
    assert result.loc[4, "count"] == 2
    # make sure no other n_domains
    assert set(result.index) == {0, 3, 4}


def test_n_domain_statistics_percents(rfs_obj1):
    type_columns = ["type1", "type2", "type3", "type4"]
    result = rfs_obj1.create_n_domain_stats_df(rf_type_columns=type_columns)
    assert result.loc[0, "percent"] == 1 / 6
    assert result.loc[3, "percent"] == 3 / 6
    assert result.loc[4, "percent"] == 2 / 6


def test_cumulative_distr_df(rfs_obj1):
    columns = ["rf1", "rf2", "rf3", "rf4", "rf5", "rf6", "rf7", "rf8"]
    result = rfs_obj1.create_cumulative_distr_df(rf_columns=columns)
    assert result.loc[0, "freq"] == 1
    assert result.loc[3, "freq"] == 2
    assert result.loc[4, "freq"] == 3

    # testing all in one function
    assert result.loc[0, "cumsum"] == 1
    assert result.loc[3, "cumsum"] == 3
    assert result.loc[4, "cumsum"] == 6

    # testing all in one function
    assert result.loc[0, "cumprop"] == 1 / 6
    assert result.loc[3, "cumprop"] == 3 / 6
    assert result.loc[4, "cumprop"] == 1
