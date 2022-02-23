#!/usr/bin/python3

# 使用pandas进行数据分析

from itertools import count, groupby
from unittest import result
import pandas as pd
data = pd.read_excel("/home/guo/Downloads/人员维度评分.xlsx", sheet_name='2月',
 usecols=['owner_id', 'big_group', '2月增速比', '1月增速比', '2月深度沟通客户数', '1月深度沟通客户数'])

data = data.fillna(0)

groups = data['big_group'].drop_duplicates(keep='first').values


_groupby = data.groupby('big_group')
data['2月增速比_Rank'] = _groupby['2月增速比'].rank(ascending=False) - 1

print('before:\n', data)
for big_group, value in _groupby.size().items():
    _result = (value - _groupby.get_group(big_group)['2月增速比_Rank']) / value
    data1 = pd.DataFrame(_result)
    print(data1)
    # data['2月增速比_Result'] = _result
    # pd.merge(data, data1, how='right')
    # pd.concat([data, data1], axis=1)
    # data['2月增速比_Test'] = (value - _groupby.get_group(big_group)['2月增速比_Rank']) / value
print('after:\n', data)
    # group_df['2月增速比_Rank'] =
#     _count = _groupby.get_group(group).count()
    # (_count - _groupby.get_group(group)['2月增速比_Rank'])/_count

    # print((_count - _groupby.get_group(group)['2月增速比_Rank'])/_count)

# writer = pd.ExcelWriter('/home/guo/Downloads/Test.xlsx')
# data.to_excel(writer, 'Test')
# writer.save()
# data = data[['last_30_live_cnt', 'last_30_publish_video', '近6个月消耗', '12月消耗', '12月活跃天数', '1月消耗']]
# data = data[:].astype(int)

# x, y = data.iloc[:, : - 1].values, data.iloc[:, 5].values
