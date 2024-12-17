#!/bin/bash
# This script is used to set up the environment for the tests
# Author: Marcel Suter
mkdir -p /tmp/testdata
echo "
def test_one():
    assert True
def test_two(capsys):
    assert False
" > /tmp/testdata/test_first.py

echo "
def test_three():  # Test case 3
    assert True
class Tests:
    def test_four():  # Test case 4
        assert False
" > /tmp/testdata/test_second.py