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
    ["script", { src: "https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js" }],
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
        text: '案例库',
        items: [
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
              { text: '股权变动/代持', link: '/types/股权变动-代持' },
              { text: '其他', link: '/types/其他' },
              { text: '数据安全/个人信息', link: '/types/数据安全-个人信息' },
              { text: '股东/实际控制人', link: '/types/股东-实际控制人' },
              { text: '业务经营/经营范围', link: '/types/业务经营-经营范围' },
              { text: '外汇/境外投资', link: '/types/外汇-境外投资' },
              { text: '全流通', link: '/types/全流通' },
              { text: '合规问题', link: '/types/合规问题' },
              { text: '外资准入', link: '/types/外资准入' },
              { text: '募集资金用途', link: '/types/募集资金用途' },
              { text: '股权架构/VIE', link: '/types/股权架构-VIE' },
              { text: '国有股东', link: '/types/国有股东' },
              { text: '董监高', link: '/types/董监高' },
              { text: '财务会计', link: '/types/财务会计' },
              { text: '关联交易/同业竞争', link: '/types/关联交易-同业竞争' },
              { text: '税务', link: '/types/税务' },
              { text: '保密/档案管理', link: '/types/保密-档案管理' }
            ]
          }
        ]
      },
      { 
        text: '规则库',
        items: [
          { text: '规则库首页', link: '/rules/' },
          { text: '核心法规', link: '/rules/核心法规/试行办法' },
          { text: '监管规则适用指引', link: '/rules/监管规则适用指引/第1号' },
          { text: '配套规定', link: '/rules/配套规定/保密和档案管理规定' },
          { text: '模板附件', link: '/rules/模板附件/备案材料清单' }
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
            { text: '股权变动/代持', link: '/types/股权变动-代持' },
            { text: '其他', link: '/types/其他' },
            { text: '数据安全/个人信息', link: '/types/数据安全-个人信息' },
            { text: '股东/实际控制人', link: '/types/股东-实际控制人' },
            { text: '业务经营/经营范围', link: '/types/业务经营-经营范围' },
            { text: '外汇/境外投资', link: '/types/外汇-境外投资' },
            { text: '全流通', link: '/types/全流通' },
            { text: '合规问题', link: '/types/合规问题' },
            { text: '外资准入', link: '/types/外资准入' },
            { text: '募集资金用途', link: '/types/募集资金用途' },
            { text: '股权架构/VIE', link: '/types/股权架构-VIE' },
            { text: '国有股东', link: '/types/国有股东' },
            { text: '董监高', link: '/types/董监高' },
            { text: '财务会计', link: '/types/财务会计' },
            { text: '关联交易/同业竞争', link: '/types/关联交易-同业竞争' },
            { text: '税务', link: '/types/税务' },
            { text: '保密/档案管理', link: '/types/保密-档案管理' }
          ]
        }
      ],
      '/rules/': [
        {
          text: '规则库',
          items: [
            { text: '规则库首页', link: '/rules/' }
          ]
        },
        {
          text: '核心法规',
          items: [
            { text: '境内企业境外发行证券和上市管理试行办法', link: '/rules/核心法规/试行办法' }
          ]
        },
        {
          text: '监管规则适用指引',
          items: [
            { text: '第1号：不得境外发行上市情形', link: '/rules/监管规则适用指引/第1号' },
            { text: '第2号：备案材料内容和格式指引', link: '/rules/监管规则适用指引/第2号-备案材料指引' },
            { text: '第3号：报告内容指引', link: '/rules/监管规则适用指引/第3号-报告内容指引' },
            { text: '第4号：备案沟通指引', link: '/rules/监管规则适用指引/第4号-备案沟通指引' },
            { text: '第5号：境外证券公司备案指引', link: '/rules/监管规则适用指引/第5号-境外证券公司备案指引' },
            { text: '第6号：GDR指引', link: '/rules/监管规则适用指引/第6号-GDR指引' },
            { text: '第7号：场外转上市指引', link: '/rules/监管规则适用指引/第7号-场外转上市指引' }
          ]
        },
        {
          text: '配套规定',
          items: [
            { text: '保密和档案管理规定', link: '/rules/配套规定/保密和档案管理规定' },
            { text: '备案管理安排通知', link: '/rules/配套规定/备案管理安排通知' },
            { text: '备案系统上线通知', link: '/rules/配套规定/备案系统上线通知' }
          ]
        },
        {
          text: '模板附件',
          items: [
            { text: '备案材料模板附件', link: '/rules/模板附件/备案材料清单' }
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

    // 目录配置
    outline: {
      level: [2, 3],  // 显示二级和三级标题
      label: '目录导航'
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
