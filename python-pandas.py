#!/usr/bin/python3

# 使用pandas进行数据分析

from itertools import count, groupby

from unittest import result
import pandas as pd
data = pd.read_excel("/home/guo/Downloads/人员维度评分.xlsx", sheet_name='2月',
 usecols=['owner_id', 'big_group', '2月增速比', '1月增速比', '2月深度沟通客户数', '1月深度沟通客户数'])

cols = ['2月增速比', '1月增速比', '2月深度沟通客户数', '1月深度沟通客户数']
data = data.fillna(0)

groups = data['big_group'].drop_duplicates(keep='first').values


_groupby = data.groupby('big_group')

def getResult(cols):
    for col in cols:
        data['{}_Rank'.format(col)] = _groupby[col].rank(ascending=False) - 1
        data1 = pd.DataFrame()
        for big_group, value in _groupby.size().items():
            _result = (value - _groupby.get_group(big_group)['{}_Rank'.format(col)]) / value
            data1 = pd.concat([data1, pd.DataFrame(_result)], axis=0)
        data['{}_Result'.format(col)] = data1['{}_Rank'.format(col)]

getResult(cols)

data['Result'] = data['2月增速比_Result'] * 0.3 + data['1月增速比_Result'] * 0.2 + data['2月深度沟通客户数_Result'] * 0.3 + data['1月深度沟通客户数_Result'] * 0.3

data['Result1'] = data['2月增速比_Result'] * 0.5 + data['2月深度沟通客户数_Result'] * 0.5

cols1 = ['Result', 'Result1']

getResult(cols1)

writer = pd.ExcelWriter('/home/guo/Downloads/Test.xlsx')
data.to_excel(writer, 'Test')
writer.save()