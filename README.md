A simple and smart Flask-based web application offering features like Language Translation, Image Editing, Text to Handwriting, ASCII Art Generation, and a Smart Chatbot.

✨ Features
🔤 Language Translator — Translate text into multiple languages.

🎨 Image Editor — Apply effects like blur, grayscale, invert, etc.

✍️ Text to Handwriting — Convert typed text into handwriting images.

🔠 ASCII Art Generator — Convert images into ASCII art.

🤖 Smart Chatbot — Chat with an AI-powered bot using OpenAI.

🌓 Dark Mode Toggle — Easily switch between light and dark themes.

🛠️ Technologies Used
Python 3.x

Flask

HTML5, CSS3, JavaScript

OpenAI API (for chatbot)

Pillow (for image editing)

Googletrans (for translation)

📦 Installation
Clone the repository:

git clone https://github.com/your-username/your-flask-project.git
cd your-flask-project
Create a virtual environment and activate it:

python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
Install dependencies:

pip install -r requirements.txt
Set environment variables (optional if using OpenAI):

# In terminal or create a .env file
OPENAI_API_KEY=your_openai_api_key
FLASK_ENV=development
Run the application:

python run.py

Open your browser:
http://127.0.0.1:5000/

📂 Project Structure

flask_project/
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── api_routes.py
│   │   ├── chatbot.py
│   ├── utils/
│   │   ├── translator.py
│   │   ├── image_editor.py
│   │   ├── handwriting_generator.py
│   │   ├── ascii_generator.py
│   │   └── openai_chatbot.py
│   ├── templates/
│   │   ├── base.html
│   │   └── index.html
│   ├── static/
│       ├── css/
│       │   └── style.css
│       ├── js/
│       │   └── script.js
│       ├── fonts/
│       └── images/
├── run.py
├── requirements.txt
└── README.md
📄 API Endpoints

Method	Endpoint	Description
POST	/translate	Translate text
POST	/edit-image	Apply image editing effect
POST	/generate-handwriting	Convert text to handwriting image
POST	/generate-ascii	Generate ASCII art from image
POST	/chat	Chatbot conversation
✍️ Author
Your Name

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgements
Flask

OpenAI

Googletrans

Pillow

New Features coming Soon on 1 May

Added by GitHub
