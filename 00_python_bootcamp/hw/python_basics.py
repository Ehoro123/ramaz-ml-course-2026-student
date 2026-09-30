"""HW00 — Python Bootcamp: Implementation

Complete the functions below. Each function has a docstring describing
what it should do, along with examples. Run `uv run pytest` to check
your work, and `uv run python score.py` to see your current grade.
"""

from __future__ import annotations

from typing import Callable

# ── Part 1: Lists ─────────────────────────────────────────────────────────────


def flatten(nested: list[list]) -> list:
    """Return a single flat list from a list of lists.

    Examples:
        >>> flatten([[1, 2], [3, 4], [5]])
        [1, 2, 3, 4, 5]
        >>> flatten([[], [1]])
        [1]
        >>> flatten([])
        []
    """
    # repeat through the list and then repeat thu the lists inside so oyu just append each thing to one list you defined before the for loops
    result = []

    for i in nested:
        for j in i:
            result.append(j)

    return result
    # raise NotImplementedError("Implement flatten()")

# print(flatten([[1, 2], [3, 4], [5]]))

def most_frequent(items: list) -> object:
    """Return the element that appears most often in items.

    If there is a tie, returning any one of the tied elements is fine.
    Raise ValueError if items is empty.

    Examples:
        >>> most_frequent([1, 2, 2, 3])
        2
        >>> most_frequent(['a', 'b', 'a', 'c', 'a'])
        'a'
    """
    if items == []:
        raise ValueError()
    highCount=0
    highElement={}
    for i in items:
        
        if items.count(i) >= highCount:
            highCount = items.count(i)
            highElement = i


    return  highElement
# print(most_frequent(['a', 'b', 'a', 'c','c']))  
    
    
    # raise NotImplementedError("Implement most_frequent()")
# print("hi")


def running_average(numbers: list[float]) -> list[float]:
    """Return the cumulative average at each position.

    The i-th element of the result is the mean of numbers[0], ..., numbers[i].

    Examples:
        >>> running_average([10.0, 20.0, 30.0])
        [10.0, 15.0, 20.0]
        >>> running_average([4.0])
        [4.0]
        >>> running_average([])
        []
    """
    lst=[]

    for i,v in enumerate(numbers): 
        
        # lst.append((numbers[0]+numbers[i])/2)
        lst.append(sum(numbers[:i+1])/(i+1))

    return lst
    # raise NotImplementedError("Implement running_average()")
# print(running_average([10.0, 20.0, 30.0, 50]))

def chunk(items: list, size: int) -> list[list]:
    """Split items into sublists of length size.

    The last sublist may be shorter if len(items) is not divisible by size.

    Examples:
        >>> chunk([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
        >>> chunk([1, 2, 3], 3)
        [[1, 2, 3]]
        >>> chunk([], 4)
        []
    """
    if items == []:
        return []
    # What i would do is, cases: perfect fit, overflow, and empty list 
    lst = []
    counter = 0
    # minilist = []
    for i in range(0, len(items), size):
        minilist = []
        minilist = [items[counter]]

        for j in range(size-1):
            index = j+1+counter
            if index < len(items):
                minilist.append(items[index])

        lst.append(minilist)
        counter += size
    return lst
# print(chunk([1, 2, 3, 4, 5], 2))

    # raise NotImplementedError("Implement chunk()")


def rotate(items: list, k: int) -> list:
    """Rotate items left by k positions.

    A negative k rotates right. If items is empty, return [].
    k larger than len(items) wraps around correctly.

    Examples:
        >>> rotate([1, 2, 3, 4, 5], 2)
        [3, 4, 5, 1, 2]
        >>> rotate([1, 2, 3], -1)
        [3, 1, 2]
        >>> rotate([1, 2, 3], 4)
        [2, 3, 1]
    """
    if items == []:
        return []

    split = k % len(items)
    newlist = items[split:]+items[:split]

    # items[2:] and items[:2]

    return newlist
    

    # raise NotImplementedError("Implement rotate()")


def run_length_encode(items: list) -> list[tuple]:
    """Compress consecutive identical elements into (count, value) tuples.
        Examples:
        >>> run_length_encode(['a', 'a', 'b', 'b', 'b', 'a'])
        [(2, 'a'), (3, 'b'), (1, 'a')]
        >>> run_length_encode([1, 2, 3])
        [(1, 1), (1, 2), (1, 3)]
        >>> run_length_encode([])
        []
    """
    
    i = 0
    result = []
    while i < len(items):
        find = items[i]
        count = 0
        
        while i < len(items) and items[i] == find:  
            i += 1
            count += 1
        
        result.append((count,find))
    
    return result

    # for i in items:
        # find = items[0]
        # while items[j] == find:
            # count = 
    # raise NotImplementedError("Implement run_length_encode()")


def sliding_window(items: list, size: int) -> list[list]:
    """Return all consecutive windows of length size.

    Each window overlaps with the previous one by size-1 elements.
    If len(items) < size, return [].

    Examples:
        >>> sliding_window([1, 2, 3, 4, 5], 3)
        [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        >>> sliding_window([1, 2, 3], 2)
        [[1, 2], [2, 3]]
        >>> sliding_window([1, 2], 3)
        []
        >>> sliding_window([], 2)
        []
    """ 
    # it's like a chunk 
    if len(items) < size: 
        return []

    result = []

    windows = len(items)-size+1

    for i in range(windows):
        result.append(items[i:size+i])

    return result
        

    
    # raise NotImplementedError("Implement sliding_window()")


# ── Part 2: Dictionaries ──────────────────────────────────────────────────────


def count_occurrences(items: list) -> dict:
    """Return a dict mapping each unique element to its count in items.

    Examples:
        >>> count_occurrences(['a', 'b', 'a', 'c', 'b', 'b'])
        {'a': 2, 'b': 3, 'c': 1}
        >>> count_occurrences([])
        {}
    """
    # from collections import Counter
    # result = dict(Counter(items))

    counts = {}
    for item in items:
        if item not in counts:
            counts[item] = 0
        counts[item] += 1
        
    return counts

    # raise NotImplementedError("Implement count_occurrences()")


def invert_dict(d: dict) -> dict:
    """Return a new dict with keys and values swapped.

    Examples:
        >>> invert_dict({'a': 1, 'b': 2})
        {1: 'a', 2: 'b'}
    """
    inverted = {}

    for key,value in d.items():
        inverted[value] = key
    return inverted
    # raise NotImplementedError("Implement invert_dict()")


def group_by(items: list[dict], key: str) -> dict[str, list[dict]]:
    """Group a list of dicts by the value at the given key.

    Examples:
        >>> records = [
        ...     {'name': 'Alice', 'dept': 'Eng'},
        ...     {'name': 'Bob', 'dept': 'HR'},
        ...     {'name': 'Carol', 'dept': 'Eng'},
        ... ]
        >>> result = group_by(records, 'dept')
        >>> len(result['Eng'])
        2
        >>> len(result['HR'])
        1
    """
        # >>> result = { "Eng" : [
        # ...     {'name': 'Alice', 'dept': 'Eng'},
        # ...     {'name': 'Carol', 'dept': 'Eng'},
        # ... ],
        #         "HR" : [
        #       {'name': 'Bob', 'dept': 'HR'},
        #             ]
        #         }
    

    result = {}

    for record in items:
        group_name = record[key]
        if group_name not in result:
            result[group_name] = []
        result[group_name].append(record)

    return result
    # raise NotImplementedError("Implement group_by()")
# records = [
#              {'name': 'Alice', 'dept': 'Eng'},
#              {'name': 'Bob', 'dept': 'HR'},
#              {'name': 'Carol', 'dept': 'Eng'},
#          ]
# result = group_by(records, 'dept')
# print(result)



def deep_get(d: dict, path: str, default: object = None) -> object: 
    #only in the case that object isn't entered as a paremter is it equal to none which is basically null
    """Retrieve a value from a nested dict using a dot-separated key path.

    Return default if any key along the path is missing.

    Examples:
        >>> deep_get({'a': {'b': {'c': 42}}}, 'a.b.c')
        42
        >>> deep_get({'a': 1}, 'a.b', default=-1)
        -1
        >>> deep_get({'x': 10}, 'y')  # returns None (default)
    """

    pathList = path.split(".")

    result = d
    for i in pathList:
        if not isinstance(result, dict) or i not in result:
            return default
        result = result[i]

    return result
    # raise NotImplementedError("Implement deep_get()")
# print(deep_get({'a': {'b': {'c': 42}}}, 'a.b.c'))

# deep_get({},"a.b")
# l = [1,2,3,4,5]
    # p = [x*x for x in l if x%2 == 0]
    # print(p)

def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    """Return indices (i, j) where nums[i] + nums[j] == target, with i < j.

    Return None if no such pair exists.

    Hint: There is an elegant O(n) solution using a dict. As you scan through
    nums, ask: "have I already seen the number I need to pair with this one?"

    Examples:
        >>> two_sum([2, 7, 11, 15], 9)
        (0, 1)
        >>> two_sum([3, 2, 4], 6)
        (1, 2)
        >>> two_sum([1, 2, 3], 100)
        None
    """
    nums_dict = {v:i for i,v in enumerate(nums)}

    for i,num in enumerate(nums):
        if target - num in nums_dict and num != target - num:
            return (i,nums_dict[target-num])

print(two_sum([3, 2, 4], 100))

    # solutions = {}
    # solutions[i] = target - i
    # j = solutions[i]

    # raise NotImplementedError("Implement two_sum()")


# ── Part 3: Sets ──────────────────────────────────────────────────────────────


def find_duplicates(items: list) -> set:
    """Return the set of elements that appear more than once in items.

    Examples:
        >>> find_duplicates([1, 2, 2, 3, 3, 3, 4])
        {2, 3}
        >>> find_duplicates([1, 2, 3])
        set()
        >>> find_duplicates([])
        set()
    """
    firsts = set()
    extras = set()
    for i in items:
        if i in firsts:
            extras.add(i)
        firsts.add(i)

    return extras

# print(find_duplicates([1, 2, 2, 3, 3, 3, 4, 4]))



    # raise NotImplementedError("Implement find_duplicates()")


def jaccard_similarity(a: set, b: set) -> float:
    """Return |A intersection B| / |A union B|.

    Return 0.0 if both sets are empty.

    Examples:
        >>> jaccard_similarity({1, 2, 3}, {2, 3, 4})
        0.5
        >>> jaccard_similarity({1, 2}, {3, 4})
        0.0
        >>> jaccard_similarity(set(), set())
        0.0
    """
    top = a.intersection(b)
    bottom = a.union(b)
    if len(a)+len(b) == 0:
        return 0.0
    return len(top)/len(bottom)
# print(jaccard_similarity(set(), set()))


    # raise NotImplementedError("Implement jaccard_similarity()")


# ── Part 4: Higher-order functions ────────────────────────────────────────────


def apply_twice(f: Callable, x: object) -> object:
    """Apply f to x, then apply f to the result: f(f(x)).

    Examples:
        >>> apply_twice(lambda n: n * 2, 3)
        12
        >>> apply_twice(str.upper, 'hello')
        'HELLO'
    """
    return f(f(x))

    # raise NotImplementedError("Implement apply_twice()")


def make_multiplier(n: float) -> Callable[[float], float]:
    """Return a function that multiplies its argument by n.

    Each call to make_multiplier returns an independent function.

    Examples:
        >>> double = make_multiplier(2)
        >>> double(5)
        10.0
        >>> triple = make_multiplier(3)
        >>> triple(4)
        12.0
    """
    factor = n

    def mult(n):
        return factor*n
    
    # return lambda n:k*n interesting one liner function
    return mult
    
    # raise NotImplementedError("Implement make_multiplier()")


def pipeline(*funcs: Callable) -> Callable:
    """Return a single function that applies each func in sequence (left to right).

    pipeline(f, g, h)(x) is equivalent to h(g(f(x))).
    If no functions are provided, the returned function is the identity: f(x) == x.
    Examples:
        >>> add1 = lambda x: x + 1
        >>> double = lambda x: x * 2
        >>> pipeline(add1, double)(3)
        8
        >>> pipeline()(42)
        42
    """
    
    def pipe(x):
        for func in funcs:
            x = func(x)
        return x

    return pipe

# add1 = lambda x: x + 1
# double = lambda x: x * 2
# p=pipeline(add1, double)
# print(p(3))
# print(p(4))

    # funcs[1](funcs[0](x))
    # raise NotImplementedError("Implement pipeline()")


def memoize(f: Callable) -> Callable:
    """Return a version of f that caches results by argument.

    Calling the memoized function with the same argument a second time
    must return the cached result WITHOUT calling f again.

    Use a closure over a dict to store previously computed results.

    Examples:
        >>> call_count = 0
        >>> def tracked(x):
        ...     global call_count
        ...     call_count += 1
        ...     return x ** 2
        >>> cached = memoize(tracked)
        >>> cached(4)
        16
        >>> cached(4)   # should not increment call_count
        16
    """
    cache = {}

    def mem(x):
        if x not in cache:
            cache[x] = f(x)

        return cache[x]

    return mem
    # raise NotImplementedError("Implement memoize()")



# def logger(f: Callable) -> Callable:
#     def logged(x):
#         print(f"Logging the calculation of {f}")
#         result = f(x)
#         print(f"Result it {result}")
#         return result
     
#     return logged


# from functools import lru_cache



# #@logger
# def long_function(x):
#     # print(f"calculating for {x}..")
#     time.sleep(1)
#     # print(f"done calculating for {x}.")
#     return 3*x


# #long_function = memoize(long_function)

# print(long_function(3))
# print(long_function(4))
# print(long_function(3)) 


# ── Part 5: Classes ───────────────────────────────────────────────────────────


class Student:
    """A student with a name and a list of grades (0-100).

    Supports comparison via average grade, enabling natural sorting.
    """

    def __init__(self, name: str, grades: list[float]) -> None:
        self.name = name
        self.grades = grades

    def average(self) -> float:
        """Return the mean of all grades. Returns 0.0 if grades is empty."""
        if len(self.grades) == 0:
            return 0.0
        average = sum(self.grades)/len(self.grades)
        return average
        # raise NotImplementedError("Implement Student.average()")

    def highest(self) -> float:
        """Return the highest grade. Returns 0.0 if grades is empty."""
        # for i in self.grades:
        #     max = i
        if len(self.grades) == 0:
                    return 0.0
        return max(self.grades)
        # raise NotImplementedError("Implement Student.highest()")

    def letter_grade(self) -> str:
        """Return the letter grade for this student's average.
        Boundaries: A >= 90, B >= 80, C >= 70, D >= 60, F otherwise.
        """
        mean = self.average()
        if mean >= 90:
            letter = "A"
        elif mean >= 80:
            letter = "B"
        elif mean >= 70:
            letter = "C"
        elif mean >= 60:
            letter = "D"
        else:
            letter = "F"

        return letter
        # raise NotImplementedError("Implement Student.letter_grade()"

    def __repr__(self) -> str:
        """Return a string like: Student('Alice', avg=88.5)"""
        return f"Student('{self.name}', avg={self.average()})"
        # raise NotImplementedError("Implement Student.__repr__()")

    def __lt__(self, other: "Student") -> bool:
        """Compare students by average grade (enables sorted() and min/max)."""
        return self.average() < other.average()
        # raise NotImplementedError("Implement Student.__lt__()") why does the min and max depend on this?

# a = Student("dumbo", [1,2,34,4,4])
# b = Student("smarty", [99,80,90,88])
# print(a)
# print(b)
# print(min(a,b))
# print(max(a,b))

class Gradebook:
    """Manages a collection of students, keyed by name."""

    def __init__(self) -> None:
        self.students: dict[str, Student] = {}

    def add_student(self, student: Student) -> None:
        """Add a student to the gradebook.
        Raises ValueError if a student with the same name already exists.
        """
        if student.name in self.students:
            raise ValueError(f"{student.name} already in book")
        self.students[student.name] = student

        # raise NotImplementedError("Implement Gradebook.add_student()")

    def top_students(self, n: int) -> list[Student]:
        """Return the n students with the highest averages, in descending order."""
        sorted_students = sorted(self.students.values(), reverse=True)

        return sorted_students[:n]
        # self.student.values()
        # raise NotImplementedError("Implement Gradebook.top_students()")

    def class_average(self) -> float:
        """Return the mean of all student averages. Returns 0.0 if empty."""
        # comprehension = [x for x in list]
        if len(self.students) == 0:
            return 0.0
        averages_list = [student.average() for student in self.students.values()]
        return sum(averages_list)/len(averages_list)
        # raise NotImplementedError("Implement Gradebook.class_average()")

