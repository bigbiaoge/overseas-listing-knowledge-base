#!/usr/bin/env python3
"""
从 parsed_data.json 生成网站页面
"""

import json
from pathlib import Path
from collections import defaultdict

def load_data():
    """加载解析好的数据"""
    with open('../parsed_data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def load_links():
    """加载链接数据"""
    links_file = Path('../links_data.json')
    if links_file.exists():
        with open(links_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def get_period_title(filename):
    """从文件名获取期号标题"""
    # 文件名格式: 2025-01-03_09.md 或 2025-12-22_26.md
    parts = filename.replace('.md', '').split('_')
    if len(parts) == 2:
        start_date = parts[0]
        end_period = parts[1]
        year, month, day = start_date.split('-')
        # 计算结束日期
        if '-' in end_period:
            end_day = end_period.split('-')[1]
        else:
            end_day = end_period
        
        return f"境外发行上市备案补充材料要求公示（{year}年{int(month)}月{int(day)}日—{year}年{int(month)}月{int(end_day)}日）"
    return filename

def get_date_key_from_filename(filename):
    """从文件名提取日期键，用于匹配链接"""
    # 文件名格式: 2025-01-03_09.md
    parts = filename.replace('.md', '').split('_')
    if len(parts) >= 1:
        return parts[0]  # 返回开始日期
    return None

def generate_year_page(year, year_data, links_data):
    """生成某一年的页面"""
    
    # 统计
    total_periods = len(year_data)
    total_companies = sum(len(item['companies']) for item in year_data)
    
    content = f"""---
title: {year}年境外上市备案补充材料要求
description: {year}年证监会境外发行上市备案补充材料要求汇总
---

# {year}年境外发行上市备案补充材料要求

本页面汇总了{year}年所有境外发行上市备案补充材料要求，共**{total_periods}期**，涉及**{total_companies}家公司**。

"""
    
    # 按日期倒序排列
    for item in sorted(year_data, key=lambda x: x['date'], reverse=True):
        # 获取期号标题
        filename = Path(item.get('filepath', '')).stem
        period_title = get_period_title(filename)
        date_key = get_date_key_from_filename(filename)
        
        content += f"""## {period_title}

"""
        
        # 添加原文链接
        if date_key and date_key in links_data:
            url = links_data[date_key]['url']
            content += f"""📎 **原文链接**：{url}

"""
        
        # 添加公司信息
        for company in item['companies']:
            company_name = company['name']
            questions = company['questions']
            
            content += f"""### {company_name}

"""
            
            if questions:
                for i, q in enumerate(questions, 1):
                    # 如果问题以"一、"开头，保持原样
                    if q.startswith(('一、', '二、', '三、', '四、', '五、', '六、', '七、', '八、', '九、', '十、')):
                        content += f"{q}\n\n"
                    else:
                        content += f"{i}. {q}\n\n"
            else:
                content += "\n"
        
        content += "\n"
    
    return content

def main():
    print("开始生成页面...")
    
    # 加载数据
    data = load_data()
    all_data = data['all_data']
    links_data = load_links()
    print(f"加载了 {len(links_data)} 条链接数据")
    
    # 按年份分组
    years_data = defaultdict(list)
    for item in all_data:
        year = item['date'][:4]
        if year != 'Unkn':  # 跳过未知日期
            years_data[year].append(item)
    
    # 生成各年份页面
    output_dir = Path('../timeline')
    output_dir.mkdir(exist_ok=True)
    
    for year in ['2023', '2024', '2025', '2026']:
        if year in years_data:
            print(f"生成 {year} 年页面...")
            content = generate_year_page(year, years_data[year], links_data)
            output_file = output_dir / f'{year}.md'
            output_file.write_text(content, encoding='utf-8')
            print(f"  已保存: {output_file}")
    
    print("\n页面生成完成！")

if __name__ == '__main__':
    main()
