from pprint import pprint

from .args import get_args 
from .openapifile import OpenAPIFile
from .ceresfile import CeresFile

def main():
    args = get_args()

    input_file = OpenAPIFile()
    input_file.load(args.input)
    output_producer = CeresFile(input_file, args.output_dir)
    output_producer.process()
    