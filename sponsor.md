---
layout: page
title: 打赏支持
---

# ☕ 打赏支持

如果这个知识库对你有帮助，欢迎请我喝杯咖啡 ☕

你的支持是我持续维护和更新的动力！

---

## 选择打赏金额

<div class="sponsor-options">

<div class="sponsor-card" onclick="showPayModal(5, '别喝咖啡了，矿泉水更健康！')">
  <div class="sponsor-amount">¥5</div>
  <div class="sponsor-desc">别喝咖啡了，矿泉水更健康！</div>
</div>

<div class="sponsor-card" onclick="showPayModal(9.9, '请你喝杯瑞幸')">
  <div class="sponsor-amount">¥9.9</div>
  <div class="sponsor-desc">请你喝杯瑞幸</div>
</div>

<div class="sponsor-card highlight" onclick="showPayModal(29.9, '一杯不够，连喝三杯')">
  <div class="sponsor-amount">¥29.9</div>
  <div class="sponsor-desc">一杯不够，连喝三杯</div>
</div>

</div>

<!-- 支付模态框 -->
<div id="payModal" class="modal" onclick="closeModal(event)">
  <div class="modal-content" onclick="event.stopPropagation()">
    <span class="close-btn" onclick="closeModal()">&times;</span>
    <h3 id="modalTitle">扫码打赏</h3>
    <div class="modal-amount" id="modalAmount">¥5</div>
    <div class="modal-desc" id="modalDesc">别喝咖啡了，矿泉水更健康！</div>
    <img src="/wechat-pay.png" alt="微信收款码" class="modal-qrcode" />
    <p class="modal-tip">请使用微信扫码支付</p>
  </div>
</div>

<script>
function showPayModal(amount, desc) {
  document.getElementById('modalAmount').textContent = '¥' + amount;
  document.getElementById('modalDesc').textContent = desc;
  document.getElementById('payModal').style.display = 'flex';
  document.body.style.overflow = 'hidden';
}

function closeModal(event) {
  if (event && event.target !== document.getElementById('payModal')) return;
  document.getElementById('payModal').style.display = 'none';
  document.body.style.overflow = 'auto';
}
</script>

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
  cursor: pointer;
  user-select: none;
}

.sponsor-card:hover {
  border-color: var(--vp-c-brand-1);
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

.sponsor-card:active {
  transform: translateY(-2px);
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

/* 模态框样式 */
.modal {
  display: none;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(4px);
  align-items: center;
  justify-content: center;
}

.modal-content {
  background: var(--vp-c-bg);
  border-radius: 16px;
  padding: 32px;
  text-align: center;
  max-width: 360px;
  width: 90%;
  position: relative;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  animation: modalIn 0.3s ease;
}

@keyframes modalIn {
  from {
    opacity: 0;
    transform: scale(0.9);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.close-btn {
  position: absolute;
  right: 16px;
  top: 12px;
  font-size: 28px;
  color: var(--vp-c-text-3);
  cursor: pointer;
  line-height: 1;
  transition: color 0.2s;
}

.close-btn:hover {
  color: var(--vp-c-text-1);
}

.modal-content h3 {
  margin: 0 0 16px 0;
  font-size: 18px;
  color: var(--vp-c-text-1);
}

.modal-amount {
  font-size: 36px;
  font-weight: bold;
  color: var(--vp-c-brand-1);
  margin-bottom: 8px;
}

.modal-desc {
  font-size: 14px;
  color: var(--vp-c-text-2);
  margin-bottom: 20px;
}

.modal-qrcode {
  width: 200px;
  height: 200px;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.modal-tip {
  margin-top: 16px;
  font-size: 13px;
  color: var(--vp-c-text-3);
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
  
  .modal-content {
    padding: 24px;
  }
  
  .modal-qrcode {
    width: 180px;
    height: 180px;
  }
}
</style>
