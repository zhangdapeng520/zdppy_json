import orjson
import json


def loads(json_str: str):
    """
    将json字符串加载为python对象
    :return:
    """
    return orjson.loads(json_str)


def dumps(py_obj):
    """
    将python对象转换为json字符串
    :param py_obj:
    :return:
    """
    return orjson.dumps(py_obj,
                        option=orjson.OPT_PASSTHROUGH_DATACLASS | orjson.OPT_OMIT_MICROSECONDS | orjson.OPT_NON_STR_KEYS | orjson.OPT_APPEND_NEWLINE | orjson.OPT_INDENT_2 | orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY
                        ).decode("utf8")


def load(file_name: str):
    """
    加载文件数据
    :param file_name:
    :return:
    """
    data = None
    with open(file_name, "r", encoding="UTF-8") as f:
        data = json.load(f)
    return data


def dump(file_name: str, data):
    """
    写入文件数据
    :param file_name:
    :return:
    """
    with open(file_name, "w+", encoding="UTF-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


class Json:
    def __init__(self):
        self.__data = None

    def set(self, data):
        self.__data = data

    def get_key_list(self, key, child_keys):
        """
        获取指定key下多个子key的数据
        :param key:
        :param child_keys:
        :return:
        """
        data = self.__data.get(key)
        result = {}
        for k in child_keys:
            result[k] = data.get(k)
        return result

    def get_all_child_keys(self, keys):
        """
        根据子键获取所有数据
        :param keys:
        :return:
        """
        result = {}
        for k in self.__data.keys:
            temp = self.__data.get(k)
            temp_result = []
        pass
