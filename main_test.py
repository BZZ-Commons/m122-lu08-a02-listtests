import pytest

from main import find_test_modules, find_test_functions, sanitize_function_name, output_json


def test_find_test_modules(testpath):
    """
    Test that the find_test_modules function returns the correct list of test modules.
    """
    modules = find_test_modules(testpath)
    assert modules == ['test_first.py', 'test_second.py']


def test_find_test_functions(testpath):
    """
    Test that the find_test_functions function returns the correct list of test functions.
    """
    functions = find_test_functions(path=testpath, file_name='test_first.py')
    assert functions == ['test_one', 'test_two']
    functions = find_test_functions(path=testpath, file_name='test_second.py')
    assert functions == ['test_three', 'test_four']


def test_sanitize_function_name():
    """
    Test that the sanitize_function_name function returns the correct function
    """
    assert sanitize_function_name('def test_one():') == 'test_one'
    assert sanitize_function_name('def test_two(capsys):') == 'test_two'
    assert sanitize_function_name('def test_three(): # Some text') == 'test_three'
    assert sanitize_function_name('    def test_four():') == 'test_four'


def test_output_json(capsys):
    """
    Test that the output_json function returns the correct JSON string.
    """
    output_json(['test_one', 'test_two', 'test_four'])
    captured = capsys.readouterr()
    assert captured.out == '[\n    "test_one",\n    "test_two",\n    "test_four"\n]\n'


@pytest.fixture
def testpath():
    """ Set the test path to the test data folder """
    return '/tmp/testdata'
