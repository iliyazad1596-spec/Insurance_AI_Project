# ==========================================================
# INSURANCE POLICY SUMMARIZER
# Compatible with latest Transformers
# ==========================================================

from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM

print("=" * 60)
print("Loading Summarization Model...")
print("=" * 60)

model_name = "facebook/bart-large-cnn"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

policy = """
This insurance policy provides comprehensive coverage for accidental
damage, hospitalization, emergency medical expenses, third-party liability,
vehicle theft, natural disasters, roadside assistance, towing services,
cashless hospitalization, and personal accident benefits.

Policyholders must notify the insurance company within 24 hours after
an accident.

Claims require submission of:

• FIR
• Hospital bills
• Repair estimates
• Identity proof
• Policy documents

Failure to submit documents within the required period may result in
claim rejection.

Coverage exclusions include:

• Driving under the influence of alcohol
• Intentional damage
• Illegal activities
• War
• Nuclear events
"""

inputs = tokenizer(
    policy,
    max_length=1024,
    truncation=True,
    return_tensors="pt"
)

summary_ids = model.generate(
    **inputs,
    max_length=80,
    min_length=30,
    num_beams=4,
    early_stopping=True
)

summary = tokenizer.decode(
    summary_ids[0],
    skip_special_tokens=True
)

print("\nOriginal Policy\n")
print(policy)

print("\nSummary\n")
print(summary)