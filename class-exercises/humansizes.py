SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

# Instead of the word `function`, in Python, you use `def`
def approximate_size(size, a_kilobyte_is_1024_bytes=True):

    '''Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000

    Returns: string

    '''
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')

# if __name__ == '__main__':
#     print(approximate_size(16384, False))
#     print(approximate_size(size=16384, a_kilobyte_is_1024_bytes=True))
#     print(approximate_size(-16384))



# Global Variables
# name = "Fred"
# def say_name():
#     global name
#     name = "Bubba"
#     print("internal", name)

# say_name()
# print("external", name)


# if/else
# name = "Joe"

# if name == "Steve" :
#     print("I feel great")
# elif name == "Joe":
#     print("You've got the better instructor")
# else:
#     print("I have a cold")


# String Concatenation
# print(f"My name is {name}")



# Collections
# List
# junk = ["Fred", True, [1,2,3], 234]
# junk.append("uh-oh")
# print("Junk", junk)
# junk.insert(3, False)
# print(junk)
# junk.extend(["Mary", "Joseph", "Bob"])
# print(junk)
# names = ["Mary", "Joseph", "Bob"]
# print(", ".join(names))


# Dictionaries
# my_pairs = {
#     123: "Number",
#     "name": "Broomhilda"
# }
# print(my_pairs[123], my_pairs["name"])
# my_pairs["test"] = "This is working"
# print(my_pairs["test"])
# my_pairs["address"] = {"number": 123,
# "street": "Sesame St"}
# print(my_pairs["address"]["street"])
# print(my_pairs.items())
# print(my_pairs.values())
# print(my_pairs.keyss())




# Sets
# my_stuff = {"Fred", True, 123, "Jones", "Fred"}
# my_list = ["Fred", True, 123, "Jones", "Fred"]

# print(my_stuff)
# print(set(my_list))
# print(list(set(my_list)))


# my_set = {1,2,3}
# my_set.add("feed me")
# print(my_set)


# tuple
# my_tup = (1,2,3,3,"hello")
# print(my_tup)
# print(my_tup[1])

# my_tup = ("hello", 1)
# print(my_tup)


# loops
# my_tup = (1,2,3,3,"hello")
# my_set = {1,2,3}
# junk = ["Fred", True, [1,2,3], 234]
# my_pairs = {
#     123: "Number",
#     "name": "Broomhilda"
# }
# for foo in junk: 
#     print(f"Why do I still have {foo} in this drawer?")
# for foo in my_set: 
#     print(f"Why do I still have {foo} in this drawer?")
# for foo in my_tup: 
#     print(f"Why do I still have {foo} in this drawer?")
# for foo in my_pairs: 
#     print(f"Why do I still have {my_pairs[foo]} in this drawer?")
# for foo in my_pairs.values(): 
#     print(f"Why do I still have {foo} in this drawer?")
# for foo in my_pairs.keys(): 
#     print(f"Why do I still have {foo} in this drawer?")


my_list = [1,2,4, "hello", "monkey"]
# my_subset = my_list[0:3]
# my_subset = my_list[1:3]
# my_subset = my_list[:3]
# my_subset = my_list[2:]
# my_subset = my_list[2:34]
my_subset = my_list[2:-1]
print(my_subset)

# tupple needs comma after to return true!!!!
my_little_tup = ("hello",)

my_little_tup1 = ("hello")

print(isinstance(my_little_tup, tuple))
print(isinstance(my_little_tup1, tuple))


# declares an empty set
my_hmm = set()



