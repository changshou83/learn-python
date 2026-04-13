from pathlib import Path
import json
import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = 'browser'

# 1. 读取并解析GeoJSON
path = Path(__file__).with_name('eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)  # 转为Python字典

# 2. 提取关键数据（震级、经纬度、标题）
all_eq_dicts = all_eq_data['features']
mags, lons, lats, titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])  # 震级
    lons.append(eq_dict['geometry']['coordinates'][0])  # 经度
    lats.append(eq_dict['geometry']['coordinates'][1])  # 纬度
    titles.append(eq_dict['properties']['title'])  # 地震标题

# 3. 绘制交互式地图
title = all_eq_data['metadata']['title']  # 自动获取数据集标题
fig = go.Figure(
    data=go.Scattergeo(
        lat=lats,
        lon=lons,
        text=titles,
        hovertext=titles,
        hoverinfo='text',
        marker={
            'size': [max((mag or 0) * 4, 4) for mag in mags],
            'color': mags,
            'colorscale': 'Viridis',
            'colorbar': {'title': '震级'},
            'line': {'width': 0.5, 'color': 'white'},
        },
    )
)
fig.update_layout(title=title, geo={'projection_type': 'natural earth'})
fig.show()  # 在浏览器打开交互式图表
