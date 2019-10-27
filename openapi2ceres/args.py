import argparse
parser = argparse.ArgumentParser(description='This tool converts openapi yaml file to ceres files')
parser.add_argument("-i", '--input', dest='input', help='Set the openapi file path')
parser.add_argument("-o", '--output', dest='output_dir', help='Set the output directory for ceres entity files')

def get_args(args_list=None):
    return parser.parse_args(args_list)
