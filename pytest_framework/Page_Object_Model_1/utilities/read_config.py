from configparser import ConfigParser


def get_config(category,key):
    config=ConfigParser()
    config.read(r"E:\\py_selenium\\py_project\\pytest_framework\\Page_Object_Model_1\\configuration\\config.ini")
    return config.get(category,key)