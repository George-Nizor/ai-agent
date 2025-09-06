import os

def write_file(working_directory, file_path, content):
    # Convert to absolute paths for proper comparison
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    # Check if the file path is within the working directory
    if not abs_file_path.startswith(abs_working_dir):
        raise Exception(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
    
    # Create parent directories if they don't exist
    parent_dir = os.path.dirname(abs_file_path)
    if parent_dir and not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
    
    # Write the file
    with open(abs_file_path, "w") as f:
        f.write(content)
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'