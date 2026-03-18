import pandas as pd
import plotly.express as px

def user_growth_chart(df_users):

    df_users["created_at"] = pd.to_datetime(df_users["created_at"])
    df_users["month"] = df_users["created_at"].dt.to_period("M").astype(str)

    df = (
        df_users
        .groupby("month")
        .agg(new_users=("id", "nunique"))
        .reset_index()
    )

    fig = px.line(
        df,
        x="month",
        y="new_users",
        # title="User Growth"
    )

    fig.update_layout(
        xaxis_title=None,
        yaxis_title=None,
    )
    return fig

def funnel_chart(df):

    fig = px.funnel(
        df,
        x="users",
        y="stage",
        # title="Conversion Funnel"
    )

    fig.update_layout(
        xaxis_title=None,
        yaxis_title=None,
    )
    return fig

def activation_chart(df):

    fig = px.line(
        df,
        x="month",
        y="activation_rate",
        # title="Activation Rate Over Time",
        markers=True 
    )

    fig.update_traces(
        text=df["activation_rate"],
        texttemplate="%{text:.1%}",
        textposition="top center"
    )

    fig.update_layout(
        yaxis_tickformat=".0%",
        xaxis_title=None,
        yaxis_title=None
    )

    return fig
    return fig