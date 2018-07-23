import json
from bunch import Bunch
import os
import argparse

def get_config_from_json(json_file):

    with open(json_file, 'r') as config_file:
        config_dict = json.load(config_file)

    config = Bunch(config_dict)

    return config, config_dict

def process_config(json_file):
    config_file, _ = get_config_from_json(json_file)
    config.summary_dir = os.path.join("../experiments", config.exp_name, "summary/")
    config.checkpoint_dir = os.path.join("../experiments", config.exp_name, "checkpoint/")

    return config

def get_args():
    argparser = argparse.ArgumentParser(description=__doc__)
    argparser.add_argument('-c', '--config', metavar='C', default='None', help='specify the configuration file (JSON file)')

    args = argparser.parse_args()

    return args

def create_dir(dirs):

    try:
        for dir_ in dirs:
            if not os.path.exist(dir_):
                os.makedir(dir_)
        return 0
    except Exception as err:
        print("Creating directories error :{0}".format(err))
        exit(-1)

