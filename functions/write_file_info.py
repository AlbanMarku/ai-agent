import os

def write_file(working_dir, file_path, content):
    if not file_path.endswith('.txt'):
        file_path += '.txt'
    working_dir_abs = os.path.abspath(working_dir)
    full_path_abs = os.path.abspath(os.path.join(working_dir, file_path))
    if not full_path_abs.startswith(working_dir_abs):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        with open(full_path_abs, "w") as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {str(e)}"