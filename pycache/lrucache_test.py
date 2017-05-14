import unittest
from lrucache import LRUCache

class LRUCacheNormalTest(unittest.TestCase):
    def setUp(self):
        self.c = LRUCache(maxsize=10)

    def test_set_get1(self):
        self.c[1] = 2
        self.assertEqual(self.c[1], 2)

    def test_set_get2(self):
        self.c[1] = None
        self.assertEqual(self.c[1], None)

    def test_lru_expiry(self):
        for i in range(0, 11):
            self.c[i] = "test"
        self.assertEqual(10, len(self.c))
        self.assertTrue(0 not in self.c)
        self.assertTrue(10 in self.c)

    def test_lru_expiry1(self):
        for i in range(0, 20):
            self.c[i] = "test"
        self.assertEqual(10, len(self.c))
        for i in range(0, 10):
            self.assertTrue(i not in self.c, "i is {}".format(i))


if __name__ == '__main__':
    unittest.main()
