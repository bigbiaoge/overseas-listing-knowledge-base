import json
import os
from collections import defaultdict
from datetime import datetime

def load_parsed_data():
    with open('境外上市备案知识库/parsed_data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def create_time_sorted_readme(data):
    """按时间顺序整理"""
    # 按月份分组
    months = defaultdict(list)
    
    for item in data['all_data']:
        date = item['date']
        if date == 'Unknown':
            continue
        
        # 提取年月
        year_month = date[:7]  # YYYY-MM
        months[year_month].append(item)
    
    # 生成Markdown内容
    content = []
    content.append("# 境外发行上市备案补充材料要求 - 按时间顺序")
    content.append("")
    content.append("本目录按时间倒序整理所有境外发行上市备案补充材料要求。")
    content.append("")
    content.append("---\n")
    
    # 按月份排序（倒序）
    for year_month in sorted(months.keys(), reverse=True):
        content.append(f"\n## {year_month}\n")
        
        # 获取该月所有条目
        month_items = sorted(months[year_month], key=lambda x: x['date'], reverse=True)
        
        for item in month_items:
            date = item['date']
            content.append(f"### {date}\n")
            
            for company in item['companies']:
                content.append(f"#### {company['name']}")
                content.append("")
                content.append("**具体问题**：")
                
                for i, q in enumerate(company['questions'], 1):
                    content.append(f"{i}. {q}")
                content.append("")
            
            # 添加来源链接
            content.append(f"> 来源：[证监会官网](https://www.csrc.gov.cn/csrc/c100098/common_list.shtml)")
            content.append("")
    
    return '\n'.join(content)

def main():
    data = load_parsed_data()
    content = create_time_sorted_readme(data)
    
    with open('境外上市备案知识库/按时间顺序/README.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("按时间顺序整理完成，已保存到 境外上市备案知识库/按时间顺序/README.md")

if __name__ == '__main__':
    main()
