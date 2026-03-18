import pandas as pd

def calculate_kpis(users, events, transactions):

    total_users = users["id"].nunique()

    signup_completed = events[events["event_name"] == "signup_completed"]["user_id"].nunique()

    activated_users = transactions["account_id"].nunique()

    activation_rate = activated_users / signup_completed if signup_completed else 0

    transactions["revenue"] = transactions["amount"] * 0.01
    total_revenue = transactions["revenue"].sum()

    return {
        "total_users": total_users,
        "signup_completed": signup_completed,
        "activated_users": activated_users,
        "activation_rate": activation_rate,
        "total_revenue": total_revenue
    }
def get_funnel_data(events, transactions):

    app_open = events[events["event_name"] == "app_open"]["user_id"].nunique()

    signup_started = events[events["event_name"] == "signup_started"]["user_id"].nunique()

    signup_completed = events[events["event_name"] == "signup_completed"]["user_id"].nunique()

    activated = transactions["account_id"].nunique()

    return {
        "App Open": app_open,
        "Signup Started": signup_started,
        "Signup Completed": signup_completed,
        "Activated": activated
    }
def activation_trend(events, transactions, accounts):

    import pandas as pd

    # =========================
    # SIGNUP
    # =========================
    signup = events[events["event_name"] == "signup_completed"].copy()
    signup["created_at"] = pd.to_datetime(signup["created_at"])
    signup["month"] = signup["created_at"].dt.to_period("M")

    signup = signup[["user_id", "month"]]

    # =========================
    # USERS QUE ATIVARAM (DISTINCT)
    # =========================
    activated_accounts = transactions["account_id"].dropna().unique()

    acc = accounts[["id", "user_id"]]

    activated_users = acc[acc["id"].isin(activated_accounts)]["user_id"].unique()

    # =========================
    # MARCAR ATIVAÇÃO
    # =========================
    signup["activated"] = signup["user_id"].isin(activated_users)

    # =========================
    # AGREGAR
    # =========================
    result = signup.groupby("month").agg(
        signup_completed=("user_id", "nunique"),
        activated=("activated", "sum")
    ).reset_index()

    # =========================
    # TAXA
    # =========================
    result["activation_rate"] = result["activated"] / result["signup_completed"]

    result["month"] = result["month"].astype(str)

    return result