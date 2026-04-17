---
title: 统计分析
description: 境外上市备案补充材料要求统计分析
---

# 统计分析

本页面展示境外发行上市备案补充材料要求的统计分析数据。

## 📊 总体概览

| 指标 | 数值 |
|------|------|
| 总条目数（涉及公司数） | 729 家 |
| 总问题数 | 3129 条 |
| 问题类型数 | 17 类 |
| 数据时间范围 | 2023年4月 - 2026年 |

---

## 📈 问题类型分布

### 按问题数量排序

```echarts
{
  "title": {
    "text": "问题类型分布（按数量）",
    "left": "center"
  },
  "tooltip": {
    "trigger": "axis",
    "axisPointer": {
      "type": "shadow"
    }
  },
  "grid": {
    "left": "3%",
    "right": "4%",
    "bottom": "3%",
    "containLabel": true
  },
  "xAxis": {
    "type": "value"
  },
  "yAxis": {
    "type": "category",
    "data": ["股权变动/代持", "其他", "数据安全/个人信息", "股东/实际控制人", "业务经营/经营范围", "外汇/境外投资", "全流通", "合规问题", "外资准入", "募集资金用途", "股权架构/VIE", "国有股东", "董监高", "财务会计", "关联交易/同业竞争", "税务", "保密/档案管理"],
    "inverse": true
  },
  "series": [
    {
      "name": "问题数量",
      "type": "bar",
      "data": [544, 492, 273, 272, 268, 261, 219, 207, 181, 133, 75, 71, 69, 26, 17, 17, 4],
      "itemStyle": {
        "color": "#5470c6"
      },
      "label": {
        "show": true,
        "position": "right"
      }
    }
  ]
}
```

### 占比分布（饼图）

```echarts
{
  "title": {
    "text": "问题类型占比",
    "subtext": "TOP 10 类型",
    "left": "center"
  },
  "tooltip": {
    "trigger": "item",
    "formatter": "{b}: {c} ({d}%)"
  },
  "legend": {
    "orient": "vertical",
    "right": "5%",
    "top": "center"
  },
  "series": [
    {
      "name": "问题类型",
      "type": "pie",
      "radius": ["35%", "65%"],
      "center": ["40%", "50%"],
      "avoidLabelOverlap": false,
      "itemStyle": {
        "borderRadius": 5,
        "borderColor": "#fff",
        "borderWidth": 2
      },
      "label": {
        "show": true,
        "formatter": "{b}: {d}%"
      },
      "data": [
        { "value": 544, "name": "股权变动/代持", "itemStyle": { "color": "#5470c6" } },
        { "value": 492, "name": "其他", "itemStyle": { "color": "#91cc75" } },
        { "value": 273, "name": "数据安全/个人信息", "itemStyle": { "color": "#fac858" } },
        { "value": 272, "name": "股东/实际控制人", "itemStyle": { "color": "#ee6666" } },
        { "value": 268, "name": "业务经营/经营范围", "itemStyle": { "color": "#73c0de" } },
        { "value": 261, "name": "外汇/境外投资", "itemStyle": { "color": "#3ba272" } },
        { "value": 219, "name": "全流通", "itemStyle": { "color": "#fc8452" } },
        { "value": 207, "name": "合规问题", "itemStyle": { "color": "#9a60b4" } },
        { "value": 181, "name": "外资准入", "itemStyle": { "color": "#ea7ccc" } },
        { "value": 133, "name": "募集资金用途", "itemStyle": { "color": "#d97757" } }
      ]
    }
  ]
}
```

---

## 📅 时间趋势

### 按年份统计

| 年份 | 公示期数 | 涉及公司数 | 问题数量 |
|------|----------|------------|----------|
| 2023年 | 31期 | 157家 | 678条 |
| 2024年 | 37期 | 146家 | 556条 |
| 2025年 | 49期 | 341家 | 1506条 |
| 2026年 | 12期 | 87家 | 374条 |

```echarts
{
  "title": {
    "text": "各年问题数量对比",
    "left": "center"
  },
  "tooltip": {
    "trigger": "axis"
  },
  "grid": {
    "left": "3%",
    "right": "4%",
    "bottom": "3%",
    "containLabel": true
  },
  "xAxis": {
    "type": "category",
    "data": ["2023年", "2024年", "2025年", "2026年"],
    "axisLabel": {
      "color": "#666"
    }
  },
  "yAxis": {
    "type": "value",
    "name": "问题数量",
    "axisLabel": {
      "color": "#666"
    }
  },
  "series": [
    {
      "name": "问题数量",
      "type": "bar",
      "data": [678, 556, 1506, 374],
      "itemStyle": {
        "color": "#5470c6"
      },
      "barWidth": "50%"
    }
  ]
}
```

---

## 📋 详细数据表

### 问题类型统计

| 排名 | 问题类型 | 问题数量 | 占比 |
|------|----------|----------|------|
| 1 | 股权变动/代持 | 544 | 17.4% |
| 2 | 其他 | 492 | 15.7% |
| 3 | 数据安全/个人信息 | 273 | 8.7% |
| 4 | 股东/实际控制人 | 272 | 8.7% |
| 5 | 业务经营/经营范围 | 268 | 8.6% |
| 6 | 外汇/境外投资 | 261 | 8.3% |
| 7 | 全流通 | 219 | 7.0% |
| 8 | 合规问题 | 207 | 6.6% |
| 9 | 外资准入 | 181 | 5.8% |
| 10 | 募集资金用途 | 133 | 4.3% |
| 11 | 股权架构/VIE | 75 | 2.4% |
| 12 | 国有股东 | 71 | 2.3% |
| 13 | 董监高 | 69 | 2.2% |
| 14 | 财务会计 | 26 | 0.8% |
| 15 | 关联交易/同业竞争 | 17 | 0.5% |
| 16 | 税务 | 17 | 0.5% |
| 17 | 保密/档案管理 | 4 | 0.1% |
