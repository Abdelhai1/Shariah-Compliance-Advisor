
# Shariah Compliance Advisor


📘 An AI-powered assistant that checks financial clauses for **compliance with AAOIFI Shariah standards** (FAS 4, 10, 32) using **LangChain** and **OpenAI GPT-4**.

---

## 📌 Overview

The **Shariah Compliance Advisor** was built for the **Hackathon Challenge 4 – Teams' Own Category**, focused on innovating tools for Islamic Finance using AI.

This tool provides:
- Automated Shariah compliance analysis
- Support for both **text input** and **PDF upload**
- Explanations and references to AAOIFI Financial Accounting Standards
- Suggestions for compliant alternatives when issues are found

---

## 💡 Key Features

✨ Built with [LangChain](https://www.langchain.com/) and [OpenAI GPT-4](https://platform.openai.com/)  
📄 Upload contracts as PDF or paste clauses directly  
🧠 Provides verdicts, reasoning, and compliant rewrites  
📚 Cites **FAS 4, FAS 10, FAS 32** based on content  
🧩 Modular structure for easy customization  
📈 Optional LangSmith integration for observability and debugging

---

## 🧱 System Architecture

graph TD;
    A[User Input (PDF/Text)] --> B[Loader/Extractor]
    B --> C[LangChain + GPT-4]
    C --> D[Shariah Compliance Prompt]
    D --> E[Analysis Engine]
    E --> F[Verdict + Correction]
    F --> G[Streamlit Display]


## 🧪 Test Cases

### ❌ Non-Halal Input Example

**Input:**
"The lessee shall pay DZD 5,000,000 annually and an interest of 5%. Ownership shall transfer automatically after 4 years."

**AI Output:**

- **Compliance Verdict:** ❌ Not compliant
- **Applicable Standard:** FAS 32
- **Reason:** Includes riba (interest) and automatic ownership transfer
- **Suggested Fix:** Remove interest; add a separate sale contract for ownership

### ✅ Halal Input Example

**Input:**
"The lessee shall pay DZD 5,000,000 per year. Ownership may be transferred through a separate agreement at the end of the lease for DZD 100,000."

**AI Output:**

- **Compliance Verdict:** ✅ Compliant
- **Applicable Standard:** FAS 32
- **Reason:** Meets Ijarah Muntahia Bi Tamleek conditions

---

## 🛠 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/abdelhai1/shariah-compliance-advisor.git
cd shariah-compliance-advisor
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
Create a `.env` file:
```ini
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 4. Run the App
```bash
streamlit run app.py
```

---

## 🧰 Built With

| Tool                   | Purpose                                |
| ---------------------- | -------------------------------------- |
| 🧠 OpenAI GPT-4         | Core LLM for natural language analysis |
| 🔗 LangChain            | Prompt management and agent chaining   |
| 📚 AAOIFI Standards     | Compliance reference                   |
| 📄 PyPDFLoader          | PDF clause extraction                  |
| 🖥️ Streamlit            | Web UI                                 |
| 📊 LangSmith            | Observability (optional)              |

---

## 🧑‍🤝‍🧑 Team

Barakah Crew

---

## 📬 Contact

For questions or collaboration, reach out at: m_guir@estin.dz

---

## 📜 License

This project is licensed under the MIT License.

---

## 📝 Submitted as part of the AI Hackathon — Challenge 4: Teams' Own Category


