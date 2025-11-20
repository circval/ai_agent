import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Add any content in quotation marks to the specified file, creating the file first if it doesn't exist, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to write the file in, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to add to the requested directory",
                ),
            },
        ),
    )

def write_file(working_directory, file_path, content):
    active_working = os.path.abspath(working_directory)
    absolute_active_directory = os.path.abspath(os.path.join(working_directory, file_path))

    try:
        if not absolute_active_directory.startswith(active_working + os.sep):
            return (f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
        
        if os.path.exists(absolute_active_directory) == False:
            os.makedirs(os.path.dirname(absolute_active_directory), exist_ok=True)
       
        with open(absolute_active_directory, "w") as f:
            f.write(content)

    except Exception as e:
        return f"Error: {e}"
    
    return (f'Successfully wrote to "{file_path}" ({len(content)} characters written)')