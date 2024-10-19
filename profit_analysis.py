import pandas as pd
import matplotlib.pyplot as plt
import hvplot.pandas
import warnings

warnings.filterwarnings("ignore")


def profit_analysis_by_customer(data):
    """Анализ прибыли по клиентам и категориям"""

    # Проверка на пустой DataFrame
    if data.empty:
        print("Данные пустые. Невозможно выполнить анализ.")
        return

    # Группировка данных по клиентам и сортировка по прибыли
    profit_by_customer = (
        data.groupby("Customer")["Profit"].sum().sort_values(ascending=False).head(10)
    )

    # Визуализация топ-10 клиентов с наибольшей прибылью
    plt.figure(figsize=(10, 6))
    profit_by_customer.plot(kind="bar", color="skyblue")
    plt.title("Топ-10 клиентов по прибыли")
    plt.xlabel("Клиент")
    plt.ylabel("Прибыль")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Группировка данных по клиентам и категориям товаров
    customer_category_group = (
        data.groupby(["Customer", "Category"])[["Profit", "Sales"]].sum().reset_index()
    )

    # Интерактивная визуализация: топ-10 клиентов и их заказы по категориям товаров
    top_10_customers = customer_category_group[
        customer_category_group["Customer"].isin(profit_by_customer.index)
    ]

    # Проверка, есть ли данные для визуализации
    if top_10_customers.empty:
        print("Нет данных для топ-10 клиентов по категориям.")
        return

    # Создание интерактивной визуализации
    plot = top_10_customers.hvplot.bar(
        x="Customer",
        y="Profit",
        by="Category",
        title="Прибыль по категориям для топ-10 клиентов",
        xlabel="Клиент",
        ylabel="Прибыль",
        stacked=True,
    )

    # Отображение интерактивного графика
    hvplot.show(plot)  # Здесь нужно использовать hvplot.show
