import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    active_working = os.path.abspath(working_directory)
    absolute_active_directory = os.path.abspath(os.path.join(working_directory, file_path))

    if not absolute_active_directory.startswith(active_working + os.sep):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif os.path.isfile(absolute_active_directory) == False:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(absolute_active_directory, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            extra_content = f.read(1)
            if extra_content:
                return file_content_string + f'[...File "{file_path}" truncated at {MAX_CHARS}]'
            return file_content_string
    
    except Exception as e:
        return f"Error: {e}"