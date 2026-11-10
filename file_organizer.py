"""
=============================================================================
SMART JPG FILE ORGANIZER
Python Programming Internship – Task 3: Task Automation

Description:
    An automated Python utility to scan, identify, and organize JPG/JPEG image
    files from a specified source folder into a dedicated destination folder.
    Non-image files remain untouched, duplicate filenames are safely handled
    without overwriting, and all operations are logged with timestamps.

Author: Python Developer Intern
Language: Python 3
Modules Used: os, shutil, datetime (Standard Library)
=============================================================================
"""

import os
import shutil
from datetime import datetime

# Define base directory of the project for reliable path resolution
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_SOURCE_DIR = os.path.join(BASE_DIR, "Source_Images")
DEFAULT_DEST_DIR = os.path.join(BASE_DIR, "JPG_Images")
DEFAULT_LOG_FILE = os.path.join(BASE_DIR, "organize_log.txt")

# Supported JPG file extensions (case-insensitive)
JPG_EXTENSIONS = (".jpg", ".jpeg")


def display_menu():
    """
    Displays the main interactive terminal menu.
    Uses clean formatting and clear separation.
    """
    print("\n" + "=" * 40)
    print("SMART JPG FILE ORGANIZER")
    print("Python Automation")
    print("=" * 40)
    print("\nWelcome to Smart JPG File Organizer!")
    print("\nThis tool automatically organizes your JPG images.")
    print("\nMenu:")
    print("1. Organize JPG Images")
    print("2. View Available Files")
    print("3. Exit")
    print("=" * 40)


def view_files(folder_path=None):
    """
    Displays all files inside a given directory, categorized as JPG or other.
    
    Parameters:
        folder_path (str): The folder to scan. Defaults to DEFAULT_SOURCE_DIR.
    """
    if not folder_path:
        folder_path = DEFAULT_SOURCE_DIR

    # Resolve relative paths against BASE_DIR
    if not os.path.isabs(folder_path):
        folder_path = os.path.normpath(os.path.join(BASE_DIR, folder_path))

    print("\n" + "-" * 50)
    print(f"VIEW FILES IN: {os.path.basename(folder_path)}")
    print(f"Full Path: {folder_path}")
    print("-" * 50)

    # Check if folder exists
    if not os.path.exists(folder_path):
        print(f"[ERROR] The directory '{folder_path}' does not exist.")
        print("-" * 50)
        return

    # Check if it is a directory
    if not os.path.isdir(folder_path):
        print(f"[ERROR] The path '{folder_path}' is not a directory.")
        print("-" * 50)
        return

    try:
        all_entries = os.listdir(folder_path)
    except PermissionError:
        print(f"[ERROR] Permission denied: Cannot read folder '{folder_path}'.")
        print("-" * 50)
        return
    except Exception as e:
        print(f"[ERROR] Unable to access folder: {e}")
        print("-" * 50)
        return

    # Filter only regular files
    files = [f for f in all_entries if os.path.isfile(os.path.join(folder_path, f))]

    if not files:
        print("[INFO] The directory is empty (no files found).")
        print("-" * 50)
        return

    jpg_count = 0
    other_count = 0

    print(f"{'#':<4} {'File Name':<30} {'Type / Category':<15} {'Size (Bytes)'}")
    print("-" * 65)

    for index, filename in enumerate(sorted(files), start=1):
        filepath = os.path.join(folder_path, filename)
        file_size = os.path.getsize(filepath)

        if filename.lower().endswith(JPG_EXTENSIONS):
            category = "JPG Image"
            jpg_count += 1
        else:
            category = "Other File"
            other_count += 1

        print(f"{index:<4} {filename:<30} {category:<15} {file_size:<10}")

    print("-" * 65)
    print(f"Summary: {len(files)} file(s) total | {jpg_count} JPG image(s) | {other_count} other file(s)")
    print("-" * 65)


def get_unique_destination_path(destination_folder, filename):
    """
    Generates a unique destination path if a file with the same name already exists.
    Prevents overwriting existing files by appending an incrementing counter (_1, _2, etc.).

    Parameters:
        destination_folder (str): Target folder path.
        filename (str): Name of the file to move.

    Returns:
        tuple: (final_filepath, final_filename, was_renamed)
    """
    dest_path = os.path.join(destination_folder, filename)
    if not os.path.exists(dest_path):
        return dest_path, filename, False

    name, ext = os.path.splitext(filename)
    counter = 1
    while True:
        new_filename = f"{name}_{counter}{ext}"
        new_dest_path = os.path.join(destination_folder, new_filename)
        if not os.path.exists(new_dest_path):
            return new_dest_path, new_filename, True
        counter += 1


def generate_report(total_scanned, jpg_found, moved_count, skipped_count, source_folder, destination_folder, status):
    """
    Prints a formatted organization summary report.

    Parameters:
        total_scanned (int): Total files scanned.
        jpg_found (int): Total JPG/JPEG files identified.
        moved_count (int): Images successfully transferred.
        skipped_count (int): Non-image and un-moved files.
        source_folder (str): Source directory name/path.
        destination_folder (str): Destination directory name/path.
        status (str): Overall process status message.
    """
    print("\n========== ORGANIZATION REPORT ==========")
    print(f"Total files scanned: {total_scanned}")
    print(f"JPG images found: {jpg_found}")
    print(f"Images successfully moved: {moved_count}")
    print(f"Other files skipped: {skipped_count}")
    print(f"\nStatus: {status}")
    print(f"\nSource Folder: {os.path.basename(source_folder) or source_folder}")
    print(f"Destination Folder: {os.path.basename(destination_folder) or destination_folder}")
    print("=========================================\n")


def save_log(log_file, source_folder, destination_folder, total_scanned, moved_count, errors=None):
    """
    Appends an operation log entry to organize_log.txt with timestamps.

    Parameters:
        log_file (str): Path to log file.
        source_folder (str): Source directory.
        destination_folder (str): Destination directory.
        total_scanned (int): Files scanned.
        moved_count (int): Files moved.
        errors (list or None): List of error strings, if any occurred.
    """
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_msg = "; ".join(errors) if errors else "None"

        log_entry = (
            f"[{timestamp}] "
            f"Source: '{source_folder}' | "
            f"Destination: '{destination_folder}' | "
            f"Scanned: {total_scanned} | "
            f"Moved: {moved_count} | "
            f"Errors: {error_msg}\n"
        )

        with open(log_file, "a", encoding="utf-8") as f:
            f.write(log_entry)

    except Exception as e:
        print(f"[WARNING] Could not write to log file '{log_file}': {e}")


def organize_jpg_files(source_folder=None, destination_folder=None, log_file=None):
    """
    Main automation engine to scan, identify, and move JPG/JPEG files.
    
    Parameters:
        source_folder (str): Directory containing source files.
        destination_folder (str): Directory to receive organized JPG images.
        log_file (str): File path for operation logs.

    Returns:
        dict: Summary statistics and execution status.
    """
    # Use default paths if not provided
    if not source_folder:
        source_folder = DEFAULT_SOURCE_DIR
    if not destination_folder:
        destination_folder = DEFAULT_DEST_DIR
    if not log_file:
        log_file = DEFAULT_LOG_FILE

    # Normalize relative paths against BASE_DIR
    if not os.path.isabs(source_folder):
        source_folder = os.path.normpath(os.path.join(BASE_DIR, source_folder))
    if not os.path.isabs(destination_folder):
        destination_folder = os.path.normpath(os.path.join(BASE_DIR, destination_folder))
    if not os.path.isabs(log_file):
        log_file = os.path.normpath(os.path.join(BASE_DIR, log_file))

    errors = []
    total_scanned = 0
    jpg_found = 0
    moved_count = 0
    skipped_count = 0

    print("\nStarting file organization...")
    print(f"Source Folder:      {source_folder}")
    print(f"Destination Folder: {destination_folder}")

    # 1. Check whether source folder exists
    if not os.path.exists(source_folder):
        error_msg = f"Source folder '{source_folder}' does not exist."
        print(f"\n[ERROR] {error_msg}")
        errors.append(error_msg)
        status = "Failed: Source Folder Not Found"
        generate_report(total_scanned, jpg_found, moved_count, skipped_count, source_folder, destination_folder, status)
        save_log(log_file, source_folder, destination_folder, total_scanned, moved_count, errors)
        return {
            "total_scanned": total_scanned,
            "jpg_found": jpg_found,
            "moved_count": moved_count,
            "skipped_count": skipped_count,
            "status": status,
            "errors": errors
        }

    # Verify that source is a directory
    if not os.path.isdir(source_folder):
        error_msg = f"Source path '{source_folder}' is a file, not a directory."
        print(f"\n[ERROR] {error_msg}")
        errors.append(error_msg)
        status = "Failed: Invalid Source Directory"
        generate_report(total_scanned, jpg_found, moved_count, skipped_count, source_folder, destination_folder, status)
        save_log(log_file, source_folder, destination_folder, total_scanned, moved_count, errors)
        return {
            "total_scanned": total_scanned,
            "jpg_found": jpg_found,
            "moved_count": moved_count,
            "skipped_count": skipped_count,
            "status": status,
            "errors": errors
        }

    # 2. Read contents of the source folder
    try:
        items = os.listdir(source_folder)
    except PermissionError:
        error_msg = f"Permission denied while reading source folder '{source_folder}'."
        print(f"\n[ERROR] {error_msg}")
        errors.append(error_msg)
        status = "Failed: Permission Denied"
        generate_report(total_scanned, jpg_found, moved_count, skipped_count, source_folder, destination_folder, status)
        save_log(log_file, source_folder, destination_folder, total_scanned, moved_count, errors)
        return {
            "total_scanned": total_scanned,
            "jpg_found": jpg_found,
            "moved_count": moved_count,
            "skipped_count": skipped_count,
            "status": status,
            "errors": errors
        }

    # Filter only regular files (ignore directories)
    files = [f for f in items if os.path.isfile(os.path.join(source_folder, f))]
    total_scanned = len(files)

    # 3. Check if source folder is empty
    if total_scanned == 0:
        print(f"\n[INFO] The source folder '{os.path.basename(source_folder)}' is empty. No files to process.")
        status = "Completed: Source Folder Is Empty"
        generate_report(total_scanned, jpg_found, moved_count, skipped_count, source_folder, destination_folder, status)
        save_log(log_file, source_folder, destination_folder, total_scanned, moved_count, errors)
        return {
            "total_scanned": total_scanned,
            "jpg_found": jpg_found,
            "moved_count": moved_count,
            "skipped_count": skipped_count,
            "status": status,
            "errors": errors
        }

    # 4. Identify JPG/JPEG images
    jpg_files = [f for f in files if f.lower().endswith(JPG_EXTENSIONS)]
    jpg_found = len(jpg_files)
    skipped_count = total_scanned - jpg_found

    # 5. Check if no JPG images are found
    if jpg_found == 0:
        print(f"\n[INFO] No JPG or JPEG images found in '{os.path.basename(source_folder)}'.")
        print(f"[INFO] All {skipped_count} non-image file(s) remain untouched in the source folder.")
        status = "Completed: No JPG Images Found"
        generate_report(total_scanned, jpg_found, moved_count, skipped_count, source_folder, destination_folder, status)
        save_log(log_file, source_folder, destination_folder, total_scanned, moved_count, errors)
        return {
            "total_scanned": total_scanned,
            "jpg_found": jpg_found,
            "moved_count": moved_count,
            "skipped_count": skipped_count,
            "status": status,
            "errors": errors
        }

    # 6. Create destination folder if it does not exist
    if not os.path.exists(destination_folder):
        try:
            os.makedirs(destination_folder, exist_ok=True)
            print(f"[INFO] Created destination folder: '{destination_folder}'")
        except Exception as e:
            error_msg = f"Failed to create destination folder: {e}"
            print(f"[ERROR] {error_msg}")
            errors.append(error_msg)
            status = "Failed: Destination Folder Creation Error"
            generate_report(total_scanned, jpg_found, moved_count, skipped_count, source_folder, destination_folder, status)
            save_log(log_file, source_folder, destination_folder, total_scanned, moved_count, errors)
            return {
                "total_scanned": total_scanned,
                "jpg_found": jpg_found,
                "moved_count": moved_count,
                "skipped_count": skipped_count,
                "status": status,
                "errors": errors
            }

    # 7. Move identified JPG images into the destination folder
    print(f"\nProcessing {jpg_found} JPG image(s)...")

    for filename in jpg_files:
        src_path = os.path.join(source_folder, filename)
        
        # Safe duplicate handling: generate unique filename if name already exists in destination
        dest_path, final_name, was_renamed = get_unique_destination_path(destination_folder, filename)

        if was_renamed:
            print(f"[DUPLICATE] '{filename}' already exists in destination. Renaming to '{final_name}'...")

        try:
            shutil.move(src_path, dest_path)
            moved_count += 1
            print(f"[SUCCESS] Moved: '{filename}' -> '{final_name}'")
        except PermissionError:
            err = f"Permission denied while moving '{filename}'."
            print(f"[ERROR] {err}")
            errors.append(err)
            skipped_count += 1
        except Exception as e:
            err = f"Error moving '{filename}': {e}"
            print(f"[ERROR] {err}")
            errors.append(err)
            skipped_count += 1

    # 8. Determine final status
    if errors:
        status = "Completed With Warnings/Errors"
    else:
        status = "Completed Successfully!"

    # 9. Generate and display final report
    generate_report(total_scanned, jpg_found, moved_count, skipped_count, source_folder, destination_folder, status)

    # 10. Record operation in organize_log.txt
    save_log(log_file, source_folder, destination_folder, total_scanned, moved_count, errors)

    return {
        "total_scanned": total_scanned,
        "jpg_found": jpg_found,
        "moved_count": moved_count,
        "skipped_count": skipped_count,
        "status": status,
        "errors": errors
    }


def main():
    """
    Main interactive entry point for the Smart JPG File Organizer CLI.
    Runs the terminal menu loop, prompts user inputs, and triggers operations safely.
    """
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("\n" + "=" * 40)
            print("OPTION 1: ORGANIZE JPG IMAGES")
            print("=" * 40)

            # Accept source folder path with default option
            print("\nDefault Source Folder: 'Source_Images'")
            source_input = input("Enter source folder path (or press Enter for default): ").strip()
            source_folder = source_input if source_input else DEFAULT_SOURCE_DIR

            # Safety check: if user specifies a custom folder, require explicit confirmation
            if source_input:
                resolved_source = os.path.normpath(os.path.join(BASE_DIR, source_input)) if not os.path.isabs(source_input) else source_input
                if resolved_source != os.path.normpath(DEFAULT_SOURCE_DIR):
                    print(f"\n[SAFETY CHECK] You specified a custom source folder:")
                    print(f"               '{resolved_source}'")
                    confirm = input("Are you sure you want to move JPG images from this folder? (y/n): ").strip().lower()
                    if confirm != "y":
                        print("[CANCELLED] Operation cancelled. No files were moved.")
                        input("\nPress Enter to return to the menu...")
                        continue

            # Accept destination folder path with default option
            print("\nDefault Destination Folder: 'JPG_Images'")
            dest_input = input("Enter destination folder path (or press Enter for default): ").strip()
            destination_folder = dest_input if dest_input else DEFAULT_DEST_DIR

            # Execute organization
            organize_jpg_files(source_folder, destination_folder)
            input("Press Enter to return to the menu...")

        elif choice == "2":
            print("\n" + "=" * 40)
            print("OPTION 2: VIEW AVAILABLE FILES")
            print("=" * 40)

            print("\nDefault Source Folder: 'Source_Images'")
            target_input = input("Enter folder path to inspect (or press Enter for default): ").strip()
            target_folder = target_input if target_input else DEFAULT_SOURCE_DIR

            view_files(target_folder)
            input("\nPress Enter to return to the menu...")

        elif choice == "3":
            print("\n" + "=" * 40)
            print("Thank you for using Smart JPG File Organizer!")
            print("Exiting application. Have a great day!")
            print("=" * 40 + "\n")
            break

        else:
            print("\n[INVALID INPUT] Please enter a valid number (1, 2, or 3).")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
