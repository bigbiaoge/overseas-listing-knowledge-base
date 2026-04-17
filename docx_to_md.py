#!/usr/bin/env python3
"""
docx_to_md.py - 将docx文件正确转换为markdown格式

关键处理：
1. 软换行（Shift+Enter）应该连接同一段落，不生成新行
2. 处理加粗、斜体等格式
3. 保留段落结构
"""

import os
import sys
import re
from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn


def get_paragraph_full_text(para):
    """
    获取段落的完整文本，包括软换行的处理
    
    Word中：
    - Enter键：段落分隔符 (paragraph break)
    - Shift+Enter：行分隔符/软换行 (line break)
    
    【关键修复】软换行应该被转换为换行符，而不是忽略！
    因为软换行通常表示逻辑分隔（如引导语和问题之间的分隔）
    """
    para_xml = para._element.xml
    
    # 使用正则提取文本和软换行的位置
    # 方法：按顺序提取 <w:t> 和 <w:br> 标签
    
    # 构建文本片段列表，保留软换行位置
    parts = []
    
    # 匹配所有文本节点和软换行
    # 使用更精确的正则，按出现顺序处理
    pattern = r'<w:t[^>]*>([^<]*)</w:t>|<w:br[^/]*/>'
    
    for match in re.finditer(pattern, para_xml):
        matched = match.group(0)
        if matched.startswith('<w:t'):
            # 文本节点
            text = re.search(r'<w:t[^>]*>([^<]*)</w:t>', matched).group(1)
            parts.append(text)
        elif '<w:br' in matched:
            # 检查是否是软换行（不是分页符）
            if 'type="page"' not in matched and 'type="column"' not in matched:
                # 这是软换行，添加换行符标记
                parts.append('\n')
    
    # 拼接所有部分
    full_text = ''.join(parts)
    
    return full_text


def get_text_with_formatting(para):
    """
    获取段落文本，保留加粗、斜体等格式
    """
    para_xml = para._element.xml
    
    # 解析XML
    from xml.etree import ElementTree as ET
    
    ns = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
    
    # 使用正则提取并处理格式
    # 找到所有run及其格式
    runs_info = []
    
    # 分割XML为独立的run
    run_pattern = r'<w:r[^>]*>.*?</w:r>'
    runs = re.findall(run_pattern, para_xml, re.DOTALL)
    
    for run_xml in runs:
        # 提取文本
        texts = re.findall(r'<w:t[^>]*>([^<]*)</w:t>', run_xml)
        text = ''.join(texts)
        
        # 检查格式
        is_bold = '<w:b/>' in run_xml or '<w:b ' in run_xml or '<w:bCs/>' in run_xml
        is_italic = '<w:i/>' in run_xml or '<w:i ' in run_xml
        
        # 检查是否在加粗/斜体标签内
        if not is_bold:
            # 检查父级是否有格式
            run_elem = re.search(r'<w:r[^>]*>.*?</w:r>', run_xml, re.DOTALL)
            if run_elem:
                parent_context = para_xml[para_xml.find(run_elem.group()):para_xml.find(run_elem.group())+500]
                if '<w:rPr>' in parent_context[:300]:
                    pr_section = re.search(r'<w:rPr>.*?</w:rPr>', parent_context, re.DOTALL)
                    if pr_section and ('<w:b/>' in pr_section.group() or '<w:i/>' in pr_section.group()):
                        is_bold = '<w:b/>' in pr_section.group()
                        is_italic = '<w:i/>' in pr_section.group()
        
        runs_info.append({
            'text': text,
            'bold': is_bold,
            'italic': is_italic
        })
    
    # 拼接文本并应用格式
    result = ''
    for run in runs_info:
        if run['text']:
            if run['bold']:
                result += f'**{run["text"]}**'
            elif run['italic']:
                result += f'*{run["text"]}*'
            else:
                result += run['text']
    
    return result


def docx_to_markdown(docx_path, output_path=None):
    """
    将docx文件转换为markdown格式
    
    Args:
        docx_path: docx文件路径
        output_path: 输出md文件路径，默认与docx同目录
    """
    doc = Document(docx_path)
    
    md_lines = []
    
    for para in doc.paragraphs:
        # 获取完整文本（处理软换行）
        text = get_paragraph_full_text(para)
        
        # 跳过空段落
        if not text or not text.strip():
            continue
        
        # 【关键修复】软换行产生的换行符应该保留！
        # 不要把 \n 替换成空格，而是按换行拆分
        
        # 按软换行拆分为多行
        sub_lines = text.split('\n')
        
        for sub_line in sub_lines:
            sub_line = sub_line.strip()
            if sub_line:
                # 合并多个空格（但保留换行结构）
                sub_line = re.sub(r'[ \t]+', ' ', sub_line)
                md_lines.append(sub_line)
    
    # 生成markdown内容
    md_content = '\n\n'.join(md_lines)
    
    # 如果没有指定输出路径，生成默认路径
    if output_path is None:
        base_name = os.path.basename(docx_path)
        output_path = docx_path.replace('.docx', '.md')
    
    # 写入文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    return output_path


def batch_convert(data_dir='原始数据'):
    """
    批量转换data_dir目录下所有docx文件为md文件
    """
    converted = []
    errors = []
    
    files = sorted(os.listdir(data_dir))
    docx_files = [f for f in files if f.endswith('.docx') and not f.endswith('.parsed.md')]
    
    print(f"找到 {len(docx_files)} 个docx文件需要转换\n")
    
    for filename in docx_files:
        docx_path = os.path.join(data_dir, filename)
        md_path = docx_path.replace('.docx', '.md')
        
        try:
            result = docx_to_markdown(docx_path, md_path)
            converted.append(filename)
            print(f"✓ {filename}")
        except Exception as e:
            errors.append((filename, str(e)))
            print(f"✗ {filename}: {e}")
    
    print(f"\n转换完成: {len(converted)} 成功, {len(errors)} 失败")
    
    if errors:
        print("\n失败的文件:")
        for filename, error in errors:
            print(f"  {filename}: {error}")
    
    return converted, errors


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='docx转md工具')
    parser.add_argument('input', nargs='?', help='输入docx文件路径')
    parser.add_argument('-o', '--output', help='输出md文件路径')
    parser.add_argument('-b', '--batch', action='store_true', help='批量转换原始数据目录')
    
    args = parser.parse_args()
    
    if args.batch or not args.input:
        # 批量转换
        batch_convert('原始数据')
    elif args.input:
        # 单文件转换
        result = docx_to_markdown(args.input, args.output)
        print(f"转换完成: {result}")
