# 📦 Shanaya - Package Documentation

This file explains the external Python packages used in Shanaya Virtual Assistant and their purpose.

---

## 1️⃣ pyttsx3
**Purpose:** Offline Text-to-Speech Engine  
Shanaya uses this package to convert text into speech without requiring an internet connection.

---

## 2️⃣ SpeechRecognition
**Purpose:** Voice Recognition  
This package captures microphone input and converts spoken words into text using Google's Speech API.

---

## 3️⃣ PyAudio
**Purpose:** Microphone Access  
Required by SpeechRecognition to access the system microphone for voice input.

---

## 4️⃣ wikipedia
**Purpose:** Fetch Information  
Allows Shanaya to fetch short summaries from Wikipedia when the user asks informational queries.

---

## 5️⃣ datetime (Built-in)
**Purpose:** Date & Time Handling  
Used for greetings (Good Morning / Afternoon / Evening) and telling current time.

---

## 6️⃣ webbrowser (Built-in)
**Purpose:** Open Websites  
Allows Shanaya to open websites like Google, GitHub, etc.

---

## 7️⃣ os (Built-in)
**Purpose:** System Operations  
Used to open applications, access folders, and play music from local directories.

---

# 🚀 Installation

Install required packages using:

pip install -r requirements.txt

---

Created for: Shanaya Virtual Assistant 🔥
Developer: Subhrajeet Biswas