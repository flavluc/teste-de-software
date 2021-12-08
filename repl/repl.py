from datalg.bfs import bfs
from datalg.binary_search import binary_search
from datalg.dfs import dfs
from datalg.graph import DirectedGraph, GraphInterface, UndirectedGraph
from datalg.linked_list import LinkedList
from datalg.queue import Queue
from datalg.stack import Stack
from datalg.tree import Tree


class Repl:
    def __init__(self):
        self.env = {}
        self.history = Stack()

    def eval(self, msg):
        command = msg.split(" ", 1)[0]

        if command == "list":
            for key in self.env:
                print(key + ": " + str(self.env[key]))
            return

        args = msg.split(" ", 1)[1]

        if command == "delete":
            del self.env[args]
        elif command == "create":
            self.parse_create(args)
        elif command == "add":
            self.parse_add(args)
        elif command == "remove":
            self.parse_remove(args)
        elif command == "sort":
            raise NotImplementedError
        elif command == "search":
            self.parse_search(args)
        else:
            raise "Unexpected command"

    def parse_search(self, args):
        alg, name, args = args.split(" ")
        el = int(args)
        structure = self.env[name]
        if alg == "bfs":
            print(bfs(structure, el))
        elif alg == "dfs":
            print(dfs(structure, el))
        elif alg == "binary":
            arr = structure.to_list()
            print(binary_search(arr, el))

    def parse_create(self, args):
        structure, name = args.split(" ", 1)
        if structure == "stack":
            self.create(name, Stack())
        elif structure == "queue":
            self.create(name, Queue())
        elif structure == "list":
            self.create(name, LinkedList())
        elif structure == "directed_graph":
            self.create(name, DirectedGraph())
        elif structure == "directed_graph":
            self.create(name, UndirectedGraph())
        elif structure == "tree":
            raise NotImplementedError

    def parse_add(self, args):
        name, args = args.split(" ", 1)
        structure = self.env[name]
        if isinstance(structure, Stack):
            self.add_stack_element(name, args)
        elif isinstance(structure, Queue):
            self.add_queue_element(name, args)
        elif isinstance(structure, LinkedList):
            el, n = args.split()
            self.add_list_element(name, el, n)
        elif isinstance(structure, Tree) or isinstance(
            structure, GraphInterface
        ):
            raise NotImplementedError

    def parse_remove(self, args):
        name = args
        structure = self.env[name]
        if isinstance(structure, Stack):
            print(self.remove_stack_element(name))
        elif isinstance(structure, Queue):
            print(self.remove_queue_element(name))
        elif isinstance(structure, LinkedList):
            name, n = args.split(" ", 1)
            print(self.remove_list_element(name, n))
        elif (
            isinstance(structure, Tree)
            or isinstance(structure, UndirectedGraph)
            or isinstance(structure, DirectedGraph)
        ):
            raise NotImplementedError

    def create(self, name, structure):
        self.env[name] = structure

    def add_stack_element(self, name, el):
        el = int(el)
        stack = self.env[name]
        stack.push(el)

    def add_queue_element(self, name, el):
        el = int(el)
        queue = self.env[name]
        queue.enqueue(el)

    def add_list_element(self, name, el, n):
        el = int(el)
        li = self.env[name]
        if n == "head":
            li.insert_head(el)
        elif n == "tail":
            li.insert_tail(el)
        else:
            n = int(n)
            li.insert_nth(el, n)

    def remove_stack_element(self, name):
        stack = self.env[name]
        return stack.pop()

    def remove_queue_element(self, name):
        queue = self.env[name]
        return queue.dequeue()

    def remove_list_element(self, name, n):
        li = self.env[name]
        if n == "head":
            return li.delete_head()
        elif n == "tail":
            return li.delete_tail()
        else:
            n = int(n)
            return li.delete_nth(n)

    def loop(self):
        try:
            while True:
                try:
                    _in = input(">>> ")
                    if self.history.size() >= 100:
                        self.history.pop()
                    self.history.push(_in)
                    self.eval(_in)
                except Exception as e:
                    print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nExiting...")


if __name__ == "__main__":
    print()
    print("Welcome to python datalg-REPL")
    print("crtl-c to quit")
    print()
    repl = Repl()
    repl.loop()
