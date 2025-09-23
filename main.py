from google import genai
import tkinter as tk

client = genai.Client(api_key="AIzaSyBsCPI710WmC5Fxq9UrPa_yMh159kam_2Y")
window = tk.Tk()
window.title("Text Box Sederhana")
window.geometry("300x150")  # ukuran window (opsional)

# Text box
entry = tk.Entry(window, width=30)
entry.pack(pady=10)


def submit():
    user_input = entry.get()
    classify = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        Pertanyaan: "{user_input}"
        
        Tentukan apakah pertanyaan ini terkait dengan pembelajaran (matematika, IPA, IPS, Sejarah, bahasa, Informatika).
        Jawab hanya dengan 'pembelajaran' atau 'luar'.
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
        message = "Pertanyaan Anda di luar materi pembelajaran."

    label.config(text=f"From ARIES:\n{message}")

# Membuat window

# Tombol
button = tk.Button(window, text="Submit", command=submit)
button.pack(pady=5)

# Label untuk output
label = tk.Label(window, text="")
label.pack(pady=10)

# Jalankan window
window.mainloop()
