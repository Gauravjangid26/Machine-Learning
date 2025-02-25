import pandas as pd

df=pd.read_csv('/Users/gauravjangid/Desktop/Data Science/data set/supermarket_sales.csv')
print(df.columns)

df=df[['Gender','Product line','Total']]

#creating pivot table-->how much gender spent in each product line(aggregate function)

pivot_table=df.pivot_table(index='Gender',columns='Product line',values='Total',aggfunc='sum').round(0)
print(pivot_table)

# i am goona export this pivot table in excel file
pivot_table.to_excel(excel_writer='supermarket_sales_pivot_table.xlsx', 
                      sheet_name='Report', 
                      startrow=4)


