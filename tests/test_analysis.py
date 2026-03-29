import pandas as pd
from sales_analyzer.analyzer import SalesAnalyzer

def test_basic_stats():
    data = {
        'total_amount': [100, 200, 300],
        'customer_id': [1, 2, 3],
        'product_id': ['A', 'B', 'C']
    }

    df = pd.DataFrame(data)
    analyzer = SalesAnalyzer(df)

    stats = analyzer.basic_stats()

    assert stats["Total Sales"] == 600
    assert stats["Total Orders"] == 3