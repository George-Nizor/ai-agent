import os

def get_files_info(working_directory, directory="."):
    # Resolve the full path of the directory to check
    if os.path.isabs(directory):
        full_path = directory
    else:
        full_path = os.path.join(working_directory, directory)
    
    # Check if the resolved path is a directory
    if not os.path.isdir(full_path):
        raise Exception(f'"{directory}" is not a directory')

    # Check if the resolved path is outside working directory
    if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
        raise Exception(f'Cannot list "{directory}" as it is outside the permitted working directory')

    files_info = {}
    for file in os.listdir(full_path):
        file_path = os.path.join(full_path, file)
        files_info[file] = {
            "file_size": os.path.getsize(file_path),
            "is_dir": os.path.isdir(file_path)
        }
    for file, info in files_info.items():
        print(f"- {file}: file_size={info['file_size']} bytes, is_dir={info['is_dir']}")
    return files_info