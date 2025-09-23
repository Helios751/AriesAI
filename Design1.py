import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

class AriesUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("ARIES Assistant")
        self.geometry("400x700")  # Default ukuran untuk mobile
        self.configure(bg="#1a1a3d")  

        # Background gradient
        self.canvas = tk.Canvas(self, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.bind("<Configure>", self.draw_gradient)

        # Animasi bintang
        self.stars = []
        for _ in range(40):
            x, y = random.randint(0, 400), random.randint(0, 700)
            star = self.canvas.create_oval(x, y, x+2, y+2, fill="white", outline="")
            self.stars.append((star, random.choice([-1, 1])))

        # Logo (gunakan gambar PNG transparan biar rapi)
        try:
            logo = Image.open("awal ui (1).jpg")  # ganti dengan logo Aries kamu (PNG)
            logo = logo.resize((200, 200))
            self.logo_img = ImageTk.PhotoImage(logo)
            self.logo_label = tk.Label(self.canvas, image=self.logo_img, bg="#000000", bd=0)
            self.logo_window = self.canvas.create_window(200, 280, window=self.logo_label)
        except:
            self.logo_label = tk.Label(self.canvas, text="♈", font=("Arial", 80), fg="white", bg="#000000")
            self.logo_window = self.canvas.create_window(200, 280, window=self.logo_label)

        # Teks sapaan
        self.text_label = tk.Label(
            self.canvas,
            text="Selamat Siang!\nAdakah yang bisa saya bantu?",
            font=("Arial", 14, "bold"),
            fg="white",
            bg="#000000"
        )
        self.text_window = self.canvas.create_window(200, 500, window=self.text_label)

        # Mulai animasi
        self.animate_stars()

    def draw_gradient(self, event=None):
        """Buat background gradasi"""
        self.canvas.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = height
        (r1,g1,b1) = (26,26,61)
        (r2,g2,b2) = (102,0,204)
        for i in range(limit):
            r = int(r1 + (float(i)/limit)*(r2-r1))
            g = int(g1 + (float(i)/limit)*(g2-g1))
            b = int(b1 + (float(i)/limit)*(b2-b1))
            color = "#%02x%02x%02x" % (r,g,b)
            self.canvas.create_line(0,i,width,i, tags=("gradient",), fill=color)

        self.canvas.lower("gradient")

    def animate_stars(self):
        """Animasi bintang berkedip"""
        for star, direction in self.stars:
            current_color = self.canvas.itemcget(star, "fill")
            if current_color == "white" and direction == 1:
                self.canvas.itemconfig(star, fill="gray")
            else:
                self.canvas.itemconfig(star, fill="white")
        self.after(500, self.animate_stars)

if __name__ == "__main__":
    app = AriesUI()
    app.mainloop()
