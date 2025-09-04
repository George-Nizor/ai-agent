import os
from pathlib import Path
from .config import FILE_CHAR_LIMIT

def get_file_content(working_directory, file_path):
    try:
        # Resolve working dir and target (follow symlinks; no crash if missing)
        wd = Path(working_directory).resolve()
        target = Path(file_path)
        target = (target if target.is_absolute() else wd / target).resolve(strict=False)

        # Scope check (robust to prefix tricks and cross-drive on Windows)
        try:
            if os.path.commonpath([str(wd), str(target)]) != str(wd):
                return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        except Exception:
            # Covers ValueError on different drives, etc.
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Must be a regular file
        if not target.is_file():
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read up to limit+1 and truncate if needed
        limit = FILE_CHAR_LIMIT
        with open(target, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read(limit + 1)

        if len(content) > limit:
            content = content[:limit] + f'[...File "{file_path}" truncated at {limit} characters]'

        return content

    except Exception as e:
        return f"Error: {e}"
