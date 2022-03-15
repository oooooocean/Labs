import os
from common.commons import save_files
import conf


def save_images(image_metas) -> [str]:
    """
    保存图片到本地
    :param image_metas: 图片元数据
    :return: 图片的完整link
    """
    cwd = os.getcwd()
    save_image_path = os.path.join(cwd, 'static/upload/')
    file_name_list = save_files(image_metas, save_image_path)
    return [conf.base.SERVER_HOST + '/static/upload/' + i for i in file_name_list]


def camel_case(string: str) -> str:
    """
    转驼峰
    abc_def -> Abc Def -> AbcDef -> abcDef
    """
    from re import sub
    string = sub(r'(_|-)+', ' ', string).title().replace(' ', '')
    return string[0].lower() + string[1:]
