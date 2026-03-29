import pandas as pd

class SalesAnalyzer:
    """
    Perform sales data analysis
    """

    def __init__(self, df):
        self.df = df

    def basic_stats(self):
        """
        Calculate basic statistics
        """
        stats = {
            "Total Sales": self.df['total_amount'].sum(),
            "Average Order Value": self.df['total_amount'].mean(),
            "Total Orders": len(self.df),
            "Unique Customers": self.df['customer_id'].nunique(),
            "Unique Products": self.df['product_id'].nunique()
        }
        return stats

    def sales_by_category(self):
        """
        Sales grouped by category
        """
        return (
            self.df.groupby('category')['total_amount']
            .sum()
            .sort_values(ascending=False)
        )

    def monthly_trend(self):
        """
        Monthly sales trend
        """
        if 'order_date' not in self.df.columns:
            return pd.Series()

        self.df['month'] = self.df['order_date'].dt.to_period('M')

        return self.df.groupby('month')['total_amount'].sum()

    def top_products(self, n=5):
        """
        Top N products by sales
        """
        return (
            self.df.groupby('product_id')['total_amount']
            .sum()
            .sort_values(ascending=False)
            .head(n)
        )

    def average_order_value(self):
        """
        Average order value
        """
        return self.df['total_amount'].mean()

    def peak_sales_day(self):
        """
        Find peak sales day
        """
        daily_sales = self.df.groupby('order_date')['total_amount'].sum()
        return daily_sales.idxmax(), daily_sales.max()