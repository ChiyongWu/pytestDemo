import yaml, os
from pathlib import Path
from config.ConfigHandler import ConfigHandler


absolute_path = Path().resolve()

# 定义一个类，用于存储YAML中的数据
class DataObject:
    pass

# 定义一个函数，用于递归地将YAML映射为对象
def yaml_to_object(data, obj):
    for key, value in data.items():
        if isinstance(value, dict):
            # 如果值是字典类型，则创建新的对象并递归调用此函数
            new_obj = DataObject()
            setattr(obj, key, new_obj)
            yaml_to_object(value, new_obj)
        else:
            # 如果值不是字典类型，则将其映射到对象属性中
            setattr(obj, key, value)


with open(ConfigHandler.setting_path, 'rb') as f:
    data = yaml.safe_load(f)

# 使用递归函数将YAML映射为对象
config_processor = DataObject()
yaml_to_object(data, config_processor)

