import os

def get_files_info(working_directory, directory="."):
    # Check if directory is a directory
    if not os.path.isdir(directory):
        raise Exception(f'Error: "{directory}" is not a directory')

    # Check if directory is outside working directory
    if not os.path.abspath(directory).startswith(working_directory):
        raise Exception(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

    files_info = {}
    full_path = os.path.join(working_directory, directory)
    for file in os.listdir(full_path):
        file_path = os.path.join(full_path, file)
        files_info[file] = {
            "file_size": os.path.getsize(file_path),
            "is_dir": os.path.isdir(file_path)
        }
    for file, info in files_info.items():
        print(f"- {file}: file_size={info['file_size']} bytes, is_dir={info['is_dir']}")
    return files_info