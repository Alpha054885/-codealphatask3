# 📁 Smart JPG File Organizer

> **Python Programming Internship – Task 3: Task Automation**  
> *A clean, modular, and beginner-friendly Python automation tool designed to scan, filter, and organize JPG/JPEG image files safely and efficiently.*

---

## 📌 1. Project Introduction

In everyday computer workflows, downloading files, sorting camera uploads, and managing project media often leaves directories cluttered with a mixture of images, text documents, PDFs, and spreadsheets. Manually sifting through hundreds of files to locate and relocate images is tedious and error-prone.

**Smart JPG File Organizer** is a lightweight, professional Python automation script designed to eliminate manual sorting. It automatically scans any designated source directory, identifies all `.jpg` and `.jpeg` image files, and safely moves them into a dedicated destination folder (`JPG_Images/`), while leaving all other files completely intact in their original locations.

---

## 🎯 2. Project Objective

- **Automate Repetitive Tasks**: Save time and effort by automatically identifying and moving image files.
- **Maintain File Integrity**: Ensure non-image files (documents, spreadsheets, archives) remain untouched.
- **Prevent Accidental Overwrites**: Implement collision detection to automatically generate unique filenames if a file with the same name already exists in the destination.
- **Transparent Execution**: Provide an attractive terminal interface, comprehensive visual reports, and persistent chronological logging with timestamps.
- **Demonstrate Core Python Competencies**: Showcase proficiency with Python standard libraries (`os`, `shutil`), file I/O, control flow, functions, and defensive error handling.

---

## ✨ 3. Key Features

- **Automated Image Detection**: Scans files and accurately identifies `.jpg` and `.jpeg` extensions in a case-insensitive manner (e.g., `.JPG`, `.JPEG`, `.jpg`).
- **Interactive Terminal UI**: Simple, menu-driven command-line interface with distinct visual separators, headers, and status messages.
- **Non-Image Preservation**: Completely preserves documents (`.pdf`, `.txt`, `.docx`, etc.) in the source directory.
- **Collision Protection**: Automatically appends incremental counters (`photo1_1.jpg`, `photo1_2.jpg`) if duplicate filenames exist in the destination.
- **Safe Directory Operations**: Auto-creates the destination folder if it does not exist using `os.makedirs()`.
- **Safety Confirmation**: Asks for user confirmation before performing file operations on custom, user-specified directories.
- **Automated Summary Reporting**: Produces an executive summary table detailing total files scanned, images identified, images moved, and files skipped.
- **Persistent Logging**: Appends execution history, timestamps, file counts, and error details to `organize_log.txt`.
- **Zero External Dependencies**: Built 100% on Python's standard library—no `pip install` required.

---

## 🛠️ 4. Technologies & Tools Used

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Language** | Python 3 (3.8+) | Core programming language |
| **System Operations** | `os` module | Path handling, directory checks, file size retrieval, file listing |
| **File Operations** | `shutil` module | High-level file moving (`shutil.move`) |
| **Time & Logging** | `datetime` module | Timestamp generation for operation auditing |
| **Development Tools** | VS Code / Mac Terminal | Development environment and command-line execution |

---

## 🧠 5. Core Python Concepts Demonstrated

1. **`os` Module**:
   - `os.path.exists()`: Checks whether folders and files exist before attempting operations.
   - `os.path.isdir()` & `os.path.isfile()`: Differentiates subdirectories from regular files.
   - `os.listdir()`: Retrieves file entries from source directories.
   - `os.makedirs()`: Safely creates destination directories with `exist_ok=True`.
   - `os.path.splitext()`: Splits filename from its extension to support duplicate renaming.
   - `os.path.join()` & `os.path.normpath()`: Cross-platform directory path manipulation.

2. **`shutil` Module**:
   - `shutil.move()`: Performs safe, atomic file movement from source to destination.

3. **Modular Function Design**:
   - `display_menu()`: Renders the menu.
   - `view_files()`: Inspects and displays files in a table.
   - `organize_jpg_files()`: Core automation engine.
   - `get_unique_destination_path()`: Generates safe collision-free filenames.
   - `generate_report()`: Formats and displays the organization summary.
   - `save_log()`: Appends execution records to `organize_log.txt`.
   - `main()`: Orchestrates the user loop and CLI interactions.

4. **Control Flow & Loops**:
   - `while True` main interaction loop.
   - `for` loops to iterate through file listings.
   - `if-elif-else` branches to classify extensions and process user choices.

5. **Defensive Programming & Exception Handling**:
   - `try-except` blocks catching `PermissionError`, `OSError`, and `shutil.Error`.
   - Graceful handling of empty directories, non-existent paths, and missing JPG images without application crashes.

6. **File I/O**:
   - Reading binary and text files.
   - Context-managed (`with open(...) as f:`) log appending (`mode="a"`).

---

## 📂 6. Project Folder Structure

```text
Smart_JPG_Organizer/
│
├── file_organizer.py        # Main Python automation program
├── README.md                # Comprehensive project documentation
├── requirements.txt         # Project requirements and dependency notes
├── organize_log.txt         # Chronological log file with timestamps
├── reset_samples.py         # Utility script to re-create test demo files
├── test_organizer.py        # Automated test suite covering all 5 test cases
│
├── Source_Images/           # Default source folder with mixed files
│   ├── photo1.jpg           # Sample JPG image
│   ├── photo2.jpg           # Sample JPG image
│   ├── photo3.jpeg          # Sample JPEG image
│   ├── document.pdf         # Non-image file (preserved)
│   └── notes.txt            # Non-image file (preserved)
│
└── JPG_Images/              # Destination folder for organized images
    ├── photo1.jpg
    ├── photo2.jpg
    └── photo3.jpeg
```

---

## 🚀 7. Installation & Setup Instructions

### Prerequisites
- Python 3.8 or higher installed on your system.
- To verify your Python installation, open your terminal and run:
  ```bash
  python3 --version
  ```

### Step 1: Navigate to Project Directory
```bash
cd /Users/asiyaimran/.gemini/antigravity/scratch/Smart_JPG_Organizer
```

### Step 2: Check Dependencies
All dependencies are included with standard Python installations. To verify, inspect `requirements.txt`:
```bash
cat requirements.txt
```

---

## 💻 8. How to Run the Program

### Running in Mac Terminal / Linux / Windows Command Prompt
1. Open your terminal.
2. Navigate to the project directory:
   ```bash
   cd /Users/asiyaimran/.gemini/antigravity/scratch/Smart_JPG_Organizer
   ```
3. Run the organizer:
   ```bash
   python3 file_organizer.py
   ```

### Running in Visual Studio Code (VS Code)
1. Open VS Code.
2. Select **File > Open Folder...** and select `/Users/asiyaimran/.gemini/antigravity/scratch/Smart_JPG_Organizer`.
3. Open `file_organizer.py` in the editor.
4. Click the **Run** play button in the top right corner, or open the integrated terminal (`Ctrl + ~` or `Cmd + ~`) and type:
   ```bash
   python3 file_organizer.py
   ```

---

## 🖥️ 9. Sample Terminal Output

### Main Menu Interface
```text
========================================
SMART JPG FILE ORGANIZER
Python Automation
========================================

Welcome to Smart JPG File Organizer!

This tool automatically organizes your JPG images.

Menu:
1. Organize JPG Images
2. View Available Files
3. Exit
========================================
Choose an option: 1
```

### Viewing Files Before Organization (Option 2)
```text
--------------------------------------------------
VIEW FILES IN: Source_Images
Full Path: /.../Smart_JPG_Organizer/Source_Images
--------------------------------------------------
#    File Name                      Type / Category Size (Bytes)
-----------------------------------------------------------------
1    document.pdf                   Other File      32        
2    notes.txt                      Other File      56        
3    photo1.jpg                     JPG Image       149       
4    photo2.jpg                     JPG Image       149       
5    photo3.jpeg                    JPG Image       149       
-----------------------------------------------------------------
Summary: 5 file(s) total | 3 JPG image(s) | 2 other file(s)
-----------------------------------------------------------------
```

### Organization Process & Final Report (Option 1)
```text
Starting file organization...
Source Folder:      /.../Smart_JPG_Organizer/Source_Images
Destination Folder: /.../Smart_JPG_Organizer/JPG_Images

Processing 3 JPG image(s)...
[SUCCESS] Moved: 'photo1.jpg' -> 'photo1.jpg'
[SUCCESS] Moved: 'photo2.jpg' -> 'photo2.jpg'
[SUCCESS] Moved: 'photo3.jpeg' -> 'photo3.jpeg'

========== ORGANIZATION REPORT ==========
Total files scanned: 5
JPG images found: 3
Images successfully moved: 3
Other files skipped: 2

Status: Completed Successfully!

Source Folder: Source_Images
Destination Folder: JPG_Images
=========================================
```

### Sample Log Output (`organize_log.txt`)
```text
[2026-11-10 08:56:05] Source: '/.../Source_Images' | Destination: '/.../JPG_Images' | Scanned: 5 | Moved: 3 | Errors: None
```

---

## 🧪 10. Testing Details & Test Scenarios

The project includes an automated test harness (`test_organizer.py`) covering all five required test cases.

To execute the full test suite:
```bash
python3 test_organizer.py
```

### Test Case Matrix

| Test Case | Scenario / Condition | Expected Behavior | Actual Result |
| :--- | :--- | :--- | :--- |
| **Test 1** | Source folder contains 3 JPGs and 2 non-image files | 3 JPGs moved to destination; 2 non-images preserved in source | **PASSED** |
| **Test 2** | Source folder contains no JPG files | Displays notice; 0 files moved; original files untouched | **PASSED** |
| **Test 3** | Source folder path does not exist | Displays user-friendly error message without crashing | **PASSED** |
| **Test 4** | Destination already contains a file with same name | Preserves both files; appends unique counter (`photo1_1.jpg`) | **PASSED** |
| **Test 5** | Source folder is empty | Displays informative empty folder notice; exits gracefully | **PASSED** |

### Resetting Test Files
Whenever you want to re-run demonstrations, simply run:
```bash
python3 reset_samples.py
```
This instantly restores `Source_Images/` with 3 JPGs and 2 documents, and cleans `JPG_Images/`.

---

## 🎓 11. Internship Evaluation Guide (Q&A for Students)

When presenting this project during an internship viva or evaluation:

- **Q: Why use `shutil.move` instead of `os.rename`?**  
  *A:* `shutil.move` is higher-level and works seamlessly across different filesystems or storage partitions, whereas `os.rename` can raise an `OSError` (EXDEV) if source and destination reside on separate mount points.
- **Q: How does the program avoid overwriting files?**  
  *A:* The `get_unique_destination_path()` function checks if a file with the target name exists in the destination. If found, it parses the filename and extension using `os.path.splitext()` and dynamically appends an incrementing counter (`_1`, `_2`, etc.) until a free filename is found.
- **Q: How are subdirectories handled inside the source folder?**  
  *A:* The script uses `os.path.isfile()` to process only regular files, ignoring nested folders to prevent accidental directory moves or crashes.
- **Q: How is user safety ensured?**  
  *A:* If the user specifies a custom directory instead of the project's default sample folder, an explicit confirmation prompt (`(y/n)`) is presented before any operation begins.

---

## 🏁 12. Conclusion

The **Smart JPG File Organizer** demonstrates how foundational Python scripting concepts—file systems, defensive programming, automated logging, and command-line interfaces—can be combined into a robust and valuable real-world automation tool. It adheres strictly to industry standards for code readability, error tolerance, user safety, and project organization.
