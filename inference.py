from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="oschan77/OpenPipe-7B-slerp",
    max_new_tokens=50,
)
result = pipe("How do you cook a really good egg fried rice?")
generated_text = result[0]["generated_text"]
print(generated_text)
