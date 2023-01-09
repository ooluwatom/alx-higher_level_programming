#!/usr/bin/python3
'''This function returns the dictionary description for\
     Json serialization of an object'''


def class_to_json(obj):
    def convert_to_serializable(obj):
        if isinstance(obj, (list, tuple)):
            return [convert_to_serializable(item) for item in obj]
        elif isinstance(obj, dict):
            return {key: convert_to_serializable(value) for key, value in obj.items()}
        elif isinstance(obj, (int, float, str, bool)):
            return obj
        else:
            raise TypeError("Object of type '%s' is not JSON serializable" % type(obj).__name__)

    return convert_to_serializable(obj)
