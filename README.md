# ✦ Aarva AI Assistant

A sleek AI chatbot built with **Streamlit** and powered by **Meta's Llama 3.1 8B Instruct** model via Hugging Face Inference API.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat&logo=huggingface&logoColor=black)


---

## 🖥️ Preview

> Dark blackish-gray UI with clean white chat bubbles, smooth message flow, and a minimal header.

---

## ✨ Features

- 💬 Real-time conversational AI powered by Llama 3.1
- 🎨 Dark blackish-gray themed UI 
- 🧠 Full chat history maintained across messages
- 🗑️ One-click clear conversation button
- ⚡ Fast and lightweight 

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/aarva-ai.git
cd aarva-ai
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your Hugging Face API key

Open `chatBot.py` and replace the API key with your HF Token :

replace at line 134 of `chatBot.py`
```python
client = InferenceClient(api_key="your_hf_api_key_here")
```

> 🔑 Get your free API key at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

### 4. Run the app

```bash
streamlit run chatbot_app.py
```

Then open your browser at `http://localhost:8501`

---

## 📁 Project Structure

```
aarva-ai/
├── chatbot_app.py      # Main Streamlit app
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 📦 Requirements

```
streamlit
huggingface_hub
```

---

## 🔐 Important — API Key Safety

> **Never push your real API key to GitHub.**

Before pushing, either:
- Replace the key with a placeholder string
- Use an environment variable:

```python
import os
client = InferenceClient(api_key=os.environ.get("HF_API_KEY"))
```

Then set it in your terminal:
```bash
export HF_API_KEY="your_hf_api_key_here"
```

Or use a `.env` file with the `python-dotenv` package and add `.env` to your `.gitignore`.

---

## 🤖 Model

| Property | Value |
|----------|-------|
| Model | `meta-llama/Llama-3.1-8B-Instruct` |
| Provider | Hugging Face Inference API |
| Max tokens | 300 |

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [Streamlit](https://streamlit.io/) — for the web framework
- [Hugging Face](https://huggingface.co/) — for the inference API
- [Meta AI](https://ai.meta.com/) — for the Llama 3.1 model
