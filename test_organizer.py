"""
=============================================================================
SMART JPG FILE ORGANIZER - AUTOMATED TEST SUITE
Python Programming Internship – Task 3: Task Automation

This test script validates all 5 required test cases:
- Test 1: Source folder contains 3 JPG files and 2 non-image files.
- Test 2: Source folder contains no JPG files.
- Test 3: Source folder does not exist.
- Test 4: Destination already contains a file with the same name (collision).
- Test 5: Source folder is empty.
=============================================================================
"""

import os
import shutil
import tempfile
import sys
from file_organizer import organize_jpg_files, view_files, get_unique_destination_path

# Minimal valid JPEG binary data for test files
DUMMY_JPG = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00\xff\xd9'


def run_all_tests():
    print("==================================================")
    print("RUNNING AUTOMATED TEST SUITE: SMART JPG ORGANIZER")
    print("==================================================")
    
    passed_tests = 0
    total_tests = 5

    temp_root = tempfile.mkdtemp(prefix="smart_organizer_tests_")
    test_log = os.path.join(temp_root, "test_log.txt")

    try:
        # ----------------------------------------------------
        # TEST 1: 3 JPG files and 2 non-image files
        # ----------------------------------------------------
        print("\n[TEST 1] Source with 3 JPG files and 2 non-image files...")
        src1 = os.path.join(temp_root, "test1_src")
        dst1 = os.path.join(temp_root, "test1_dst")
        os.makedirs(src1, exist_ok=True)

        # Create files
        for name in ["photo1.jpg", "photo2.jpg", "photo3.jpeg"]:
            with open(os.path.join(src1, name), "wb") as f:
                f.write(DUMMY_JPG)
        for name in ["document.pdf", "notes.txt"]:
            with open(os.path.join(src1, name), "w") as f:
                f.write("sample content")

        result1 = organize_jpg_files(src1, dst1, log_file=test_log)

        assert result1["total_scanned"] == 5, f"Expected 5 scanned, got {result1['total_scanned']}"
        assert result1["jpg_found"] == 3, f"Expected 3 JPGs, got {result1['jpg_found']}"
        assert result1["moved_count"] == 3, f"Expected 3 moved, got {result1['moved_count']}"
        assert result1["skipped_count"] == 2, f"Expected 2 skipped, got {result1['skipped_count']}"
        
        # Verify source retains 2 non-image files and 0 JPGs
        src1_files = os.listdir(src1)
        assert set(src1_files) == {"document.pdf", "notes.txt"}, f"Source files unexpected: {src1_files}"
        
        # Verify destination has 3 images
        dst1_files = os.listdir(dst1)
        assert set(dst1_files) == {"photo1.jpg", "photo2.jpg", "photo3.jpeg"}, f"Dest files unexpected: {dst1_files}"
        
        print(">>> TEST 1 PASSED: 3 JPGs moved, 2 non-images preserved in source.")
        passed_tests += 1

        # ----------------------------------------------------
        # TEST 2: Source contains no JPG files
        # ----------------------------------------------------
        print("\n[TEST 2] Source contains NO JPG files...")
        src2 = os.path.join(temp_root, "test2_src")
        dst2 = os.path.join(temp_root, "test2_dst")
        os.makedirs(src2, exist_ok=True)

        for name in ["report.docx", "data.csv", "archive.zip"]:
            with open(os.path.join(src2, name), "w") as f:
                f.write("data")

        result2 = organize_jpg_files(src2, dst2, log_file=test_log)

        assert result2["total_scanned"] == 3, f"Expected 3 scanned, got {result2['total_scanned']}"
        assert result2["jpg_found"] == 0, f"Expected 0 JPGs, got {result2['jpg_found']}"
        assert result2["moved_count"] == 0, f"Expected 0 moved, got {result2['moved_count']}"
        assert result2["skipped_count"] == 3, f"Expected 3 skipped, got {result2['skipped_count']}"
        assert "No JPG Images Found" in result2["status"]
        assert len(os.listdir(src2)) == 3, "Source files should not have been deleted or moved."

        print(">>> TEST 2 PASSED: Correct message displayed, 0 files moved.")
        passed_tests += 1

        # ----------------------------------------------------
        # TEST 3: Source folder does not exist
        # ----------------------------------------------------
        print("\n[TEST 3] Source folder does not exist...")
        src3 = os.path.join(temp_root, "non_existent_folder_xyz")
        dst3 = os.path.join(temp_root, "test3_dst")

        result3 = organize_jpg_files(src3, dst3, log_file=test_log)

        assert "Failed: Source Folder Not Found" in result3["status"]
        assert len(result3["errors"]) > 0
        assert result3["moved_count"] == 0

        print(">>> TEST 3 PASSED: Non-existent folder caught safely without crashing.")
        passed_tests += 1

        # ----------------------------------------------------
        # TEST 4: Destination already contains a file with the same name
        # ----------------------------------------------------
        print("\n[TEST 4] Duplicate filename collision in destination...")
        src4 = os.path.join(temp_root, "test4_src")
        dst4 = os.path.join(temp_root, "test4_dst")
        os.makedirs(src4, exist_ok=True)
        os.makedirs(dst4, exist_ok=True)

        # Existing file in destination
        with open(os.path.join(dst4, "photo1.jpg"), "w") as f:
            f.write("ORIGINAL_DESTINATION_FILE")

        # File in source with identical name
        with open(os.path.join(src4, "photo1.jpg"), "w") as f:
            f.write("NEW_INCOMING_FILE")

        result4 = organize_jpg_files(src4, dst4, log_file=test_log)

        assert result4["moved_count"] == 1
        dst4_files = sorted(os.listdir(dst4))
        assert "photo1.jpg" in dst4_files, "Original photo1.jpg must be preserved!"
        assert "photo1_1.jpg" in dst4_files, "New file should be renamed to photo1_1.jpg to avoid overwrite!"

        # Verify content integrity
        with open(os.path.join(dst4, "photo1.jpg"), "r") as f:
            original_content = f.read()
        with open(os.path.join(dst4, "photo1_1.jpg"), "r") as f:
            new_content = f.read()

        assert original_content == "ORIGINAL_DESTINATION_FILE", "Original file was overwritten!"
        assert new_content == "NEW_INCOMING_FILE", "New file content mismatch!"

        print(">>> TEST 4 PASSED: Duplicate preserved safely as 'photo1_1.jpg' without overwriting.")
        passed_tests += 1

        # ----------------------------------------------------
        # TEST 5: Source folder is empty
        # ----------------------------------------------------
        print("\n[TEST 5] Source folder is empty...")
        src5 = os.path.join(temp_root, "test5_empty_src")
        dst5 = os.path.join(temp_root, "test5_dst")
        os.makedirs(src5, exist_ok=True)

        result5 = organize_jpg_files(src5, dst5, log_file=test_log)

        assert result5["total_scanned"] == 0
        assert result5["moved_count"] == 0
        assert "Empty" in result5["status"]

        print(">>> TEST 5 PASSED: Handled empty source folder appropriately.")
        passed_tests += 1

    finally:
        shutil.rmtree(temp_root, ignore_errors=True)

    print("\n" + "=" * 50)
    print(f"TEST RESULTS: {passed_tests}/{total_tests} Tests Passed Successfully!")
    print("=" * 50)
    return passed_tests == total_tests


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
