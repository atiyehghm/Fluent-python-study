# ## the first takeaway is that iterable is the object that implements either of __iter__ or __getitem__
# ## Example 1
# from collections import abc

# class duck:
#     def __getitem__(self, i):
#         pass

# class goose:
#     def __iter__(self):
#         pass

# print(issubclass(duck, abc.Iterable))
# print(issubclass(goose, abc.Iterable))

# ## but still you can iterate both of them. --> duck typing

# ##Exmaple 2
# import random

# def pick_a_name():
#     names = ["Ali", "Atiyeh", "Hasssan", "Zahra", "Maryam", "Leila", "STOP"]
#     index  = random.randint(0, len(names)-1)
#     return names[index]


# names_iter = iter(pick_a_name, "STOP")
# print(names_iter)
# for name in names_iter:
#     print(name)

# ## Key takeaway here is the iter function which can get another callable and a sentinel and return an Iterator

# ## Example 3
# ## point:Once the iterator is exhausted, you should define a new one

# l = [1, 2, 3, 4, 5, 6, 7, 8]
# it = iter(l)
# for _ in range(len(l)-3):
#     print(next(it))

# print(list(it))
# ## output: [6, 7, 8]
# ## when we use list it we exhaust the iterator so then it gives the StopIteration and returns empty list.
# # print(next(it))
# # print(next(it))
# print(list(it))

# '''iterables have an __iter__ method that instantiates a new iterator every
# time. Iterators implement a __next__ method that returns individual items, and an
# __iter__ method that returns self.
# '''

# ## Example 4
# import re
# import reprlib

# class Sentence:
#     def __init__(self, text):
#         self.text = text
#         self.words = re.compile(r'\w+').findall(text)

#     def _repr__(self):
#         return 'Sentence(%s)'%reprlib.repr(self.text)
    
#     def __iter__(self):
#         for word in self.words:
#             yield word


# s1 = Sentence("Hello my name is Atiyeh from cartesian labs")
# it = iter(s1)
# print(iter(s1))
# ## output: <generator object Sentence.__iter__ at 0x79086db35cc0>
# print(list(it))
# ## This class is an iterable despite the fact that it doesn't return an iterator

# def foo():
#     yield "hello"
#     yield "world"
#     yield "atiyeh"


# print(next(foo()))
# print(next(foo()))

# # example of using next
# def foo():
#     for i in range(10):
#         yield i

# f = foo()
# for i in range(11):
#     print(next(f))

#output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# Traceback (most recent call last):
#   File "/home/atiyehghm/Desktop/Building-LLM_book/chapter17.py", line 94, in <module>
#     print(next(f))
#           ^^^^^^^
# StopIteration

