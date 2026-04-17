import json
from collections import defaultdict

with open('parsed_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

total_periods = len(data['all_data'])
total_companies = sum(len(issue['companies']) for issue in data['all_data'])
total_questions = sum(len(c['questions']) for issue in data['all_data'] for c in issue['companies'])

monthly_questions = defaultdict(int)
monthly_companies = defaultdict(int)
yearly_questions = defaultdict(int)
yearly_companies = defaultdict(int)
type_stats = defaultdict(int)
companies_list = []

for issue in data['all_data']:
    date = issue['date']
    if date == 'Unknown':
        continue
    year_month = date[:7]
    year = date[:4]
    
    companies_in_issue = len(issue['companies'])
    questions_in_issue = sum(len(c['questions']) for c in issue['companies'])
    
    monthly_questions[year_month] += questions_in_issue
    monthly_companies[year_month] += companies_in_issue
    yearly_questions[year] += questions_in_issue
    yearly_companies[year] += companies_in_issue
    
    for company in issue['companies']:
        companies_list.append(company['name'])
        for q in company['questions']:
            if '股权代持' in q or '代持' in q or '股权变动' in q:
                type_stats['股权变动-代持'] += 1
            elif '实际控制人' in q or '控股股东' in q:
                type_stats['股东-实际控制人'] += 1
            elif '数据安全' in q or '个人信息' in q or '网络安全' in q:
                type_stats['数据安全-个人信息'] += 1
            elif '全流通' in q or '内资股' in q:
                type_stats['全流通'] += 1
            elif '关联交易' in q or '同业竞争' in q:
                type_stats['关联交易-同业竞争'] += 1
            elif '募集资金' in q or '融资规模' in q:
                type_stats['募集资金用途'] += 1
            elif '外资准入' in q or '外商投资' in q or '负面清单' in q:
                type_stats['外资准入'] += 1
            elif '外汇' in q or '境外投资' in q:
                type_stats['外汇-境外投资'] += 1
            elif '保密' in q or '档案管理' in q:
                type_stats['保密-档案管理'] += 1
            elif '独立性' in q or '资产独立' in q:
                type_stats['独立性'] += 1
            elif '税务' in q or '所得税' in q:
                type_stats['税务'] += 1
            elif '合规' in q or '合法合规' in q or '行政处罚' in q:
                type_stats['合规问题'] += 1
            elif '国有股东' in q or '国资' in q:
                type_stats['国有股东'] += 1
            elif 'vie' in q.lower() or '协议控制' in q:
                type_stats['股权架构-VIE'] += 1
            elif '经营范围' in q or '主营业务' in q:
                type_stats['业务经营-经营范围'] += 1
            else:
                type_stats['其他'] += 1

all_months = sorted(monthly_questions.keys())
years = sorted(yearly_questions.keys())
sorted_types = sorted(type_stats.items(), key=lambda x: -x[1])
unique_companies = sorted(set(companies_list))

months_str = json.dumps(all_months)
questions_str = json.dumps([monthly_questions[m] for m in all_months])
companies_str = json.dumps([monthly_companies[m] for m in all_months])
years_str = json.dumps(years)
yearly_q_str = json.dumps([yearly_questions[y] for y in years])

pie_items = []
for name, value in sorted_types:
    pie_items.append('{"name":"' + name.replace('"', '\\"') + '","value":' + str(value) + '}')
pie_str = '[' + ','.join(pie_items) + ']'

page = """# 境外上市备案统计分析

## 数据概览

| 指标 | 数值 |
|-----|------|
| 累计期数 | {periods} |
| 涉及公司数 | {companies} |
| 问题总数 | {questions} |
| 平均每期问题数 | {avg_period:.1f} |
| 平均每家公司问题数 | {avg_company:.1f} |

## 问题类型分布

| 类型 | 问题数 | 占比 |
|-----|-------|-----|
""".format(
    periods=total_periods,
    companies=total_companies,
    questions=total_questions,
    avg_period=total_questions/total_periods,
    avg_company=total_questions/total_companies
)

for t, c in sorted_types:
    pct = c / total_questions * 100
    page += '| ' + t + ' | ' + str(c) + ' | ' + '{:.1f}%'.format(pct) + ' |\n'

page += """
## 年度趋势

| 年度 | 公司数 | 问题数 |
|-----|-------|-------|
"""

for y in years:
    page += '| ' + y + ' | ' + str(yearly_companies[y]) + ' | ' + str(yearly_questions[y]) + ' |\n'

page += """
## 可视化分析

### 问题数量月度趋势

<div id="trendChart" style="width:100%;height:400px;"></div>

### 问题类型分布

<div id="typeChart" style="width:100%;height:500px;"></div>

### 年度对比

<div id="yearChart" style="width:100%;height:400px;"></div>

### 公司数量月度趋势

<div id="companyChart" style="width:100%;height:400px;"></div>

<script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>
<script>
var monthsData = """ + months_str + """;
var questionsData = """ + questions_str + """;
var companiesData = """ + companies_str + """;
var pieData = """ + pie_str + """;
var yearsData = """ + years_str + """;
var yearlyQuestionsData = """ + yearly_q_str + """;

document.addEventListener('DOMContentLoaded', function() {
    var trendChart = echarts.init(document.getElementById('trendChart'));
    trendChart.setOption({
        tooltip: { trigger: 'axis' },
        legend: { data: ['问题数量'] },
        grid: { left: '3%', right: '4%', bottom: '3%', containLabel: true },
        xAxis: { type: 'category', boundaryGap: false, data: monthsData },
        yAxis: { type: 'value', name: '问题数' },
        series: [{
            name: '问题数量',
            type: 'line',
            smooth: true,
            data: questionsData,
            areaStyle: { opacity: 0.3 },
            lineStyle: { width: 2 },
            itemStyle: { color: '#5470C6' }
        }],
        dataZoom: [{ type: 'inside', start: 0, end: 100 }]
    });

    var typeChart = echarts.init(document.getElementById('typeChart'));
    typeChart.setOption({
        tooltip: { trigger: 'item', formatter: '{b}: {c} ({d}%)' },
        legend: { type: 'scroll', orient: 'vertical', right: 10, top: 20, bottom: 20 },
        series: [{
            name: '问题类型',
            type: 'pie',
            radius: ['40%', '70%'],
            avoidLabelOverlap: false,
            itemStyle: { borderRadius: 10, borderColor: '#fff', borderWidth: 2 },
            label: { show: false, position: 'center' },
            emphasis: { label: { show: true, fontSize: 16, fontWeight: 'bold' } },
            labelLine: { show: false },
            data: pieData
        }]
    });

    var yearChart = echarts.init(document.getElementById('yearChart'));
    yearChart.setOption({
        tooltip: { trigger: 'axis' },
        legend: { data: ['问题数量'] },
        grid: { left: '3%', right: '4%', bottom: '3%', containLabel: true },
        xAxis: { type: 'category', data: yearsData },
        yAxis: { type: 'value', name: '问题数' },
        series: [{
            name: '问题数量',
            type: 'bar',
            data: yearlyQuestionsData,
            itemStyle: {
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                    { offset: 0, color: '#83bff6' },
                    { offset: 1, color: '#5470C6' }
                ])
            }
        }]
    });

    var companyChart = echarts.init(document.getElementById('companyChart'));
    companyChart.setOption({
        tooltip: { trigger: 'axis' },
        legend: { data: ['公司数量'] },
        grid: { left: '3%', right: '4%', bottom: '3%', containLabel: true },
        xAxis: { type: 'category', boundaryGap: false, data: monthsData },
        yAxis: { type: 'value', name: '公司数' },
        series: [{
            name: '公司数量',
            type: 'line',
            smooth: true,
            data: companiesData,
            areaStyle: { opacity: 0.3 },
            lineStyle: { width: 2 },
            itemStyle: { color: '#91CC75' }
        }],
        dataZoom: [{ type: 'inside', start: 0, end: 100 }]
    });

    window.addEventListener('resize', function() {
        trendChart.resize();
        typeChart.resize();
        yearChart.resize();
        companyChart.resize();
    });
});
</script>

## 完整公司列表

共计 **""" + str(total_companies) + """** 家公司：

"""

for i, company in enumerate(unique_companies, 1):
    page += str(i) + '. ' + company + '\n'

with open('statistics.md', 'w', encoding='utf-8') as f:
    f.write(page)

print("Statistics page generated!")
print("Total: {} periods, {} companies, {} questions".format(total_periods, total_companies, total_questions))
