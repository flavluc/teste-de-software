import sys
import time

from datalg.bfs import bfs
from datalg.binary_search import binary_search
from datalg.bubble_sort import bubble_sort
from datalg.dfs import dfs
from datalg.graph import DirectedGraph, GraphInterface, UndirectedGraph
from datalg.linked_list import LinkedList
from datalg.merge_sort import merge_sort
from datalg.queue import Queue
from datalg.quick_sort import quicksort
from datalg.stack import Stack
from datalg.tree import Tree


class Repl:
    def __init__(self, output_stream):
        self.env = {}
        self.history = Stack()
        self.__ostream = output_stream

    def eval(self, msg):
        command = msg.split(" ", 1)[0]

        if command == "list":
            for key in self.env:
                print(key + ": " + str(self.env[key]), file=self.__ostream)
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
            self.parse_sort(args)
        elif command == "search":
            self.parse_search(args)
        else:
            raise "Unexpected command"

    def dfs_path(self, name, el):
        return str(dfs(self.env[name], el))

    def bfs_path(self, name, el):
        return str(bfs(self.env[name], el))

    def bin_search(self, name, el):
        arr = self.env[name].to_list()
        print(binary_search(arr, el), file=self.__ostream)

    def sort(self, li, sort_alg, inplace=False):
        t1 = time.time()
        if inplace:
            sort_alg(li)
            t2 = time.time()
            print(li, file=self.__ostream)
        else:
            li = sort_alg(li)
            t2 = time.time()
            print(li, file=self.__ostream)
        print("Tempo: " + str(t2 - t1), file=self.__ostream)

    def parse_sort(self, args):
        alg, name = args.split(" ")
        structure = self.env[name]
        li = structure.to_list()
        if alg == "quick_sort":
            self.sort(li, quicksort)
        elif alg == "merge_sort":
            self.sort(li, merge_sort)
        elif alg == "bubble_sort":
            self.sort(li, bubble_sort, inplace=True)

    def parse_search(self, args):
        alg, name, args = args.split(" ")
        el = int(args)
        if alg == "bfs":
            print(self.bfs_path(name, el), file=self.__ostream)
        elif alg == "dfs":
            print(self.dfs_path(name, el), file=self.__ostream)
        elif alg == "binary":
            print(self.bin_search(name, el), file=self.__ostream)

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
        elif structure == "undirected_graph":
            self.create(name, UndirectedGraph())
        elif structure == "tree":
            _, name, root_id, content = args.split(" ", 3)
            self.create(name, Tree(int(root_id), int(content)))

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
        elif isinstance(structure, GraphInterface):
            elm_type = args.split(" ", 1)[0]
            if elm_type == "edge":
                _, start_node, end_node = args.split(" ", 2)
                self.add_graph_edge(name, int(start_node), int(end_node))
            elif elm_type == "node":
                self.add_graph_node(name, args.split(" ", 1)[1])
        elif isinstance(structure, Tree):
            parent_id, node_id, content = args.split(" ", 2)
            self.add_tree_node(
                name, int(parent_id), int(node_id), int(content)
            )

    def add_graph_edge(self, name, start_node, end_node):
        self.env[name].add_edge(start_node, end_node)

    def add_graph_node(self, name, node_id):
        self.env[name].add_node(int(node_id), int(node_id))

    def add_tree_node(self, name, parent_id, node_id, content):
        self.env[name].add_node(parent_id, node_id, content)

    def remove_graph_element(self, name, node_id):
        self.env[name].remove_node(node_id)

    def parse_remove(self, args):
        name = args.split(" ", 1)[0]
        structure = self.env[name]
        if isinstance(structure, Stack):
            print(self.remove_stack_element(name), file=self.__ostream)
        elif isinstance(structure, Queue):
            print(self.remove_queue_element(name), file=self.__ostream)
        elif isinstance(structure, LinkedList):
            n = args.split(" ", 1)[1]
            print(self.remove_list_element(name, n), file=self.__ostream)
        elif isinstance(structure, GraphInterface):
            _, n = args.split(" ", 1)
            print(structure.get_node_content(int(n)), file=self.__ostream)
            self.remove_graph_element(name, n)

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
            return li.delete_head().content
        elif n == "tail":
            return li.delete_tail().content
        else:
            n = int(n)
            return li.delete_nth(n).content

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
                    print(f"Error: {e}", file=self.__ostream)
        except KeyboardInterrupt:
            print("\nExiting...", file=self.__ostream)


if __name__ == "__main__":
    print()
    print("Welcome to python datalg-REPL")
    print("crtl-c to quit")
    print()
    repl = Repl(sys.stdout)
    repl.loop()
