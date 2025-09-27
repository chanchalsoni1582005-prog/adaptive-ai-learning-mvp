# adaptive-ai-learning-mvp
Adaptive AI-Powered Learning Assessment Tool
# Adaptive AI-Powered Learning Assessment & Practice Tool

## 🚀 Overview
This project is a prototype (MVP) for an **AI-powered adaptive assessment and practice tool**.  
It moves beyond traditional one-size-fits-all testing by diagnosing student-specific learning gaps in:
- **Listening skills** (concentration during lessons)  
- **Grasping power** (comprehension ability)  
- **Retention power** (memory during revision)  
- **Application** (applying concepts to new problems)

The system dynamically adjusts question difficulty and provides **personalized reports** for students, teachers, and parents.

---

## 🎯 Features
- Adaptive assessments (easy → hard questions, depending on answers)  
- Personalized practice content targeting weaknesses  
- Flexible practice modes (difficulty-based / mixed-chapter)  
- Diagnostic skill reports (listening, grasping, retention, application)  
- Simple backend API (FastAPI) with sample question bank  

---

## 🏗️ System Design
- **Backend:** FastAPI (Python)  
- **Adaptive Engine:** Tracks student answers, adjusts difficulty level, logs skill-wise performance  
- **Data:** JSON question bank with difficulty + skill mapping  
- **Frontend (future):** Simple web app (React/Next.js) or can use FastAPI docs for demo  

---

## 📂 Project Structure
