# src/report_generator.py

import json
from datetime import datetime

class ReportGenerator:
    def __init__(self, output_path="report.json"):
        self.output_path = output_path

    def _make_json_safe(self, data):
        """
        Recursively convert non-serializable values (e.g. bytes) to JSON-safe formats.
        """
        if isinstance(data, dict):
            return {k: self._make_json_safe(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [self._make_json_safe(i) for i in data]
        elif isinstance(data, bytes):
            return data.decode(errors="ignore")
        else:
            return data

    def generate(self, image_path, metadata, faces, entities, privacy_report):
        """
        Generate and save a privacy report in JSON format.
        """
        report = {
            "report_generated_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "image_analyzed": image_path,
            "face_count": len(faces),
            "exif_metadata": metadata,
            "entities_detected": entities,
            "privacy_risk": {
                "score": privacy_report["score"],
                "level": privacy_report["risk_level"],
                "reasons": privacy_report["reasons"]
            }
        }

        # ✅ Convert unsafe data before dumping to JSON
        safe_report = self._make_json_safe(report)

        with open(self.output_path, "w", encoding="utf-8") as f:
            json.dump(safe_report, f, indent=4)

        return safe_report
