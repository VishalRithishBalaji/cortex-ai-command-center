# 🏙 CORTEX – AI Decision Intelligence Platform for Smart City Operations

> **Team:** Syntactic Systems

CORTEX is an AI-powered Decision Intelligence Platform that helps municipal authorities analyze urban incidents from video inputs, prioritize risks, generate actionable insights, and support faster operational decisions using multimodal AI, Retrieval-Augmented Generation (RAG), and interactive analytics.

---

## 📌 Problem Statement

Modern cities generate large volumes of visual and operational data, but converting this information into timely, actionable decisions remains a challenge.

Municipal authorities often rely on manual inspections, delayed reporting, and fragmented workflows, resulting in:

- Slow incident detection
- Inefficient maintenance planning
- Delayed response to infrastructure issues
- Limited decision support for city administrators

CORTEX addresses these challenges by combining AI-powered vision, structured analytics, and decision intelligence into a single platform.

---

# 🚀 Features

- 🎥 Video-based infrastructure inspection
- 🧠 Gemini-powered multimodal incident analysis
- 📊 Interactive analytics dashboard
- 📍 Incident visualization on map
- ⚠️ Risk scoring and prioritization
- 🏛 Department recommendation engine
- 📈 Executive decision dashboard
- 📚 RAG-based municipal knowledge retrieval
- 💾 SQLite incident repository
- 📑 AI-generated operational summaries

---

# 🏗 System Architecture

```text
                    User
                      │
                      ▼
              Streamlit Dashboard
                      │
                      ▼
              Upload Service
                      │
                      ▼
          Video Frame Extraction
                      │
                      ▼
             Gemini Vision Analysis
                      │
                      ▼
          Decision Intelligence Engine
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
 Recommendation Engine      Risk Assessment
                      │
                      ▼
             SQLite Repository
                      │
                      ▼
             Analytics Engine
                      │
      ┌───────────────┴───────────────┐
      ▼                               ▼
 Executive Dashboard             Ask CORTEX
```

---

# 🛠 Technology Stack

## AI

- Google Gemini API
- Retrieval-Augmented Generation (RAG)
- Sentence Transformers
- ChromaDB

## Computer Vision

- OpenCV
- Pillow

## Backend

- Python
- SQLite

## Dashboard

- Streamlit
- Plotly
- Pandas

---

# 📂 Project Structure

```text
CORTEX/

├── ai/
├── analytics/
├── components/
├── config/
├── dashboard/
├── database/
├── decision/
├── preprocessing/
├── rag/
├── repository/
├── services/
├── data/
├── assets/
├── docs/
├── app.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🔄 Workflow

1. Upload a city surveillance or dashcam video.
2. Extract the most representative frame.
3. Analyze the frame using Gemini Vision.
4. Generate structured incident information.
5. Calculate risk score and priority.
6. Store results in the repository.
7. Update analytics dashboard.
8. Support operational decision-making through AI insights.

---

# 📊 Dashboard

The CORTEX AI Command Center provides:

- City Health Score
- Operational Status
- Incident Analytics
- Department Workload
- Maintenance Budget
- Interactive Map
- Executive Summary
- Incident Database

---

# 🤖 AI Decision Engine

The platform converts unstructured visual information into structured operational intelligence.

Generated outputs include:

- Incident Type
- Risk Index
- Severity
- Priority
- Responsible Department
- Estimated Repair Cost
- Repair Timeline
- Recommended Actions

---

# 📚 RAG Module

CORTEX uses Retrieval-Augmented Generation (RAG) to retrieve municipal regulations and decision-support context from a vector database before producing recommendations.


# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/cortex-ai-command-center.git

cd cortex-ai-command-center
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create `.env`

```env
GOOGLE_API_KEY=YOUR_API_KEY

PROJECT_NAME=CORTEX

PROJECT_VERSION=2.0

CITY=Coimbatore
```

Run

```bash
streamlit run app.py
```

---

# 🎯 Future Enhancements

- Real-time CCTV integration
- GIS integration
- Cloud deployment
- Mobile application
- Predictive maintenance
- Citizen reporting portal

---

# 👥 Team

## Syntactic Systems

Syntactic Systems develops AI-powered decision intelligence platforms that combine multimodal AI, retrieval-augmented generation, and analytics to improve operational decision-making for smart city environments.

---

# 📄 License

This project is released under the MIT License.

---

# 🙏 Acknowledgements

- Google Gemini API
- Streamlit
- Plotly
- ChromaDB
- Sentence Transformers
- OpenCV