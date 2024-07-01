from solution_1 import *


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
            assert expected.lower().split(r"\s") == actual.lower().split(
                r"\s"
            ), f"{prefix} - Expected output to be '{expected}' when given inputs: {case['inputs']}; instead, it was '{actual}'."
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

    def test_first_input_invalid(self, capsys, monkeypatch):
        """
        Test that the program correctly handles invalid input for the first input
        """
        unexpected_outputs = [
            "Too small",
            "+",
            "=",
        ]  # these should not be in the output
        cases = [
            {
                "inputs": ["abcd"],
                "expected-output": "Invalid number!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "inputs": ["3.2"],
                "expected-output": "Invalid number!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "inputs": ["-10.2"],
                "expected-output": "Invalid number!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "inputs": ["-2"],
                "expected-output": "Invalid number!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "inputs": ["-2"],
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
                Tests.check_assertions(case, actual, prefix="Q1")
            except Exception as e:
                assert (
                    False
                ), f"Q1 - Program should not crash when given invalid first input: {case['inputs']}, however it did: {e};"

    def test_second_input_invalid(self, capsys, monkeypatch):
        unexpected_outputs = ["Too small", "+", "="]
        cases = [
            {
                "inputs": ["20", "abcd"],
                "expected-output": "Invalid number!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 2,
                "actual-input-count": 0,
            },
            {
                "inputs": ["18", "3.2"],
                "expected-output": "Invalid number!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 2,
                "actual-input-count": 0,
            },
            {
                "inputs": ["155", "-10.2"],
                "expected-output": "Invalid number!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 2,
                "actual-input-count": 0,
            },
            {
                "inputs": ["16", "-2"],
                "expected-output": "Invalid number!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 2,
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
                Tests.check_assertions(case, actual, prefix="Q1")
            except Exception as e:
                assert (
                    False
                ), f"Q1 - Program should not crash when given invalid second input: {case['inputs']}, however it did: {e};"

    def test_first_input_too_small(self, capsys, monkeypatch):
        unexpected_outputs = ["Invalid input", "+", "="]
        cases = [
            {
                "inputs": ["5"],
                "expected-output": "Too small!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "inputs": ["9"],
                "expected-output": "Too small!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "inputs": ["1"],
                "expected-output": "Too small!",
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
                Tests.check_assertions(case, actual, prefix="Q1")
            except Exception as e:
                assert (
                    False
                ), f"Q1 - Program should not crash when given too small first input: {case['inputs']}, however it did: {e};"

    def test_second_input_too_small(self, capsys, monkeypatch):
        unexpected_outputs = ["Invalid input", "+", "="]
        cases = [
            {
                "inputs": ["20", "5"],
                "expected-output": "Too small!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 2,
                "actual-input-count": 0,
            },
            {
                "inputs": ["155", "9"],
                "expected-output": "Too small!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 2,
                "actual-input-count": 0,
            },
            {
                "inputs": ["2023", "1"],
                "expected-output": "Too small!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 2,
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
                Tests.check_assertions(case, actual, prefix="Q1")
            except Exception as e:
                assert (
                    False
                ), f"Q1 - Program should not crash when given too small second input: {case['inputs']}, however it did: {e};"

    def test_main_correct(self, capsys, monkeypatch):
        unexpected_outputs = ["Invalid input", "Too small"]
        cases = [
            {
                "inputs": ["10", "10"],
                "expected-output": "10 + 10 = 20",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 2,
                "actual-input-count": 0,
            },
            {
                "inputs": ["15", "1000"],
                "expected-output": "15 + 1000 = 1015",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 2,
                "actual-input-count": 0,
            },
            {
                "inputs": ["101", "10"],
                "expected-output": "101 + 10 = 111",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 2,
                "actual-input-count": 0,
            },
            {
                "inputs": ["12", "1120"],
                "expected-output": "12 + 1120 = 1132",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 2,
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
                Tests.check_assertions(case, actual, prefix="Q1")
            except Exception as e:
                assert (
                    False
                ), f"Q1 - Program should not crash when given correct inputs: {case['inputs']}, however it did: {e};"
