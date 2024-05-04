import pyarrow.parquet as pq
import pandas as pd
""" 
prqt_file = pq.ParquetFile('part-00000-ac716c56-5c56-4a36-a14d-8ae4529d40a8-c000.snappy.parquet')
print('row_groups: ', prqt_file.num_row_groups)
print(prqt_file.metadata)
print(prqt_file.schema)

rowgrp =  prqt_file.read_row_group(0)

print(rowgrp[0:3,1])
 """

dataset = pq.ParquetDataset('hotel-dataset')
table = dataset.read()

dataframe = table.to_pandas()
dataframe['DescLength'] = dataframe['Description'].str.len()
dataframe_analysis = dataframe.drop(['Description','PhoneNumber','CityName','Address','Pincode','uuid','match_id','match_confidence_score'], axis=1)

print(dataframe_analysis.describe(include='all'))

print(dataframe_analysis.info(verbose=True))

print(dataframe_analysis.head())
