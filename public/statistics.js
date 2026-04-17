// 统计数据
var monthsData = ["2023-04", "2023-05", "2023-06", "2023-07", "2023-08", "2023-09", "2023-10", "2023-11", "2023-12", "2024-01", "2024-02", "2024-03", "2024-04", "2024-05", "2024-06", "2024-07", "2024-08", "2024-09", "2024-10", "2024-11", "2024-12", "2025-01", "2025-02", "2025-03", "2025-04", "2025-05", "2025-06", "2025-07", "2025-08", "2025-09", "2025-10", "2025-11", "2025-12", "2026-01", "2026-02", "2026-03", "2026-04"];
var questionsData = [30, 70, 117, 114, 150, 95, 29, 40, 33, 57, 63, 69, 30, 60, 88, 86, 54, 9, 9, 14, 17, 49, 55, 131, 79, 70, 110, 125, 160, 145, 189, 202, 191, 178, 15, 132, 49];
var companiesData = [7, 17, 21, 24, 41, 22, 8, 10, 7, 19, 16, 19, 8, 12, 22, 18, 16, 3, 4, 5, 4, 11, 17, 36, 26, 15, 25, 29, 37, 34, 40, 35, 36, 38, 4, 34, 11];
var pieData = [{"name":"其他","value":850},{"name":"外资准入","value":388},{"name":"股权变动-代持","value":354},{"name":"全流通","value":293},{"name":"数据安全-个人信息","value":272},{"name":"合规问题","value":245},{"name":"股东-实际控制人","value":206},{"name":"外汇-境外投资","value":177},{"name":"募集资金用途","value":109},{"name":"国有股东","value":72},{"name":"业务经营-经营范围","value":70},{"name":"关联交易-同业竞争","value":28},{"name":"税务","value":25},{"name":"独立性","value":13},{"name":"股权架构-VIE","value":7},{"name":"保密-档案管理","value":5}];
var yearsData = ["2023", "2024", "2025", "2026"];
var yearlyQuestionsData = [678, 556, 1506, 374];

document.addEventListener('DOMContentLoaded', function() {
    if (typeof echarts === 'undefined') return;
    
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
