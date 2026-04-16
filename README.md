# 证监会境外发行上市备案知识库

> 证监会境外发行上市备案补充材料要求知识库网页版

## 📚 项目介绍

本项目是[证监会境外发行上市备案补充材料要求知识库](https://github.com/your-repo)的网页版，使用 [VitePress](https://vitepress.dev/) 构建，部署在 Cloudflare Pages。

### 功能特性

- ✅ **按时间顺序浏览** - 按月份整理所有备案补充材料要求
- ✅ **按问题类型分类** - 按监管关注点类型分类，便于横向分析
- ✅ **全文搜索** - 支持关键词快速检索
- ✅ **统计分析** - 可视化展示问题类型分布、时间趋势
- ✅ **响应式设计** - 支持手机、平板、电脑等多种设备
- ✅ **定期自动更新** - 持续跟踪证监会最新公示信息

## 🚀 快速开始

### 本地开发

```bash
# 进入网站目录
cd website

# 安装依赖
npm install

# 启动开发服务器
npm run dev

# 构建生产版本
npm run build

# 预览生产版本
npm run preview
```

### 目录结构

```
website/
├── .vitepress/
│   ├── config.mts        # VitePress 配置
│   └── theme/            # 主题定制
│       ├── index.ts     # 主题入口
│       └── custom.css    # 自定义样式
├── public/               # 静态资源
│   └── logo.svg         # 网站 Logo
├── timeline/             # 按时间顺序页面
│   ├── 2026.md
│   ├── 2025.md
│   ├── 2024.md
│   └── 2023.md
├── types/                # 按问题类型页面
│   ├── 股东-实际控制人.md
│   ├── 股权变动-代持.md
│   └── ...
├── statistics.md         # 统计分析页面
├── changelog.md          # 更新日志页面
├── index.md              # 首页
├── DEPLOY.md             # 部署说明
├── package.json
└── .github/
    └── workflows/
        └── deploy.yml    # CI/CD 配置
```

## ☁️ 部署到 Cloudflare Pages

### 方式一：通过 GitHub Actions 自动部署

1. Fork 本仓库
2. 在 Cloudflare Dashboard 创建 API Token（需要 Pages Edit 权限）
3. 在 GitHub 仓库的 Settings → Secrets and variables → Actions 中添加：
   - `CLOUDFLARE_API_TOKEN`: 您的 Cloudflare API Token
   - `CLOUDFLARE_ACCOUNT_ID`: 您的 Cloudflare Account ID
4. 推送代码到 main 分支，部署自动开始

详细步骤请参考 [DEPLOY.md](./DEPLOY.md)

### 方式二：手动部署

```bash
# 安装 Wrangler CLI
npm install -g wrangler

# 登录 Cloudflare
wrangler login

# 构建网站
npm run build

# 部署
wrangler pages deploy dist --project-name=csrc-listing-knowledge-base
```

## 🔄 数据更新

### 手动更新

```bash
# 运行更新脚本
bash scripts/update.sh
```

### 自动更新

设置 GitHub Actions 的定时任务，每日自动更新：

```yaml
on:
  schedule:
    - cron: '0 2 * * *'  # 每天凌晨2点执行
```

## 📊 数据来源

- **官网地址**: https://www.csrc.gov.cn/csrc/c100098/common_list.shtml
- **数据范围**: 2023年4月至今的备案补充材料要求公示

## 📈 统计数据

| 指标 | 数值 |
|------|------|
| 涉及公司数 | 304 家 |
| 问题总数 | 1,464 条 |
| 数据时间范围 | 2023年4月 - 2026年4月 |

### TOP 5 问题类型

1. 股东/实际控制人 - 583条 (39.8%)
2. 合规问题 - 332条 (22.7%)
3. 股权变动/代持 - 305条 (20.8%)
4. 业务经营/经营范围 - 251条 (17.1%)
5. 全流通 - 200条 (13.7%)

## 🛠️ 技术栈

- **框架**: [VitePress](https://vitepress.dev/)
- **部署**: [Cloudflare Pages](https://pages.cloudflare.com/)
- **图表**: [ECharts](https://echarts.apache.org/)
- **搜索**: VitePress 本地搜索

## 📝 License

MIT License

## 🙏 致谢

- 数据来源：[中国证监会官网](https://www.csrc.gov.cn/)
- 参考项目：[巴菲特股东信知识库](https://github.com/example/buffett-letters)
