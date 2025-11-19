import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )

def get_files_info(working_directory, directory="."):
    active_working = os.path.abspath(working_directory)
    absolute_active_directory = os.path.abspath(os.path.join(working_directory, directory))

    if not (absolute_active_directory == active_working or absolute_active_directory.startswith(active_working + os.sep)):
        return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"
    elif os.path.isdir(absolute_active_directory) == False:
        return f"Error: '{directory}' is not a directory"
    
    try:
        directory_content = []
        for name in os.listdir(path=absolute_active_directory):
            full = os.path.join(absolute_active_directory, name)
            size = os.path.getsize(full)
            is_dir = os.path.isdir(full)
            directory_content.append(f"- {name}: file_size={size} bytes, is_dir={is_dir}")
        return "\n".join(directory_content)
    except Exception as e:
        return f"Error: {e}"
    

    

