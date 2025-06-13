📖 Project Browser — Mini Search Engine & Website Creator
This project includes multiple implementations of a simple search engine and website creator — both for web and console use, along with a Windows installer.

📥 Installation & Usage
Important:
After downloading the project ZIP file:

Extract the entire ZIP file to a folder.

Run the installer:
ProjectBrowserInstaller.exe

Follow the installer steps to install Project Browser to
C:\Program Files\BittoSystem

(Optional) Check the box to create a desktop shortcut.

Once installed, the program will automatically run grace.cmd which launches a .html file for no reason lol

📦 Contents:
🖥️ 1. Python Web Version (Flask)
File: app.py

How to run:

bash
Copy
Edit
pip install flask
python app.py
Access: http://127.0.0.1:5000/ in your browser

Output: HTML files stored in the websites folder

🖥️ 2. Python Console Version
File: console_app.py

How to run:

bash
Copy
Edit
python console_app.py
Output: HTML files saved to the websites folder

💾 3. C++ Console Version
File: main.cpp

Compile and run:

bash
Copy
Edit
g++ -std=c++17 -o main main.cpp
./main
Output: HTML files stored in the websites folder

📦 📦 4. Windows Installer Version
Installer file: ProjectBrowserInstaller.exe

Installs:

All INTERNALS files

Optional desktop shortcut

Auto-runs grace.cmd post-install

Installation path: C:\Program Files\BittoSystem

✅ Features
Search engine functionality

Website creation (HTML file generator)

Cross-platform console and web-based versions

Windows installer for easy setup

Optional desktop shortcut

📜 License
MIT License — free for personal and commercial use.

