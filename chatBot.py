import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="Aarva AI", page_icon="✦", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
* { font-family: 'Inter', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }

.stApp, body { background: #1c1c1e !important; }
.block-container { padding: 0 1rem 1rem; max-width: 720px; }

/* ── Header ── */
.top-bar {
    display: flex; align-items: center; justify-content: space-between;
    background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
    border-radius: 16px; padding: 14px 20px;
    margin: 1rem 0; border: 1px solid #3a3a3a;
    box-shadow: 0 4px 20px rgba(0,0,0,0.18);
}
.logo {
    width: 42px; height: 42px; border-radius: 12px;
    background: linear-gradient(135deg, #fff 0%, #d0d0d0 100%);
    display: flex; align-items: center; justify-content: center;
    color: #1a1a1a; font-size: 1.2rem; font-weight: 700;
    margin-right: 13px; flex-shrink: 0;
}
.bot-name { font-size: 1.1rem; font-weight: 700; color: #ffffff; letter-spacing: -.02em; }
.bot-sub  { font-size: .68rem; color: #888; margin-top: 2px; }
.pill {
    font-size: .68rem; color: #1a1a1a; font-weight: 600;
    background: #f0f0f0; border-radius: 20px; padding: 4px 12px;
    border: 1px solid #ccc;
}

/* ── Chat bubbles ── */
.msg-user { display:flex; justify-content:flex-end; margin:.45rem 0; }
.msg-ai   { display:flex; justify-content:flex-start; margin:.45rem 0; }

.bubble-user {
    background: #1a1a1a; color: #f5f5f5;
    padding: 10px 15px; border-radius: 18px 18px 4px 18px;
    max-width: 78%; font-size: .88rem; line-height: 1.65;
    border: 1px solid #333;
}
.bubble-ai {
    background: #2c2c2e; color: #e8e8e8;
    padding: 10px 15px; border-radius: 18px 18px 18px 4px;
    max-width: 78%; font-size: .88rem; line-height: 1.65;
    border: 1px solid #3a3a3a;
    box-shadow: 0 2px 8px rgba(0,0,0,0.3);
}

/* ── Divider between header and chat ── */
.chat-box {
    background: #252528; border-radius: 16px;
    border: 1px solid #333; padding: 1rem 1rem .5rem;
    margin-bottom: .75rem; min-height: 120px;
    box-shadow: inset 0 1px 4px rgba(0,0,0,0.3);
}

/* ── Input ── */
.stTextInput>div>div>input {
    background: #2c2c2e !important; border: 1.5px solid #3a3a3a !important;
    border-radius: 12px !important; color: #f0f0f0 !important;
    font-size: .9rem !important; padding: .75rem 1rem !important;
    box-shadow: none !important;
}
.stTextInput>div>div>input:focus {
    border-color: #888 !important;
    box-shadow: 0 0 0 3px rgba(255,255,255,0.08) !important;
}
.stTextInput>div>div>input::placeholder { color: #666 !important; }

/* ── Send button ── */
.stButton>button {
    background: #1a1a1a !important; color: #fff !important;
    border: none !important; border-radius: 12px !important;
    padding: .75rem 1.2rem !important; font-weight: 600 !important;
    width: 100% !important; font-size: .88rem !important;
    transition: background .2s !important;
}
.stButton>button:hover { background: #333 !important; }

/* ── Clear button override ── */
.stButton+.stButton>button {
    background: #2c2c2e !important; color: #888 !important;
    border: 1px solid #3a3a3a !important; font-weight: 500 !important;
    font-size: .8rem !important; margin-top: .4rem !important;
}
.stButton+.stButton>button:hover { background: #3a3a3a !important; color: #ccc !important; }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="top-bar">
    <div style="display:flex;align-items:center">
        <div class="logo">✦</div>
        <div>
            <div class="bot-name">Aarva AI Assistant</div>
            <div class="bot-sub">Powered by Llama 3.1 · 8B Instruct</div>
        </div>
    </div>
    <div class="pill">● Online</div>
</div>
""", unsafe_allow_html=True)

# ── State ─────────────────────────────────────────────────────────────────────
if "history" not in st.session_state:
    st.session_state.history = [{"role":"system","content":"You are Aarva, a helpful AI assistant."}]

# ── Chat messages ─────────────────────────────────────────────────────────────
st.markdown('<div class="chat-box">', unsafe_allow_html=True)
for m in st.session_state.history:
    if m["role"] == "system": continue
    css = "user" if m["role"] == "user" else "ai"
    st.markdown(f'<div class="msg-{css}"><div class="bubble-{css}">{m["content"]}</div></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── Input row ─────────────────────────────────────────────────────────────────
c1, c2 = st.columns([5, 1])
with c1:
    user_input = st.text_input("msg", placeholder="Message aarva…", label_visibility="collapsed")
with c2:
    send = st.button("Send ↑")

# ── Generation ────────────────────────────────────────────────────────────────
if send and user_input.strip():
    st.session_state.history.append({"role":"user","content":user_input.strip()})
    try:
        client = InferenceClient(api_key="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")
        r = client.chat.completions.create(
            model="meta-llama/Llama-3.1-8B-Instruct",
            messages=st.session_state.history, max_tokens=300
        )
        reply = r.choices[0].message.content
    except Exception as e:
        reply = f"⚠️ Error: {e}"
    st.session_state.history.append({"role":"assistant","content":reply})
    st.rerun()

if st.button("Clear chat"):
    st.session_state.history = [{"role":"system","content":"You are Nova, a helpful AI assistant."}]
    st.rerun()