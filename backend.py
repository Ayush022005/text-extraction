import pytesseract
from PIL import Image

def extract_text_from_image(image):
    try:
        # Extract text from the image
        text = pytesseract.image_to_string(image)

        return text.strip()
    except Exception as e:
        print("Error occurred during text extraction:", e)
        return None
