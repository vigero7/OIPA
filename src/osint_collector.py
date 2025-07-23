import os
import requests
from PIL import Image
from io import BytesIO

class OSINTImageCollector:
    def __init__(self, save_dir="data/sample_images"):
        self.save_dir = save_dir
        os.makedirs(save_dir, exist_ok=True)

    def save_uploaded_image(self, image_file, filename=None):
        """
        Save a user-uploaded image (e.g. from Streamlit) to the sample_images folder.
        """
        if not filename:
            filename = image_file.name
        save_path = os.path.join(self.save_dir, filename)
        image_file.save(save_path)
        return save_path

    def download_image_from_url(self, url, filename="downloaded_image.jpg"):
        """
        Download image from a URL and save it to the folder.
        """
        try:
            response = requests.get(url)
            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                save_path = os.path.join(self.save_dir, filename)
                image.save(save_path)
                return save_path
            else:
                print(f"Error: Failed to fetch image. Status code: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error downloading image: {e}")
            return None
