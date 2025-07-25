# src/ai_processor.py

import re
import spacy

class AIDataProcessor:
    def __init__(self, model="en_core_web_sm"):
        try:
            self.nlp = spacy.load(model)
        except OSError:
            from spacy.cli import download
            download(model)
            self.nlp = spacy.load(model)

    def extract_entities(self, text):
        """
        Extract names, emails, dates, and locations from text using spaCy and regex.
        """
        doc = self.nlp(text)
        entities = {
            "names": [],
            "locations": [],
            "emails": [],
            "dates": []
        }

        for ent in doc.ents:
            if ent.label_ == "PERSON":
                entities["names"].append(ent.text)
            elif ent.label_ == "GPE":
                entities["locations"].append(ent.text)
            elif ent.label_ == "DATE":
                entities["dates"].append(ent.text)

        # Extract emails
        emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
        entities["emails"].extend(emails)

        return entities
