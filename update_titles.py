#!/usr/bin/env python3
"""
更新境外上市备案知识库的标题格式和链接
从原始数据文件中提取标题和日期范围
"""

import re
import os
import glob

# 从证监会官网获取的链接映射 (日期范围 -> URL)
LINK_MAP = {
    # 2026年
    "2026年4月7日—2026年4月10日": "http://www.csrc.gov.cn/csrc/c100098/c7625725/content.shtml",
    "2026年3月30日—2026年4月3日": "http://www.csrc.gov.cn/csrc/c100098/c7624298/content.shtml",
    "2026年3月23日—2026年3月27日": "http://www.csrc.gov.cn/csrc/c100098/c7622709/content.shtml",
    "2026年3月16日—2026年3月20日": "http://www.csrc.gov.cn/csrc/c100098/c7621321/content.shtml",
    "2026年3月3日—2026年3月13日": "http://www.csrc.gov.cn/csrc/c100098/c7620010/content.shtml",
    "2026年2月9日—2026年3月2日": "http://www.csrc.gov.cn/csrc/c100098/c7617372/content.shtml",
    "2026年2月2日—2026年2月6日": "http://www.csrc.gov.cn/csrc/c100098/c7614254/content.shtml",
    "2026年1月26日—2026年1月30日": "http://www.csrc.gov.cn/csrc/c100098/c7612550/content.shtml",
    "2026年1月19日—2026年1月23日": "http://www.csrc.gov.cn/csrc/c100098/c7610921/content.shtml",
    "2026年1月12日—2026年1月16日": "http://www.csrc.gov.cn/csrc/c100098/c7609744/content.shtml",
    "2026年1月5日—2026年1月9日": "http://www.csrc.gov.cn/csrc/c100098/c7608139/content.shtml",
    # 2025年
    "2025年12月29日—2026年1月4日": "http://www.csrc.gov.cn/csrc/c100098/c7606660/content.shtml",
    "2025年12月22日—2025年12月26日": "http://www.csrc.gov.cn/csrc/c100098/c7604980/content.shtml",
    "2025年12月15日—2025年12月19日": "http://www.csrc.gov.cn/csrc/c100098/c7603466/content.shtml",
    "2025年12月8日—2025年12月12日": "http://www.csrc.gov.cn/csrc/c100098/c7601771/content.shtml",
    "2025年12月1日—2025年12月5日": "http://www.csrc.gov.cn/csrc/c100098/c7600150/content.shtml",
    "2025年11月24日—2025年11月28日": "http://www.csrc.gov.cn/csrc/c100098/c7598280/content.shtml",
    "2025年11月17日—2025年11月21日": "http://www.csrc.gov.cn/csrc/c100098/c7596555/content.shtml",
    "2025年11月10日—2025年11月14日": "http://www.csrc.gov.cn/csrc/c100098/c7595394/content.shtml",
    "2025年11月3日—2025年11月7日": "http://www.csrc.gov.cn/csrc/c100098/c7593889/content.shtml",
    "2025年10月27日—2025年10月31日": "http://www.csrc.gov.cn/csrc/c100098/c7592322/content.shtml",
    "2025年10月20日—2025年10月24日": "http://www.csrc.gov.cn/csrc/c100098/c7591047/content.shtml",
    "2025年10月12日—2025年10月17日": "http://www.csrc.gov.cn/csrc/c100098/c7589856/content.shtml",
    "2025年9月26日—2025年10月11日": "http://www.csrc.gov.cn/csrc/c100098/c7588110/content.shtml",
    "2025年9月19日—2025年9月25日": "http://www.csrc.gov.cn/csrc/c100098/c7585848/content.shtml",
    "2025年9月12日—2025年9月18日": "http://www.csrc.gov.cn/csrc/c100098/c7584475/content.shtml",
    "2025年9月5日—2025年9月11日": "http://www.csrc.gov.cn/csrc/c100098/c7583189/content.shtml",
    "2025年8月29日—2025年9月4日": "http://www.csrc.gov.cn/csrc/c100098/c7581728/content.shtml",
    "2025年8月22日—2025年8月28日": "http://www.csrc.gov.cn/csrc/c100098/c7580441/content.shtml",
    "2025年8月15日—2025年8月21日": "http://www.csrc.gov.cn/csrc/c100098/c7579266/content.shtml",
    "2025年8月8日—2025年8月14日": "http://www.csrc.gov.cn/csrc/c100098/c7577666/content.shtml",
    "2025年8月1日—2025年8月7日": "http://www.csrc.gov.cn/csrc/c100098/c7576302/content.shtml",
    "2025年7月25日—2025年7月31日": "http://www.csrc.gov.cn/csrc/c100098/c7574963/content.shtml",
    "2025年7月18日—2025年7月24日": "http://www.csrc.gov.cn/csrc/c100098/c7573497/content.shtml",
    "2025年7月4日—2025年7月10日": "http://www.csrc.gov.cn/csrc/c100098/c7570804/content.shtml",
    "2025年6月27日—2025年7月3日": "http://www.csrc.gov.cn/csrc/c100098/c7569317/content.shtml",
    "2025年6月20日—2025年6月26日": "http://www.csrc.gov.cn/csrc/c100098/c7567476/content.shtml",
    "2025年6月13日—2025年6月19日": "http://www.csrc.gov.cn/csrc/c100098/c7565708/content.shtml",
    "2025年6月6日—2025年6月12日": "http://www.csrc.gov.cn/csrc/c100098/c7564432/content.shtml",
    "2025年5月30日—2025年6月5日": "http://www.csrc.gov.cn/csrc/c100098/c7562892/content.shtml",
    "2025年5月23日—2025年5月29日": "http://www.csrc.gov.cn/csrc/c100098/c7561656/content.shtml",
    "2025年5月16日—2025年5月22日": "http://www.csrc.gov.cn/csrc/c100098/c7560148/content.shtml",
    "2025年5月12日—2025年5月15日": "http://www.csrc.gov.cn/csrc/c100098/c7558565/content.shtml",
    "2025年4月25日—2025年5月9日": "http://www.csrc.gov.cn/csrc/c100098/c7556671/content.shtml",
    "2025年4月18日—2025年4月24日": "http://www.csrc.gov.cn/csrc/c100098/c7553567/content.shtml",
    "2025年4月11日—2025年4月17日": "http://www.csrc.gov.cn/csrc/c100098/c7552373/content.shtml",
    "2025年4月3日—2025年4月10日": "http://www.csrc.gov.cn/csrc/c100098/c7550985/content.shtml",
    "2025年3月28日—2025年4月2日": "http://www.csrc.gov.cn/csrc/c100098/c7549184/content.shtml",
    "2025年3月21日—2025年3月27日": "http://www.csrc.gov.cn/csrc/c100098/c7547922/content.shtml",
    "2025年3月14日—2025年3月20日": "http://www.csrc.gov.cn/csrc/c100098/c7546039/content.shtml",
    "2025年2月28日—2025年3月6日": "http://www.csrc.gov.cn/csrc/c100098/c7543140/content.shtml",
    "2025年2月21日—2025年2月27日": "http://www.csrc.gov.cn/csrc/c100098/c7541830/content.shtml",
}


def extract_date_range_from_source(filepath):
    """从原始数据文件中提取日期范围"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 匹配日期范围格式: **（2026年4月7日---2026年4月10日）** 或 **（2026年3月23日------2026年3月27日）**
    # 支持 --- 或 ------ 分隔符
    pattern = r'\*\*（(\d{4}年\d{1,2}月\d{1,2}日)[-—]{3,}(\d{4}年\d{1,2}月\d{1,2}日)）\*\*'
    match = re.search(pattern, content)
    if match:
        start_date = match.group(1)
        end_date = match.group(2)
        return f"{start_date}—{end_date}"
    return None


def get_title_from_date_range(date_range):
    """根据日期范围构建完整标题"""
    if date_range:
        return f"境外发行上市备案补充材料要求公示（{date_range}）"
    return None


def build_link_map_from_sources():
    """从原始数据文件构建日期范围到链接的映射"""
    source_dir = "./境外上市备案知识库/原始数据"
    result = {}
    
    # 获取所有2025和2026年的md文件
    for filepath in sorted(glob.glob(f"{source_dir}/*.md")):
        filename = os.path.basename(filepath)
        
        # 只处理2025和2026年的文件
        if not (filename.startswith("2025-") or filename.startswith("2026-")):
            continue
        
        date_range = extract_date_range_from_source(filepath)
        if date_range:
            # 查找对应的链接
            url = LINK_MAP.get(date_range)
            result[date_range] = {
                'title': get_title_from_date_range(date_range),
                'url': url
            }
    
    return result


def update_file(filepath, title_map):
    """更新单个文件的标题格式"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    updates_count = 0
    
    # 对每个日期范围，替换简化标题
    for date_range, info in sorted(title_map.items(), reverse=True):
        title = info['title']
        url = info['url']
        
        # 从date_range中提取开始日期来构建正则
        # 例如: 2026年4月7日—2026年4月10日
        start_match = re.match(r'(\d{4}年)(\d{1,2}月)(\d{1,2}日)—.*', date_range)
        if start_match:
            year = start_match.group(1)[:-1]  # 去掉"年"
            month = start_match.group(2)[:-1]  # 去掉"月"
            day = start_match.group(3)[:-1]  # 去掉"日"
            
            # 构建要匹配的模式
            # 例如: ## 📅 2026-04-07（10期） 或 ## 📅 2026-03-30（04-03期）
            old_pattern = rf'## 📅 {year}-{month.zfill(2)}-{day.zfill(2)}（[^）]+\）'
            
            if url:
                new_title = f"## {title}\n\n📎 **原文链接**：{url}\n"
            else:
                new_title = f"## {title}\n"
            
            new_content = re.sub(old_pattern, new_title, content)
            if new_content != content:
                updates_count += 1
                content = new_content
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return updates_count
    return 0


def main():
    # 构建日期范围到标题和链接的映射
    title_map = build_link_map_from_sources()
    
    print("从原始数据中提取的日期范围和链接：")
    for dr, info in sorted(title_map.items()):
        url_status = "✓" if info['url'] else "✗"
        print(f"  {dr}: {url_status}")
    
    # 更新文件
    base_dir = "./境外上市备案知识库/website/timeline"
    
    total_updates = 0
    for year_file in ["2026.md", "2025.md"]:
        filepath = os.path.join(base_dir, year_file)
        if os.path.exists(filepath):
            print(f"\n处理文件: {filepath}")
            updates = update_file(filepath, title_map)
            if updates > 0:
                print(f"  ✓ 已更新 {updates} 个标题")
                total_updates += updates
            else:
                print(f"  - 无需更新")
    
    print(f"\n总共更新了 {total_updates} 个标题")


if __name__ == "__main__":
    main()
