import pandas as pd

df = pd.read_csv("clean_data.csv")

def calculate_nutrition(weight, foods):
    required = {
        "protein": weight * 0.8,
        "carbs": weight * 3,
        "fat": weight * 0.8,
        "calories": weight * 30,
        "iron": 17
    }

    daily_total = {
        "protein": 0,
        "carbs": 0,
        "fat": 0,
        "calories": 0,
        "iron": 0
    }

    # ===== CALCULATE TOTAL =====
    for item in foods:
        food = item["name"]
        qty = item["qty"]/100

        food_clean = food.strip().lower()

        row = df[df["Dish Name"].str.lower().str.contains(food_clean, na=False)]

        if not row.empty:
           

           daily_total["protein"] += row["Protein (g)"].values[0] * qty
           daily_total["carbs"] += row["Carbohydrates (g)"].values[0] * qty
           daily_total["fat"] += row["Fats (g)"].values[0] * qty
           daily_total["calories"] += row["Calories (kcal)"].values[0] * qty
           daily_total["iron"] += row["Iron (mg)"].values[0] * qty

    # # ===== SUGGESTIONS =====
    # suggestions = {}

    # for nutrient in daily_total:
    #     deficit = required[nutrient] - daily_total[nutrient]

    #     if deficit > 0:
    #         sorted_df = df.sort_values(by={
    #             "protein": "Protein (g)",
    #             "carbs": "Carbohydrates (g)",
    #             "fat": "Fats (g)",
    #             "calories": "Calories (kcal)",
    #             "iron": "Iron (mg)"
    #         }[nutrient], ascending=False)

    #         recs = []
    #         for _, row in sorted_df.iterrows():
    #             if row[{
    #                 "protein": "Protein (g)",
    #                 "carbs": "Carbohydrates (g)",
    #                 "fat": "Fats (g)",
    #                 "calories": "Calories (kcal)",
    #                 "iron": "Iron (mg)"
    #             }[nutrient]] > 5:
    #                 recs.append(row["Dish Name"])
                
    #             if len(recs) == 2:
    #                 break

    #         suggestions[nutrient] = recs
    # ===== SUGGESTIONS =====
    suggestions = {}
    

    column_map = {
    "protein": "Protein (g)",
    "carbs": "Carbohydrates (g)",
    "fat": "Fats (g)"
    }

    for nutrient in ["protein", "carbs", "fat"]:
        deficit = required[nutrient] - daily_total[nutrient]

    if deficit > 0:
        col = column_map[nutrient]
        sorted_df = df.sort_values(by=col, ascending=False)

        recs = []
        for _, row in sorted_df.iterrows():
            if row[col] > (deficit * 0.1):
                recs.append(row["Dish Name"])

            if len(recs) == 2:
                break

        suggestions[nutrient] = recs

    return {
        "totals": daily_total,
        "required": required,
        "suggestions": suggestions
    }
