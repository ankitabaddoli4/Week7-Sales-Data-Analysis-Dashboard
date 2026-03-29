import os
import pandas as pd

print("🚀 Starting Sales Data Analysis...")

# ----------------------------
# Step 1: Ensure folders exist
# ----------------------------
os.makedirs('data/raw', exist_ok=True)
os.makedirs('data/processed', exist_ok=True)
os.makedirs('reports', exist_ok=True)

# ----------------------------
# Step 2: Ensure raw CSV exists
# ----------------------------
raw_file = 'data/raw/sales_data.csv'

if not os.path.exists(raw_file):
    print(f"⚠️  Raw file missing. Creating sample data at {raw_file}...")
    # New sample dataset
    data = {
        "order_id": list(range(101, 111)),
        "order_date": [
            "2024-01-08","2024-02-15","2024-02-20","2024-03-10","2024-04-05",
            "2024-05-22","2024-06-18","2024-07-12","2024-08-30","2024-09-25"
        ],
        "customer_id": ["CU01","CU02","CU03","CU01","CU04","CU02","CU05","CU06","CU03","CU07"],
        "product_id": ["PRD1","PRD2","PRD3","PRD4","PRD2","PRD5","PRD6","PRD7","PRD3","PRD8"],
        "category": ["Electronics","Clothing","Books","Electronics","Clothing","Home","Sports","Books","Books","Home"],
        "quantity": [1,2,1,3,2,1,4,2,1,3],
        "total_amount": [1200,400,150,3600,800,500,2000,300,150,900]
    }
    pd.DataFrame(data).to_csv(raw_file, index=False)
    print(f"✅ Sample data created at {raw_file}")

# ----------------------------
# Step 3: Load and clean data
# ----------------------------
df = pd.read_csv(raw_file)
df['order_date'] = pd.to_datetime(df['order_date'])
df = df.drop_duplicates()

# Save cleaned data
clean_file = 'data/processed/clean_sales_data.csv'
df.to_csv(clean_file, index=False)
print(f"✅ Cleaned data saved to {clean_file}")

# ----------------------------
# Step 4: Generate report stats
# ----------------------------
# Basic statistics
total_sales = df['total_amount'].sum()
total_orders = df.shape[0]
average_order = df['total_amount'].mean()
unique_customers = df['customer_id'].nunique()
unique_products = df['product_id'].nunique()

# Top categories
category_sales = df.groupby('category')['total_amount'].sum().sort_values(ascending=False)
top_categories = category_sales.head(5)

# Monthly trends
df['month'] = df['order_date'].dt.month
monthly_sales = df.groupby('month')['total_amount'].sum()
highest_month = monthly_sales.idxmax()
lowest_month = monthly_sales.idxmin()
avg_monthly = monthly_sales.mean()

# Repeat customers
customer_orders = df.groupby('customer_id')['order_id'].count()
repeat_customers = (customer_orders > 1).sum()
avg_customer_value = df.groupby('customer_id')['total_amount'].sum().mean()
top_customers_pct = df.groupby('customer_id')['total_amount'].sum().sort_values(ascending=False).head(int(0.1*len(customer_orders))+1).sum() / total_sales * 100

# ----------------------------
# Step 5: Print & save textual report
# ----------------------------
report_text = f"""
📊 SALES DATA ANALYSIS REPORT
===============================

📅 Analysis Period: Jan 2024 - Dec 2024

📈 BASIC STATISTICS:
- Total Sales: ${total_sales:,.2f}
- Total Orders: {total_orders}
- Average Order Value: ${average_order:,.2f}
- Unique Customers: {unique_customers}
- Unique Products: {unique_products}

🏆 TOP PRODUCT CATEGORIES:
"""
for i, (cat, amt) in enumerate(top_categories.items(), 1):
    pct = amt / total_sales * 100
    report_text += f"{i}. {cat}: ${amt:,.0f} ({pct:.1f}%)\n"

report_text += f"""
📅 MONTHLY TRENDS:
- Highest Sales Month: {highest_month} (${monthly_sales[highest_month]:,.0f})
- Lowest Sales Month: {lowest_month} (${monthly_sales[lowest_month]:,.0f})
- Average Monthly Sales: ${avg_monthly:,.2f}

👥 CUSTOMER INSIGHTS:
- Repeat Customers: {repeat_customers} ({repeat_customers/unique_customers*100:.1f}%)
- Average Customer Value: ${avg_customer_value:,.2f}
- Top 10% Customers Generate: {top_customers_pct:.1f}% of revenue

💰 RECOMMENDATIONS:
1. Focus marketing on top product categories
2. Improve customer retention programs
3. Consider seasonal promotions in high sales months
4. Expand product range in high-performing categories
"""

print(report_text)

# Save report as txt file
report_file = 'reports/sales_report.txt'
with open(report_file, 'w', encoding='utf-8') as f:
    f.write(report_text)

print(f"✅ Text report saved to {report_file}")
print("🎉 Analysis complete!")