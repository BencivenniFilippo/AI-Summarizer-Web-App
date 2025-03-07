from transformers import BartForConditionalGeneration, BartTokenizer

model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

def summarize(text):
    length = len(text.split())

    if length <= 50:
        max_length = 30
        min_length = 5
        length_penalty = 1.5
        num_beams = 5

    elif length <= 300:
        max_length = 130
        min_length = 25
        length_penalty = 2.0
        num_beams = 5

    else:
        max_length = 200
        min_length = 50
        length_penalty = 2.5
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