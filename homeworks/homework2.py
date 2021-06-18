import pandas as pd
import openpyxl

df = pd.DataFrame([[11, 21, 31], [12, 22, 32], [31, 32, 33]],
                  index=None, columns=['a', 'b', 'c'])
"""
      a   b   c
     11  21  31
     12  22  32
     31  32  33
"""
print(df)

df.to_excel('exampleeeeeeeee.xlsx', sheet_name='new_sheet_name')
