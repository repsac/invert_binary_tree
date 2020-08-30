def invert(tree):
    end = 1
    inverted = []
    while end <= len(tree):
        start = end
        end = end * 2 + 1
        inverted.extend(reversed(tree[start:end]))
    inverted.insert(0, tree[0])
    return tuple(inverted)