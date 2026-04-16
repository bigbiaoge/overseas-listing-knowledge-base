import json
import os
from collections import defaultdict

def load_parsed_data():
    with open('境外上市备案知识库/parsed_data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def create_question_type_readme(data):
    """按问题类型分类整理"""
    content = []
    content.append("# 境外发行上市备案补充材料要求 - 按问题类型分类")
    content.append("")
    content.append("本目录按问题类型分类整理所有境外发行上市备案补充材料要求。")
    content.append("")
    content.append("---\n")
    
    question_types = data['question_types']
    
    # 按问题数量排序
    sorted_types = sorted(question_types.items(), key=lambda x: -len(x[1]))
    
    for qtype, items in sorted_types:
        content.append(f"\n## {qtype}")
        content.append("")
        content.append(f"**问题数量**: {len(items)}")
        content.append("")
        content.append("| 序号 | 发文日期 | 公司名称 | 具体问题 |")
        content.append("|------|----------|----------|----------|")
        
        for i, item in enumerate(items, 1):
            # 截断过长的问题
            question = item['question']
            if len(question) > 100:
                question = question[:100] + "..."
            
            # 转义表格中的竖线
            question = question.replace('|', '\\|')
            
            content.append(f"| {i} | {item['date']} | {item['company']} | {question} |")
        
        content.append("")
    
    return '\n'.join(content)

def main():
    data = load_parsed_data()
    content = create_question_type_readme(data)
    
    with open('境外上市备案知识库/按问题类型/README.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("按问题类型整理完成，已保存到 境外上市备案知识库/按问题类型/README.md")

if __name__ == '__main__':
    main()
