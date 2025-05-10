from langchain.prompts import PromptTemplate

compliance_prompt = PromptTemplate.from_template("""
You are a Shariah compliance auditor. Review the financial clause below for compliance with AAOIFI standards (focus on FAS 4, 10, and 32):

Clause:
{clause}

Respond with:
1. Applicable AAOIFI FAS (with explanation)
2. Is the clause compliant? (Yes/No)
3. Why or why not?
4. Suggested compliant alternative (if needed)
""")
