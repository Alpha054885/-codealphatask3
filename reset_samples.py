"""
=============================================================================
SMART JPG FILE ORGANIZER - DEMO RESET UTILITY
=============================================================================
Quickly restores the demonstration files in 'Source_Images' and clears 'JPG_Images'
so the user, evaluator, or internship mentor can test the program repeatedly.
=============================================================================
"""

import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_DIR = os.path.join(BASE_DIR, "Source_Images")
DEST_DIR = os.path.join(BASE_DIR, "JPG_Images")

# Minimal valid 1x1 JPEG binary
SAMPLE_JPEG_BYTES = (
    b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00\xff\xdb\x00C\x00'
    b'\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\t\t\x08\n\x0c\x14\r\x0c\x0b\x0b\x0c\x19'
    b'\x12\x13\x0f\x14\x1d\x1a\x1f\x1e\x1d\x1a\x1c\x1c $.\' ",#\x1c\x1c(7),01444\x1f\'9=82<.342'
    b'\xff\xc0\x00\x0b\x08\x00\x01\x00\x01\x01\x01\x11\x00\xff\xc4\x00\x1f\x00\x00\x01\x05'
    b'\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07'
    b'\x08\t\n\x0b\xff\xda\x00\x08\x01\x01\x00\x00?\x00\xbf\x00\xff\xd9'
)


def reset_environment():
    print("Resetting demo environment for Smart JPG File Organizer...")
    
    # 1. Clean and recreate Source_Images
    os.makedirs(SOURCE_DIR, exist_ok=True)
    for f in os.listdir(SOURCE_DIR):
        file_path = os.path.join(SOURCE_DIR, f)
        if os.path.isfile(file_path):
            os.remove(file_path)

    # 2. Clean and recreate JPG_Images
    os.makedirs(DEST_DIR, exist_ok=True)
    for f in os.listdir(DEST_DIR):
        file_path = os.path.join(DEST_DIR, f)
        if os.path.isfile(file_path):
            os.remove(file_path)

    # 3. Create fresh sample files in Source_Images
    with open(os.path.join(SOURCE_DIR, "photo1.jpg"), "wb") as f:
        f.write(SAMPLE_JPEG_BYTES)

    with open(os.path.join(SOURCE_DIR, "photo2.jpg"), "wb") as f:
        f.write(SAMPLE_JPEG_BYTES)

    with open(os.path.join(SOURCE_DIR, "photo3.jpeg"), "wb") as f:
        f.write(SAMPLE_JPEG_BYTES)

    with open(os.path.join(SOURCE_DIR, "document.pdf"), "w", encoding="utf-8") as f:
        f.write("%PDF-1.4 Sample Document Content for testing non-image preservation.")

    with open(os.path.join(SOURCE_DIR, "notes.txt"), "w", encoding="utf-8") as f:
        f.write("Internship Task Notes: Ensure all non-JPG files remain untouched.")

    print(f"Sample environment successfully reset:")
    print(f" - Source_Images : 3 JPG/JPEG images, 2 non-image documents")
    print(f" - JPG_Images    : Directory cleared and ready")


if __name__ == "__main__":
    reset_environment()
