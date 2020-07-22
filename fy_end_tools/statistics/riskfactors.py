import pandas as pd


class RiskFactorStatistics:
    """
    Holds functionality for calculating statistics 
    from a riskfactor dataframe
    """

    def __init__(self, df):
        self.df = df

    @property
    def n_obs(self):
        return len(self.df)

    def _calculate_column_sums(self, columns):
        _df = self.df[columns].copy()
        return _df.sum(axis=0)

    def create_column_stats_df(self, columns):
        """
        Calculate count and percent stats by summing columns.
        Useful at the lower level by setting columns to all riskfactor
        columns or at a higher level by setting columns to the type
        indicator columns.
        """
        sums = self._calculate_column_sums(columns=columns)
        percents = sums / self.n_obs
        stat_df = pd.concat([sums, percents], axis=1)
        stat_df.columns = ["count", "percent"]
        return stat_df

    def create_n_domain_stats_df(self, rf_type_columns):
        types_df = self.df.loc[:, rf_type_columns].copy()
        types_df["n_domains"] = types_df.sum(axis=1)
        types_df["count"] = 1
        domain_counts = types_df.groupby("n_domains")["count"].count()
        domain_percents = domain_counts / self.n_obs
        stat_df = pd.concat([domain_counts, domain_percents], axis=1)
        stat_df.columns = ["count", "percent"]
        return stat_df

    def create_cumulative_distr_df(self, rf_columns):
        rf_df = self.df[rf_columns].copy()
        rf_df["n_client_rf"] = rf_df.sum(axis=1)
        rf_df["freq"] = 1
        n_rf_groupby = rf_df[["n_client_rf", "freq"]].groupby("n_client_rf").count()
        n_rf_groupby["cumsum"] = n_rf_groupby["freq"].cumsum()
        n_rf_groupby["cumprop"] = n_rf_groupby["cumsum"] / self.n_obs
        return n_rf_groupby
