import functions.get_files_info as get_files_info
import functions.get_file_content as get_file_content
from functions.write_file import write_file
import os

def test_get_files_info():
    print("Testing get_files_info function...\n")
    
    # Test 1: Current directory
    print("get_files_info(\"calculator\", \".\"):")
    print("Result for current directory:")
    try:
        result = get_files_info.get_files_info("calculator", ".")
    except Exception as e:
        print(f"    Error: {e}")
    print()
    
    # Test 2: pkg directory
    print("get_files_info(\"calculator\", \"pkg\"):")
    print("Result for 'pkg' directory:")
    try:
        result = get_files_info.get_files_info("calculator", "pkg")
    except Exception as e:
        print(f"    Error: {e}")
    print()
    
    # Test 3: /bin directory (should fail)
    print("get_files_info(\"calculator\", \"/bin\"):")
    print("Result for '/bin' directory:")
    try:
        result = get_files_info.get_files_info("calculator", "/bin")
    except Exception as e:
        print(f"    Error: {e}")
    print()
    
    # Test 4: ../ directory (should fail)
    print("get_files_info(\"calculator\", \"../\"):")
    print("Result for '../' directory:")
    try:
        result = get_files_info.get_files_info("calculator", "../")
    except Exception as e:
        print(f"    Error: {e}")
    print()


def test_get_file_content():
    print("Testing get_file_content function...\n")
    
    # Test cases
    test_cases = [
        ("calculator", "main.py", "Valid file in working directory"),
        ("calculator", "pkg/calculator.py", "Valid file in subdirectory"),
        ("calculator", "/bin/cat", "File outside working directory (should error)"),
        ("calculator", "pkg/does_not_exist.py", "Non-existent file (should error)")
    ]
    
    for working_dir, file_path, description in test_cases:
        print(f"Testing: {description}")
        print(f"get_file_content(\"{working_dir}\", \"{file_path}\"):")
        
        result = get_file_content.get_file_content(working_dir, file_path)
        
        # Check if the result is an error or actual content
        if result.startswith("Error:"):
            print(f"    Error occurred: {result}")
        else:
            print(f"    Success! Read {len(result)} characters")
            print(f"    Full content:\n{result}")
        
        print()


def test_write_file():
    print("Testing write_file function...\n")
    
    # Test cases with expected outcomes
    test_cases = [
        ("calculator", "lorem.txt", "wait, this isn't lorem ipsum", True),
        ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet", True),
        ("calculator", "/tmp/temp.txt", "this should not be allowed", False),
        ("calculator", "../outside.txt", "this should not be allowed", False)
    ]
    
    for working_dir, file_path, content, should_succeed in test_cases:
        try:
            result = write_file(working_dir, file_path, content)
            print(result)
        except Exception as e:
            print(e)
        print()

if __name__ == "__main__":
    # test_get_files_info()
    #test_get_file_content()
    test_write_file()