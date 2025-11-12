# reading the cvs files
import pandas as pd
from dateutil import parser
import numpy as np

def parse_multi_format(date_str):
    """Parses date string using YYYY-MM-DD first, then M/D/YYYY."""
    
    # 1. Handle NaN/Null values if they are present
    if pd.isna(date_str):
        return np.nan
    
    # 2. Try the ISO format first (YYYY-MM-DD)
    if '-' in str(date_str):
        try:
            return pd.to_datetime(date_str, format='%Y-%m-%d')
        except:
            pass # Fall through to the next check

    # 3. Try the M/D/YYYY format
    if '/' in str(date_str):
        try:
            # We explicitly use M/D/Y format for the non-ISO dates
            return pd.to_datetime(date_str, format='%m/%d/%Y')
        except:
            pass # Fall through
            
    # 4. If all fails, return NaT
    return pd.NaT



df_0 = pd.read_csv('data/daily_sales_data_0.csv')
df_1 = pd.read_csv('data/daily_sales_data_1.csv')
df_2 = pd.read_csv('data/daily_sales_data_2.csv')

combined_df = pd.concat([df_0, df_1, df_2], ignore_index = True) 
#print(f' conc of three dataframses {combined_df.head()}')

column_name = 'product'

combined_df = combined_df[combined_df[column_name].str.contains('pink morsel', case=False, na=False)]
#print(f'filter {combined_df}')

combined_df['price'] = combined_df['price'].str.replace('$', '', regex=False).astype(float)
#print(f'removing $ sign {combined_df}')

combined_df['quantity'] = pd.to_numeric(combined_df['quantity'])
#print(f'fixing the qty data type {combined_df}')


combined_df['sales'] = combined_df['price'] * combined_df['quantity']
#print(f'computation {combined_df}')

# Apply the function to your column
combined_df['date'] = combined_df['date'].apply(parse_multi_format)

del combined_df['price']
#print(combined_df.head())
del combined_df['quantity']
#print(combined_df.head())
del combined_df['product']
#print(combined_df.head())

# Create a list with the desired column order
new_order = ['sales', 'date', 'region']

# Reorder the DataFrame columns
combined_df = combined_df[new_order]

combined_df.to_csv('processed_data.csv', index=False)
