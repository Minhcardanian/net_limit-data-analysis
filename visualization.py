import pandas as pd
import matplotlib.pyplot as plt

# Load Excel data (Yearly Projection sheet)
excel_path = '../data/NCL_Models.xlsx'
xls = pd.ExcelFile(excel_path)
yearly_projection_df = pd.read_excel(xls, sheet_name='Yearly projection')

# Rename and clean columns (assuming the first row is header information)
yearly_projection_df.columns = ['Year', 'Emission', 'Amt From Treasury', 'Amt to Treasury Reserve', 'Avg Cardano Floating']
yearly_projection_df = yearly_projection_df.drop(0).reset_index(drop=True)
yearly_projection_df[['Year', 'Emission', 'Amt From Treasury', 'Amt to Treasury Reserve', 'Avg Cardano Floating']] = \
    yearly_projection_df[['Year', 'Emission', 'Amt From Treasury', 'Amt to Treasury Reserve', 'Avg Cardano Floating']].apply(pd.to_numeric, errors='coerce')

# Visualization: Create subplots for each key metric
fig, ax = plt.subplots(2, 2, figsize=(15, 10))

# Emission Trend
ax[0, 0].bar(yearly_projection_df['Year'], yearly_projection_df['Emission'], color='skyblue')
ax[0, 0].set_title('Annual Emission')
ax[0, 0].set_xlabel('Year')
ax[0, 0].set_ylabel('Emission')

# Amt From Treasury
ax[0, 1].bar(yearly_projection_df['Year'], yearly_projection_df['Amt From Treasury'], color='salmon')
ax[0, 1].set_title('Annual Amount from Treasury')
ax[0, 1].set_xlabel('Year')
ax[0, 1].set_ylabel('Amount from Treasury')

# Amt to Treasury Reserve
ax[1, 0].bar(yearly_projection_df['Year'], yearly_projection_df['Amt to Treasury Reserve'], color='lightgreen')
ax[1, 0].set_title('Annual Amount to Treasury Reserve')
ax[1, 0].set_xlabel('Year')
ax[1, 0].set_ylabel('Amount to Treasury Reserve')

# Average Cardano Floating
ax[1, 1].plot(yearly_projection_df['Year'], yearly_projection_df['Avg Cardano Floating'], marker='o', linestyle='-', color='orchid')
ax[1, 1].set_title('Average Cardano Floating')
ax[1, 1].set_xlabel('Year')
ax[1, 1].set_ylabel('Avg Cardano Floating')

plt.tight_layout()
plt.show()
