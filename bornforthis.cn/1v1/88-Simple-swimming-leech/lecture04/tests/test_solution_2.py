import re

from solution_2 import *


class Tests:
    @classmethod
    def mock_input(cls, mock_data, monkeypatch):
        """
        Mock the builtin input function
        :param mock_data: Dictionary of data to mock.
        :param call_counter: Dictionary of counters for function calls
        :param monkeypatch: pytest's monkeypatch object
        """
        # make a duplicate of the inputs, so we retain the originals
        mock_data["inputs-copy"] = mock_data["inputs"].copy()

        # mock the input function
        def new_input(message):
            mock_data["actual-input-count"] += 1
            return mock_data["inputs-copy"].pop(0)

        monkeypatch.setattr("builtins.input", lambda x: new_input(x))

    @classmethod
    def check_assertions(
        cls, case, actual, ignore_spaces=False, exact_match=True, prefix=""
    ):
        """
        Run standard assertions on the test case and its results.
        :param case: The test case, as a dictionary
        :param actual: The actual output
        :param ignore_spaces: Whether to ignore spaces when comparing the expected and actual output
        :param prefix: A prefix to add to the error message
        """
        # check for expected input count
        expected = case["expected-output"].strip()
        expected_input_count = case["expected-input-count"]
        actual_input_count = case["actual-input-count"]
        unexpected_outputs = case["unexpected-outputs"]
        # do the assertions
        assert (
            actual_input_count == expected_input_count
        ), f"{prefix} - Expected {expected_input_count} inputs requested when given inputs: {case['inputs']}, instead {case['actual-input-count']} inputs were requested;"
        # check for expected output
        if ignore_spaces:
            # exact match, ignoring spaces
            assert re.split(r"\s+", expected.lower().strip()) == re.split(
                r"\s+", actual.lower().strip()
            ), f"{prefix} - Expected output to be '{expected}' when given inputs: {case['inputs']}; instead, it was '{actual}'."
            # assert expected.lower().split(r'\s') == actual.lower().split(r'\s'), f"{prefix} - Expected output to be '{expected}' when given inputs: {case['inputs']}; instead, it was '{actual}'."

        elif exact_match:
            # exact match
            assert (
                expected.lower() == actual.lower()
            ), f"{prefix} - Expected output to be '{expected}' when given inputs: {case['inputs']}, instead, it was '{actual}';"
        else:
            # not exact match
            assert (
                expected.lower() in actual.lower()
            ), f"{prefix} - Expected output to contain '{expected}' when given inputs: {case['inputs']}, instead, it was '{actual}';"
        # check for unexpected output
        for unexpected in unexpected_outputs:
            assert (
                unexpected.lower() not in actual.lower()
            ), f"{prefix} - Did not expect '{unexpected}' in output when given inputs: {case['inputs']}, but it was present;"

    def test_input_invalid_string(self, capsys, monkeypatch):
        unexpected_outputs = ["Too small", "Phew", "Hello world"]
        cases = [
            {
                "inputs": ["abcd"],
                "expected-output": "Invalid number!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "inputs": ["abcd"],
                "expected-output": "Invalid number!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "inputs": ["abcd"],
                "expected-output": "Invalid number!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "inputs": ["20abcd"],
                "expected-output": "Invalid number!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
        ]

        for case in cases:
            Tests.mock_input(case, monkeypatch)  # mock the input function

            try:
                main()
                actual = capsys.readouterr().out
                actual = actual.strip()

                # check for expected input count
                Tests.check_assertions(case, actual, prefix="Q2")
            except Exception as e:
                assert (
                    False
                ), f"Q2 - Program should not crash when given invalid alphabetic string input: {case['inputs']}, however it did: {e};"

    def test_input_invalid_negative(self, capsys, monkeypatch):
        unexpected_outputs = ["Too small", "Phew", "Hello world"]
        cases = [
            {
                "inputs": ["-2"],
                "expected-output": "Invalid number!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "inputs": ["-2", "200"],
                "expected-output": "Invalid number!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "inputs": ["-12.2"],
                "expected-output": "Invalid number!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
        ]

        for case in cases:
            Tests.mock_input(case, monkeypatch)  # mock the input function

            try:
                main()
                actual = capsys.readouterr().out
                actual = actual.strip()

                # check for expected input count
                Tests.check_assertions(case, actual, prefix="Q2")
            except Exception as e:
                assert (
                    False
                ), f"Q2 - Program should not crash when given invalid negative numeric inputs: {case['inputs']}, however it did: {e};"

    def test_input_invalid_numeric(self, capsys, monkeypatch):
        unexpected_outputs = ["Too small", "Phew", "Hello world"]
        cases = [
            {
                "inputs": ["2.2"],
                "expected-output": "Invalid number!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "inputs": ["0"],
                "expected-output": "Invalid number!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "inputs": ["21"],
                "expected-output": "Invalid number!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "inputs": ["621"],
                "expected-output": "Invalid number!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "inputs": ["621", "20"],
                "expected-output": "Invalid number!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
        ]

        for case in cases:
            Tests.mock_input(case, monkeypatch)  # mock the input function

            try:
                main()
                actual = capsys.readouterr().out
                actual = actual.strip()

                # check for expected input count
                Tests.check_assertions(case, actual, prefix="Q2")
            except Exception as e:
                assert (
                    False
                ), f"Q2 - Program should not crash when given invalid numeric inputs: {case['inputs']}, however it did: {e};"

    def test_low_hello_count(self, capsys, monkeypatch):
        unexpected_outputs = ["Too small", "Phew"]
        cases = [
            {
                "inputs": ["1"],
                "expected-output": "Hello world!\n",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "inputs": ["2"],
                "expected-output": "Hello world!\nHello world!\n",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "inputs": ["5"],
                "expected-output": "Hello world!\nHello world!\nHello world!\nHello world!\nHello world!\n",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "inputs": ["1", "10"],
                "expected-output": "Hello world!\n",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "inputs": ["4", "1"],
                "expected-output": "Hello world!\nHello world!\nHello world!\nHello world!\n",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
        ]

        for case in cases:
            Tests.mock_input(case, monkeypatch)  # mock the input function

            try:
                main()
                actual = capsys.readouterr().out
                actual = actual.strip()

                # check for expected input count
                Tests.check_assertions(case, actual, prefix="Q2")
            except Exception as e:
                assert (
                    False
                ), f"Q2 - Program should not crash when given valid inputs: {case['inputs']}, however it did: {e};"

    def test_high_hello_count(self, capsys, monkeypatch):
        unexpected_outputs = ["Too small"]
        cases = [
            {
                "inputs": ["6"],
                "expected-output": "Hello world!\n" * 6 + "Phew!\n",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "inputs": ["16"],
                "expected-output": "Hello world!\n" * 16 + "Phew!\n",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "inputs": ["20"],
                "expected-output": "Hello world!\n" * 20 + "Phew!\n",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "inputs": ["6", "10"],
                "expected-output": "Hello world!\n" * 6 + "Phew!\n",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "inputs": ["16", "1"],
                "expected-output": "Hello world!\n" * 16 + "Phew!\n",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
        ]

        for case in cases:
            Tests.mock_input(case, monkeypatch)  # mock the input function

            try:
                main()
                actual = capsys.readouterr().out
                actual = actual.strip()

                # check for expected input count
                Tests.check_assertions(case, actual, prefix="Q2", ignore_spaces=True)
            except Exception as e:
                assert (
                    False
                ), f"Q2 - Program should not crash when given valid large inputs: {case['inputs']}, however it did: {e};"
