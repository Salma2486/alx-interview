#!/usr/bin/python3
"""lockboxes module"""


def canUnlockAll(boxes):
    opened_boxes = set([0])
    used_keys = boxes[0][:]
    while used_keys:
        key = used_keys.pop()
        if key < len(boxes) and key not in opened_boxes:
            opened_boxes.add(key)
            used_keys += boxes[key]
    return len(opened_boxes) == len(boxes)
