---
title: 统计分析
description: 境外上市备案补充材料要求统计分析
---

# 统计分析

本页面展示境外发行上市备案补充材料要求的统计分析数据。

## 📊 总体概览

| 指标 | 数值 |
|------|------|
| 总条目数（涉及公司数） | 304 家 |
| 总问题数 | 1,464 条 |
| 数据时间范围 | 2023年4月 - 2026年4月 |

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
    "data": ["股东/实际控制人", "合规问题", "股权变动/代持", "业务经营/经营范围", "全流通", "其他", "外汇/境外投资", "募集资金用途", "数据安全/个人信息", "税务", "诉讼/仲裁", "国有股东", "董监高", "控制权", "股权架构/VIE", "AI技术", "人类遗传资源", "财务问题", "关联交易/同业竞争", "保密/档案管理"],
    "inverse": true
  },
  "series": [
    {
      "name": "问题数量",
      "type": "bar",
      "data": [583, 332, 305, 251, 200, 180, 163, 95, 94, 72, 68, 60, 52, 48, 46, 35, 32, 27, 11, 4],
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
        { "value": 583, "name": "股东/实际控制人", "itemStyle": { "color": "#5470c6" } },
        { "value": 332, "name": "合规问题", "itemStyle": { "color": "#91cc75" } },
        { "value": 305, "name": "股权变动/代持", "itemStyle": { "color": "#fac858" } },
        { "value": 251, "name": "业务经营/经营范围", "itemStyle": { "color": "#ee6666" } },
        { "value": 200, "name": "全流通", "itemStyle": { "color": "#73c0de" } },
        { "value": 180, "name": "其他", "itemStyle": { "color": "#3ba272" } },
        { "value": 163, "name": "外汇/境外投资", "itemStyle": { "color": "#fc8452" } },
        { "value": 95, "name": "募集资金用途", "itemStyle": { "color": "#9a60b4" } },
        { "value": 94, "name": "数据安全/个人信息", "itemStyle": { "color": "#ea7ccc" } },
        { "value": 72, "name": "税务", "itemStyle": { "color": "#d97757" } }
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
| 2026年 | 11期 | 57家 | 320条 |
| 2025年 | 35期 | 247家 | 1,144条 |

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
      "data": [0, 0, 1144, 320],
      "itemStyle": {
        "color": "#5470c6"
      },
      "label": {
        "show": true,
        "position": "top"
      }
    }
  ]
}
```

---

## 💡 监管关注点解读

### 🔹 股东/实际控制人（占比最高 39.8%）

**监管关注点**：
- 5%以上股东的穿透核查
- 股东资格合法性
- 实际控制人认定
- 股权代持还原
- 信托持股披露

**典型问题示例**：
1. 请说明股东向上穿透后的境内主体是否存在法律法规规定禁止持股的主体
2. 请说明控股股东、实际控制人具体情况
3. 请补充说明股东入股价格的合理性

### 🔹 合规问题（占比 22.7%）

**监管关注点**：
- 业务合规性
- 资质许可
- 行政处罚情况
- 合法合规经营

### 🔹 股权变动/代持（占比 20.8%）

**监管关注点**：
- 历次增资转让的定价依据
- 股权代持的形成与解除
- 员工股权激励计划
- 股权变动合法合规性

---

## 📋 数据说明

1. **数据来源**：中国证监会官网国际合作部公示信息
2. **更新时间**：每周定期更新
3. **分类标准**：根据问题内容关键词自动分类，部分问题可能涉及多个类型
4. **数据范围**：2023年4月至2026年4月

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0;
}

th, td {
  padding: 0.75rem;
  text-align: left;
  border-bottom: 1px solid #eee;
}

th {
  background: #f8f9fa;
  font-weight: 600;
}
</style>
