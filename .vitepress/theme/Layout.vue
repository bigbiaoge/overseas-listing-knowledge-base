<script setup>
import DefaultTheme from 'vitepress/theme'
const { Layout } = DefaultTheme
</script>

<template>
  <Layout>
    <template #doc-footer-before>
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
  border-top: 1px solid var(--vp-c-divider);
}
.divider {
  margin: 0 8px;
}
</style>
