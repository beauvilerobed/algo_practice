import unittest
from word_trie_generator import generate_words, generate_trie,\
                                generate_other_words
from get_all_words import get_all_words
from find_total import get_total, get_total_naive


words = generate_words()
trie = generate_trie(words)
other_words = generate_other_words(words)


class TestTrie(unittest.TestCase):
    def test_search_method(self):
        for word in other_words:
            expected = ''
            if word in words:
                expected = "word found"
            else:
                expected = "word not found"
            actual = trie.search(word)
            self.assertEqual(actual, expected)

    def test_query_method(self):
        for i, prefix in enumerate(other_words):
            actual = False
            expected = False
            prefix = prefix[:-2]
            querys = trie.query(prefix)
            if len(querys) == 0:
                actual = True
            if i % 3 == 0:
                expected = True
            self.assertEqual(actual, expected)

    def test_get_all_words(self):
        actual = get_all_words(trie)
        actual.sort()
        expected = words
        expected.sort()
        self.assertEqual(actual, expected)

    def test_total_attr(self):
        self.assertEqual(get_total(trie), trie.word_number)

    def test_find_total(self):
        self.assertEqual(get_total(trie), get_total_naive(trie))


if __name__ == '__main__':
    unittest.main()
