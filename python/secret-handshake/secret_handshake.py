event = {0b1: "wink",
         0b10: "double blink",
         0b100: "close your eyes",
         0b1000: "jump"}
reverse = 0b10000
binary = {v: k for k, v in event.items()}


def handshake(number):
    if isinstance(number, str):
        try:
            number = int(number, 2)
        except ValueError:
            return []
    if number < 0:
        return []

    events = [e for c, e in sorted(event.items()) if number & c]

    if number & reverse:
        events = list(reversed(events))

    return events


def code(events):
    if not set(events).issubset(event.values()):
        return '0'

    number = 0
    for c, e in event.items():
        if e in events:
            number |= c

    if len(events) > 1 and binary[events[0]] > binary[events[1]]:
        number |= reverse

    return '{:0b}'.format(number)
