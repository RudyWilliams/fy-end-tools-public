import plotly.graph_objects as go
from plotly.subplots import make_subplots


def make_cumulative_distr_plot(data):
    """
    Data comes from the statistics module so we know what
    columns to extract.
    """
    x = data.index
    y = data["cumprop"]
    plot = go.Bar(x=x, y=y, showlegend=False)

    return plot


def make_distr_plot(data):

    x = data.index
    y = data["freq"]
    plot = go.Bar(x=x, y=y, showlegend=False)

    return plot


def make_n_domain_stacked_bar_plot(data):

    x = [""]
    data_rows = [*data.itertuples()]
    plots = [
        go.Bar(name=f"# Domains: {r.Index}", x=x, y=[r.percent]) for r in data_rows
    ]
    return plots


def make_column_stats_bar_plot(data):

    x = data.index
    y = data["percent"]
    plot = go.Bar(x=x, y=y, showlegend=False)

    return plot


def organize_all_plots(bar_plot, stacked_bar_plots, distr_plot, cum_distr_plot):
    subplot_fig = make_subplots(
        rows=2,
        cols=2,
        shared_xaxes=False,
        shared_yaxes=False,
        subplot_titles=(
            "Proportion with Risk Factor Domain",
            "Proportion with Number of Risk Factor Domains Present",
            "Number of Risk Factors Distribution",
            "Number of Risk Factors Cumulative Distribution",
        ),
    )
    subplot_fig.add_trace(bar_plot, row=1, col=1)
    for p in stacked_bar_plots:
        subplot_fig.add_trace(p, row=1, col=2)
    subplot_fig.add_trace(distr_plot, row=2, col=1)
    subplot_fig.add_trace(cum_distr_plot, row=2, col=2)

    subplot_fig.update_layout(barmode="stack",)

    # update axes per plot
    subplot_fig.update_xaxes(title="Risk Factor Domain", row=1, col=1)
    subplot_fig.update_yaxes(title="Proportion of Youth", row=1, col=1)
    subplot_fig.update_yaxes(title="Proportion of Youth", row=1, col=2)
    subplot_fig.update_xaxes(title="Number of Risk Factors", row=2, col=1)
    subplot_fig.update_yaxes(title="Number of Youth", row=2, col=1)
    subplot_fig.update_xaxes(title="Number of Risk Factors", row=2, col=2)
    subplot_fig.update_yaxes(title="Proportion At or Below X", row=2, col=2)

    return subplot_fig
