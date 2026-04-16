# 部署到 Cloudflare Pages 详细指南

## 丰哥专属部署手册 🚀

### 第一步：准备工作

#### 1.1 创建 GitHub 仓库

1. 打开 https://github.com 并登录
2. 点击右上角 **+** → **New repository**
3. 填写仓库信息：
   - Repository name: `csrc-listing-knowledge-base`
   - Description: `证监会境外发行上市备案补充材料要求知识库`
   - 选择 **Private** 或 **Public**（根据需要）
4. 点击 **Create repository**

#### 1.2 上传代码到 GitHub

在终端中执行：

```bash
cd 境外上市备案知识库/website

# 初始化 Git（如果还没有）
git init
git add .
git commit -m "Initial commit: VitePress knowledge base"

# 添加远程仓库（替换为你的仓库地址）
git remote add origin https://github.com/你的用户名/csrc-listing-knowledge-base.git

# 推送代码
git branch -M main
git push -u origin main
```

### 第二步：配置 Cloudflare

#### 2.1 登录 Cloudflare

1. 打开 https://dash.cloudflare.com
2. 登录你的 Cloudflare 账号（如果没有，免费注册一个）

#### 2.2 获取 Account ID

1. 在 Cloudflare Dashboard 右侧，点击你的域名（或任意网站）
2. 滚动到页面底部，找到 **Account ID**
3. 复制这个 ID，后面会用到

#### 2.3 创建 API Token

1. 进入 https://dash.cloudflare.com/profile/api-tokens
2. 点击 **Create Token**
3. 选择 **Custom token** → **Get started**
4. 配置 Token：
   - **Token name**: `Pages Deploy Token`
   - **Account Permissions**:
     - 添加 `Account` → `Cloudflare Pages: Edit`
   - **Zone Permissions**（可选）: 如果有自定义域名，添加对应权限
5. 点击 **Continue to summary**
6. 点击 **Create Token**
7. **重要**：立即复制 Token，它只会显示一次！

### 第三步：在 GitHub 中配置 Secrets

1. 打开你的 GitHub 仓库
2. 点击 **Settings** → **Secrets and variables** → **Actions**
3. 点击 **New repository secret**，添加两个 Secret：

**Secret 1: CLOUDFLARE_API_TOKEN**
- Value: 粘贴你刚才创建的 API Token

**Secret 2: CLOUDFLARE_ACCOUNT_ID**
- Value: 粘贴你的 Cloudflare Account ID

### 第四步：触发部署

1. 在 GitHub 仓库页面，点击 **Actions** 标签
2. 你应该能看到 "Deploy to Cloudflare Pages" workflow
3. 点击 **Run workflow** → 选择 **main** 分支 → 点击绿色按钮
4. 等待几分钟后，部署完成！

### 第五步：访问你的网站

部署成功后：
1. 进入 https://dash.cloudflare.com/pages
2. 找到你的项目 `csrc-listing-knowledge-base`
3. 点击项目，你会看到自定义域名（默认是 `xxx.pages.dev`）
4. 点击链接访问你的网站！

---

## 🎉 恭喜！你的知识库已经上线了！

### 后续操作

#### 设置自定义域名（可选）

如果你有自己的域名（如 `knowledge.yourdomain.com`）：

1. 在 Cloudflare Pages 项目设置中，点击 **Custom domains**
2. 添加你的域名
3. 按照提示在 DNS 中添加 CNAME 记录
4. 等待 SSL 证书自动配置（通常几分钟）

#### 自动更新配置（可选）

要实现每日自动更新数据：

1. 编辑 `.github/workflows/deploy.yml`
2. 取消注释 `schedule` 部分：

```yaml
on:
  schedule:
    - cron: '0 2 * * *'  # 每天凌晨2点执行
  workflow_dispatch:      # 保留这个允许手动触发
```

---

## 常见问题

### Q: 部署失败怎么办？

1. 点击 **Actions** → 查看失败的 workflow run
2. 点击失败的任务，查看日志
3. 常见错误：
   - `CLOUDFLARE_API_TOKEN` 无效 → 重新创建 Token
   - 权限不足 → 检查 Token 权限设置

### Q: 如何更新网站内容？

1. 修改 `timeline/` 或 `types/` 目录下的 Markdown 文件
2. 推送代码后，网站会自动重新部署

### Q: 如何更新数据？

1. 将新的 `原始数据/*.md` 文件放入 `原始数据/` 目录
2. 运行更新脚本：
   ```bash
   cd 境外上市备案知识库/website
   bash scripts/update.sh
   ```
3. 提交并推送更改

### Q: 搜索功能不工作？

搜索功能需要先构建网站才能生效。确保执行过 `npm run build`。

---

## 技术支持

如果遇到问题，可以：
1. 查看 VitePress 文档：https://vitepress.dev/
2. 查看 Cloudflare Pages 文档：https://developers.cloudflare.com/pages/
3. 提交 GitHub Issue

---

**祝部署顺利！** 🎊
