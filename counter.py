import shelve

filename = 'counter.shelve'


def read_counter():
    with shelve.open(filename) as db:
        return db.get('counter', 1)


def write_counter(count):
    with shelve.open(filename) as db:
        db['counter'] = count


def increment_counter():
    count = read_counter() + 1
    write_counter(count)
    return count
#
# print(read_counter())
#
# increment_counter()

