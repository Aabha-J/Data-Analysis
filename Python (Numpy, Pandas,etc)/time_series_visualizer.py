import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import numpy as np

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col = "date")

# Clean data
df = df[
    (df["value"] >= df["value"].quantile(0.025)) &
    (df["value"] <= df["value"].quantile(0.975))
]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df.index, df["value"], label="Page View")

    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.set_title("Daily Page Views on FreeCodeCamp Forum")
    ax.grid(True)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    # Draw bar plot
    df_bar["Year"] = df_bar.index.year
    df_bar["Month"] = df_bar.index.strftime("%B")

    df_bar = df_bar.groupby(["Year", "Month"])["value"].mean().unstack()

    fig, ax = plt.subplots(figsize=(10, 6))
    df_bar.plot(kind="bar", ax=ax)
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.set_title("Average Daily Page Views on FreeCodeCamp Forum (Monthly)")
    ax.legend(title="Months")


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = [d.year for d in df_box.date]
    df_box['Month'] = [d.strftime('%b') for d in df_box.date]
    df_box["value"] = df_box["value"].astype(float)
    print(df_box)
    


    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    sns.boxplot(x="Year", y="value", data=df_box, ax=axes[0])
    sns.boxplot(x="Month", y="value", data=df_box, ax=axes[1])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[0].set_xlabel("Year")
    axes[1].set_xlabel("Month")
    axes[0].set_ylabel("Page Views")
    axes[1].set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
