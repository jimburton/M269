from Sorting import *
import unittest

class Testing(unittest.TestCase):

    def setUp(self):
        self.people = list()
        self.people.append(Name("Hubert",  "Huncke",    datetime(1915, 1, 9)))
        self.people.append(Name("Gary",    "Snyder",    datetime(1930, 5, 8)))
        self.people.append(Name("Gregory", "Corso",     datetime(1930, 3, 26)))
        self.people.append(Name("Neal",    "Cassady",   datetime(1926, 2, 8)))
        self.people.append(Name("Jack",    "Kerouac",   datetime(1922, 3, 12)))
        self.people.append(Name("Allen",   "Ginsberg",  datetime(1926, 6, 3)))
        self.people.append(Name("William", "Burroughs", datetime(1914, 2, 5)))

    def test_sort_builtin(self):
        """Test that we can sort using the default method.
        """
        p = sort_builtin(self.people.copy())
        result = "[William Burroughs, Neal Cassady, Gregory Corso, Allen Ginsberg, Hubert Huncke, Jack Kerouac, Gary Snyder]"
        self.assertEqual(str(p), result)

    def test_sort_fullname(self):
        """Test that we can sort by full name.
        """
        p = sort_fullname(self.people.copy())
        result = "[Allen Ginsberg, Gary Snyder, Gregory Corso, Hubert Huncke, Jack Kerouac, Neal Cassady, William Burroughs]"
        self.assertEqual(str(p), result)

    def test_sort_dob(self):
        """Test that we can sort by arbitrary date of birth.
        """
        p = sort_dob(self.people.copy())
        result = "[William Burroughs, Hubert Huncke, Jack Kerouac, Neal Cassady, Allen Ginsberg, Gregory Corso, Gary Snyder]"
        self.assertEqual(str(p), result)

    def test_sort_opred(self):
        """Test that we can sort by the occurence of the character 'o'.
        """
        p = sort_opred(self.people.copy())
        result = "[Gregory Corso, Jack Kerouac, William Burroughs, Hubert Huncke, Gary Snyder, Neal Cassady, Allen Ginsberg]"
        self.assertEqual(str(p), result)

    def test_sort_char_pred(self):
        """Test that we can sort by arbitrary characters.
        """
        p = sort_char_pred(self.people.copy(), "l")
        result = "[Allen Ginsberg, William Burroughs, Neal Cassady, Hubert Huncke, Gary Snyder, Gregory Corso, Jack Kerouac]"
        self.assertEqual(str(p), result)
  
# If this script is run directly, run the tests
if __name__ == '__main__':
    unittest.main()
