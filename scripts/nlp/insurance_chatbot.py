# ==========================================================
# INSURANCE KNOWLEDGE ASSISTANT
# ==========================================================

import re

print("=" * 60)
print("INSURANCE AI KNOWLEDGE ASSISTANT")
print("=" * 60)

knowledge_base = {

    "coverage": """
Your insurance policy covers:

• Accidental Damage
• Hospitalization
• Emergency Medical Expenses
• Vehicle Theft
• Natural Disasters
• Third-Party Liability
• Roadside Assistance
• Personal Accident Benefits
""",

    "claim": """
Claim Process

1. Inform the insurance company within 24 hours.
2. Submit claim form.
3. Provide FIR (if applicable).
4. Submit hospital bills.
5. Submit repair estimate.
6. Submit identity proof.
7. Submit policy documents.
""",

    "documents": """
Documents Required

• Policy Copy
• Identity Proof
• FIR (if required)
• Hospital Bills
• Repair Estimate
• Photographs of Damage
""",

    "exclusions": """
Policy Exclusions

• Driving under the influence of alcohol
• Intentional damage
• Illegal activities
• War
• Nuclear events
""",

    "premium": """
Premium depends on:

• Vehicle value
• Age
• Claim history
• Coverage selected
• Driver profile
""",

    "renewal": """
Policy Renewal

You can renew your policy online before the expiry date.
Late renewal may require vehicle inspection.
""",

    "contact": """
Customer Support

Email:
support@insurance.com

Phone:
1800-123-456

Working Hours:
9 AM - 6 PM
"""
}


def chatbot(question):

    question = question.lower()

    if re.search(r"cover|coverage|benefit", question):
        return knowledge_base["coverage"]

    elif re.search(r"claim|file claim|process", question):
        return knowledge_base["claim"]

    elif re.search(r"document|paper|proof|fir", question):
        return knowledge_base["documents"]

    elif re.search(r"exclude|not cover|alcohol|illegal", question):
        return knowledge_base["exclusions"]

    elif re.search(r"premium|price|cost", question):
        return knowledge_base["premium"]

    elif re.search(r"renew|renewal", question):
        return knowledge_base["renewal"]

    elif re.search(r"contact|phone|email|support", question):
        return knowledge_base["contact"]

    else:

        return """
I'm sorry.

I couldn't understand your question.

Try asking:

• What does my insurance cover?
• How do I file a claim?
• What documents are required?
• What is not covered?
• How can I renew my policy?
• How can I contact support?
"""


print("\nInsurance Assistant Started")
print("Type 'exit' to quit.\n")

while True:

    user = input("You : ")

    if user.lower() == "exit":
        print("\nThank you for using the Insurance Assistant!")
        break

    answer = chatbot(user)

    print("\nBot:")
    print(answer)

    print("-" * 60)