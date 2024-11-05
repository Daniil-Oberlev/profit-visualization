import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def units_in_stock_visualization(data):
    """Визуализация количества единиц на складе по странам"""

    stock_by_country = data.groupby("Country")["UnitsInStock"].sum().reset_index()

    top_10_countries = stock_by_country.nlargest(10, "UnitsInStock")

    plt.figure(figsize=(10, 6))
    sns.barplot(
        x="Country", y="UnitsInStock", data=top_10_countries, palette="coolwarm"
    )
    plt.title("Топ-10 стран по количеству товаров на складе")
    plt.xlabel("Страна")
    plt.ylabel("Количество на складе")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
