#!/usr/bin/env python3
import camelot
import sys
from decimal import Decimal
from re import sub



def floatTryParse(value):
    try:
        return float(sub(r'[,]', '', value))
    except ValueError:
        return 0

def MoneyTryParse(value):
    try:
        return Decimal(value)
    except:
        return 0



#patern = "sushi"
patern = sys.argv[2]
file   = sys.argv[1]
print(f'looking for {sys.argv[2].lower()} in the file {file}')

tables = camelot.read_pdf(file, pages = 'all' ,flavor='stream', columns = ['46, 90, 370, 400, 500'])
# mydf = tables[0].d

for table in tables:
    for i in range(len(table.df)):
        if floatTryParse(table.df[3].iloc[i]) > 0:
            if patern.lower() in str(table.df[2].iloc[i]).lower():
                print(f'{table.df[0].iloc[i]:.6s} {table.df[2].iloc[i]:>50} {table.df[3].iloc[i]:>10s}')

## camelot.plot(tables[0], kind='text').savefig("page2.png")


""" try:
    float(element)
except ValueError:
    print "Not a float" 
    
0 - Date
1 - Op type
2 - Operation
3 - Withdrawals
4 - Deposits
5 - Balance    
    
    
    """