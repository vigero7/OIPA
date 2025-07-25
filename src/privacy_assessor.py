# src/privacy_assessor.py

class PrivacyAssessor:
    def __init__(self):
        # Define point values per item
        self.sensitivity_weights = {
            "face": 30,
            "name": 15,
            "email": 20,
            "location": 15,
            "date": 10,
            "gps": 25
        }

    def assess_privacy(self, metadata, faces, entities):
        score = 0
        reasons = []

        # Face detected
        if faces and len(faces) > 0:
            score += self.sensitivity_weights["face"]
            reasons.append("Faces detected")

        # Check entities
        if entities.get("names"):
            score += self.sensitivity_weights["name"]
            reasons.append("Name(s) found")
        if entities.get("emails"):
            score += self.sensitivity_weights["email"]
            reasons.append("Email(s) found")
        if entities.get("locations"):
            score += self.sensitivity_weights["location"]
            reasons.append("Location(s) found")
        if entities.get("dates"):
            score += self.sensitivity_weights["date"]
            reasons.append("Date(s) found")

        # EXIF GPS data
        gps_keys = ["GPS", "GPSInfo", "GPSLatitude", "GPSLongitude"]
        if any(key in metadata for key in gps_keys):
            score += self.sensitivity_weights["gps"]
            reasons.append("GPS metadata found")

        # Determine risk level
        if score >= 70:
            level = "HIGH"
        elif score >= 40:
            level = "MEDIUM"
        else:
            level = "LOW"

        return {
            "score": score,
            "risk_level": level,
            "reasons": reasons
        }
