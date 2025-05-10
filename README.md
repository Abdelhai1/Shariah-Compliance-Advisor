
# Shariah Compliance Advisor

This project provides an AI-powered tool to check the compliance of contractual clauses with Shariah standards. It uses OpenAI GPT-4 to analyze and provide verdicts on lease and sale contracts, ensuring they align with Islamic financial principles.

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


