import os


def save_files(file_metas, in_rel_path):
    file_name_list = []
    for meta in file_metas:
        file_name = meta['filename']
        file_path = os.path.join(in_rel_path, file_name)
        file_name_list.append(file_name)

        with open(file_path, 'wb') as file:
            file.write(meta['body'])
    return file_name_list
