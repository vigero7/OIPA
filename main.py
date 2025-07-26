import argparse
import os
import tempfile
import pprint

from src.osint_collector import OSINTImageCollector
from src.image_analyzer import extract_exif_metadata, detect_faces
from src.ai_processor import AIDataProcessor
from src.privacy_assessor import PrivacyAssessor
from src.report_generator import ReportGenerator


def download_from_url(url):
    collector = OSINTImageCollector()
    temp_dir = tempfile.gettempdir()
    filename = os.path.join(temp_dir, "downloaded_image.jpg")
    collector.download_image_from_url(url, filename)
    return filename


def get_caption(image_path):
    """
    Get a caption for NLP entity extraction.
    1. If a .txt file with the same name exists, use its content
    2. Else, fallback to image file name
    """
    base, _ = os.path.splitext(image_path)
    caption_file = base + ".txt"

    if os.path.exists(caption_file):
        print(f"[i] Found caption file: {caption_file}")
        with open(caption_file, "r", encoding="utf-8") as f:
            return f.read().strip()
    else:
        print("[i] Using image filename as caption")
        return os.path.basename(image_path).replace("_", " ")


def analyze(image_path):
    print("\n🔍 Analyzing image:", image_path)

    # 1. EXIF metadata
    metadata = extract_exif_metadata(image_path)
    print("[✓] Metadata extracted")

    # 2. Face detection
    faces = detect_faces(image_path)
    print(f"[✓] {len(faces)} face(s) detected")

    # 3. NLP entity extraction from caption
    caption = get_caption(image_path)
    processor = AIDataProcessor()
    entities = processor.extract_entities(caption)
    print("[✓] Entities extracted")

    # 4. Privacy assessment
    assessor = PrivacyAssessor()
    privacy_report = assessor.assess_privacy(metadata, faces, entities)
    print(f"[✓] Privacy Risk: {privacy_report['risk_level']} (Score: {privacy_report['score']})")

    # 5. Report generation
    reporter = ReportGenerator("report.json")
    final = reporter.generate(
        image_path=image_path,
        metadata=metadata,
        faces=faces,
        entities=entities,
        privacy_report=privacy_report
    )

    print("\n📄 Final Report Summary:")
    pprint.pprint(final)
    print("\n✅ Report saved to: report.json")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OIPA - Open Source Image Privacy Analyzer")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--image", help="Path to local image file")
    group.add_argument("--url", help="Image URL to download and analyze")
    args = parser.parse_args()

    if args.url:
        local_path = download_from_url(args.url)
        analyze(local_path)
    else:
        analyze(args.image)
