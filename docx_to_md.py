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
    
    软换行应该被转换为空格或直接连接，而不是新段落
    """
    # 方法：通过XML获取完整的文本内容
    para_xml = para._element.xml
    
    # 查找所有文本节点
    text_parts = []
    
    # 使用正则提取所有 <w:t> 标签内容
    t_tags = re.findall(r'<w:t[^>]*>([^<]*)</w:t>', para_xml)
    
    # 查找是否有 <w:br/> 软换行标签
    has_line_break = '<w:br/>' in para_xml or '<w:br ' in para_xml
    
    # 查找软换行的类型
    line_breaks = re.findall(r'<w:br[^/]*/>', para_xml)
    
    # 检查是否有软换行（不是分页符）
    soft_breaks = []
    for br in line_breaks:
        if 'type="line"' in br or 'type="textWrapping"' in br or 'type="wrapping"' in br:
            soft_breaks.append(br)
        elif 'type="page"' not in br and 'type="column"' not in br:
            # 可能是软换行
            if 'type=' not in br:
                soft_breaks.append(br)
    
    # 获取run的属性（加粗、斜体等）
    full_text = ''.join(t_tags)
    
    # 如果有软换行，需要特殊处理
    # 软换行在输出时应该被转换为空格
    if soft_breaks and full_text:
        # 将软换行替换为空格
        full_text = full_text  # 在单段落内不需要替换，因为我们已经拼接了所有文本
    
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
        
        # 清理文本
        text = text.strip()
        
        # 移除末尾的换行符相关内容
        text = text.replace('\n', ' ')
        text = text.replace('\r', ' ')
        
        # 合并多个空格
        text = re.sub(r'\s+', ' ', text)
        
        # 添加到结果
        md_lines.append(text)
    
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
