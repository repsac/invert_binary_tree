import invert_binary_tree


TREE_A1 = tuple(range(1, 8))
TREE_A2 = (1, 3, 2, 7, 6, 5, 4)

TREE_B1 = tuple(range(1, 32))
TREE_B2 = tuple([1, 3, 2] + list(reversed(range(4, 8))) 
                + list(reversed(range(8, 16)))
                + list(reversed(range(16, 32))))

def run_tests():
    assert invert_binary_tree.invert(TREE_A1) == TREE_A2, \
        "Failed to invert first tree"
    assert invert_binary_tree.invert(TREE_B1) == TREE_B2, \
        "Failed to invert first tree"


def _main():
    run_tests()

if __name__ == '__main__':
    _main()