import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import './custom.css'

export default {
  extends: DefaultTheme,
  layout: DefaultTheme.Layout,
  enhanceApp({ app, router, siteData }) {
    // 添加自定义组件
  }
}
