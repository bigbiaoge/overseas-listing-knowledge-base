import re
import os
from collections import defaultdict
import json

def parse_file(filepath):
    """解析单个markdown文件，提取公司名称、问题类型和具体问题"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取日期范围
    date_match = re.search(r'\((\d{4})年(\d{1,2})月(\d{1,2})日.*?(\d{4})年(\d{1,2})月(\d{1,2})日\)', content)
    if date_match:
        end_date = f"{date_match.group(1)}-{int(date_match.group(2)):02d}-{int(date_match.group(3)):02d}"
    else:
        end_date = "Unknown"
    
    # 提取公司名称和对应问题
    # 匹配公司名称（通常是独立一行，后面跟着问题）
    companies = []
    lines = content.split('\n')
    current_company = None
    current_questions = []
    
    for line in lines:
        line = line.strip()
        # 跳过标题和空行
        if not line or line.startswith('**') or line.startswith('请你公司'):
            continue
        
        # 公司名称通常以"XXX"格式出现，后面跟着"请你公司补充说明"
        if '请你公司补充说明以下事项' in line or '请你公司补充说明' in line:
            continue
        
        # 如果遇到新的公司名称，保存当前公司
        if current_company and (line.startswith('一、') or line.startswith('二、') or 
                                  line.startswith('三、') or line.startswith('四、') or
                                  line.startswith('五、') or line.startswith('六、') or
                                  line.startswith('七、') or line.startswith('八、') or
                                  line.startswith('九、') or line.startswith('十、')):
            # 继续累积问题
            current_questions.append(line)
        elif line and not line.startswith('##') and not line.startswith('请你公司'):
            # 检查是否是公司名称
            if len(line) < 20 and not line.startswith('一、') and not line.startswith('（'):
                if current_company:
                    # 保存前一个公司
                    companies.append({
                        'name': current_company,
                        'questions': current_questions
                    })
                current_company = line
                current_questions = []
    
    # 保存最后一个公司
    if current_company:
        companies.append({
            'name': current_company,
            'questions': current_questions
        })
    
    return {
        'date': end_date,
        'companies': companies,
        'filepath': filepath
    }

def classify_question(question):
    """根据问题内容分类"""
    question_lower = question.lower()
    
    # 股权变动/股权代持
    if any(kw in question for kw in ['股权变动', '股权代持', '代持', '股权转让', '增资', '股权激励', '员工持股']):
        return '股权变动/代持'
    
    # 股权架构/VIE架构
    if any(kw in question for kw in ['股权架构', '红筹架构', 'VIE', '协议控制', '架构搭建', '返程并购']):
        return '股权架构/VIE'
    
    # 股东/实际控制人
    if any(kw in question for kw in ['股东', '实际控制人', '穿透', '5%以上']):
        return '股东/实际控制人'
    
    # 外汇登记
    if any(kw in question for kw in ['外汇登记', '37号文', '外汇管理', '境外投资']):
        return '外汇/境外投资'
    
    # 关联交易
    if any(kw in question for kw in ['关联交易', '关联关系', '利益输送', '同业竞争']):
        return '关联交易/同业竞争'
    
    # 合规问题
    if any(kw in question for kw in ['合规性', '合法合规', '合法合规性', '禁止性情形', '法律法规']):
        return '合规问题'
    
    # 募集资金用途
    if any(kw in question for kw in ['募集资金', '募集资金用途', '超募', '发行数量']):
        return '募集资金用途'
    
    # 全流通
    if any(kw in question for kw in ['全流通', '流通股份', '减持']):
        return '全流通'
    
    # 董监高
    if any(kw in question for kw in ['董监高', '董事', '监事', '高管', '永久居留权']):
        return '董监高'
    
    # 业务经营/经营范围
    if any(kw in question for kw in ['经营范围', '主营业务', '业务经营', '业务开展', '许可经营']):
        return '业务经营/经营范围'
    
    # 财务问题
    if any(kw in question for kw in ['财务', '收入', '利润', '亏损', '净资产']):
        return '财务问题'
    
    # 诉讼/仲裁
    if any(kw in question for kw in ['诉讼', '仲裁', '重大诉讼', '法律纠纷']):
        return '诉讼/仲裁'
    
    # 备案材料/招股说明书
    if any(kw in question for kw in ['备案材料', '招股说明书', '备案报告']):
        return '备案材料'
    
    # 保密/档案管理
    if any(kw in question for kw in ['保密', '档案管理', '信息安全']):
        return '保密/档案管理'
    
    # 国有股东
    if any(kw in question for kw in ['国有股东', '国有资产', '国有股']):
        return '国有股东'
    
    # 知识产权/专利
    if any(kw in question for kw in ['知识产权', '专利', '商标']):
        return '知识产权/专利'
    
    # 税务
    if any(kw in question for kw in ['税务', '税费', '税收']):
        return '税务'
    
    # 人类遗传资源
    if any(kw in question for kw in ['人类遗传资源', '干细胞', '基因']):
        return '人类遗传资源'
    
    # 境外子公司
    if any(kw in question for kw in ['境外子公司', '境外投资', '境外公司']):
        return '境外子公司'
    
    # 控制权
    if any(kw in question for kw in ['控制权', '控制权变更']):
        return '控制权'
    
    # AI技术
    if any(kw in question for kw in ['AI', '人工智能', '大模型']):
        return 'AI技术'
    
    # 其他
    return '其他'

def main():
    data_dir = '境外上市备案知识库/原始数据'
    all_data = []
    
    # 解析所有markdown文件
    for filename in sorted(os.listdir(data_dir)):
        if filename.endswith('.md'):
            filepath = os.path.join(data_dir, filename)
            parsed = parse_file(filepath)
            all_data.append(parsed)
    
    # 统计信息
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
    
    # 输出统计
    print(f"总条目数（公司数）: {total_companies}")
    print(f"总问题数: {len(all_questions)}")
    print(f"问题类型统计:")
    for qtype, items in sorted(question_types.items(), key=lambda x: -len(x[1])):
        print(f"  {qtype}: {len(items)}")
    
    # 保存解析结果
    with open('境外上市备案知识库/parsed_data.json', 'w', encoding='utf-8') as f:
        json.dump({
            'all_data': all_data,
            'question_types': {k: [{'date': i['date'], 'company': i['company'], 'question': i['question']} for i in v] 
                             for k, v in question_types.items()}
        }, f, ensure_ascii=False, indent=2)
    
    print("\n数据已保存到 parsed_data.json")

if __name__ == '__main__':
    main()
