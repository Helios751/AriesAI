from google import genai

client = genai.Client(
    api_key="AIzaSyBsCPI710WmC5Fxq9UrPa_yMh159kam_2Y"
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="berikan saya sinergi bagus di mcgg dan berikan penjelasan detail terhadap semua sinergi beserta hero dan commander di mc gg di late mid dan early game agar optimal mendapatkan peringkat 1 dengan kombinasi hero komander dan sinergi terbaik di mcgg 2025",
)

print(response.text)