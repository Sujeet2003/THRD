import pandas as pd

# Load the uploaded CSV files
products_df = pd.read_csv("products.csv")
sales_df = pd.read_csv("sales.csv")

# Merge dataframes
merged_df = pd.merge(products_df, sales_df, on='sku', how='left')
merged_df['quantity_sold'] = merged_df['quantity_sold'].fillna(0)



def apply_pricing_rules(row):
    current_price = row['current_price']
    cost_price = row['cost_price']
    stock = row['stock']
    quantity_sold = row['quantity_sold']
    new_price = current_price

    if stock < 20 and quantity_sold > 30:
        new_price = current_price * 1.15
    elif stock > 200 and quantity_sold == 0:
        new_price = current_price * 0.7
    elif stock > 100 and quantity_sold < 20:
        new_price = current_price * 0.9

    min_price = cost_price * 1.2
    if new_price < min_price:
        new_price = min_price

    return round(new_price, 2)

merged_df['new_price'] = merged_df.apply(apply_pricing_rules, axis=1)


output_df = merged_df[["sku", "current_price", "new_price"]].copy()
output_df.rename(columns={"current_price": "old_price"}, inplace=True)
output_df["old_price"] = output_df["old_price"].map(lambda x: f"{x:.2f} USD")
output_df["new_price"] = output_df["new_price"].map(lambda x: f"{x:.2f} USD")

# Save to CSV
output_df.to_csv("updated_prices.csv", index=False)

