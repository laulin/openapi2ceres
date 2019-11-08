import os
import os.path as path
from pprint import pprint

import yaml

class CeresFile:
    def __init__(self, openapi_file, output_dir):
        self._openapi_file = openapi_file
        self._output_dir = path.abspath(output_dir)

    def _path_sanitize(self, entity):
        # from a path like foo/bar/, create foo_bar
        path_splitted = entity["path"].split("/")
        path_splitted = tuple(filter(lambda x: x, path_splitted))
        return "_".join(path_splitted)

    def _create_name(self, entity):
        # return name like get.foo_bar
        path_sanitized = self._path_sanitize(entity).lower()
        return f"{path_sanitized}"

    def _create_filename(self, entity):
        # return filename like get.foo_bar.yml
        return self._create_name(entity) + ".yml"

    def process(self):

        global_vars = self._openapi_file.get_globals()

        for entity in self._openapi_file.get_entities():
            filename = self._create_filename(entity)
            #pprint(entity)

            full_path = path.join(self._output_dir, filename)
            print("Create file "+full_path)
            with open(full_path, "w") as f:
                tmp = dict()
                tmp["entity"] = entity
                tmp["globals"] = global_vars
                tmp["name"] = self._create_name(entity)
                raw_data = yaml.dump(tmp)
                f.write(raw_data)
            
