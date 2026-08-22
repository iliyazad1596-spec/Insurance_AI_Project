from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

print("="*60)
print("Loading Translation Model...")
print("="*60)

model_name = "Helsinki-NLP/opus-mt-en-fr"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

text = """
Your insurance policy covers accidental damages,
medical expenses, hospitalization and emergency assistance.
"""

inputs = tokenizer(text, return_tensors="pt")

translated = model.generate(**inputs)

output = tokenizer.decode(
    translated[0],
    skip_special_tokens=True
)

print("\nOriginal Text:\n")
print(text)

print("\nFrench Translation:\n")
print(output)