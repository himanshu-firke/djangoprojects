import google.generativeai as genai

genai.configure(api_key="AIzaSyDFxz3BiLvsHUZ7KSHQfbrgl7tKeElp9kQ")

# List all available models
models = genai.list_models()
for model in models:
    print(model.name, model)
