
from typing import List

def find_choices(path: List[int], initial_seating: List[int]):
    choices = []
    current_seating = path + initial_seating[len(path):]
    for i in range(len(path), len(initial_seating)):
        if initial_seating[i]:
            continue
        ppl_close = 0
        if 0 <= i-1:
            ppl_close += current_seating[i-1]
        if 0 <= i-2:
            ppl_close += current_seating[i-2]
        if i+1 < len(current_seating):
            ppl_close += current_seating[i+1]
        if i+2 < len(current_seating):
            ppl_close += current_seating[i+2]
        if ppl_close == 0:
            choices.append(i)
    return choices


def seat_at_i(path, initial_seating, i):
    current_seating = path + initial_seating[len(path):]
    current_seating[i] = 1
    return current_seating[:i+1]


def maximum_seating(initial_seating):
    initial_seated = sum(initial_seating)
    ans = 0


    def backtrack(path: List[int], ans: int) -> int:

        choices_to_seat = find_choices(path, initial_seating)

        if len(path) == len(initial_seating):
            seated = sum(path) - initial_seated
            if seated > ans:
                ans = seated
            return ans

        if not choices_to_seat:
            current_seating = path + initial_seating[len(path):]
            seated = sum(current_seating) - initial_seated
            if seated > ans:
                ans = seated
            return ans

        for choice in choices_to_seat:
            new_path = seat_at_i(path, initial_seating, choice)
            ans = backtrack(new_path, ans)

        return ans

    return backtrack([], 0)



import unittest
class TestSolution(unittest.TestCase):

    def test_maximum_seating(self):
        # print(maximum_seating([0, 0, 0, 1, 0, 0, 1, 0, 0, 0]))
        assert maximum_seating([0, 0, 0, 1, 0, 0, 1, 0, 0, 0]) == 2
        assert maximum_seating([0, 0, 0, 0]) == 2
        # print(maximum_seating([1, 0, 0, 0, 0, 0, 1]))
        assert maximum_seating([1, 0, 0, 0, 0, 0, 1]) == 1
        assert maximum_seating([1, 0, 0, 0, 0, 0, 0, 1]) == 1
        assert maximum_seating([1, 0, 0, 0, 0, 1]) == 0
        assert maximum_seating([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 4
        assert maximum_seating([0]) == 1
        assert maximum_seating([0, 0]) == 1
        assert maximum_seating([1]) == 0
        assert maximum_seating(
            [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0]) == 1


    def test_seat_at_i(self):
        path = [1, 0, 0]
        initial_seating = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
        # print(seat_at_i(path, initial_seating, 9))
        assert seat_at_i(path, initial_seating, 9) == [1, 0, 0, 1, 0, 0, 1, 0, 0, 1]

        path = [0, 0]
        assert seat_at_i(path, initial_seating, 9) == [0, 0, 0, 1, 0, 0, 1, 0, 0, 1]

    def test_find_choices(self):
        initial_seating = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
        assert find_choices([], initial_seating) == [0, 9]
        assert find_choices([1], initial_seating) == [9]
        assert find_choices([1, 0, 0, 1], initial_seating) == [9]

        initial_seating = [0, 0, 0, 0]
        assert find_choices([], initial_seating) == [0, 1, 2, 3]
        assert find_choices([1], initial_seating) == [3]