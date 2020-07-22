from pypkgs import __version__
from pypkgs import pypkgs
import pandas as pd
from pytest import raises, fixture

@fixture()
def test_data():
    return {'a': pd.Categorical(["character", "hits", "your", "eyeballs"]),
            'b': pd.Categorical(["but", "integer", "where it", "counts"]),
            'c': ["but", "integer", "where it", "counts"]}

class Testpypkgs:
    def test_version(self):
        assert __version__ == '0.1.0'

    def test_catbind(self, test_data):
        assert ((pypkgs.catbind(test_data['a'], test_data['b'])).codes == 
                [1, 4, 7, 3, 0, 5, 6, 2]).all()
        assert ((pypkgs.catbind(test_data['a'], test_data['b'])).categories == 
                ["but", "character", "counts", "eyeballs", "hits", "integer", "where it", "your"]).all()

    def test_input_type(self, test_data):
        with raises(TypeError):
            pypkgs.catbind(test_data['a'], test_data['c'])