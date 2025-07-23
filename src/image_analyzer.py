# src/image_analyzer.py

import face_recognition
from PIL import Image
import piexif

def extract_exif_metadata(image_path):
    """
    Extract EXIF metadata from an image (like GPS, camera model, datetime).
    """
    try:
        image = Image.open(image_path)

        # Check if image has EXIF data
        if "exif" not in image.info:
            print("[INFO] No EXIF data found in image.")
            return {}

        # Load EXIF using piexif
        exif_dict = piexif.load(image.info["exif"])
        readable = {}

        for ifd_name in exif_dict:
            if exif_dict[ifd_name] is None:
                continue
            for tag in exif_dict[ifd_name]:
                tag_name = piexif.TAGS[ifd_name].get(tag, {"name": tag})["name"]
                readable[tag_name] = exif_dict[ifd_name][tag]

        return readable

    except Exception as e:
        print(f"[ERROR] EXIF extraction failed: {e}")
        return {}

def detect_faces(image_path):
    """
    Detect faces in the image and return face bounding boxes (top, right, bottom, left).
    """
    try:
        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)
        return face_locations

    except Exception as e:
        print(f"[ERROR] Face detection failed: {e}")
        return []
