def is_number(word):
    try:
        float(word)
        return True
    except ValueError:
        return False


def calculate(text):
    ops = dict(plus='+', minus='-', multiplied='*', divided='/')
    task = [ops[w] if w in ops else w for w in text.rstrip('?').split() if is_number(w) or w in ops]
    while len(task) != 1:
        if not is_number(task[0]) or task[1] not in ops.values() or not is_number(task[2]):
            raise ValueError
        result = eval(''.join(task[0:3]))
        task = task[3:]
        task.insert(0, str(result))
    return int(float(task[0]))
