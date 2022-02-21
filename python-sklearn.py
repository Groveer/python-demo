#!/usr/bin/python3

# 使用随机森林算法进行权重分配

import sys

def print_args():
    args = len(sys.argv)
    for index in range(1,args):
        print("第{}个参数：{}。".format(index, sys.argv[index]))
    return args - 1

if print_args() < 1:
    print("无效的数据路径！！！")
    exit()

import pandas as pd
data = pd.read_csv(sys.argv[1])

data = data[['last_30_live_cnt', 'last_30_publish_video', '近6个月消耗', '12月消耗', '12月活跃天数', '1月消耗']]
data = data[:].astype(int)

x, y = data.iloc[:, : - 1].values, data.iloc[:, 5].values

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state = 0)
# print("x_train:{}\n".format(x_train), "y_train:{}\n".format(y_train))
forest = RandomForestClassifier(random_state=0, n_jobs=-1)
forest.fit(x_train, y_train)
forest_importances = forest.feature_importances_

from xgboost import XGBClassifier
xgb = XGBClassifier()
xgb.fit(x_train, y_train)
xgb_importances = xgb.feature_importances_

feat_labels = data.columns[0:]
import numpy as np
forest_indices = np.argsort(forest_importances)[::-1] #[::-1]表示将各指标按权重大小进行排序输出
xgb_indices = np.argsort(xgb_importances)[::-1]
print("forest:\n")
for f in range(x_train.shape[1]):
    print("%2d) %-*s %f" % (f + 1, 30, feat_labels[forest_indices[f]], forest_importances[forest_indices[f]]))
print("xgboost:\n")
for f in range(x_train.shape[1]):
    print("%2d) %-*s %f" % (f + 1, 30, feat_labels[xgb_indices[f]], xgb_importances[xgb_indices[f]]))
