import List_Queue
import List_Stack
import Queue
import Stack
import cProfile
import numpy as np


def verify_datatypes():
    queue = Queue.Queue()
    for i in range(10):
        queue.enqueue(i)
    print("Linked List Queue")
    print(queue)
    for i in range(5):
        print(queue.dequeue())

    stack = Stack.Stack()
    for i in range(10):
        stack.push(i)
    print("Linked List Stack")
    print(stack)
    for i in range(5):
        print(stack.pop())

    list_queue = List_Queue.Queue()
    for i in range(10):
        list_queue.enqueue(i)
    print("Python List Queue")
    print(list_queue)
    for i in range(5):
        print(list_queue.dequeue())

    list_stack = List_Stack.Stack()
    for i in range(10):
        list_stack.push(i)
    print("Python List Stack")
    print(list_stack)
    for i in range(5):
        print(list_stack.pop())


def test_queue():
    numbers = np.random.randint(0, 1000, 100000)
    queue = Queue.Queue()
    for i in range(len(numbers)):
        queue.enqueue(numbers[i])
    for i in range(len(numbers)):
        queue.dequeue()


def test_stack():
    numbers = np.random.randint(0, 1000, 100000)
    stack = Stack.Stack()
    for i in range(len(numbers)):
        stack.push(i)
    for i in range(len(numbers)):
        stack.pop()


def test_list_queue():
    numbers = np.random.randint(0, 1000, 100000)
    list_queue = List_Queue.Queue()
    for i in range(len(numbers)):
        list_queue.enqueue(numbers[i])
    for i in range(len(numbers)):
        list_queue.dequeue()


def test_list_stack():
    numbers = np.random.randint(0, 1000, 100000)
    list_stack = List_Stack.Stack()
    for i in range(len(numbers)):
        list_stack.push(i)
    for i in range(len(numbers)):
        list_stack.pop()


def test_full_stack():
    print("Test run of Linked List Queue")
    cProfile.run("test_queue()", sort="tottime")
    print("Test run of Python List Queue")
    cProfile.run("test_list_queue()", sort="tottime")
    print("Test run of Linked List Stack")
    cProfile.run("test_stack()", sort="tottime")
    print("Test run of Python List Stack")
    cProfile.run("test_list_stack()", sort="tottime")


test_full_stack()
