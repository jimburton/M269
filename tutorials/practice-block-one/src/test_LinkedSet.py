from LinkedSet import LinkedSet
import unittest

class Testing(unittest.TestCase):

    def test_add_and_size(self):
        """Test that we can add items to a set and the size method
        works as expected.
        """
        s1 = LinkedSet()
        self.assertEqual(s1.size(), 0)
        for i in range(0,10):
            s1.add(i)
        self.assertEqual(s1.size(), 10)

    def test_add_and_member(self):
        """Test that we can add items to a set and the member method
        can find them. Also test that we can't find items which aren't there.
        """
        s1 = LinkedSet()
        s1.add("hi")
        self.assertTrue(s1.member("hi"))
        self.assertFalse(s1.member("ho"))
        for i in range(0,10):
            s1.add(i)
        for i in range(0,10):
            self.assertTrue(s1.member(i))

    def test_isdisjoint(self):
        """Test the isdisjoint method."""
        s1 = LinkedSet()
        for i in range(0,10):
            s1.add(i)
        s2 = LinkedSet()
        for i in range(10,20):
            s2.add(i)
        self.assertTrue(s1.isdisjoint(s2))
        self.assertTrue(s2.isdisjoint(s1))
        s1.add(10)
        self.assertFalse(s1.isdisjoint(s2))
        self.assertFalse(s2.isdisjoint(s1))

    def test_issubset(self):#
        """Test the issubset method."""
        s1 = LinkedSet()
        for i in range(0,10):
            s1.add(i)
        self.assertTrue(s1.issubset(s1))
        s2 = LinkedSet()
        for i in range(3,8):
            s2.add(i)
        self.assertTrue(s2.issubset(s1))
        self.assertFalse(s1.issubset(s2))

    def test_issuperset(self):
        """Test the issuperset method."""
        s1 = LinkedSet()
        for i in range(0,10):
            s1.add(i)
        self.assertTrue(s1.issubset(s1))
        s2 = LinkedSet()
        for i in range(3,8):
            s2.add(i)
        self.assertTrue(s1.issuperset(s2))
        self.assertFalse(s2.issuperset(s1))

    def test_clone_and_eq(self):
        """Test the clone method and the builtin equality method __eq__."""
        s1 = LinkedSet()
        for i in range(0,10):
            s1.add(i)
        s2 = s1.clone()
        self.assertEqual(s1.size(), s2.size())
        self.assertTrue(s1 == s2)
        s3 = LinkedSet()
        self.assertNotEqual(s1, s3)
        for i in range(0,11):
            s3.add(i)
        self.assertNotEqual(s1, s3)

    def test_union(self):
        """Test the union method."""
        s1 = LinkedSet()
        for i in range(0,10):
            s1.add(i)
        s2 = LinkedSet()
        for i in range(10,20):
            s2.add(i)
        s3 = LinkedSet()
        for i in range(0,20):
            s3.add(i)
        self.assertEqual(s1.union(s2), s3)

    def test_intersection(self):
        """Test the intersection method."""
        s1 = LinkedSet()
        for i in range(0,14):
            s1.add(i)
        s2 = LinkedSet()
        for i in range(10,20):
            s2.add(i)
        s3 = LinkedSet()
        for i in range(10,14):
            s3.add(i)
        self.assertEqual(s1.intersection(s2), s3)

    def test_difference(self):
        """Test the difference method."""
        s1 = LinkedSet()
        for i in range(0,14):
            s1.add(i)
        s2 = LinkedSet()
        for i in range(10,20):
            s2.add(i)
        s3 = LinkedSet()
        for i in range(0,10):
            s3.add(i)
        self.assertEqual(s1.difference(s2), s3)
        s4 = LinkedSet()
        for i in range(14,20):
            s4.add(i)
        self.assertEqual(s2.difference(s1), s4)

    def test_remove(self):
        """Test the remove method."""
        s1 = LinkedSet()
        for i in range(0,10):
            s1.add(i)
        s1.remove(5)
        self.assertTrue(s1.size() == 9)
        self.assertFalse(s1.member(5))

    def test_remove_missing(self):
        """Test that the remove method throws a KeyError."""
        s1 = LinkedSet()
        # try to remove from the empty set
        with self.assertRaises(KeyError):
            s1.remove(5)
        s1.add(99)
        # try to remove a missing item from a non-empty set
        with self.assertRaises(KeyError):
            s1.remove(5)
        

# If this script is run directly, run the tests
if __name__ == '__main__':
    unittest.main()
