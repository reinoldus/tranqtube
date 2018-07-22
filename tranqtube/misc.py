import base64


def string_to_base64(string: str):
    return base64.b64encode(string.encode())