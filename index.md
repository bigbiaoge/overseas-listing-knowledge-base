---
layout: home

hero:
  name: "境外上市备案知识库"
  text: "证监会境外发行上市备案补充材料要求"
  tagline: "为资本市场非诉律师及相关从业人员提供监管关注点参考"
  actions:
    - theme: brand
      text: 快速开始
      link: /timeline/2026
    - theme: alt
      text: 查看统计
      link: /statistics

features:
  - icon: 📅
    title: 按时间顺序
    details: 按月份整理所有备案补充材料要求，便于追踪监管动态
    link: /timeline/2026
    linkText: 浏览时间线
  - icon: 📋
    title: 按问题类型
    details: 按问题类型分类整理，便于横向对比分析监管关注点
    link: /types/shareholders
    linkText: 查看类型
  - icon: 📊
    title: 统计分析
    details: 可视化展示问题类型分布、时间趋势等统计数据
    link: /statistics
    linkText: 查看统计
  - icon: 🔄
    title: 定期更新
    details: 持续跟踪证监会最新公示信息，保持数据时效性
    link: /changelog
    linkText: 更新日志
---

<div class="stats-container">
  <h2>📈 总体统计</h2>
  <div class="stats-grid">
    <div class="stat-card">
      <div class="stat-value">429</div>
      <div class="stat-label">涉及公司数</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">1,556</div>
      <div class="stat-label">问题总数</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">64</div>
      <div class="stat-label">公示期数</div>
    </div>
    <div class="stat-card">
      <div class="stat-value">2023-2026</div>
      <div class="stat-label">数据时间范围</div>
    </div>
  </div>
</div>

<div class="hot-topics">
  <h2>🔥 热点问题类型 TOP 5</h2>
  <table class="topic-table">
    <thead>
      <tr>
        <th>排名</th>
        <th>问题类型</th>
        <th>数量</th>
        <th>占比</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>🥇</td>
        <td>股东/实际控制人</td>
        <td>373</td>
        <td>24.0%</td>
      </tr>
      <tr>
        <td>🥈</td>
        <td>股权变动/代持</td>
        <td>296</td>
        <td>19.0%</td>
      </tr>
      <tr>
        <td>🥉</td>
        <td>其他</td>
        <td>270</td>
        <td>17.4%</td>
      </tr>
      <tr>
        <td>4</td>
        <td>业务经营/经营范围</td>
        <td>194</td>
        <td>12.5%</td>
      </tr>
      <tr>
        <td>5</td>
        <td>外汇/境外投资</td>
        <td>81</td>
        <td>5.2%</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="data-source">
  <h2>📚 数据来源</h2>
  <ul>
    <li><strong>官网地址</strong>：<a href="https://www.csrc.gov.cn/csrc/c100098/common_list.shtml" target="_blank">中国证监会官网 - 境外发行上市类</a></li>
    <li><strong>数据范围</strong>：2023年4月至今的备案补充材料要求公示</li>
    <li><strong>更新时间</strong>：每周定期更新</li>
  </ul>
</div>

<style scoped>
.stats-container {
  margin: 3rem 0;
  padding: 1.5rem;
  background: linear-gradient(135deg, #f5f7fa 0%, #e4e8ec 100%);
  border-radius: 12px;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}

.stat-card {
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  text-align: center;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.stat-value {
  font-size: 2rem;
  font-weight: bold;
  color: #1a73e8;
}

.stat-label {
  margin-top: 0.5rem;
  color: #666;
  font-size: 0.9rem;
}

.hot-topics {
  margin: 2rem 0;
}

.topic-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
  background: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.topic-table th,
.topic-table td {
  padding: 1rem;
  text-align: left;
  border-bottom: 1px solid #eee;
}

.topic-table th {
  background: #f8f9fa;
  font-weight: 600;
}

.topic-table tr:last-child td {
  border-bottom: none;
}

.data-source {
  margin: 2rem 0;
  padding: 1.5rem;
  background: #f8f9fa;
  border-radius: 8px;
}

.data-source ul {
  list-style: none;
  padding: 0;
}

.data-source li {
  padding: 0.5rem 0;
}

.data-source a {
  color: #1a73e8;
  text-decoration: none;
}

.data-source a:hover {
  text-decoration: underline;
}
</style>
