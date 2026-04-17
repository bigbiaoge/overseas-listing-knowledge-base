#!/usr/bin/env python3
"""
境外上市备案知识库解析脚本 - 最终版
解决引导语断开、公司名识别不完整等问题

关键修复：
1. 引导语断开处理（龙电华鑫）- 跳过空行检测
2. 问题行识别（非一、二开头的问题，如双林股份）
3. 完整性验证
4. 往前找公司名时跳过引导语前缀
"""

import re
import os
import json
from collections import defaultdict

# ==================== 引导语模式库 ====================
INTRO_FULL_PATTERNS = [
    r'请你公司补充说明以下事项，请律师核查并出具明确的法律意见[：:]',
    r'请你补充说明以下事项，请律师核查并出具明确的法律意见[：:]',
    r'请你补充说明以下事项，请律师核查并明确的法律意见[：:]',
    r'就以下事项补充说明，请律师进行核查并出具明确的法律意见[：:]',
]
COMPILED_FULL_PATTERNS = [re.compile(p, re.DOTALL) for p in INTRO_FULL_PATTERNS]

INTRO_PREFIXES = [
    r'^请你公司补充说明以下事项，请律师核查并出具明确的法律意见',
    r'^请你补充说明以下事项，请律师核查并出具明确的法律意见',
    r'^请你公司就以下事项补充说明，请律师进行核查并出具',
    r'^请你补充说明以下事项，请律师进行核查并出具',
]
COMPILED_PREFIXES = [re.compile(p) for p in INTRO_PREFIXES]


def is_intro_prefix(line):
    """检查是否是引导语前缀"""
    line = line.strip()
    if not line:
        return False
    for pattern in COMPILED_PREFIXES:
        if pattern.match(line):
            return True
    return False


def find_intro_in_text(text):
    """在文本中查找完整引导语"""
    for pattern in COMPILED_FULL_PATTERNS:
        match = pattern.search(text)
        if match:
            return match
    return None


def is_summary_line(line):
    """检查是否是摘要行（跳过不解析）"""
    line = line.strip()
    if '本周国际司共对' in line or '本周国际部共对' in line:
        return True
    if '境外发行上市备案补充材料要求' in line:
        return True
    if re.match(r'[（(]\d{4}年\d{1,2}月\d{1,2}日', line):
        return True
    return False


def is_question_start(line):
    """检查是否是以问题序号开头"""
    line = line.strip()
    if not line:
        return False
    if re.match(r'^[一二三四五六七八九十]、', line):
        return True
    if re.match(r'^\d+\.', line):
        return True
    return False


def extract_expected_count(content):
    """从文件中提取预期企业数量"""
    match = re.search(r'本周国际司共对(\d+)家企业', content)
    if match:
        return int(match.group(1))
    return None


def is_likely_question_content(line):
    """检查是否可能是问题内容（不以序号开头的问题，如双林股份）"""
    line = line.strip()
    if not line:
        return False
    if len(line) < 10:
        return False
    if line.startswith('**') or line.startswith('##'):
        return False
    if is_summary_line(line):
        return False
    if is_question_start(line):
        return True
    if is_intro_prefix(line):
        return False
    if line.startswith('请') and '公司' in line:
        return True
    return False


def parse_file(filepath):
    """
    重写的解析逻辑：
    1. 按行扫描，处理引导语断开的情况
    2. 公司名 = 引导语前面的非空行（跳过引导语前缀）
    3. 问题 = 从引导语后开始，直到下一个公司名或文件结束
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    date_match = re.search(r'[（(](\d{4})年(\d{1,2})月(\d{1,2})日.*?(\d{4})年(\d{1,2})月(\d{1,2})日[）)]', content)
    end_date = f"{date_match.group(4)}-{int(date_match.group(5)):02d}-{int(date_match.group(6)):02d}" if date_match else "Unknown"
    expected_count = extract_expected_count(content)
    
    lines = content.split('\n')
    
    companies = []
    current_company = None
    current_questions = []
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        if not line:
            i += 1
            continue
        
        if is_summary_line(line):
            i += 1
            continue
        
        intro_match = find_intro_in_text(line)
        is_intro_line = is_intro_prefix(line)
        
        # 处理引导语断开的情况
        if not intro_match and is_intro_line:
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines):
                next_line = lines[j].strip()
                if next_line == '明确的法律意见：' or next_line == '明确的法律意见:':
                    intro_match = True
                    i = j
        
        if intro_match:
            if current_company:
                companies.append({'name': current_company, 'questions': current_questions})
                current_questions = []
            
            j = i - 1
            while j >= 0:
                prev_line = lines[j].strip()
                if not prev_line:
                    j -= 1
                    continue
                if is_summary_line(prev_line):
                    j -= 1
                    continue
                if is_intro_prefix(prev_line):
                    j -= 1
                    continue
                current_company = prev_line
                break
                j -= 1
            
            i += 1
            while i < len(lines):
                current_line = lines[i].strip()
                if not current_line:
                    i += 1
                    continue
                if is_summary_line(current_line):
                    break
                if is_intro_prefix(current_line):
                    break
                if is_question_start(current_line):
                    current_questions.append(current_line)
                elif is_likely_question_content(current_line):
                    current_questions.append(current_line)
                i += 1
            continue
        
        i += 1
    
    if current_company:
        companies.append({'name': current_company, 'questions': current_questions})
    
    warnings = []
    if expected_count is not None and len(companies) != expected_count:
        warnings.append(f"预期{expected_count}家，实际{len(companies)}家")
    
    return {
        'date': end_date,
        'expected_count': expected_count,
        'actual_count': len(companies),
        'companies': companies,
        'filepath': filepath,
        'warnings': warnings
    }


def classify_question(question):
    """根据问题内容分类"""
    if any(kw in question for kw in ['股权变动', '股权代持', '代持', '股权转让', '增资', '股权激励', '员工持股']):
        return '股权变动/代持'
    if any(kw in question for kw in ['股权架构', '红筹架构', 'VIE', '协议控制', '架构搭建', '返程并购']):
        return '股权架构/VIE'
    if any(kw in question for kw in ['股东', '实际控制人', '穿透', '5%以上']):
        return '股东/实际控制人'
    if any(kw in question for kw in ['外汇登记', '37号文', '外汇管理', '境外投资']):
        return '外汇/境外投资'
    if any(kw in question for kw in ['关联交易', '关联关系', '利益输送', '同业竞争']):
        return '关联交易/同业竞争'
    if any(kw in question for kw in ['合规性', '合法合规', '合法合规性', '禁止性情形', '法律法规']):
        return '合规问题'
    if any(kw in question for kw in ['募集资金', '募集资金用途', '超募', '发行数量']):
        return '募集资金用途'
    if any(kw in question for kw in ['全流通', '流通股份', '减持']):
        return '全流通'
    if any(kw in question for kw in ['董监高', '董事', '监事', '高管', '永久居留权']):
        return '董监高'
    if any(kw in question for kw in ['经营范围', '主营业务', '业务经营', '业务开展', '许可经营']):
        return '业务经营/经营范围'
    if any(kw in question for kw in ['财务', '收入', '利润', '亏损', '净资产']):
        return '财务问题'
    if any(kw in question for kw in ['诉讼', '仲裁', '重大诉讼', '法律纠纷']):
        return '诉讼/仲裁'
    if any(kw in question for kw in ['备案材料', '招股说明书', '备案报告']):
        return '备案材料'
    if any(kw in question for kw in ['保密', '档案管理', '信息安全']):
        return '保密/档案管理'
    if any(kw in question for kw in ['国有股东', '国有资产', '国有股']):
        return '国有股东'
    if any(kw in question for kw in ['知识产权', '专利', '商标']):
        return '知识产权/专利'
    if any(kw in question for kw in ['税务', '税费', '税收']):
        return '税务'
    if any(kw in question for kw in ['人类遗传资源', '干细胞', '基因']):
        return '人类遗传资源'
    if any(kw in question for kw in ['境外子公司', '境外投资', '境外公司']):
        return '境外子公司'
    if any(kw in question for kw in ['控制权', '控制权变更']):
        return '控制权'
    if any(kw in question for kw in ['AI', '人工智能', '大模型']):
        return 'AI技术'
    return '其他'


def main():
    data_dir = '原始数据'
    all_data = []
    all_warnings = []
    
    for filename in sorted(os.listdir(data_dir)):
        if filename.endswith('.md'):
            filepath = os.path.join(data_dir, filename)
            parsed = parse_file(filepath)
            all_data.append(parsed)
            if parsed['warnings']:
                all_warnings.append({
                    'file': filename,
                    'warnings': parsed['warnings'],
                    'expected': parsed['expected_count'],
                    'actual': parsed['actual_count'],
                    'companies': [c['name'] for c in parsed['companies']]
                })
    
    total_companies = 0
    all_questions = []
    question_types = defaultdict(list)
    
    for data in all_data:
        for company in data['companies']:
            total_companies += 1
            for q in company['questions']:
                qtype = classify_question(q)
                question_types[qtype].append({
                    'date': data['date'],
                    'company': company['name'],
                    'question': q,
                    'filepath': data['filepath']
                })
                all_questions.append(q)
    
    print("=" * 70)
    print("境外上市备案知识库解析报告")
    print("=" * 70)
    print(f"\n总条目数（公司数）: {total_companies}")
    print(f"总问题数: {len(all_questions)}")
    print(f"\n问题类型统计:")
    for qtype, items in sorted(question_types.items(), key=lambda x: -len(x[1])):
        print(f"  {qtype}: {len(items)}")
    
    print("\n" + "=" * 70)
    print("各期解析详情:")
    print("=" * 70)
    for data in all_data:
        status = "✓" if not data['warnings'] else "⚠️"
        print(f"\n{status} {data['date']} ({os.path.basename(data['filepath'])}):")
        print(f"  预期: {data['expected_count']}, 实际: {data['actual_count']}")
        if data['warnings']:
            print(f"  警告: {data['warnings']}")
        for c in data['companies']:
            q_count = len(c['questions'])
            print(f"    - {c['name']} ({q_count}个问题)")
    
    if all_warnings:
        print("\n" + "=" * 70)
        print("⚠️ 解析问题汇总:")
        print("=" * 70)
        for w in all_warnings:
            print(f"\n{w['file']}:")
            print(f"  预期 {w['expected']} 家, 解析 {w['actual']} 家")
            print(f"  已解析: {w['companies']}")
    
    with open('parsed_data.json', 'w', encoding='utf-8') as f:
        json.dump({
            'all_data': all_data,
            'question_types': {k: [{'date': i['date'], 'company': i['company'], 'question': i['question']} for i in v] 
                             for k, v in question_types.items()}
        }, f, ensure_ascii=False, indent=2)
    
    print("\n" + "=" * 70)
    print(f"数据已保存到 parsed_data.json")
    print("=" * 70)


if __name__ == '__main__':
    main()
