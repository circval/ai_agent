import os

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