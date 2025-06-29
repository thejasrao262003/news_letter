# 📰 AI Tech News Digest

Welcome to **AI Tech News Digest** — your automated, serverless, agentic pipeline for staying on top of the latest in AI and technology! This project fetches, summarizes, fact-checks, and emails trending AI/Tech news to your inbox, all on autopilot. Built with Python, LangGraph, Gemini API, and AWS, it is fully modular and production-ready.

---

## 🚀 Features

* Fetches trending news exclusively from Tech & AI sources
* Summarizes articles using Gemini LLM (Google GenAI)
* Fact-checks news summaries for reliability
* Sends a daily HTML email digest (via SMTP)
* Stores every digest in DynamoDB for future archive & search
* Modular, agentic architecture using LangGraph
* Easily extensible for more agents: sentiment, translation, multi-channel delivery, etc.

---

## 🏗️ Project Structure

```
agentic_app/
├── agents/                # Modular agent logic (summarizer, factcheck, newsletter, mail)
├── context/               # Model Context Protocol (MCP), pipeline state
├── orchestrator.py        # LangGraph pipeline wiring
├── integrations.py        # LLM & external API (Gemini, NewsAPI, DynamoDB, SMTP)
├── lambda_handler.py      # AWS Lambda entrypoint
├── config.py              # Config/env loader
├── requirements.txt
├── README.md
└── tests/
```

---

## 🛠️ Setup

### 1. **Clone the repo**

```bash
git clone https://github.com/YOUR_USERNAME/agentic_app.git
cd agentic_app
```

### 2. **Install dependencies**

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. **Configure environment variables**

Create a `.env` file or set environment variables:

```
NEWS_API_KEY=...           # NewsAPI or RSS integration
GEMINI_API_KEY=...         # Google GenAI API key
SMTP_HOST=...              # SMTP server (e.g., smtp.gmail.com)
SMTP_PORT=465              # SMTP port (SSL: 465, TLS: 587)
SMTP_USER=...              # SMTP username/email
SMTP_PASS=...              # SMTP password or app password
EMAIL_FROM=...             # Sender's email address
EMAIL_TO=...               # Comma-separated recipient list
DYNAMODB_TABLE=news_digest # DynamoDB table for storage
AWS_REGION=ap-south-1      # Or your preferred AWS region
```

### 4. **Configure AWS (for Lambda & DynamoDB)**

* Ensure AWS credentials are available (`~/.aws/credentials` or Lambda IAM Role).
* Create the DynamoDB table (`news_digest`) with at least a `date` partition key.
* (Optional) Deploy as AWS Lambda with EventBridge scheduled trigger.

### 5. **Run locally for testing**

```bash
python lambda_handler.py
```

---

## 💡 How It Works

1. **Fetch:** Get top tech/AI news articles from NewsAPI or RSS.
2. **Summarize:** Use Gemini to create concise summaries.
3. **Fact-Check:** Use Gemini (and optionally, web search APIs) to verify claims.
4. **Store:** Save digests in DynamoDB for archiving and future search.
5. **Email:** Compose a stylish HTML email and send via SMTP to recipients.
6. **(Planned)**: Archive/search via future frontend or API.

---

## 🌟 Extending the Pipeline

* **Add agents:** Drop new agents into `agents/` and wire them up in `orchestrator.py`.
* **New delivery channels:** Implement WhatsApp, Telegram, or Slack delivery as new agents.
* **Search/archive UI:** Add backend/API for user-facing archive/search features.
* **Personalization:** Support user preferences, topic filters, or multi-language.

---

## 📄 Example .env File

```
NEWS_API_KEY=your_newsapi_key_here
GEMINI_API_KEY=your_gemini_key_here
SMTP_HOST=smtp.gmail.com
SMTP_PORT=465
SMTP_USER=your_email@gmail.com
SMTP_PASS=your_app_password
EMAIL_FROM=your_email@gmail.com
EMAIL_TO=your_email@gmail.com,other@email.com
DYNAMODB_TABLE=news_digest
AWS_REGION=ap-south-1
```

---

## 🧪 Testing

* All agent logic is unit-tested in `tests/`.
* Test pipeline locally before deployment.
