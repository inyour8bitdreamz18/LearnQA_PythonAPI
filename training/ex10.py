#python -m pytest -s training/ex10.py

class TestNumberOfChars:
    def test_number_of_chars(self):
        phrase = input("Set a phrase: ")
        expected_result = 15

        assert len(phrase) < expected_result, f"The number of characters is more, than {expected_result}"

