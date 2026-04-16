import { defineConfig } from 'vitepress'

export default defineConfig({
  title: '境外上市备案知识库',
  description: '证监会境外发行上市备案补充材料要求知识库 - 为资本市场非诉律师及相关从业人员提供监管关注点参考',
  lang: 'zh-CN',
  
  // 明确指定源目录和输出目录
  srcDir: '.',
  outDir: 'dist',
  cacheDir: '.vitepress/cache',
  
  head: [
    ['link', { rel: 'icon', href: '/favicon.ico' }],
    ['meta', { name: 'author', content: 'CSRC Knowledge Base' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:title', content: '境外上市备案知识库' }],
    ['meta', { property: 'og:description', content: '证监会境外发行上市备案补充材料要求知识库' }]
  ],

  themeConfig: {
    logo: '/logo.svg',
    siteTitle: '境外上市备案知识库',
    
    nav: [
      { text: '首页', link: '/' },
      { 
        text: '按时间顺序',
        items: [
          { text: '2026年', link: '/timeline/2026' },
          { text: '2025年', link: '/timeline/2025' },
          { text: '2024年', link: '/timeline/2024' },
          { text: '2023年', link: '/timeline/2023' }
        ]
      },
      { 
        text: '按问题类型',
        items: [
          { text: '股东/实际控制人', link: '/types/shareholders' },
          { text: '股权变动/代持', link: '/types/equity-changes' },
          { text: '业务经营/经营范围', link: '/types/business' },
          { text: '外汇/境外投资', link: '/types/forex' },
          { text: '合规问题', link: '/types/compliance' },
          { text: '其他问题类型', link: '/types/other' }
        ]
      },
      { text: '统计分析', link: '/statistics' },
      { text: '更新日志', link: '/changelog' }
    ],

    sidebar: {
      '/timeline/': [
        {
          text: '按时间顺序',
          items: [
            { text: '2026年', link: '/timeline/2026' },
            { text: '2025年', link: '/timeline/2025' },
            { text: '2024年', link: '/timeline/2024' },
            { text: '2023年', link: '/timeline/2023' }
          ]
        }
      ],
      '/types/': [
        {
          text: '按问题类型',
          items: [
            { text: '股东/实际控制人', link: '/types/shareholders' },
            { text: '股权变动/代持', link: '/types/equity-changes' },
            { text: '业务经营/经营范围', link: '/types/business' },
            { text: '外汇/境外投资', link: '/types/forex' },
            { text: '合规问题', link: '/types/compliance' },
            { text: '股权架构/VIE', link: '/types/vie' },
            { text: '全流通', link: '/types/circulation' },
            { text: '募集资金用途', link: '/types/funds' },
            { text: '关联交易/同业竞争', link: '/types/related-party' },
            { text: '其他类型', link: '/types/other' }
          ]
        }
      ]
    },

    search: {
      provider: 'local',
      options: {
        detailedView: true
      }
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com' }
    ],

    footer: {
      message: '数据来源：中国证监会官网',
      copyright: 'Copyright © 2023-2026 境外上市备案知识库'
    }
  },

  markdown: {
    theme: {
      light: 'github-light',
      dark: 'github-dark'
    },
    lineNumbers: true
  },

  sitemap: {
    hostname: 'https://your-domain.com'
  }
})
