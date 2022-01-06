from datetime import datetime


def report(msg: str):
    _time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    print(f"Test")
    print(f"{_time}: {msg}")
