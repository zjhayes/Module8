# Zachary Hayes


def switch_average(grade):
    switch = {
        'A': 90,
        'B': 80,
        'C': 70,
        'D': 60,
        'F': 50
    }
    return switch.get(grade.upper())

