
let lastTranslatedText = "";

function showSection(sectionId) {
    // Hide all sections
    document.querySelectorAll('.section').forEach(section => {
        section.classList.remove('active');
    });

    // Show the selected section
    const targetSection = document.getElementById(sectionId);
    if (targetSection) {
        targetSection.classList.add('active');
    }
}

function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
}

async function translateText() {
    const text = document.getElementById('inputText').value;
    const lang = document.getElementById('languageSelect').value;
    const loader = document.getElementById('loader');
    const output = document.getElementById('translatedText');
    const speakBtn = document.getElementById('speakBtn');

    loader.style.display = 'block';
    output.innerHTML = '';
    speakBtn.style.display = 'none';

    try {
        const response = await fetch('/translate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text, lang })
        });

        const data = await response.json();
        console.log('Server response:', data);

        loader.style.display = 'none';

        if (data.success) {
            const colors = ['red', 'green', 'blue', 'orange', 'purple'];
            output.innerHTML = [...data.translated_text].map((char, i) =>
                `<span style="color:${colors[i % colors.length]}">${char}</span>`
            ).join('');

            lastTranslatedText = data.translated_text;
            speakBtn.style.display = 'inline-block';
        } else {
            output.innerHTML = `<span style="color:red;">❌ ${data.message}</span>`;
        }
    } catch (err) {
        loader.style.display = 'none';
        output.innerHTML = `<span style="color:red;">🚫 Error: ${err.message}</span>`;
        console.error('Error while translating:', err);
    }
}



function speakText() {
    const utterance = new SpeechSynthesisUtterance(lastTranslatedText);
    utterance.lang = document.getElementById('languageSelect').value + '-IN';
    speechSynthesis.speak(utterance);
}

document.getElementById('imageForm').addEventListener('submit', async function (event) {
    event.preventDefault();

    const formData = new FormData();
    formData.append('image', document.getElementById('imageInput').files[0]);
    formData.append('effect', document.getElementById('effectSelect').value);

    const response = await fetch('/edit-image', {
        method: 'POST',
        body: formData
    });

    const blob = await response.blob();
    const imageUrl = URL.createObjectURL(blob);
    document.getElementById('imageResult').innerHTML = `
        <img src="${imageUrl}" alt="Edited Image">
        <a href="${imageUrl}" download="edited_image.png"><button style="margin-top:10px;">⬇️ Download</button></a>
    `;
});

document.getElementById('asciiForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const formData = new FormData();
    formData.append('image', document.getElementById('asciiImageInput').files[0]);

    const response = await fetch('/ascii-art', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    const output = document.getElementById('asciiResult');

    if (result.success) {
        output.textContent = result.ascii;
    } else {
        output.textContent = `❌ ${result.message}`;
    }
});

document.getElementById('handwritingForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const text = document.getElementById('handwritingText').value;
    const font = document.getElementById('fontSelect').value;

    fetch('/generate-handwriting', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text, font: font })
    })
    .then(response => response.blob())
    .then(blob => {
        const imgURL = URL.createObjectURL(blob);
        document.getElementById('handwritingResult').innerHTML = `<img src="${imgURL}" alt="Handwriting Output"/>`;
    })
    .catch(error => {
        console.error('Error:', error);
        alert("Failed to generate handwriting.");
    });
});


function sendMessage() {
    const messageEl = document.getElementById("userMessage");
    const message = messageEl.value.trim();
    const loader = document.getElementById("loader");
    const responseEl = document.getElementById("chatbotResponse");

    if (!message) {
        responseEl.innerText = "⚠️ Please enter a message.";
        return;
    }

    loader.style.display = "block";
    responseEl.innerText = "";

    fetch("/chatbot", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    })
    .then(res => res.json())
    .then(data => {
        loader.style.display = "none";
        responseEl.innerText = data.reply || "⚠️ No response.";
    })
    .catch(err => {
        loader.style.display = "none";
        responseEl.innerText = "❌ Error occurred. Please try again.";
        console.error(err);
    });
}

function getGeolocation() {
    document.getElementById("geoLoader").style.display = "block";
    document.getElementById("geoResult").style.display = "none";

    fetch('/geolocation')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();  // Parse the JSON data
    })
    .then(data => {
        document.getElementById("geoLoader").style.display = "none";

        if (data.success) {
            document.getElementById("ip").innerText = data.ip;
            document.getElementById("city").innerText = data.city;
            document.getElementById("region").innerText = data.region;
            document.getElementById("country").innerText = data.country;
            document.getElementById("address").innerText = data.address;
            document.getElementById("mapFrame").src = data.map_url;
            document.getElementById("geoResult").style.display = "block";
        } else {
            alert("Error: " + data.message);
        }
    })
    .catch(error => {
        document.getElementById("geoLoader").style.display = "none";
        alert("Something went wrong: " + error);
    });

}

function initMap(lat, lon, city, country) {
    const map = L.map('map').setView([lat, lon], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    L.marker([lat, lon]).addTo(map)
        .bindPopup(`<b>You are here</b><br>${city}, ${country}`)
        .openPopup();
}

function downloadVideo() {
    const url = document.getElementById("youtubeUrl").value;
    const loader = document.getElementById("yt-loader");
    const responseBox = document.getElementById("ytResponse");

    if (!url.trim()) {
        responseBox.innerText = "Please enter a valid YouTube URL.";
        return;
    }

    loader.style.display = "block";
    responseBox.innerText = "";

    fetch('/download', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url: url })
    })
    .then(response => response.json())
    .then(data => {
        loader.style.display = "none";
        responseBox.innerText = data.message;
        responseBox.style.color = data.status === "success" ? "green" : "red";
    })
    .catch(error => {
        loader.style.display = "none";
        responseBox.innerText = "Download failed.";
        console.error("Error:", error);
    });
}








