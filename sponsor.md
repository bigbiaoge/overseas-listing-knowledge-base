---
layout: page
title: 打赏支持
---

# ☕ 打赏支持

如果这个知识库对你有帮助，欢迎请我喝杯咖啡 ☕

你的支持是我持续维护和更新的动力！

---

## 打赏档位

<div class="sponsor-options">

<div class="sponsor-card">
  <div class="sponsor-amount">¥5</div>
  <div class="sponsor-desc">别喝咖啡了，矿泉水更健康！</div>
</div>

<div class="sponsor-card">
  <div class="sponsor-amount">¥9.9</div>
  <div class="sponsor-desc">请你喝杯瑞幸</div>
</div>

<div class="sponsor-card highlight">
  <div class="sponsor-amount">¥29.9</div>
  <div class="sponsor-desc">一杯不够，连喝三杯</div>
</div>

</div>

---

## 扫码打赏

<div class="qrcode-container">
  <img src="/wechat-pay.png" alt="微信收款码" class="qrcode-img" />
  <p>微信扫码打赏</p>
</div>

---

## 感谢支持

你的每一份支持都将用于：
- 📚 知识库持续更新和维护
- 🔧 功能优化和迭代
- ☕ 我喝咖啡的基金

<style>
.sponsor-options {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
  margin: 30px 0;
}

.sponsor-card {
  background: var(--vp-c-bg-soft);
  border: 2px solid var(--vp-c-divider);
  border-radius: 12px;
  padding: 24px 32px;
  text-align: center;
  transition: all 0.3s ease;
  min-width: 180px;
}

.sponsor-card:hover {
  border-color: var(--vp-c-brand-1);
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

.sponsor-card.highlight {
  border-color: var(--vp-c-brand-1);
  background: linear-gradient(135deg, var(--vp-c-brand-soft), var(--vp-c-bg-soft));
}

.sponsor-amount {
  font-size: 28px;
  font-weight: bold;
  color: var(--vp-c-brand-1);
  margin-bottom: 8px;
}

.sponsor-desc {
  font-size: 14px;
  color: var(--vp-c-text-2);
}

.qrcode-container {
  text-align: center;
  margin: 30px 0;
}

.qrcode-img {
  width: 240px;
  height: 240px;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.qrcode-container p {
  margin-top: 16px;
  color: var(--vp-c-text-2);
  font-size: 14px;
}

@media (max-width: 640px) {
  .sponsor-options {
    flex-direction: column;
    align-items: center;
  }
  
  .sponsor-card {
    width: 100%;
    max-width: 280px;
  }
}
</style>
