class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value  # This will trigger the setter

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        import re
        # Split on . ? ! followed by space or end of string
        sentences = re.findall(r'\b[^.!?]+[.!?]', self._value)
        return len(sentences)
