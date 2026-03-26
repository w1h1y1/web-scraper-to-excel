import pandas as pd

file_path = "sample.xlsx"
df = pd.read_excel(file_path)

print("原始数据：")
print(df.head())
print("原始数据行数:", len(df))

# 删除重复数据
df = df.drop_duplicates()

# 删除空值
df = df.dropna()

# 按 Salary 降序排序
df = df.sort_values(by="Salary", ascending=False)

# 保存结果
output_file = "cleaned.xlsx"
df.to_excel(output_file, index=False)

print("清洗后数据行数:", len(df))
print(f"处理完成！已生成 {output_file}")