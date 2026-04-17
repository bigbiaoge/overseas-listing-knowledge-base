#!/usr/bin/env python3
"""
解析结果验证脚本
用于检查解析质量，确保数据完整性和准确性

使用方法：
    python validate_parse_result.py parsed_data.json

输出：
    - 验证报告
    - 问题列表
    - 统计信息
"""

import json
import re
import sys
from collections import defaultdict
from datetime import datetime


class ParseResultValidator:
    """解析结果验证器"""
    
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.info = []
        
    def validate_document(self, doc_result):
        """
        验证单个文档的解析结果
        
        Args:
            doc_result: 解析结果字典
            
        Returns:
            dict: 验证结果
        """
        self.errors = []
        self.warnings = []
        self.info = []
        
        # 1. 数量匹配检查
        self._check_count_match(doc_result)
        
        # 2. 空内容检查
        self._check_empty_content(doc_result)
        
        # 3. 公司名称有效性检查
        self._check_company_names(doc_result)
        
        # 4. 问题格式检查
        self._check_question_format(doc_result)
        
        # 5. 重复检查
        self._check_duplicates(doc_result)
        
        # 计算得分
        score = self._calculate_score()
        
        return {
            'date': doc_result.get('date'),
            'passed': len(self.errors) == 0,
            'score': score,
            'errors': self.errors,
            'warnings': self.warnings,
            'info': self.info
        }
    
    def _check_count_match(self, doc_result):
        """检查企业数量是否匹配"""
        expected = doc_result.get('expected_count')
        actual = doc_result.get('actual_count')
        
        if expected is None:
            self.info.append({
                'type': 'no_expected_count',
                'message': '文档未声明预期企业数量'
            })
            return
        
        if actual != expected:
            self.errors.append({
                'type': 'count_mismatch',
                'severity': 'error',
                'message': f'数量不匹配：预期{expected}家，实际{actual}家',
                'details': {
                    'expected': expected,
                    'actual': actual,
                    'difference': expected - actual
                },
                'suggestion': '检查是否有企业未被识别，可能原因：引导语断开、格式异常、公司名识别失败'
            })
    
    def _check_empty_content(self, doc_result):
        """检查是否有企业无问题内容"""
        companies = doc_result.get('companies', [])
        empty_companies = []
        
        for company in companies:
            questions = company.get('questions', [])
            if not questions:
                empty_companies.append({
                    'name': company.get('name'),
                    'reason': '问题列表为空'
                })
            elif all(not q.strip() for q in questions):
                empty_companies.append({
                    'name': company.get('name'),
                    'reason': '所有问题内容为空'
                })
        
        if empty_companies:
            self.errors.append({
                'type': 'empty_content',
                'severity': 'error',
                'message': f'发现{len(empty_companies)}家企业无问题内容',
                'details': {
                    'empty_companies': empty_companies
                },
                'suggestion': '检查这些企业的原始文档，确认是否有内容；可能原因：引导语和问题在同一行（软换行问题）、问题格式不标准'
            })
    
    def _check_company_names(self, doc_result):
        """检查公司名是否有效"""
        companies = doc_result.get('companies', [])
        invalid_companies = []
        
        # 无效公司名的特征模式
        invalid_patterns = [
            (r'^明确的法律意见', '包含引导语片段'),
            (r'^请你公司', '包含引导语片段'),
            (r'^请你补充', '包含引导语片段'),
            (r'^请律师', '包含引导语片段'),
            (r'^关于', '以关于开头'),
            (r'^一、', '以问题序号开头'),
            (r'^\d+\.', '以数字序号开头'),
        ]
        
        for company in companies:
            name = company.get('name', '').strip()
            issues = []
            
            # 检查长度
            if len(name) > 50:
                issues.append(f'公司名过长({len(name)}字)')
            
            # 检查是否匹配无效模式
            for pattern, reason in invalid_patterns:
                if re.match(pattern, name):
                    issues.append(reason)
                    break
            
            if issues:
                invalid_companies.append({
                    'name': name,
                    'issues': issues
                })
        
        if invalid_companies:
            self.warnings.append({
                'type': 'invalid_company_names',
                'severity': 'warning',
                'message': f'发现{len(invalid_companies)}个可能无效的公司名',
                'details': {
                    'invalid_companies': invalid_companies
                }
            })
    
    def _check_question_format(self, doc_result):
        """检查问题格式"""
        companies = doc_result.get('companies', [])
        format_issues = []
        
        for company in companies:
            questions = company.get('questions', [])
            for i, question in enumerate(questions):
                issues = []
                
                # 检查问题开头格式
                if not re.match(r'^[一二三四五六七八九十]+[、是]', question) and \
                   not re.match(r'^\d+\.', question) and \
                   not question.startswith('关于') and \
                   not question.startswith('请'):
                    issues.append('问题格式不规范（不以序号或"请"/"关于"开头）')
                
                # 检查问题长度
                if len(question) < 10:
                    issues.append(f'问题内容过短({len(question)}字)')
                elif len(question) > 2000:
                    issues.append(f'问题内容过长({len(question)}字)')
                
                if issues:
                    format_issues.append({
                        'company': company.get('name'),
                        'question_index': i + 1,
                        'issues': issues,
                        'preview': question[:60] + '...' if len(question) > 60 else question
                    })
        
        if format_issues:
            self.warnings.append({
                'type': 'question_format_issues',
                'severity': 'warning',
                'message': f'发现{len(format_issues)}个问题格式异常',
                'details': {
                    'format_issues': format_issues[:10]  # 只显示前10个
                }
            })
    
    def _check_duplicates(self, doc_result):
        """检查是否有重复的企业"""
        companies = doc_result.get('companies', [])
        names = [c.get('name') for c in companies]
        
        duplicates = []
        seen = {}
        for i, name in enumerate(names):
            if name in seen:
                duplicates.append({
                    'name': name,
                    'first_occurrence': seen[name],
                    'second_occurrence': i + 1
                })
            else:
                seen[name] = i + 1
        
        if duplicates:
            self.warnings.append({
                'type': 'duplicate_companies',
                'severity': 'warning',
                'message': f'发现{len(duplicates)}个重复企业',
                'details': {
                    'duplicates': duplicates
                },
                'suggestion': '检查解析逻辑，可能是引导语重复识别或公司名提取错误'
            })
    
    def _calculate_score(self):
        """计算质量得分"""
        base_score = 100
        
        # 每个错误扣20分
        base_score -= len(self.errors) * 20
        
        # 每个警告扣5分
        base_score -= len(self.warnings) * 5
        
        return max(0, base_score)


def validate_all_results(data_path):
    """
    验证所有解析结果
    
    Args:
        data_path: parsed_data.json 文件路径
        
    Returns:
        dict: 总体验证结果
    """
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    all_results = data.get('all_data', [])
    
    validator = ParseResultValidator()
    
    validation_results = []
    total_errors = 0
    total_warnings = 0
    total_passed = 0
    
    # 按日期排序
    all_results.sort(key=lambda x: x.get('date', ''))
    
    print("=" * 70)
    print("解析结果质量验证报告")
    print("=" * 70)
    print()
    
    for result in all_results:
        validation = validator.validate_document(result)
        validation_results.append(validation)
        
        if validation['passed']:
            total_passed += 1
        else:
            total_errors += len(validation['errors'])
            
        total_warnings += len(validation['warnings'])
        
        # 打印不通过的结果
        if not validation['passed']:
            date = validation['date']
            score = validation['score']
            print(f"❌ {date} - 得分: {score}/100")
            for error in validation['errors']:
                print(f"   {error['message']}")
                if 'suggestion' in error:
                    print(f"   💡 {error['suggestion']}")
            print()
    
    # 统计信息
    print("=" * 70)
    print("统计摘要")
    print("=" * 70)
    print(f"总文档数: {len(all_results)}")
    print(f"通过数: {total_passed} ({total_passed/len(all_results)*100:.1f}%)")
    print(f"失败数: {len(all_results) - total_passed}")
    print(f"总错误数: {total_errors}")
    print(f"总警告数: {total_warnings}")
    print()
    
    # 错误类型统计
    error_types = defaultdict(int)
    warning_types = defaultdict(int)
    
    for result in validation_results:
        for error in result['errors']:
            error_types[error['type']] += 1
        for warning in result['warnings']:
            warning_types[warning['type']] += 1
    
    if error_types:
        print("错误类型分布:")
        for error_type, count in sorted(error_types.items(), key=lambda x: -x[1]):
            print(f"  - {error_type}: {count}次")
        print()
    
    if warning_types:
        print("警告类型分布:")
        for warning_type, count in sorted(warning_types.items(), key=lambda x: -x[1]):
            print(f"  - {warning_type}: {count}次")
        print()
    
    return {
        'total_documents': len(all_results),
        'passed': total_passed,
        'failed': len(all_results) - total_passed,
        'total_errors': total_errors,
        'total_warnings': total_warnings,
        'pass_rate': total_passed / len(all_results) * 100 if all_results else 0,
        'error_types': dict(error_types),
        'warning_types': dict(warning_types),
        'validation_results': validation_results
    }


def main():
    if len(sys.argv) < 2:
        print("使用方法: python validate_parse_result.py parsed_data.json")
        sys.exit(1)
    
    data_path = sys.argv[1]
    
    result = validate_all_results(data_path)
    
    # 保存详细报告
    report_path = data_path.replace('.json', '_validation_report.json')
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"详细报告已保存到: {report_path}")
    
    # 如果有错误，返回非0状态码
    if result['total_errors'] > 0:
        sys.exit(1)


if __name__ == '__main__':
    main()
