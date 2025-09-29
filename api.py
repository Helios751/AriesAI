from flask import Flask, request, jsonify
from google import genai
from flask_cors import CORS

# Inisialisasi Gemini Client
client = genai.Client(api_key="AIzaSyBsCPI710WmC5Fxq9UrPa_yMh159kam_2Y")

# Inisialisasi Flask
app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return "API is running"
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_input = data.get("question", "")
    category=data.get("category","")

    if not user_input:
        return jsonify({"error": "Pertanyaan tidak boleh kosong"}), 400

    # Klasifikasi apakah pertanyaan terkait pembelajaran
    classify = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        Pertanyaan: "{user_input}"
        
        Tentukan apakah pertanyaan ini terkait dengan mata pelajaran "{category}".
        Jawab hanya dengan 'pembelajaran' atau 'luar'.
        Jawablah pertanyaan berikut menggunakan simbol matematika Unicode, 
    bukan LaTeX. Jawab dengan menggunakan bahasa Indonesia.
        """
    )

    kategori = classify.text.strip().lower()

    if "pembelajaran" in kategori:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
        )
        message = response.text
    else:
        message = "Pertanyaan Anda di luar mata pelajaran " + category + "."

    return jsonify({
        "question": user_input,
        "category": kategori,
        "answer": message
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
