import os
import sys

if __name__ == '__main__':
    tree_nodes, tree_edges = map(int, input().split())

    tree_from = [0] * tree_edges
    tree_to = [0] * tree_edges

    for tree_itr in range(tree_edges):
        tree_from[tree_itr], tree_to[tree_itr] = map(int, input().split())

    #
    # Write your code here.
    #

    dict_nodes = {}

    for i in range(len(tree_to)):
        if tree_to[i] not in dict_nodes:
            dict_nodes[tree_to[i]] = []

        dict_nodes[tree_to[i]].append(tree_from[i])


    def count_subtree_size(node):
        if node in dict_nodes:
            sum = 1
            for neighbor in dict_nodes[node]:
                sum += count_subtree_size(neighbor)
            return sum
        else:
            return 1

    edges_to_be_deleted = 0

    for node in dict_nodes:
        if count_subtree_size(node)%2 == 0:
            edges_to_be_deleted += 1

    edges_to_be_deleted -= 1
    print(edges_to_be_deleted)
