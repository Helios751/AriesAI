from google import genai

client = genai.Client(
    api_key="AIzaSyBsCPI710WmC5Fxq9UrPa_yMh159kam_2Y"
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="bagaimana konsep ai",
)

print(response.text)