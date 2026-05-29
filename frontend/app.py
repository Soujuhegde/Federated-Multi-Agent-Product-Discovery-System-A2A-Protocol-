import streamlit as st
import requests
from datetime import datetime

# ======================
# PAGE CONFIG
# ======================

st.set_page_config(
    page_title="Federated Product Discovery Network",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================
# CUSTOM CSS (Executive Slate Light Glassmorphism Theme)
# ======================

st.markdown("""
<style>
/* Import highly professional fonts */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

/* Apply global font overrides cleanly without breaking Streamlit's material icon fonts */
html, body, .stApp, .stMarkdown, p, h1, h2, h3, h4, h5, h6, .stWidgetLabel {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

code, pre {
    font-family: 'JetBrains Mono', monospace !important;
}

/* Base Theme - Light Slate Mesh Gradient Background */
.stApp {
    background-image: radial-gradient(at 0% 0%, rgba(99, 102, 241, 0.05) 0px, transparent 50%),
                      radial-gradient(at 100% 100%, rgba(56, 189, 248, 0.05) 0px, transparent 50%),
                      linear-gradient(180deg, #f1f5f9 0%, #e2e8f0 100%) !important;
    background-attachment: fixed !important;
    color: #334155 !important;
}

/* Scrollbar styling */
::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}
::-webkit-scrollbar-track {
    background: transparent;
}
::-webkit-scrollbar-thumb {
    background: #cbd5e1;
    border-radius: 9999px;
}
::-webkit-scrollbar-thumb:hover {
    background: #94a3b8;
}

/* Style cards container cleanly - Light Glassmorphism Card */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: rgba(255, 255, 255, 0.4) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(255, 255, 255, 0.6) !important;
    border-radius: 12px !important;
    padding: 20px !important;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.02) !important;
}

/* Metric cleanups */
div[data-testid="stMetric"] {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
    box-shadow: none !important;
}
div[data-testid="stMetricLabel"] > div {
    color: #64748b !important;
    font-size: 0.75rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.05em !important;
    font-weight: 600 !important;
}
div[data-testid="stMetricValue"] > div {
    font-size: 1.65rem !important;
    font-weight: 700 !important;
    color: #0f172a !important;
}

/* Text Input/TextArea customization */
.stTextInput input, .stTextArea textarea {
    background-color: rgba(255, 255, 255, 0.6) !important;
    border: 1px solid rgba(79, 70, 229, 0.2) !important;
    border-radius: 8px !important;
    color: #0f172a !important;
    font-size: 0.9rem !important;
    padding: 10px 14px !important;
    transition: all 0.15s ease !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: #4f46e5 !important;
    box-shadow: 0 0 0 1px #4f46e5 !important;
}

/* Sleek primary submit buttons - Indigo Royal Gradient */
button[data-testid="stFormSubmitButton"] {
    background: linear-gradient(135deg, #4f46e5 0%, #6366f1 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    padding: 10px 20px !important;
    transition: all 0.15s ease !important;
    box-shadow: 0 4px 12px rgba(79, 70, 229, 0.2) !important;
}
button[data-testid="stFormSubmitButton"]:hover {
    transform: translateY(-1px) !important;
    background: linear-gradient(135deg, #4338ca 0%, #4f46e5 100%) !important;
    border: none !important;
    color: #ffffff !important;
    box-shadow: 0 6px 16px rgba(79, 70, 229, 0.3) !important;
}

/* Standard theme-matching glass buttons inside forms/pages */
.stButton button {
    background-color: rgba(255, 255, 255, 0.6) !important;
    color: #4f46e5 !important;
    border: 1px solid rgba(79, 70, 229, 0.25) !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    padding: 10px 20px !important;
    transition: all 0.15s ease !important;
    backdrop-filter: blur(4px) !important;
    box-shadow: 0 2px 8px rgba(79, 70, 229, 0.04) !important;
}
.stButton button:hover {
    background-color: #4f46e5 !important;
    color: #ffffff !important;
    border-color: #4f46e5 !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 12px rgba(79, 70, 229, 0.2) !important;
}
.stButton button:active {
    transform: translateY(0px) !important;
}

/* Tab controls - Indigo Accent */
.stTabs [data-baseweb="tab-list"] {
    gap: 20px !important;
    background-color: transparent !important;
    padding: 0 !important;
    border-bottom: 1px solid #cbd5e1 !important;
    border-radius: 0 !important;
    margin-bottom: 24px !important;
}
.stTabs [data-baseweb="tab"] {
    height: 40px !important;
    background-color: transparent !important;
    border-radius: 0 !important;
    color: #64748b !important;
    font-weight: 500 !important;
    font-size: 0.9rem !important;
    border: none !important;
    padding: 0 4px !important;
    transition: color 0.15s ease !important;
}
.stTabs [data-baseweb="tab"]:hover {
    color: #0f172a !important;
}
.stTabs [aria-selected="true"] {
    color: #4f46e5 !important;
    border-bottom: 2px solid #4f46e5 !important;
    font-weight: 600 !important;
}
.stTabs [data-baseweb="tab-highlight-container"] {
    display: none !important;
}

/* Sidebar Custom Styling */
section[data-testid="stSidebar"] {
    background-color: rgba(241, 245, 249, 0.5) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.3) !important;
}

/* Chat Message Overrides */
div[data-testid="stChatMessage"] {
    background-color: rgba(255, 255, 255, 0.4) !important;
    backdrop-filter: blur(8px) !important;
    border: 1px solid rgba(79, 70, 229, 0.12) !important;
    border-radius: 12px !important;
    padding: 16px !important;
    margin-bottom: 12px !important;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.02) !important;
}
div[data-testid="stChatMessageContent"] {
    color: #334155 !important;
    font-size: 0.95rem !important;
    line-height: 1.6 !important;
}

/* Alert Override */
div[data-testid="stAlert"] {
    background-color: rgba(255, 255, 255, 0.6) !important;
    backdrop-filter: blur(8px) !important;
    border: 1px solid rgba(79, 70, 229, 0.15) !important;
    border-radius: 8px !important;
}
</style>
""", unsafe_allow_html=True)

# ======================
# SESSION STATE
# ======================

if "history" not in st.session_state:
    st.session_state.history = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "youtube_url" not in st.session_state:
    st.session_state.youtube_url = ""

if "recommendations" not in st.session_state:
    st.session_state.recommendations = []

# ======================
# SIDEBAR
# ======================

with st.sidebar:
    st.markdown("## 🤖 A2A Orchestration")
    st.caption("Federated Product Discovery Network")
    
    st.divider()
    
    st.markdown("### Agent Network Status")
    st.markdown("🟢 **YouTube Agent**  \n`rag-agent` • Active")
    st.markdown("🟢 **Product Agent**  \n`graph-agent` • Active")
    st.markdown("🟢 **FastMCP Server**  \n`router-tool` • Active")
    st.markdown("🟢 **A2A Orchestrator**  \n`langgraph-core` • Active")

    st.divider()

    st.markdown("### System Topology")
    st.code("""
User
 ➔ Streamlit Frontend
 ➔ A2A Orchestrator
 ➔ YouTube Agent (RAG)
 ➔ FastMCP Router
 ➔ Product Agent
    """, language="text")

    st.divider()

    st.markdown("### 🕒 Recent Inquiries")
    if not st.session_state.history:
        st.caption("No recent inquiries")
    else:
        for item in st.session_state.history[-5:]:
            st.markdown(f"<div style='font-size:0.8rem; color:#4f46e5; background:rgba(255,255,255,0.5); border:1px solid rgba(79, 70, 229, 0.15); padding:8px 12px; border-radius:8px; margin-bottom:8px; box-shadow:0 1px 3px rgba(0,0,0,0.02);'>• {item[:40]}</div>", unsafe_allow_html=True)

# ======================
# HERO SECTION
# ======================

st.markdown("""
<div style="margin-top: 1rem; margin-bottom: 2.5rem;">
    <div style="display: inline-flex; align-items: center; gap: 8px; background: rgba(79, 70, 229, 0.08); border: 1px solid rgba(79, 70, 229, 0.15); padding: 4px 12px; border-radius: 9999px; font-size: 0.75rem; color: #4f46e5; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1.25rem;">
        <span style="width: 6px; height: 6px; background-color: #4f46e5; border-radius: 50%; display: inline-block;"></span> Federated Agent Discovery
    </div>
    <h1 style="font-size: 2.5rem; font-weight: 700; color: #0f172a; letter-spacing: -0.03em; margin: 0 0 0.5rem 0; line-height: 1.1;">Federated Product Discovery</h1>
    <p style="font-size: 1rem; color: #475569; max-width: 680px; margin: 0; line-height: 1.5;">
        A high-performance federated agent network utilizing LangGraph orchestrations, Pinecone vector spaces, and FastMCP tooling to analyze product review data.
    </p>
</div>
""", unsafe_allow_html=True)

# ======================
# METRICS
# ======================

c1, c2, c3, c4 = st.columns(4)

with c1:
    with st.container(border=True):
        st.metric("Agents", "2 Active")

with c2:
    with st.container(border=True):
        st.metric("Protocol", "A2A Protocol")

with c3:
    with st.container(border=True):
        st.metric("Network Tools", "FastMCP")

with c4:
    with st.container(border=True):
        st.metric("System Status", "Connected")

st.divider()

# ======================
# TABS
# ======================

tab1, tab2, tab3 = st.tabs(
    [
        "🎥 Video Processing",
        "💬 Conversational AI",
        "📦 Discovered Recommendations"
    ]
)

# ======================
# VIDEO TAB
# ======================

with tab1:
    st.markdown("""
    <div style='margin-bottom: 20px;'>
        <h3 style='margin-bottom: 4px; color:#0f172a; font-size:1.25rem; font-weight:600;'>🎥 Ingest Video Review</h3>
        <p style='color:#475569; font-size:0.9rem; margin-top:0;'>Submit a YouTube product review URL. The system will download the audio, fetch the transcription, index it into Pinecone, and prepare the intelligence agents.</p>
    </div>
    """, unsafe_allow_html=True)

    youtube_url = st.text_input(
        "YouTube URL",
        value=st.session_state.youtube_url,
        placeholder="https://www.youtube.com/watch?v=...",
        label_visibility="collapsed"
    )
    st.session_state.youtube_url = youtube_url

    process_btn = st.button("🚀 Process Video")

    if process_btn:
        if not youtube_url:
            st.error("Please enter a valid YouTube URL first.")
        else:
            with st.spinner("Analyzing audio streams and fetching transcripts..."):
                try:
                    response = requests.post(
                        "http://localhost:8000/process",
                        json={"youtube_url": youtube_url}
                    )
                    
                    if response.status_code == 200:
                        st.success("Video processed successfully! Indexed to Pinecone vector store.")
                    else:
                        st.error(f"Error processing video: {response.text}")
                except Exception as e:
                    st.error(f"Could not connect to orchestrator service: {str(e)}")

# ======================
# CHAT TAB
# ======================

with tab2:
    st.markdown("""
    <div style='margin-bottom: 20px;'>
        <h3 style='margin-bottom: 4px; color:#0f172a; font-size:1.25rem; font-weight:600;'>💬 AI Conversation</h3>
        <p style='color:#475569; font-size:0.9rem; margin-top:0;'>Interact directly with the multi-agent orchestration service. Ask complex questions about features, comparisons, or recommendations from the ingested transcript.</p>
    </div>
    """, unsafe_allow_html=True)

    # Render persistent conversation
    if not st.session_state.chat_history:
        st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.5); border: 1px solid rgba(79, 70, 229, 0.15); border-radius: 12px; padding: 24px; text-align: center; margin-bottom: 24px; box-shadow: 0 4px 20px rgba(0,0,0,0.02); backdrop-filter: blur(8px);">
            <h4 style="margin: 0 0 8px 0; color: #0f172a; font-size: 1.1rem; font-weight: 600;">💬 Conversational Video Intelligence</h4>
            <p style="margin: 0 0 16px 0; color: #475569; font-size: 0.85rem;">No active messages. Submit a query below to interact with the federated agent network.</p>
            <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 8px;">
                <span style="font-size: 0.75rem; color: #4f46e5; background: rgba(79, 70, 229, 0.08); border: 1px solid rgba(79, 70, 229, 0.15); padding: 6px 12px; border-radius: 9999px;">"What are the main features of the product?"</span>
                <span style="font-size: 0.75rem; color: #4f46e5; background: rgba(79, 70, 229, 0.08); border: 1px solid rgba(79, 70, 229, 0.15); padding: 6px 12px; border-radius: 9999px;">"Summarize the pros and cons discussed."</span>
                <span style="font-size: 0.75rem; color: #4f46e5; background: rgba(79, 70, 229, 0.08); border: 1px solid rgba(79, 70, 229, 0.15); padding: 6px 12px; border-radius: 9999px;">"Is there a comparison with other brands?"</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        for msg in st.session_state.chat_history:
            role = "user" if msg["role"] == "user" else "assistant"
            with st.chat_message(role):
                st.markdown(msg["content"])

    # If user just sent a message, fetch answer before prompting for the next query
    if st.session_state.chat_history and st.session_state.chat_history[-1]["role"] == "user":
        last_query = st.session_state.chat_history[-1]["content"]
        with st.chat_message("assistant"):
            with st.spinner("Orchestrator routing query to agent network..."):
                try:
                    response = requests.post(
                        "http://localhost:8000/run",
                        json={
                            "youtube_url": st.session_state.youtube_url,
                            "user_query": last_query
                        }
                    )
                    
                    if response.status_code == 200:
                        result = response.json()
                        answer = result.get("answer", "No response from agents.")
                        st.session_state.chat_history.append({
                            "role": "agent",
                            "content": answer,
                            "time": datetime.now().strftime("%H:%M")
                        })
                        st.rerun()
                    else:
                        error_msg = f"Error from agent: {response.text}"
                        st.session_state.chat_history.append({
                            "role": "agent",
                            "content": f"⚠️ {error_msg}",
                            "time": datetime.now().strftime("%H:%M")
                        })
                        st.error(error_msg)
                        st.rerun()
                except Exception as e:
                    error_msg = f"Could not connect to orchestrator service: {str(e)}"
                    st.session_state.chat_history.append({
                        "role": "agent",
                        "content": f"⚠️ {error_msg}",
                        "time": datetime.now().strftime("%H:%M")
                    })
                    st.error(error_msg)
                    st.rerun()

    # Question Input
    with st.form("chat_form", clear_on_submit=True):
        col1, col2 = st.columns([5, 1])
        with col1:
            query = st.text_input(
                "Ask a question about the video...",
                placeholder="Type a question and click Send...",
                label_visibility="collapsed"
            )
        with col2:
            submit_btn = st.form_submit_button("💡 Send", use_container_width=True)

    if submit_btn and query:
        if not st.session_state.youtube_url:
            st.error("Please ingest a YouTube video in the 'Video Processing' tab first.")
        else:
            time_now = datetime.now().strftime("%H:%M")
            st.session_state.chat_history.append({
                "role": "user",
                "content": query,
                "time": time_now
            })
            st.session_state.history.append(query)
            st.rerun()

# ======================
# PRODUCT RECOMMENDATIONS
# ======================

with tab3:
    st.markdown("""
    <div style='margin-bottom: 20px;'>
        <h3 style='margin-bottom: 4px; color:#0f172a; font-size:1.25rem; font-weight:600;'>📦 Product Recommendations</h3>
        <p style='color:#475569; font-size:0.9rem; margin-top:0;'>Extract and discover products from the YouTube review, matching them dynamically with details like category and pricing model.</p>
    </div>
    """, unsafe_allow_html=True)

    discover_btn = st.button("📦 Discover Recommendations")

    if discover_btn:
        if not st.session_state.youtube_url:
            st.error("Please ingest a YouTube video in the 'Video Processing' tab first.")
        else:
            with st.spinner("Extracting similar product alternatives from database..."):
                try:
                    response = requests.post(
                        "http://localhost:8000/run",
                        json={
                            "youtube_url": st.session_state.youtube_url,
                            "user_query": "recommend similar products"
                        }
                    )
                    
                    if response.status_code == 200:
                        result = response.json()
                        recs = result.get("recommendations", [])
                        st.session_state.recommendations = recs
                        
                        if not recs:
                            st.warning("No product recommendations found for this video review.")
                    else:
                        st.error(f"Error fetching recommendations: {response.text}")
                except Exception as e:
                    st.error(f"Could not connect to orchestrator service: {str(e)}")

    # Render recommendations if they exist in state using standard Streamlit cards and columns
    if st.session_state.recommendations:
        st.markdown("### 📦 Discovered Alternatives")
        
        # Grid layout using Streamlit columns for robust rendering without overlap
        cols = st.columns(3)
        for idx, product in enumerate(st.session_state.recommendations):
            col = cols[idx % 3]
            with col:
                with st.container(border=True):
                    category = product.get('category', 'General')
                    name = product.get('name', 'Unknown Product')
                    price = product.get('price', 'N/A')
                    
                    st.markdown(f"<span style='font-size:0.65rem; color:#4f46e5; background:rgba(79, 70, 229, 0.08); border:1px solid rgba(79, 70, 229, 0.15); padding:4px 10px; border-radius:9999px; text-transform:uppercase; font-weight:600;'>{category}</span>", unsafe_allow_html=True)
                    st.markdown(f"<h4 style='margin:12px 0; font-size:1.05rem; font-weight:600; color:#0f172a; min-height:48px; line-height:1.3;'>{name}</h4>", unsafe_allow_html=True)
                    
                    st.divider()
                    
                    subcol1, subcol2 = st.columns([1, 1])
                    with subcol1:
                        st.markdown(f"<span style='font-size:1.25rem; font-weight:700; color:#4f46e5;'>${price}</span>", unsafe_allow_html=True)
                    with subcol2:
                        st.markdown("<p style='text-align:right; font-size:0.75rem; color:#64748b; margin-top:6px; font-weight:500;'>View Details →</p>", unsafe_allow_html=True)

# ======================
# SYSTEM INFO
# ======================

st.divider()

with st.expander("⚙️ System Infrastructure Metrics"):
    st.json({
        "frontend": "Streamlit Engine v1.48.0",
        "llm": "Gemini 2.5 Flash / 1.5 Flash",
        "vector_db": "Pinecone Vector Indexes",
        "orchestration": "LangGraph Statecharts",
        "protocol": "A2A Federated Messaging",
        "tooling": "FastMCP Interface Router",
        "status": "Green / Healthy"
    })

# ======================
# FOOTER
# ======================

st.markdown("""
<div style="text-align: center; padding: 2rem 1rem 1rem; color: #64748b; font-size: 0.8rem; border-top: 1px solid #cbd5e1; margin-top: 4rem;">
    Designed for Federated Multi-Agent Product Discovery Networks • A2A Protocol Specifications
</div>
""", unsafe_allow_html=True)