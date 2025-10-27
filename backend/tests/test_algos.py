
import pytest
from src.algos.functions import is_palindrome, compress_ranges, min_path_sum, top_k_frequent_words

def test_is_palindrome():
    assert is_palindrome("neuquen")
    assert is_palindrome("Anita lava la tina")
    assert not is_palindrome("python")

def test_compress_ranges():
    assert compress_ranges([1,2,3,5,7,8]) == ["1-3","5","7-8"]
    assert compress_ranges([]) == []
    assert compress_ranges([10]) == ["10"]
    assert compress_ranges([1,3,5]) == ["1","3","5"]
    assert compress_ranges([0,1,2,3]) == ["0-3"]

def test_min_path_sum():
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    assert min_path_sum(grid) == 7  # 1->3->1->1->1

def test_top_k_frequent_words():
    words = "a a a b b c c c c d".split()
    assert top_k_frequent_words(words, 2) == ["c", "a"]
    assert top_k_frequent_words(words, 3) == ["c", "a", "b"]
    assert top_k_frequent_words([], 1) == []
