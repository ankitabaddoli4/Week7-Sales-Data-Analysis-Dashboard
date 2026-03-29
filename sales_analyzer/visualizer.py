import matplotlib.pyplot as plt
import os

def plot_monthly_trend(monthly_data, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    plt.figure()
    monthly_data.plot(kind='line', marker='o')
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.grid()

    file_path = os.path.join(output_dir, "monthly_trend.png")
    plt.savefig(file_path)
    plt.close()

    print(f"📈 Saved: {file_path}")


def plot_category_sales(category_data, output_dir):
    plt.figure()
    category_data.plot(kind='bar')
    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Sales")

    file_path = os.path.join(output_dir, "category_sales.png")
    plt.savefig(file_path)
    plt.close()

    print(f"📊 Saved: {file_path}")


def plot_order_distribution(df, output_dir):
    plt.figure()
    plt.hist(df['total_amount'], bins=20)
    plt.title("Order Value Distribution")
    plt.xlabel("Order Value")
    plt.ylabel("Frequency")

    file_path = os.path.join(output_dir, "order_distribution.png")
    plt.savefig(file_path)
    plt.close()

    print(f"📉 Saved: {file_path}")