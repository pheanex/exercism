from itertools import cycle, chain


# Returns cycles like: 012321012321...
def fence_cycle(nr_rails):
    return cycle([x for x in range(nr_rails)]+[x for x in reversed(range(1, nr_rails-1))])


def encode(message, nr_rails):
    rails = {i: [] for i in range(nr_rails)}
    for letter, rail_number in zip(message, fence_cycle(nr_rails)):
        rails[rail_number].append(letter)
    return ''.join(chain.from_iterable(rails.values()))


def decode(message, nr_rails):
    letters_per_rail = {i: 0 for i in range(nr_rails)}
    for letter, rail_number in zip(message, fence_cycle(nr_rails)):
        letters_per_rail[rail_number] += 1
    rails = {i: [] for i in range(nr_rails)}
    for letter_count, rail_number in zip(letters_per_rail.values(), range(nr_rails)):
        rails[rail_number] = list(message[:letter_count])
        message = message[letter_count:]
    decoded_message = []
    for _, rail_number in zip(range(sum(letters_per_rail.values())), fence_cycle(nr_rails)):
        decoded_message.append(rails[rail_number].pop(0))
    return ''.join(decoded_message)
