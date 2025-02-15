from solution_3 import *
from freezegun import freeze_time


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

    def test_input_invalid_string(self, capsys, monkeypatch):
        unexpected_outputs = []
        cases = [
            {
                "inputs": ["abcd", "2013/10/13"],
                "expected-output": "Invalid date!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 2,
                "actual-input-count": 0,
            },
            {
                "inputs": ["foo/bar/baz", "2002/05/05"],
                "expected-output": "Invalid date!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 2,
                "actual-input-count": 0,
            },
            {
                "inputs": ["2013/10/baz", "2002/05/05"],
                "expected-output": "Invalid date!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 2,
                "actual-input-count": 0,
            },
            {
                "inputs": ["2013/bar/22", "2002/05/05"],
                "expected-output": "Invalid date!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 2,
                "actual-input-count": 0,
            },
            {
                "inputs": ["foo/10/22", "2002/05/05"],
                "expected-output": "Invalid date!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 2,
                "actual-input-count": 0,
            },
            {
                "inputs": ["foobar", "1999/05/12"],
                "expected-output": "Invalid date!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 2,
                "actual-input-count": 0,
            },
            {
                "inputs": ["baz/bum", "1975/10/03"],
                "expected-output": "Invalid date!",
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

                # check for expected input
                Tests.check_assertions(case, actual, prefix="Q3", exact_match=False)
            except Exception as e:
                assert (
                    False
                ), f"Q3 - Program should not crash when given invalid string inputs: {case['inputs']}, however it did: {e};"

    def test_input_invalid_date(self, capsys, monkeypatch):
        unexpected_outputs = []
        cases = [
            {
                "inputs": ["22013/10/13", "2013/10/13"],
                "expected-output": "Invalid date!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 2,
                "actual-input-count": 0,
            },
            {
                "inputs": ["02/05/05", "2002/05/05"],
                "expected-output": "Invalid date!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 2,
                "actual-input-count": 0,
            },
            {
                "inputs": ["2002/5/05", "2002/05/05"],
                "expected-output": "Invalid date!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 2,
                "actual-input-count": 0,
            },
            {
                "inputs": ["2002/05/5", "2002/05/05"],
                "expected-output": "Invalid date!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 2,
                "actual-input-count": 0,
            },
            {
                "inputs": ["99/5/12", "1999/05/12"],
                "expected-output": "Invalid date!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 2,
                "actual-input-count": 0,
            },
            {
                "inputs": ["99/05/12", "1999/05/12"],
                "expected-output": "Invalid date!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 2,
                "actual-input-count": 0,
            },
            {
                "inputs": ["5/10/03", "1975/10/03"],
                "expected-output": "Invalid date!",
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

                # check for expected input
                Tests.check_assertions(case, actual, prefix="Q3", exact_match=False)
            except Exception as e:
                assert (
                    False
                ), f"Q3 - Program should not crash when given invalid date inputs: {case['inputs']}, however it did: {e};"

    def test_input_invalid_loop(self, capsys, monkeypatch):
        unexpected_outputs = []
        cases = [
            {
                "inputs": ["22013/10/13", "22013/10/13", "2013/10/13"],
                "expected-output": "Invalid date!\n" * 2,
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 3,
                "actual-input-count": 0,
            },
            {
                "inputs": ["02/05/05", "02/05/05", "02/05/05", "2002/05/05"],
                "expected-output": "Invalid date!\n" * 3,
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 4,
                "actual-input-count": 0,
            },
            {
                "inputs": [
                    "2002/5/05",
                    "2002/5/05",
                    "2002/5/05",
                    "2002/5/05",
                    "2002/05/05",
                ],
                "expected-output": "Invalid date!\n" * 4,
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 5,
                "actual-input-count": 0,
            },
        ]

        for case in cases:
            Tests.mock_input(case, monkeypatch)  # mock the input function

            try:
                main()
                actual = capsys.readouterr().out
                actual = actual.strip()

                # check for expected input
                Tests.check_assertions(case, actual, prefix="Q3", exact_match=False)
            except Exception as e:
                assert (
                    False
                ), f"Q3 - Program should not crash when it should be asking user to re-enter response with inputs: {case['inputs']}, however it did: {e};"

    def test_correct_age_by_year(self, capsys, monkeypatch):
        """
        Validates only that the age calculation by year of birth is correct.  Months and days are ignored.
        """
        unexpected_outputs = ["Invalid date!"]
        cases = [
            {
                "mock-date": "2020/11/01",
                "inputs": ["2010/01/01"],
                "expected-output": "You are 10 years old!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "mock-date": "2033/11/01",
                "inputs": ["2002/01/01"],
                "expected-output": "You are 31 years old!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "mock-date": "2000/05/10",
                "inputs": ["1900/01/01"],
                "expected-output": "You are 100 years old!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
        ]

        for case in cases:
            Tests.mock_input(case, monkeypatch)  # mock the input function

            try:
                with freeze_time(case["mock-date"]) as frozen_time:
                    main()
                    actual = capsys.readouterr().out
                    actual = actual.strip()

                    # check for expected input
                    Tests.check_assertions(case, actual, prefix="Q3", exact_match=False)
            except Exception as e:
                assert (
                    False
                ), f"Q3 - Program should not crash when user enters valid input: {case['inputs']}, however it did: {e};"

    def test_correct_age(self, capsys, monkeypatch):
        unexpected_outputs = ["Invalid date!"]
        cases = [
            {
                "mock-date": "2020/11/01",
                "inputs": ["2010/12/13"],
                "expected-output": "You are 9 years old!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "mock-date": "2020/11/01",
                "inputs": ["2010/02/13"],
                "expected-output": "You are 10 years old!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "mock-date": "2020/11/01",
                "inputs": ["2009/02/13"],
                "expected-output": "You are 11 years old!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "mock-date": "2033/11/01",
                "inputs": ["2002/12/05"],
                "expected-output": "You are 30 years old!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "mock-date": "2033/11/01",
                "inputs": ["2002/05/05"],
                "expected-output": "You are 31 years old!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "mock-date": "2000/05/10",
                "inputs": ["1900/10/10"],
                "expected-output": "You are 99 years old!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
            {
                "mock-date": "2000/05/10",
                "inputs": ["1900/02/10"],
                "expected-output": "You are 100 years old!",
                "unexpected-outputs": unexpected_outputs,
                "expected-input-count": 1,
                "actual-input-count": 0,
            },
        ]

        for case in cases:
            Tests.mock_input(case, monkeypatch)  # mock the input function

            try:
                with freeze_time(case["mock-date"]) as frozen_time:
                    main()
                    actual = capsys.readouterr().out
                    actual = actual.strip()

                    # check for expected input
                    Tests.check_assertions(case, actual, prefix="Q3", exact_match=False)
            except Exception as e:
                assert (
                    False
                ), f"Q3 - Program should not crash when user enters valid input: {case['inputs']}, however it did: {e};"
