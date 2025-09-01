import functions.get_files_info as get_files_info
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

if __name__ == "__main__":
    test_get_files_info()
