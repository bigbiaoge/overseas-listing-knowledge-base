---
layout: page
title: 打赏支持
---

<div class="sponsor-page">

<div class="sponsor-header">
  <div class="coffee-icon">☕</div>
  <h1>打赏支持</h1>
  <p class="subtitle">如果这个知识库对你有帮助<br/>欢迎请我喝杯咖啡</p>
</div>

<div class="sponsor-card">
  <div class="card-header">
    <span class="heart">❤️</span>
    <span>感谢支持</span>
  </div>
  
  <div class="qrcode-box">
    <img src="/wechat-pay.png" alt="微信收款码" class="qrcode" />
  </div>
  
  <p class="pay-label">
    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 6px;"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
    微信扫码，金额随意
  </p>
</div>

<div class="sponsor-footer">
  <div class="footer-item">
    <span class="icon">📚</span>
    <span>知识库持续更新</span>
  </div>
  <div class="footer-item">
    <span class="icon">🔧</span>
    <span>功能优化迭代</span>
  </div>
  <div class="footer-item">
    <span class="icon">☕</span>
    <span>咖啡基金+1</span>
  </div>
</div>

</div>

<style>
.sponsor-page {
  max-width: 400px;
  margin: 0 auto;
  padding: 16px;
}

.sponsor-header {
  text-align: center;
  margin-bottom: 24px;
  padding-top: 8px;
}

.coffee-icon {
  font-size: 48px;
  margin-bottom: 12px;
  animation: bounce 2s ease infinite;
}

@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-8px); }
}

.sponsor-header h1 {
  font-size: 24px;
  font-weight: 600;
  margin: 0 0 8px 0;
  color: var(--vp-c-text-1);
}

.sponsor-header .subtitle {
  font-size: 14px;
  color: var(--vp-c-text-2);
  line-height: 1.6;
  margin: 0;
}

.sponsor-card {
  background: linear-gradient(145deg, var(--vp-c-bg-soft), var(--vp-c-bg-alt));
  border: 1px solid var(--vp-c-divider);
  border-radius: 20px;
  padding: 24px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
}

.card-header {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  font-size: 16px;
  font-weight: 500;
  color: var(--vp-c-text-1);
  margin-bottom: 20px;
}

.heart {
  animation: pulse 1.5s ease infinite;
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.1); }
}

.qrcode-box {
  background: #fff;
  border-radius: 16px;
  padding: 16px;
  display: flex;
  justify-content: center;
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.05);
}

:root.dark .qrcode-box {
  background: var(--vp-c-bg);
}

.qrcode {
  width: 200px;
  height: 200px;
  border-radius: 8px;
}

.pay-label {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 20px 0 0 0;
  padding-top: 16px;
  border-top: 1px dashed var(--vp-c-divider);
  font-size: 14px;
  color: var(--vp-c-text-2);
}

.sponsor-footer {
  margin-top: 24px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.footer-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  background: var(--vp-c-bg-soft);
  border-radius: 12px;
  font-size: 14px;
  color: var(--vp-c-text-2);
  transition: transform 0.2s, box-shadow 0.2s;
}

.footer-item:hover {
  transform: translateX(4px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

.footer-item .icon {
  font-size: 18px;
}

@media (min-width: 640px) {
  .sponsor-page {
    padding: 32px;
  }
  
  .coffee-icon {
    font-size: 56px;
  }
  
  .sponsor-header h1 {
    font-size: 28px;
  }
  
  .sponsor-card {
    padding: 32px;
  }
  
  .qrcode {
    width: 220px;
    height: 220px;
  }
}
</style>
