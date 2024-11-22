def set_geo_edit_output(file_path):

    edited_root_dir = 'I:/virtual_studio/clients'
    client = file_path.split('/')[2]
    project = file_path.split('/')[3]
    category = file_path.split('/')[4]
    sku = file_path.split('/')[6]

    path = f'{edited_root_dir}/{client}/{project}/{category}/edited/{sku}'
    return path