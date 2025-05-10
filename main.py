import os
from dotenv import load_dotenv
from chains import compliance_chain
from langsmith.run_helpers import traceable

load_dotenv()  # Loads from .env

@traceable(name="Compliance Check")
def check_clause(clause_text):
    return compliance_chain.run(clause=clause_text)

if __name__ == "__main__":
    clause = input("Paste your clause: ")
    result = check_clause(clause)
    print("\n📋 Result:\n", result)
