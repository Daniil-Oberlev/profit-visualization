import warnings
from data_loading import load_dataset
from profit_analysis import profit_analysis_by_customer
from units_in_stock_analysis import units_in_stock_visualization
from sales_discount_analysis import sales_with_discount_analysis
from profit_per_unit_analysis import profit_per_unit_analysis

warnings.filterwarnings("ignore")


def run_analysis():
    """Запуск анализа данных из набора данных Excel"""
    file_path = "dataset.xlsx"
    df = load_dataset(file_path)

    if df is None:
        print("Ошибка: Невозможно загрузить набор данных. Проверьте наличие файла.")
        return
    elif df.empty:
        print("Ошибка: Набор данных пуст. Проверьте содержимое файла.")
        return

    analyses = [
        ("Анализ прибыли по клиентам...", profit_analysis_by_customer),
        (
            "Анализ количества единиц на складе по странам...",
            units_in_stock_visualization,
        ),
        (
            "Анализ продаж с учетом скидок по категориям товаров...",
            sales_with_discount_analysis,
        ),
        ("Анализ удельной прибыли на единицу товара...", profit_per_unit_analysis),
    ]

    for description, analysis_func in analyses:
        print(f"Запуск {description}")
        analysis_func(df)


if __name__ == "__main__":
    run_analysis()
