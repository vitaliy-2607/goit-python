import json
import pickle


class SerializationInterface:
    def __init__(self, value=None):
        self.value = value

    def serial_data(self, command, name_file, format_write):
        with open(name_file, format_write) as f:
            command.dump(self.value, f)


class JsonFormat(SerializationInterface):
    def __init__(self, value):
        super().__init__(value)

    def serial_data(self, *args, **kwargs):
        return super().serial_data(json, 'format.json', 'w')


class PickleFormat(SerializationInterface):
    def __init__(self, value):
        super().__init__(value)

    def serial_data(self, *args, **kwargs):
        return super().serial_data(pickle, 'format.pickle', 'wb')
