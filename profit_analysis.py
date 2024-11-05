import pandas as pd
import matplotlib.pyplot as plt
import hvplot.pandas
import warnings

warnings.filterwarnings("ignore")


def profit_analysis_by_customer(data):
    """Анализ прибыли по клиентам и категориям"""
    profit_by_customer = (
        data.groupby("Customer")["Profit"].sum().sort_values(ascending=False).head(10)
    )

    plt.figure(figsize=(10, 6))
    profit_by_customer.plot(kind="bar", color="skyblue")
    plt.title("Топ-10 клиентов по прибыли")
    plt.xlabel("Клиент")
    plt.ylabel("Прибыль")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    customer_category_group = (
        data.groupby(["Customer", "Category"])[["Profit", "Sales"]].sum().reset_index()
    )

    top_10_customers = customer_category_group[
        customer_category_group["Customer"].isin(profit_by_customer.index)
    ]

    if top_10_customers.empty:
        print("Нет данных для топ-10 клиентов по категориям.")
        return

    plot = top_10_customers.hvplot.bar(
        x="Customer",
        y="Profit",
        by="Category",
        title="Прибыль по категориям для топ-10 клиентов",
        xlabel="Клиент",
        ylabel="Прибыль",
        stacked=True,
    )

    hvplot.show(plot)
