import yaml

class OpenAPIFile:

    def __init__(self):
        self._data = dict()

    def load(self, filename):
        # load the api file
        with open(filename) as f:
            raw_data = f.read()
            self._data = yaml.load(raw_data, Loader=yaml.FullLoader)

    def get_globals(self):
        # return all global variables

        output = dict()
        output["info"] = self._data["info"]
        output["host"] = self._data["host"]
        output["basePath"] = self._data["basePath"]
        output["schemes"] = self._data["schemes"]
        output["tags"] = self._data["tags"]
        return output

    def get_entities(self):
        # return a list of all paths
        # and flat them with method and data
        output = list()
        for path, methods in self._data["paths"].items():
            tmp = dict()
            tmp["path"] = path
            tmp["methods"] = []
            for method, data in methods.items():
                tmp["methods"].append(method)
                tmp[method] = dict()
                tmp[method].update(data)
                output.append(tmp)

        return output
    
