import random


def fake_heartbeat():
    return [random.randint(60, 100) for _ in range(60)]


def fake_blood_oxygen():
    return [random.randint(80, 100) for _ in range(60)]


def fake_sleep():
    return [random.randint(5, 9) for _ in range(30)]


def fake_average_sleep_interruptions():
    return [random.randint(0, 3) for _ in range(30)]
