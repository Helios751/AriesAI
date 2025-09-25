document.getElementById("btn-Kma").addEventListener("click", () => {
window.location.href = "chat.html?category=kimia";
});

document.getElementById("btn-Bio").addEventListener("click", () => {
window.location.href = "chat.html?category=Biologi";
});

document.getElementById("btn-fis").addEventListener("click", () => {
window.location.href = "chat.html?category=Fisika";
});

document.getElementById("btn-Main").addEventListener("click", () => {
window.location.href = "UI_Awal_Aries.html";
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

document.getElementById("btn-Informatika").addEventListener("click", () => {
window.location.href = "chat.html?category=Informatika";
});

document.getElementById("btn-PPS").addEventListener("click", () => {
window.location.href = "chat.html?category=Pendidikan Pancasila";
});

document.getElementById("btn-PJOK").addEventListener("click", () => {
window.location.href = "chat.html?category=Pendidikan Jasmani";
});

document.getElementById("btn-MTK").addEventListener("click", () => {
window.location.href = "chat.html?category=MAtematika";
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
let currentCard = 1;
document.getElementById(btnNext).addEventListener("click", () => {
    currentCard++;
    if (currentCard > 4) {
        currentCard = 1;
    }
    updateCardDisplay();
});

document.getElementById(btnBfr).addEventListener("click", () => {
    currentCard--;
    if (currentCard < 1) {
        currentCard = 4;
    }
    updateCardDisplay();
});

function updateCardDisplay() {
    for (let i = 1; i <= 4; i++) {
        const card = document.getElementById(`cardContainer${i}`);
        if (card) {
            card.style.display = 'none';
        }
    }
    const activeCard = document.getElementById(`cardContainer${currentCard}`);
    if (activeCard) {
        activeCard.style.display = 'flex';
    }
}

updateCardDisplay();