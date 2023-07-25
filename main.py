import streamlit as st
from PIL import Image
from backend import extract_text_from_image

def main():
    st.title("Text Extraction from Image using Tesseract OCR")
    st.write("Upload an image and click the 'Extract Text' button to get the extracted text.")

    # File uploader widget
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Extract text on button click
        if st.button("Extract Text"):
            extracted_text = extract_text_from_image(image)
            if extracted_text:
                st.subheader("Extracted Text:")
                st.write(extracted_text)

                # Add "Copy to Clipboard" button
                if st.button("Copy to Clipboard"):
                    st.session_state.clipboard = extracted_text
                    st.experimental_rerun()

            else:
                st.error("Failed to extract text from the image.")
    else:
        st.info("Please upload an image file.")

if __name__ == "__main__":
    main()
