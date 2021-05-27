# Programowanie I R
# Programowanie obiektowe: serializacja

import pickle

class example_class:
    a_number = 35
    a_string = "hey"
    a_list = [1, 2, 3]
    a_dict = {"first": "a", "second": 2, "third": [1, 2, 3]}
    a_tuple = (22, 23)

my_object = example_class()

my_pickled_object = pickle.dumps(my_object)
print(f"This is my pickled object:\n{my_pickled_object}\n")

my_object.a_dict = None

my_unpickled_object = pickle.loads(my_pickled_object)
print(
    f"This is a_dict of the unpickled object:\n{my_unpickled_object.a_dict}\n")

# **********************************************************************************

""" BŁĄD:
square = lambda x : x * x
my_pickle = pickle.dumps(square)
"""

import dill   # Wymaga instalacji: pip install dill

square = lambda x: x * x
my_pickle = dill.dumps(square)
print(my_pickle)


class foobar:
    def __init__(self):
        self.a = 35
        self.b = "test"
        self.c = lambda x: x * x

    def __getstate__(self):
        attributes = self.__dict__.copy()
        del attributes['c']
        return attributes

    def __setstate__(self, state):
        self.__dict__ = state
        self.c = lambda x: x * x

my_foobar_instance = foobar()
my_pickle_string = pickle.dumps(my_foobar_instance)
my_new_instance = pickle.loads(my_pickle_string)