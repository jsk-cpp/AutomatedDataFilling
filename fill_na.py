import os
import pandas as pd

src_data='./data(3)/Supplemental_Dataset_1(2).xlsx'
src=pd.read_excel(src_data,keep_default_na=False)


src['Longitude']='NA'
src['Latitude']='NA'
# print(src.head(8))

# print(src.head(3))

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter(src_data, engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
src.to_excel(writer, sheet_name='sample_all',index=False)

# Close the Pandas Excel writer and output the Excel file.
writer.save()