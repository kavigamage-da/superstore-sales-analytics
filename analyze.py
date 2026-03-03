import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Settings
sns.set_theme(style="darkgrid")
df = pd.read_csv("superstore_clean.csv")
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Year'] = df['Order_Date'].dt.year
df['Month'] = df['Order_Date'].dt.to_period('M')

# Create output folder
os.makedirs("charts", exist_ok=True)

# ── KPIs ──────────────────────────────────────────
total_revenue = df['Sales'].sum()
total_profit  = df['Profit'].sum()
total_orders  = df['Order_ID'].nunique()
avg_order_val = df.groupby('Order_ID')['Sales'].sum().mean()
profit_margin = (total_profit / total_revenue) * 100

print("=" * 40)
print("        KPI SUMMARY")
print("=" * 40)
print(f"Total Revenue    : ${total_revenue:,.2f}")
print(f"Total Profit     : ${total_profit:,.2f}")
print(f"Profit Margin    : {profit_margin:.1f}%")
print(f"Total Orders     : {total_orders:,}")
print(f"Avg Order Value  : ${avg_order_val:,.2f}")
print("=" * 40)

# ── Chart 1: Sales by Category ────────────────────
cat = df.groupby('Category')['Sales'].sum().sort_values()
plt.figure(figsize=(8,5))
cat.plot(kind='barh', color=['#4C72B0','#DD8452','#55A868'])
plt.title('Total Sales by Category')
plt.xlabel('Sales ($)')
plt.tight_layout()
plt.savefig('charts/1_sales_by_category.png')
plt.close()
print("Chart 1 saved.")

# ── Chart 2: Monthly Revenue Trend ───────────────
monthly = df.groupby('Month')['Sales'].sum()
monthly.index = monthly.index.astype(str)
plt.figure(figsize=(12,5))
plt.plot(monthly.index, monthly.values, marker='o', color='#4C72B0')
plt.xticks(rotation=45, ha='right', fontsize=7)
plt.title('Monthly Revenue Trend')
plt.ylabel('Sales ($)')
plt.tight_layout()
plt.savefig('charts/2_monthly_trend.png')
plt.close()
print("Chart 2 saved.")

# ── Chart 3: Profit by Category ──────────────────
prof = df.groupby('Category')['Profit'].sum().sort_values()
colors = ['#d9534f' if v < 0 else '#5cb85c' for v in prof.values]
plt.figure(figsize=(8,5))
prof.plot(kind='barh', color=colors)
plt.title('Total Profit by Category')
plt.xlabel('Profit ($)')
plt.tight_layout()
plt.savefig('charts/3_profit_by_category.png')
plt.close()
print("Chart 3 saved.")

# ── Chart 4: Top 10 Sub-Categories by Sales ──────
sub = df.groupby('Sub_Category')['Sales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=sub.values, y=sub.index, palette='Blues_r')
plt.title('Top 10 Sub-Categories by Sales')
plt.xlabel('Sales ($)')
plt.tight_layout()
plt.savefig('charts/4_top_subcategories.png')
plt.close()
print("Chart 4 saved.")

# ── Chart 5: Sales by Region ──────────────────────
reg = df.groupby('Region')['Sales'].sum()
plt.figure(figsize=(7,7))
plt.pie(reg.values, labels=reg.index, autopct='%1.1f%%', startangle=140)
plt.title('Sales Distribution by Region')
plt.tight_layout()
plt.savefig('charts/5_sales_by_region.png')
plt.close()
print("Chart 5 saved.")

print("\n✅ All charts saved in /charts folder!")