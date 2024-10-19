import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def profit_per_unit_analysis(data):
    """Анализ удельной прибыли на единицу товара по категориям"""

    # Проверка на пустой DataFrame
    if data.empty:
        print("Данные пустые. Невозможно выполнить анализ.")
        return

    # Добавляем новую колонку с расчетом удельной прибыли на единицу проданного товара
    data["ProfitPerUnit"] = data["Profit"] / np.where(
        data["Sales"] > 0, data["Sales"], 1
    )

    # Группировка данных по категориям товаров
    profit_per_unit_by_category = (
        data.groupby("Category")["ProfitPerUnit"].mean().reset_index()
    )

    # Визуализация средних значений удельной прибыли по категориям
    plt.figure(figsize=(10, 6))
    sns.barplot(
        x="Category",
        y="ProfitPerUnit",
        data=profit_per_unit_by_category,
        palette="viridis",
    )
    plt.title("Средняя удельная прибыль на единицу товара по категориям")
    plt.xlabel("Категория")
    plt.ylabel("Удельная прибыль на единицу товара")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Дополнительно: Визуализация распределения удельной прибыли по товарам
    plt.figure(figsize=(10, 6))
    sns.histplot(data["ProfitPerUnit"], bins=20, kde=True, color="purple")
    plt.title("Распределение удельной прибыли на единицу товара")
    plt.xlabel("Удельная прибыль на единицу товара")
    plt.ylabel("Частота")
    plt.tight_layout()
    plt.show()
