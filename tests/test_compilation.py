import unittest

from dbt.compilation import Compiler
from tests import fake_data

class CompilationTest(unittest.TestCase):

    def setUp(self):
        self.compiler = fake_data.new_base_compiler()

    def test_idk(self):
        projects = list(self.compiler.dependency_projects())
