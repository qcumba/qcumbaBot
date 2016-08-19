import yaml


def get_setting_value(setting_name):
    """
    Get the value of the required setting
    """
    with open('config.yml', 'r') as yml_file:
        cfg = yaml.load(yml_file)

    return cfg[setting_name]
