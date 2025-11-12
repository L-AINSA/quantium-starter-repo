# reading the cvs files
import pandas
df_0 = pandas.read_csv('data/daily_sales_data_0.csv')
df_1 = pandas.read_csv('data/daily_sales_data_1.csv')
df_2 = pandas.read_csv('data/daily_sales_data_2.csv')

combined_df = pandas.concat([df_0, df_1, df_2], ignore_index = True) 
#print(f' conc of three dataframses {combined_df.head()}')

column_name = 'product'

combined_df = combined_df[combined_df[column_name].str.contains('pink morsel', case=False, na=False)]
#print(f'filter {combined_df}')

combined_df['price'] = combined_df['price'].str.replace('$', '', regex=False).astype(float)
#print(f'removing $ sign {combined_df}')

combined_df['quantity'] = pandas.to_numeric(combined_df['quantity'])
#print(f'fixing the qty data type {combined_df}')


combined_df['sales'] = combined_df['price'] * combined_df['quantity']
#print(f'computation {combined_df}')

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
