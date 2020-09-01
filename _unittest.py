import invert_binary_tree


TREE_A = tuple(range(1, 8))
TREE_A_INVERT = (1, 3, 2, 7, 6, 5, 4)

TREE_B = tuple(range(1, 32))
TREE_B_INVERT = tuple([1, 3, 2] + list(reversed(range(4, 8))) 
                + list(reversed(range(8, 16)))
                + list(reversed(range(16, 32))))


def run_tests():
    assert invert_binary_tree.invert(TREE_A) == TREE_A_INVERT, \
        "Failed to invert first tree"
    assert invert_binary_tree.invert(TREE_B) == TREE_B_INVERT, \
        "Failed to invert second tree"


def _main():
    run_tests()


if __name__ == '__main__':
    _main()