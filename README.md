# Pricing Probelm (or) Analysis


This project is of data analysis over the Python - Based Pricing Analysis.


## Files

- `products.csv` – Contains product details like SKU, current price, cost price, and available stock. (Dataset)
- `sales.csv` – Holds the recent sales data with quantity sold per SKU. (Dataset)
- `THRD.py` – Python code to process input files, performing logic for final updated prices.
- `updated_prices.csv` – Output file with the final calculated prices.

---

## Pricing

Product is evaluated based on **priority order** as:

### 1 – Low Stock, High Demand
- **Problem**: `stock < 20` **&** `quantity_sold > 30`
- **Solution**: Increase price by **15%**

### 2 – Dead Stock
- **Problem**: `stock > 200` **&** `quantity_sold == 0`
- **Solution**: Decrease price by **30%**

### 3 – Overstocked Inventory
- **Problem**: `stock > 100` **&** `quantity_sold < 20`
- **Solution**: Decrease price by **10%**

### 4 – Minimum Profit
- **Problem**: If new price < `cost_price * 1.2`
- **Solution**: Set price to `cost_price * 1.2`

## Output

The output file `updated_prices.csv` contains the final output.

---

## How to Run
1. Make sure the `Pandas` library to be installed.
2. python THRD.py
