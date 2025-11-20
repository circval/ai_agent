import os, subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run python file in specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to run files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )

def run_python_file(working_directory, file_path, args=[]):
    active_working = os.path.abspath(working_directory)
    absolute_active_directory = os.path.abspath(os.path.join(working_directory, file_path))

    try:
        if not absolute_active_directory.startswith(active_working + os.sep):
            return (f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        
        elif os.path.exists(absolute_active_directory) == False:
            return (f'Error: File "{file_path}" not found.')
        
        elif file_path.endswith(".py") == False:
            return (f'Error: "{file_path}" is not a Python file.')

    except Exception as e:
        return f"Error: {e}"
        
    try:
        completed_process = subprocess.run(["python", absolute_active_directory, *args], timeout=30, capture_output=True)

        if len(completed_process.stdout) == 0 and len(completed_process.stderr) == 0:
            return "No output produced"
        elif completed_process.returncode != 0:
            return f"STDOUT: {completed_process.stdout} STDERR: {completed_process.stderr} Process exited with code {completed_process.returncode}"
        return f"STDOUT: {completed_process.stdout} STDERR: {completed_process.stderr}"
        
    except Exception as e:
        return f"Error: executing Python file: {e}"
