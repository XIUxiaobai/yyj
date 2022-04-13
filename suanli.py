   
def init(params: dict):
    return None


def run(data: dict, func=None) -> bool:
    if data["objectPath"] == "abc.jpg":
        return True
    return False


def teardown():
    pass
