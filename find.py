import pandas as pd

# 读取Excel文件
df = pd.read_excel('1.xlsx')

# 获取列数
n_cols = len(df.columns)

# 创建一个空的DataFrame，用于存储筛选后的数据
filtered_data = pd.DataFrame()

# 遍历每两列数据
for i in range(0, n_cols, 2):
    # 获取当前两列的列名
    col1 = df.columns[i]
    col2 = df.columns[i + 1]

    # 筛选数据
    filtered = df[(df[col2] >= 40)]

    # 将筛选后的数据添加到新的DataFrame中
    filtered_data = pd.concat([filtered_data, filtered[[col1, col2]]], axis=1)

# 将结果保存到Excel文件中
filtered_data.to_excel('output.xlsx', index=False)


