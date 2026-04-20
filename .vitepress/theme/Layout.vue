<script setup>
import DefaultTheme from 'vitepress/theme'
import { onMounted } from 'vue'

const { Layout } = DefaultTheme

onMounted(() => {
  // 动态加载不蒜子脚本
  const script = document.createElement('script')
  script.src = '//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js'
  script.async = true
  document.head.appendChild(script)
})
</script>

<template>
  <Layout>
    <template #layout-bottom>
      <div class="busuanzi-footer">
        <span>数据来源：中国证监会官网</span>
        <span class="divider">|</span>
        <span>访问量：<span id="busuanzi_container_site_pv"><span id="busuanzi_value_site_pv"></span> 次</span></span>
      </div>
    </template>
  </Layout>
</template>

<style scoped>
.busuanzi-footer {
  text-align: center;
  padding: 24px 0;
  font-size: 14px;
  color: var(--vp-c-text-2);
  background: var(--vp-c-bg);
}
.divider {
  margin: 0 8px;
}
</style>
