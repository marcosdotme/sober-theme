from contextlib import contextmanager

# Once upon a time...
simple_list = list()
simple_dict = dict()

(walrus := True)

x = 1 * 1

X_CONSTANT = ['Sunlight', 'Garlic']

class Vampire:
    def __init__(self, props):
        self.location = props['location']
        self.birthDate = props['birthDate']
        self.deathDate = props['deathDate']
        self.weaknesses = props['weaknesses']

    @contextmanager
    def get_age(self):
        return self.calc_age()

    def calc_age(self):
        return self.deathDate - self.birthDate

# ...there was a guy named Vlad

Dracula = Vampire({
    'location': 'Transylvania',
    'birthDate': 1428,
    'deathDate': 1476,
    'weaknesses': ['Sunlight', 'Garlic'],
    'is_dead': True
})

with Dracula.get_age():
    pass

try:
    print()
except:
    int()
else:
    bool()
finally:
    type()