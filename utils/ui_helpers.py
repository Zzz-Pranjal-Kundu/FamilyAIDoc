import base64
import os

def get_base64_of_bin_file(bin_file):
    if not os.path.exists(bin_file):
        return ""
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def get_asset_html(filename, class_name=""):
    filepath = os.path.join("assets", filename)
    base64_string = get_base64_of_bin_file(filepath)
    if not base64_string:
        return ""
    return f'<img src="data:image/png;base64,{base64_string}" class="{class_name}">'
