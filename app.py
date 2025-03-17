import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage

# Set up Gemini API Key
GEMINI_API_KEY = "past_your_api"  # Replace with your actual API key

# Initialize LangChain Chat Model
chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=GEMINI_API_KEY)

# Streamlit UI Setup
st.set_page_config(page_title="AI Data Science Tutor", layout="wide")

# Create a two-column layout
col1, col2 = st.columns([3, 1])  # Left 75%, Right 25%

# Left Column: Chat Interface
with col1:
    st.title("🤖 AI Conversational Data Science Tutor")
    st.write("🚀 Ask anything about Data Science, and get AI-powered answers!")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):  # "user" or "assistant"
            st.write(msg["content"])

    # Chat input
    user_input = st.chat_input("Ask a Data Science question...")

    if user_input:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Use LangChain to call Gemini AI
        try:
            response = chat_model([HumanMessage(content=user_input)])
            bot_response = response.content
        except Exception as e:
            bot_response = f"⚠️ Error: {e}"

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": bot_response})

        # Display new messages
        with st.chat_message("user"):
            st.write(user_input)
        with st.chat_message("assistant"):
            st.write(bot_response)

# Right Column: Image or Additional Info
with col2:
    st.image("https://thedatascientist.com/wp-content/uploads/2024/07/Conversational-AI.png", width=250)
    st.markdown("### 💡 AI-Powered Insights")
    st.write("This AI tutor is powered by Google's Gemini AI using LangChain.")
    st.write("🔹 Ask complex questions\n🔹 Get instant responses\n🔹 Improve your data science knowledge!")

# Bottom Section
st.divider()
st.subheader("📌 Learn More")
st.write("Visit [Google AI](https://ai.google/) for more advanced AI models and research.")
