import streamlit as st
from langchain.document_loaders import PyPDFLoader
from main import check_clause  # your GPT compliance function

st.title("🕌 Shariah Compliance Checker")

# Choose input method
input_method = st.radio("Choose input method:", ["📄 Upload PDF", "✍️ Write Text"])

user_text = ""

if input_method == "📄 Upload PDF":
    uploaded_file = st.file_uploader("Upload your contract or clause (PDF only)", type="pdf")

    if uploaded_file is not None:
        # Save temporarily
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())

        st.success("✅ PDF uploaded")

        # Load and extract
        loader = PyPDFLoader("temp.pdf")
        pages = loader.load_and_split()
        user_text = "\n\n".join([page.page_content for page in pages])
        st.text_area("📖 Extracted Text from PDF", user_text[:2000])

elif input_method == "✍️ Write Text":
    user_text = st.text_area("Write your financial clause or contract here:")

# Only show compliance check if there's text
if user_text.strip() != "" and st.button("✅ Check Compliance"):
    st.info("⏳ Processing with GPT...")
    result = check_clause(user_text[:3000])  # Limit size if needed
    st.subheader("📋 Compliance Result")
    st.write(result)
