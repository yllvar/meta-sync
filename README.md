# <img src="https://i.imgur.com/JQ6Z3gW.png" width="30" height="30"> MetaSync MT5 REST API

[![RapidAPI Badge](https://upload.wikimedia.org/wikipedia/commons/6/62/RapidAPI_logo.svg)](https://rapidapi.com/metasync-metasync-default/api/metasyc)
[![Python Support](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

> **Production-ready FastAPI solution for MT5 automation**  
> The most developer-friendly way to automate MetaTrader 5 trading

🔗 **[Try Now on RapidAPI](https://rapidapi.com/metasync-metasync-default/api/metasyc)** | 📚 **[Full Documentation](https://docs.metasync.com)** | 💬 [Join Our Discord](https://discord.gg/yourlink)



## 🌟 Why Choose MetaSync?

| Feature | Our API | Others |
|---------|--------|--------|
| Mock Mode | ✅ | ❌ |
| Webhooks | ✅ | ❌ |
| Latency | <100ms | 300-500ms |
| Pricing | From $14.99 | From $19.99 |

**Key Advantages:**
- 🚀 **Blazing Fast** FastAPI backend
- 🖥️ **Cross-Platform** (Windows + Mock Mode)
- 📊 **Complete Trading Suite** (Orders, History, Analytics)

## 🚀 Quick Start

### 1. Get Your API Key
```python
# Install via RapidAPI
pip install python-mt5-api
```

### 2. Connect in <1 Minute
```python
from metasync import MT5

api = MT5(api_key="your-rapidapi-key")
account = api.connect(
    login=12345,
    password="your_password",
    server="BrokerServer"
)
print(f"Connected to {account['balance']} USD")
```

### 3. Place Your First Trade
```python
order = api.create_order(
    symbol="EURUSD",
    action="buy",
    volume=0.1,
    stop_loss=1.0800,
    take_profit=1.0900
)
```

## 📊 Core Features

1. **Real-Time Market Data**
   ```python
   ticks = api.get_ticks("EURUSD", count=100)
   ```

2. **Advanced Order Types**
   ```python
   api.create_order(
       symbol="GOLD",
       action="sell",
       type="limit",
       price=1950.00,
       expiration=datetime.now() + timedelta(hours=1)
   ```

3. **Portfolio Analytics**
   ```python
   analytics = api.get_analytics(
       start_date="2023-01-01",
       metrics=["sharpe", "max_drawdown"])
   ```

## 💰 Pricing Tiers

| Tier | Price | RPM | Features |
|------|-------|-----|----------|
| ![Basic](https://i.imgur.com/basic-icon.png) **Basic** | $14.99 | 60 | Market Data + History |
| ![Pro](https://i.imgur.com/pro-icon.png) **Pro** | $49.99 | 300 | Full Trading + Webhooks |
| ![Ultra](https://i.imgur.com/ultra-icon.png) **Ultra** | $149.99 | 1000 | Priority Support + SLA |

🔹 **Special Offer:** First 100 users get **20% OFF** with code `RAPIDAPI20`

## 📚 Resources

- [📘 Interactive API Playground](https://rapidapi.com/metasync-metasync-default/api/metasyc)
- [🎥 Video Tutorials](https://youtube.com/metasync)
- [💡 Sample Bots](https://github.com/metasync/sample-bots)

## ❓ Frequently Asked Questions

**Q: Can I test without a live account?**  
A: Yes! Use our **Mock Mode** for risk-free development.

**Q: What languages are supported?**  
A: All languages via REST. We provide native Python & JS SDKs.

---

<div align="center">
  <h3>Ready to Transform Your Trading?</h3>
  <a href="https://rapidapi.com/metasync-metasync-default/api/metasyc">
    <img src="https://upload.wikimedia.org/wikipedia/commons/6/62/RapidAPI_logo.svg" width="300" alt="Get Started on RapidAPI">
  </a>
</div>
```

