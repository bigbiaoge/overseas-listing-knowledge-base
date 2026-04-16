# 知识库更新脚本

#!/bin/bash

# ===========================================
# 证监会境外发行上市备案知识库更新脚本
# ===========================================

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 目录设置
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WEBSITE_DIR="$(dirname "$SCRIPT_DIR")"
DATA_DIR="$WEBSITE_DIR/原始数据"

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}  境外上市备案知识库更新脚本${NC}"
echo -e "${GREEN}========================================${NC}"

# 1. 检查依赖
echo -e "\n${YELLOW}[1/5] 检查依赖...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}错误: 需要 Python 3${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Python 3 已安装${NC}"

# 2. 备份现有数据
echo -e "\n${YELLOW}[2/5] 备份现有数据...${NC}"
BACKUP_DIR="$WEBSITE_DIR/backup_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"
cp -r "$DATA_DIR" "$BACKUP_DIR/"
echo -e "${GREEN}✓ 数据已备份到 $BACKUP_DIR${NC}"

# 3. 爬取最新数据
echo -e "\n${YELLOW}[3/5] 爬取最新数据...${NC}"
# 注意：这里需要根据实际的爬虫脚本进行调整
# python3 "$WEBSITE_DIR/parse_data.py" || echo "爬取失败，使用现有数据"

# 如果没有爬虫脚本，可以手动下载证监会官网数据
if [ ! -f "$WEBSITE_DIR/fetch_data.py" ]; then
    echo -e "${YELLOW}提示: 未找到爬虫脚本，请手动下载最新数据到 原始数据/ 目录${NC}"
    echo -e "${YELLOW}官网地址: https://www.csrc.gov.cn/csrc/c100098/common_list.shtml${NC}"
fi

# 4. 更新解析数据
echo -e "\n${YELLOW}[4/5] 更新解析数据...${NC}"
cd "$WEBSITE_DIR"

# 重新解析数据并生成页面
python3 << 'PYTHON_SCRIPT'
import os
import re
import json
from collections import defaultdict, Counter
from pathlib import Path

print("开始解析数据...")

# 问题类型关键词
question_type_keywords = {
    '股东/实际控制人': ['股东', '实际控制人', '控股股东', '持股'],
    '股权变动/代持': ['股权变动', '代持', '增资', '转让', '减资', '股权激励'],
    '业务经营/经营范围': ['业务经营', '经营范围', '经营情况', '主营业务'],
    '外汇/境外投资': ['外汇', '境外投资', 'ODI', '外汇登记'],
    '合规问题': ['合规', '违法违规', '行政处罚', '处罚'],
    '股权架构/VIE': ['VIE', '股权架构', '协议控制'],
    '全流通': ['全流通', '流通股东', '减持'],
    '募集资金用途': ['募集资金', '募投项目', '资金用途'],
    '关联交易/同业竞争': ['关联交易', '同业竞争'],
    '诉讼/仲裁': ['诉讼', '仲裁', '纠纷'],
    '财务问题': ['财务', '收入', '利润', '毛利率'],
    'AI技术': ['AI', '人工智能', '大模型', 'ChatGPT'],
    '人类遗传资源': ['人类遗传资源', '基因', '干细胞'],
    '税务': ['税务', '纳税', '税收'],
    '控制权': ['控制权', '控制权变更'],
    '保密/档案管理': ['保密', '档案管理'],
    '董监高': ['董事', '监事', '高级管理人员', '董监高'],
    '国有股东': ['国有股东', '国资'],
    '数据安全/个人信息': ['个人信息', '数据安全', '信息保护']
}

def classify_question(question_text):
    matched_types = []
    for qtype, keywords in question_type_keywords.items():
        for keyword in keywords:
            if keyword in question_text:
                matched_types.append(qtype)
                break
    return matched_types if matched_types else ['其他']

def parse_company_questions(body, company_name):
    pattern = f'{re.escape(company_name)}\\n\\n请你公司.*?(?=\\n\\n[^\\n]{{2,30}}?\\n\\n请你公司|$)'
    match = re.search(pattern, body, re.DOTALL)
    if not match:
        return []
    
    company_content = match.group(0)
    questions = []
    question_pattern = r'[一二三四五六七八九十]+[\\.、](.*?)(?=[一二三四五六七八九十]+[\\.、]|$)'
    question_matches = re.findall(question_pattern, company_content, re.DOTALL)
    
    for q in question_matches:
        q = q.strip()
        if len(q) > 10:
            questions.append(q)
    return questions

# 解析原始数据
raw_data_dir = Path('原始数据')
timeline_data = defaultdict(list)

for md_file in sorted(raw_data_dir.glob('*.md')):
    filename = md_file.stem
    match = re.match(r'(\d{4}-\d{2}-\d{2})_(\d{2}(?:-\d{2})?)', filename)
    if match:
        start_date = match.group(1)
        period = match.group(2)
        year = start_date[:4]
        
        content = md_file.read_text(encoding='utf-8')
        body_match = re.search(r'国际司共对.*?具体如下：(.*)', content, re.DOTALL)
        if not body_match:
            continue
            
        body = body_match.group(1)
        company_pattern = r'([^\n]{2,30}?)\n\n请你公司'
        company_matches = re.findall(company_pattern, body)
        
        companies = []
        for cm in company_matches:
            cm = cm.strip()
            if cm and len(cm) > 1:
                questions = parse_company_questions(body, cm)
                qtypes = []
                for q in questions:
                    qtypes.extend(classify_question(q))
                
                if questions:
                    companies.append({
                        'name': cm,
                        'questions': questions,
                        'types': list(set(qtypes))
                    })
        
        if companies:
            timeline_data[year].append({
                'filename': filename,
                'start_date': start_date,
                'period': period,
                'companies': companies
            })

# 统计
type_counter = Counter()
for year, periods in timeline_data.items():
    for period in periods:
        for company in period['companies']:
            for q in company['questions']:
                for t in classify_question(q):
                    type_counter[t] += 1

# 输出统计
print(f"已解析 {sum(len(p['companies']) for p in sum(timeline_data.values(), []))} 家公司")
print(f"共 {sum(type_counter.values())} 条问题")
print("问题类型分布:")
for qtype, count in type_counter.most_common(5):
    print(f"  - {qtype}: {count}")

# 保存数据
output = {
    'timeline': dict(timeline_data),
    'question_types': dict(type_counter),
    'last_updated': str(Path('原始数据').stat().st_mtime)
}

with open('website/parsed_data_full.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("数据已更新: website/parsed_data_full.json")
PYTHON_SCRIPT

echo -e "${GREEN}✓ 数据解析完成${NC}"

# 5. 重新生成页面
echo -e "\n${YELLOW}[5/5] 重新生成页面...${NC}"
python3 << 'PYTHON_SCRIPT'
import json
from pathlib import Path
from collections import defaultdict

# 加载数据
with open('website/parsed_data_full.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

timeline = data['timeline']

def generate_year_page(year, year_data):
    content = f"""---
title: {year}年境外上市备案补充材料要求
description: {year}年证监会境外发行上市备案补充材料要求汇总
---

# {year}年境外发行上市备案补充材料要求

本页面汇总了{year}年所有境外发行上市备案补充材料要求，共**{len(year_data)}期**，涉及**{sum(len(item['companies']) for item in year_data)}家公司**。

"""
    
    for item in sorted(year_data, key=lambda x: x['start_date'], reverse=True):
        content += f"""## 📅 {item['start_date']}（{item['period']}期）

"""
        for company in item['companies']:
            content += f"""### {company['name']}

"""
            for i, q in enumerate(company['questions'], 1):
                content += f"{i}. {q}\n\n"
    
    return content

# 生成年份页面
for year in ['2026', '2025', '2024', '2023']:
    if year in timeline:
        content = generate_year_page(year, timeline[year])
        Path(f'website/timeline/{year}.md').write_text(content, encoding='utf-8')
        print(f"已更新: timeline/{year}.md")

print("页面更新完成")
PYTHON_SCRIPT

echo -e "${GREEN}✓ 页面已更新${NC}"

echo -e "\n${GREEN}========================================${NC}"
echo -e "${GREEN}  更新完成！${NC}"
echo -e "${GREEN}========================================${NC}"
echo -e "\n下一步:"
echo -e "1. 运行 ${YELLOW}npm run build${NC} 构建网站"
echo -e "2. 部署到 Cloudflare Pages 或其他托管平台"
