# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("المتوسط:", np.mean(arr)) # 3.0
print("مصفوفة 2x2:", np.zeros((2,2)))

import matplotlib.pyplot as plt
import numpy as np
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y, color='purple') 
plt.title("drow")

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({'فئة': ['A', 'B', 'C'], 'قيمة': [10, 25, 15]})
sns.barplot(x='فئة', y='قيمة', data=df)
plt.show()

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
X = np.array([[1], [2], [3]]) # البيانات
y = np.array([2, 4, 6]) # النتيجة
model = LinearRegression().fit(X, y)
print("التوقع لـ 4:", model.predict([[4]])) # 8


import torch
x = torch.tensor([1.0, 2.0, 3.0]) # مصفوفة زي numpy بس للـ GPU
y = x * 2
print(y) # tensor([2., 4., 6.])

 
import pandas as pd

data = {'name': ['ahmed', 'moody'], 'deg': [90, 85]}
df = pd.DataFrame(data)
print(df)
print("اhigh deg:", df['deg'].max())




