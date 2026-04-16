# Cloudflare Pages 部署配置

## 方式一：通过 Cloudflare Dashboard 部署

1. 登录 [Cloudflare Dashboard](https://dash.cloudflare.com/)
2. 进入 **Workers & Pages** → **Create application** → **Pages** → **Upload direct**
3. 连接您的 Git 仓库或直接上传构建产物
4. 设置构建命令和输出目录：
   - **Build command**: `npm run build`
   - **Build output directory**: `dist`

## 方式二：通过 Wrangler CLI 部署

```bash
# 安装 Wrangler CLI
npm install -g wrangler

# 登录 Cloudflare
wrangler login

# 部署
wrangler pages deploy dist --project-name=csrc-listing-knowledge-base
```

## 方式三：通过 GitHub Actions 自动部署

在 `.github/workflows/deploy.yml` 中配置：

```yaml
name: Deploy to Cloudflare Pages

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          
      - name: Install dependencies
        run: npm ci
        
      - name: Build
        run: npm run build
        
      - name: Deploy to Cloudflare Pages
        uses: cloudflare/pages-action@v1
        with:
          apiToken: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          accountId: ${{ secrets.CLOUDFLARE_ACCOUNT_ID }}
          projectName: csrc-listing-knowledge-base
          directory: dist
```

### 需要设置的 Secrets

在 GitHub 仓库的 **Settings** → **Secrets and variables** → **Actions** 中添加：

- `CLOUDFLARE_API_TOKEN`: Cloudflare API Token
- `CLOUDFLARE_ACCOUNT_ID`: Cloudflare Account ID

### 获取 Cloudflare API Token

1. 进入 [Cloudflare API Tokens](https://dash.cloudflare.com/profile/api-tokens)
2. 点击 **Create Token**
3. 选择 **Pages Edit** 模板
4. 设置账户和区域权限
5. 生成 Token 并保存

## 环境变量配置

如需自定义域名，在 `vitepress.config.js` 中添加：

```javascript
export default defineConfig({
  // ...
  sitemap: {
    hostname: 'https://your-domain.com'
  }
})
```

## 预览部署

部署完成后，Cloudflare 会提供一个 `*.pages.dev` 的域名，您可以通过该域名预览网站。
