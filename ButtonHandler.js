document.getElementById("btn-Kma").addEventListener("click", () => {
window.location.href = "chat.html?category=kimia";
});

document.getElementById("btn-Bio").addEventListener("click", () => {
window.location.href = "chat.html?category=Biologi";
});

document.getElementById("btn-fis").addEventListener("click", () => {
window.location.href = "chat.html?category=Fisika";
});

document.getElementById("btn-Eko").addEventListener("click", () => {
window.location.href = "chat.html?category=Ekonomi";
});

document.getElementById("btn-Geo").addEventListener("click", () => {
window.location.href = "chat.html?category=Fisika";
});

document.getElementById("btn-Sjrh").addEventListener("click", () => {
window.location.href = "chat.html?category=Sejarah";
});

document.getElementById("btn-Sos").addEventListener("click", () => {
window.location.href = "chat.html?category=Sosiologi";
});

document.getElementById("btn-Tari").addEventListener("click", () => {
window.location.href = "chat.html?category=Seni Tari";
});

document.getElementById("btn-Infor").addEventListener("click", () => {
            window.location.href = "chat.html?category=Informatika";
        });

document.getElementById("btn-PPS").addEventListener("click", () => {
window.location.href = "chat.html?category=Pendidikan Pancasila";
});

document.getElementById("btn-PJOK").addEventListener("click", () => {
window.location.href = "chat.html?category=Pendidikan Jasmani";
});

document.getElementById("btn-MTK").addEventListener("click", () => {
window.location.href = "chat.html?category=Matematika";
});

document.getElementById("btn-Ind").addEventListener("click", () => {
window.location.href = "chat.html?category=Bahasa Indonesia";
});

document.getElementById("btn-ing").addEventListener("click", () => {
window.location.href = "chat.html?category=Bahasa Inggris";
});

document.getElementById("btn-jpn").addEventListener("click", () => {
window.location.href = "chat.html?category=Bahasa Jepang";
});

document.getElementById("btn-Bl").addEventListener("click", () => {
window.location.href = "chat.html?category=Bahasa Bali";
});

//Next Page and Before Page
let currentIndex = 1; // mulai dari cardContainer1
  const totalCards = 4; // total cardContainer yang ada

  function showCard(index) {
    for (let i = 1; i <= totalCards; i++) {
      document.getElementById("cardContainer" + i).classList.add("hidden");
    }
    document.getElementById("cardContainer" + index).classList.remove("hidden");
  }

  document.getElementById("nxtbtn").addEventListener("click", () => {
    currentIndex++;
    if (currentIndex > totalCards) currentIndex = 1; // balik lagi ke awal
    showCard(currentIndex);
  });

  document.getElementById("prevbtn").addEventListener("click", () => {
    currentIndex--;
    if (currentIndex < 1) currentIndex = totalCards; // ke terakhir
    showCard(currentIndex);
  });

showCard(currentIndex); // tampilkan card pertama saat load