# OIPA - Open Source Image Privacy Analyzer

> OIPA is a lightweight yet powerful image privacy analysis tool. Built for cybersecurity & OSINT research, it scans images for embedded metadata, detects faces, extracts entities using AI/NLP, and generates privacy risk reports based on your findings.

---

## ✨ Features

* ✅ EXIF Metadata Extraction (GPS, timestamps, camera info)
* ✅ Face Detection using `face_recognition`
* ✅ AI-based Named Entity Recognition with spaCy
* ✅ OSINT scraping & entity merging (URLs, names, emails, etc.)
* ✅ Privacy Risk Scoring & Categorization
* ✅ Clean JSON Report Generation
* ✅ CLI Tool with support for local files and image URLs

---

## 📁 Project Structure

```
OIPA/
├── src/
│   ├── ai_processor.py
│   ├── image_analyzer.py
│   ├── osint_collector.py
│   ├── privacy_assessor.py
│   ├── report_generator.py
│   └── reverse_image_search.py
├── data/sample_images/
└── main.py
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/OIPA.git
cd OIPA
```

### 2. Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Unix
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 3. Run the Analyzer

```bash
python main.py --image data/sample_images/1.jpg
# or
python main.py --url https://example.com/photo.jpg
```

---

## 📊 Sample Output

```json
{
  "image_analyzed": "data/sample_images/1.jpg",
  "face_count": 1,
  "exif_metadata": {},
  "entities_detected": {
    "names": ["John Doe"],
    "emails": ["johndoe@email.com"],
    "locations": ["New York"],
    "dates": ["2022-05-12"]
  },
  "privacy_risk": {
    "score": 60,
    "level": "HIGH",
    "reasons": ["Name detected", "Email found"]
  },
  "report_generated_on": "2025-07-25 19:32:58"
}
```

---

## 🫡 Use Cases

* Cybersecurity & Digital Privacy Awareness
* OSINT Investigations
* Image Data Audits before Uploading
* Educational Demonstrations on Metadata & PII

---

## ⚖️ License

This project is licensed under the **MIT License**. Feel free to use, modify, and distribute with credit.

---

## ✨ Future Enhancements

* 🔍 Real-time face recognition from live camera feeds
* 🌐 Reverse image search across multiple engines (e.g. Google, Bing, Tineye)
* 🧠 Advanced AI-based OSINT enrichment (detecting real-time location, phone, emails)
* 📡 Geolocation triangulation based on EXIF + facial region
* 🧬 Face vector profiling and persistent identity tracking
* 📺 Streamlit-based Web UI for easier interaction

---

## 🙌 Author

**Ankit Singh**
Cybersecurity Student | OSINT Enthusiast | Python Developer
GitHub: [@ankit-singh](https://github.com/<your-username>)

---

> If you find this project useful, consider giving it a ⭐ star!
