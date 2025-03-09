from transformers import BartForConditionalGeneration, BartTokenizer

model_name = "sshleifer/distilbart-cnn-12-6"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

def summarize(text):
    length = len(text.split())

    if length <= 50:
        max_length = 30
        min_length = 5
        length_penalty = 1.0
        num_beams = 4

    elif length <= 300:
        max_length = 100
        min_length = 20
        length_penalty = 1.5
        num_beams = 5

    else:
        max_length = 150
        min_length = 40
        length_penalty = 2.0
        num_beams = 5

    inputs = tokenizer.encode(text, return_tensors="pt", max_length=1024, truncation=True)

    summary_ids = model.generate(
        inputs,
        max_length=max_length,
        min_length=min_length,
        length_penalty=length_penalty,
        num_beams=num_beams,
        early_stopping=True
    )

    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)