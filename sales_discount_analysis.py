import pandas as pd
import altair as alt


def sales_with_discount_analysis(df, filename="sales_discount_analysis.html"):
    """Анализ продаж с учетом и без учета скидок по категориям товаров."""
    sales_by_category = (
        df.groupby(["Category", "Discount"])["Sales"].sum().reset_index()
    )

    sales_by_category["SalesWithoutDiscount"] = sales_by_category.apply(
        lambda r: r["Sales"] if r["Discount"] == 0 else 0, axis=1
    )
    sales_by_category["SalesWithDiscount"] = sales_by_category.apply(
        lambda r: r["Sales"] if r["Discount"] > 0 else 0, axis=1
    )

    sales_summary = (
        sales_by_category.groupby("Category")[
            ["SalesWithDiscount", "SalesWithoutDiscount"]
        ]
        .sum()
        .reset_index()
    )

    sales_melted = pd.melt(
        sales_summary,
        id_vars="Category",
        value_vars=["SalesWithDiscount", "SalesWithoutDiscount"],
        var_name="Type",
        value_name="Sales",
    )

    chart = (
        alt.Chart(sales_melted)
        .mark_bar()
        .encode(
            x=alt.X("Category:N", title="Категория"),
            y=alt.Y("Sales:Q", title="Продажи"),
            color=alt.Color(
                "Type:N", title="Тип продаж", scale=alt.Scale(scheme="spectral")
            ),
        )
        .properties(width=600, height=400, title="Продажи по категориям товаров")
        .interactive()
    )

    chart.save(filename)
    print(f"График анализа продаж по скидкам сохранен в '{filename}'")
