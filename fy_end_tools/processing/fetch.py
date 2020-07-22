import pandas as pd


class MergeData:
    def __init__(self, log_fpath, rf_fpath, progs_fpath):
        self.log_fpath = log_fpath
        self.rf_fpath = rf_fpath
        self.progs_fpath = progs_fpath

    def _merge_log_rf(
        self,
        on,
        start,
        end,
        intake_column,
        exit_column,
        prog_id_column,
        log_columns,
        rf_columns,
        subset,
        prog_ids,
    ):
        subset_dict = {
            "served": self._trim_log_served,
            "intake": self._trim_log_intake,
            "exit": self._trim_log_exit,
        }
        trim_method = subset_dict[subset]

        parse_dates = [intake_column, exit_column]
        log_df = pd.read_csv(
            self.log_fpath, usecols=log_columns, parse_dates=parse_dates
        )
        trim_log_df = trim_method(
            log_df=log_df,
            start=start,
            end=end,
            intake_column=intake_column,
            exit_column=exit_column,
            prog_id_column=prog_id_column,
            prog_ids=prog_ids,
        )
        rf_df = pd.read_csv(self.rf_fpath, usecols=rf_columns)

        self._merged_log_rf_df = trim_log_df.merge(rf_df, on=on, how="inner")

        return self

    def merge_data(
        self,
        log_rf_on,
        log_progs_on,
        start,
        end,
        intake_column,
        exit_column,
        prog_id_column,
        log_columns,
        rf_columns,
        progs_columns,
        subset,
        prog_ids,
    ):
        self._merge_log_rf(
            on=log_rf_on,
            start=start,
            end=end,
            intake_column=intake_column,
            exit_column=exit_column,
            prog_id_column=prog_id_column,
            log_columns=log_columns,
            rf_columns=rf_columns,
            subset=subset,
            prog_ids=prog_ids,
        )
        intermed_merged_df = self._merged_log_rf_df
        progs_df = pd.read_csv(self.progs_fpath, usecols=progs_columns)

        final_merged_df = intermed_merged_df.merge(
            progs_df, on=log_progs_on, how="inner"
        )

        return final_merged_df

    @staticmethod
    def _trim_log_served(
        log_df, start, end, intake_column, exit_column, prog_id_column, prog_ids
    ):
        copy_df = log_df.copy()

        date_columns = [intake_column, exit_column]
        for c in date_columns:
            copy_df[c] = copy_df[c].dt.floor("D")

        is_intake_lte_end = copy_df[intake_column] <= end
        is_exit_gte_start = copy_df[exit_column] >= start
        is_open = copy_df[exit_column].isna()

        if prog_ids:  # if not None or []
            # perform extra subsetting
            is_prog_id = copy_df[prog_id_column].isin(prog_ids)
            trim_df = copy_df.loc[
                is_prog_id & is_intake_lte_end & (is_exit_gte_start | is_open), :
            ].copy()
        else:
            trim_df = copy_df.loc[
                is_intake_lte_end & (is_exit_gte_start | is_open), :
            ].copy()

        return trim_df

    @staticmethod
    def _trim_log_intake(
        log_df, start, end, intake_column, exit_column, prog_id_column, prog_ids
    ):
        """exit column for consistency and not actually"""
        copy_df = log_df.copy()

        copy_df[intake_column] = copy_df[intake_column].dt.floor("D")

        is_intake_lte_end = copy_df[intake_column] <= end
        is_intake_gte_start = copy_df[intake_column] >= start

        if prog_ids:  # if not None or []
            # perform extra subsetting
            is_prog_id = copy_df[prog_id_column].isin(prog_ids)
            trim_df = copy_df.loc[
                is_prog_id & is_intake_lte_end & is_intake_gte_start, :
            ].copy()
        else:
            trim_df = copy_df.loc[is_intake_lte_end & is_intake_gte_start, :].copy()

        return trim_df

    @staticmethod
    def _trim_log_exit(
        log_df, start, end, intake_column, exit_column, prog_id_column, prog_ids
    ):
        copy_df = log_df.copy()

        copy_df[exit_column] = copy_df[exit_column].dt.floor("D")

        is_exit_lte_end = copy_df[exit_column] <= end
        is_exit_gte_start = copy_df[exit_column] >= start

        if prog_ids:  # if not None or []
            # perform extra subsetting
            is_prog_id = copy_df[prog_id_column].isin(prog_ids)
            trim_df = copy_df.loc[
                is_prog_id & is_exit_lte_end & is_exit_gte_start, :
            ].copy()
        else:
            trim_df = copy_df.loc[is_exit_lte_end & is_exit_gte_start, :].copy()

        return trim_df
