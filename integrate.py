#Integrate OpenAI ChatCompletion API
import openai

openai.api_key = "your_openai_api_key"

def extract_ai_features(article_text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Extract AI-related features from the following news article."},
            {"role": "user", "content": article_text}
        ]
    )
    return response.choices[0].message['content']
