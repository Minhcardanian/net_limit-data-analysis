import pandas as pd

# Load CSV data
csv_path = '../data/NCL_Models.csv'
csv_df = pd.read_csv(csv_path)

# Clean CSV data: Remove commas and convert columns to numeric
numeric_columns = ['Treasury Balance', 'Amt to Treasury Reserve', 'Amt From Treasury',
                   'Cardano Locked', 'Cardano Floating', 'Emission', 'transactions', 'usage', 'px']
for column in numeric_columns:
    csv_df[column] = pd.to_numeric(csv_df[column].astype(str).str.replace(',', '').str.replace('#VALUE!', '0'), errors='coerce')

# Filter data for 2025 and 2026
csv_2025_2026 = csv_df[csv_df['Year'].isin([2025, 2026])]
print("CSV Data for 2025-2026:")
print(csv_2025_2026.head())

# Load Excel data with multiple sheets
excel_path = '../data/NCL_Models.xlsx'
xls = pd.ExcelFile(excel_path)
hissim_df = pd.read_excel(xls, sheet_name='HisSim data model')
variables_df = pd.read_excel(xls, sheet_name='Variables')
yearly_projection_df = pd.read_excel(xls, sheet_name='Yearly projection')
basic_model_df = pd.read_excel(xls, sheet_name='Basic model start vs end')

# Print a preview of each sheet
print("\nHisSim Data Model Preview:")
print(hissim_df.head())
print("\nVariables Preview:")
print(variables_df.head())
print("\nYearly Projection Preview:")
print(yearly_projection_df.head())
print("\nBasic Model Start vs End Preview:")
print(basic_model_df.head())
