# AI Translator (English ↔ Urdu)

A simple command‑line translator built in Python using OpenAI Agents and the Gemini API. It automatically detects whether the input is English or Urdu and returns the translation in the opposite language—no extra text, just the translated sentence.

## ⚙️ Features
- **Bidirectional translation**: English → Urdu & Urdu → English  
- Powered by **Gemini API** via OpenAI Agents  
- Clean, straightforward **CLI** workflow  
- Modular codebase—easy to tweak or extend  

## 🚀 Quick Setup
```bash
git clone https://github.com/yourusername/uv.git
cd uv
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux
pip install -r requirements.txt

Create a .env file in the root directory:
GEMINI_API_KEY=your_api_key_here

▶️ How to Run
python main.py
