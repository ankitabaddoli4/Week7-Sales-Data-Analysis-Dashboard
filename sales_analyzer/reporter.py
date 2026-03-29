import pandas as pd

def generate_excel_report(stats, category_data, monthly_data, output_file):
    """
    Generate Excel report with multiple sheets
    """
    try:
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:

            # Summary
            pd.DataFrame([stats]).to_excel(
                writer, sheet_name='Summary', index=False
            )

            # Category Analysis
            category_data.to_excel(
                writer, sheet_name='Category Analysis'
            )

            # Monthly Trends
            monthly_data.to_excel(
                writer, sheet_name='Monthly Trends'
            )

        print(f"📄 Report Generated: {output_file}")

    except Exception as e:
        print(f"❌ Error generating report: {e}")


def generate_text_report(stats):
    """
    Print summary report in console
    """
    print("\n📊 SALES REPORT")
    print("=" * 30)

    for key, value in stats.items():
        print(f"{key}: {value}")