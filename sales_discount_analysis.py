import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def sales_with_discount_analysis(data):
    """Анализ продаж с учетом скидок по категориям товаров"""

    # Проверка на пустой DataFrame
    if data.empty:
        print("Данные пустые. Невозможно выполнить анализ.")
        return

    # Группировка данных по категориям товаров
    sales_by_category = (
        data.groupby("Category")[["Sales", "Discount"]].sum().reset_index()
    )

    # Проверка на корректные значения скидок (меньше 1.0 и больше или равно 0)
    sales_by_category["SalesWithDiscount"] = sales_by_category.apply(
        lambda row: (
            row["Sales"] * (1 - row["Discount"])
            if 0 <= row["Discount"] < 1
            else row["Sales"]
        ),
        axis=1,
    )

    # Визуализация продаж без учета скидок
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Category", y="Sales", data=sales_by_category, palette="coolwarm")
    plt.title("Продажи по категориям товаров (без учета скидок)")
    plt.xlabel("Категория")
    plt.ylabel("Продажи")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Визуализация продаж с учетом скидок
    plt.figure(figsize=(10, 6))
    sns.barplot(
        x="Category", y="SalesWithDiscount", data=sales_by_category, palette="coolwarm"
    )
    plt.title("Продажи по категориям товаров (с учетом скидок)")
    plt.xlabel("Категория")
    plt.ylabel("Продажи со скидками")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
