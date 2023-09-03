# -*- coding: utf-8 -*-
"""FinalTest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZfvtaZUw4GlhsmGyXmmE9YsXpOl18xYE
"""

import pandas as pd
import datetime 
import numpy as np

final_pd = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/sales.csv')
final_pd.head(1)

# 1. Lấy thông tin về Mã đơn hàng, mã sản phẩm, mã khách hàng, số lượng sản phẩm của những dòng dữ liệu thỏa điều kiện Ship Mode là Standard Class
final_pd[final_pd['Ship Mode']=='Standard Class'][['Order ID','Product ID','Customer ID','Quantity']]

# 2. Lấy thông tin về những mã đơn hàng của những dòng dữ liệu thỏa mãn điều kiện sản phẩm (Product ID) thuộc nhóm category là Office Supplies và có quantity > 3
final_pd[(final_pd['Category']=='Office Supplies')& (final_pd['Quantity'] > 3)]['Product ID']

# 3. Thống kê số lượng mã đơn hàng, số lượng các loại sản phẩm (product ID), tổng doanh thu 
# và tổng lợi nhuận theo từng Category, sắp xếp theo thứ tự giảm dần của doanh thu
#final_pd[final_pd.groupby('Category').sum('Sales')][['Product ID']]
#['Sales'].agg('sum','count')&
pd1=final_pd.groupby('Category')['Order ID','Product ID'].count()
#print(pd1)
pd2=final_pd.groupby('Category')['Sales', 'Profit'].agg('sum')
#print(pd2)
#dùng concat để nối 2 dataframe, axis=1: 
fresult=[pd1,pd2]
result= pd.concat(fresult, axis=1).sort_values('Sales', ascending=False)
print(result)