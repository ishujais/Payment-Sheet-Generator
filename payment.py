#importing pandas
import pandas as pd

print('Processing.....')
#reading from first payment_sheet
a = pd.read_csv('one.csv')

#reading from second payment_sheet
b = pd.read_csv('two.csv')

#Append the two dataframes from two payment sheets into one table i.e. c
c = a.append(b)

#Calculating total market charge by adding three columns in the dataframe c
Total_Marketplace_Charge = c['Commission'] + c['Payment Gateway'] + c['PickPack Fee']

#Calculating loss/profit
Profit_loss = c['Sale Amount'] - (c['Cost Price'] + Total_Marketplace_Charge)

#Creating new dataframe & writing it into a new table.
df = pd.DataFrame()
df['Order Number'] = c['OrderNum']
df['Profit/loss(%)'] = Profit_loss
df['Transferred Amount'] = c['Transferred Amount']
df['Total Marketplace Charge'] = Total_Marketplace_Charge

#Reset the index value
df.reset_index(drop=True, inplace=True)

#Generating a new file 
df.to_csv('Final_PaymentSheet.csv', index = False)
print('Final PaymentSheet.csv has been generated in the same folder')
