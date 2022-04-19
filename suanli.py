   
def init(params: dict):
    return None


def run(data: dict, func=None) -> bool:
   try:
        raise CustomError('异常')
    except CustomError as e:
        print(e)

def teardown():
    pass
