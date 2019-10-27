import unittest
from openapi2ceres.args import get_args

class TestArgs(unittest.TestCase):
    def test_1(self):
        args= get_args(["-i", "www.yaml", "-o", "out/"])
        result = (args.input, args.output_dir)
        self.assertEquals(result, ("www.yaml", "out/"))
