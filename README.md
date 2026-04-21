# Client Directory Web App (Vue + Flask + MS Access)

# Overview
This project is a full-stack web application that manages a simple client directory. It allows users to add and view client records through a web interface built with Vue.js, while a Flask API handles backend logic and stores data in a Microsoft Access database.

The system demonstrates front-end and back-end integration, API development, and database connectivity using Python and ODBC. AI-assisted techniques were used to enhance data parsing, improve data quality, and streamline development.

---

# Features
- Add new clients through a web form
- View all stored clients in real time
- REST API built with Flask
- Data stored in Microsoft Access database
- Vue.js frontend for dynamic UI updates
- CORS-enabled API communication between frontend and backend

---

# Tech Stack
- Frontend: Vue.js (CDN)
- Backend: Python Flask
- Database: Microsoft Access (.accdb)
- Driver: pyodbc (ODBC connection)
- Styling: CSS

---

# Project Structure (Parent/Child file hierarchy):

project-name/
│
├── access_db/
			└── db.accdb
├── backend/
			└── __pycache__/
			└── static/
				└──	app.js
					styles.css
			└── templates/
				└──	index.html
			└── app.py
			└── db.py
├── venv/
├── .env
├── .gitignore
├── README.md
└── requirements.txt
    
---

# Setup Instructions

# 1. Create a project folder and install tools 
   While operating the CMD from the new project folder/directory, use "pip" command to install "venv" virtual environment, which creates a sandbox environment isolating other python projects from integrating to this project.  
   Create a "requirements" file (i.e., type nul > requirements) to keep dependencies in this file.
   Also, create a ".gitignore" file to withhold any confidential files you wish not to get pushed via your GitHub project repository.
   Ensure to add these last two aforementioned files to your ".gitignore" file 
cmd:
   pip install flask flask-cors pyodbc python-dotenv

   Once installed, run "pip freeze > requirements.txt" to save all your dependencies.

# 2. Configure environment variables (secure your passwords, config path, etc.)
   Create a ".env" file inside your project folder, open the file via coding platform (i.e., Visual Studio Code, Jupyter Notebook, etc.), type the file names (containing any personal or config information), and save it.

# 3. Run Flask Server
CMD:
   python app.py

# 4. Open the application
   Visit: http://127.0.0.1:5000 to add client's input and push the button to send it via the designated MS Access file.

Authored by: Anthony Reyes
