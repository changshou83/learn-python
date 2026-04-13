from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

# 1. 定位文件（基于脚本目录，避免受当前工作目录影响）
path = Path(__file__).with_name('sitka_weather_2018_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()  # 统一编码避免乱码

# 2. 解析CSV头与数据
reader = csv.reader(lines)
header_row = next(reader)  # 跳过表头，获取列名索引
# 关键：用index()自动找目标列（无需硬编码）
date_idx = header_row.index('DATE')
high_idx = header_row.index('TMAX')
low_idx = header_row.index('TMIN')

# 3. 提取数据
dates, highs, lows = [], [], []
for row in reader:
    try:
        current_date = datetime.strptime(row[date_idx], '%Y-%m-%d')
        high = int(row[high_idx])
        low = int(row[low_idx])
    except (ValueError, IndexError):  # 捕获缺失数据/列错误
        print(f"跳过无效行：日期{row[date_idx] if date_idx < len(row) else '未知'}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# 4. 绘制温度折线图（带填充区域）
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(12, 6))  # 调整画布大小更清晰
ax.plot(dates, highs, color='red', alpha=0.7, label='Maximum Temperature')  # alpha=透明度
ax.plot(dates, lows, color='blue', alpha=0.7, label='Minimum Temperature')
ax.fill_between(dates, highs, lows, color='lightblue', alpha=0.3)  # 填充温差区域

# 5. 图表美化（标题/轴/刻度）
ax.set_title("Daily high/low temperatures in Sitka, 2018", fontsize=20, pad=20)
ax.set_xlabel('', fontsize=14)
fig.autofmt_xdate()  # 自动旋转日期避免重叠
ax.set_ylabel("Temperature (℉)", fontsize=14)
ax.tick_params(labelsize=12)
ax.legend(fontsize=12)
ax.set_ylim(10, 140)  # 统一Y轴范围，方便对比

plt.show()
