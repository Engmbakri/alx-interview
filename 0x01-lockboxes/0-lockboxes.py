#!/usr/bin/python3
"""
Solution to lockboxes problem
"""


def canUnlockAll(boxes):
    """
    Determines whether all locked boxes can be opened based on available keys.

    Args:
    - boxes (list of lists): A list where each index represents a box
    and each box
    contains a list of keys (integers) to other boxes.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    n = len(boxes)
    visited = set()
    visited.add(0)  # Start with the first box unlocked

    queue = [0]  # Initialize queue with the first box

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if key < n and key not in visited:
                visited.add(key)
                queue.append(key)

    return len(visited) == n
