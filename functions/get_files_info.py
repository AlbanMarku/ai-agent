import os

def get_files_info(working_dir, dir="."):
    # Ensure both paths are absolute
    working_dir_abs = os.path.abspath(working_dir)
    full_path_abs = os.path.abspath(os.path.join(working_dir, dir))
    if not full_path_abs.startswith(working_dir_abs):
        return f'Error: Cannot list "{dir}" as it is outside the permitted working directory'

    if not os.path.isdir(full_path_abs):
        return f'Error: {dir} is not a directory'
    try:
        # get list of files and directories
        items = os.listdir(full_path_abs)
        # for each item, get name, size, is_dir
        items_info = []
        for item in items:
            item_path = os.path.join(full_path_abs, item)
            item_info = {
                "name": item,
                "size": os.path.getsize(item_path),
                "is_dir": os.path.isdir(item_path)
            }
            items_info.append(item_info)
    
        # parse list into string
        items_info_str = " - " + "\n - ".join([f"{item['name']}: file_size={item['size']} bytes, {'is_dir=True' if item['is_dir'] else 'is_dir=False'}" for item in items_info])
        return items_info_str
    except Exception as e:
        return f"Error: {str(e)}"
    
def get_file_content(working_dir, file_path):
    working_dir_abs = os.path.abspath(working_dir)
    full_path_abs = os.path.abspath(os.path.join(working_dir, file_path))
    if not full_path_abs.startswith(working_dir_abs):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path_abs):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    MAX_CHARS = 10000
    try:
        with open(full_path_abs, "r") as file:
            file_string = file.read(MAX_CHARS + 1)
            if len(file_string) > MAX_CHARS:
                file_string = file_string[:MAX_CHARS] + f' [...File "{file_path}" truncated at 10000 characters]'
        return file_string
    except Exception as e:
        return f"Error: {str(e)}"
