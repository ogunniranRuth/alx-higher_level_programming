                 """Test a string."""

                                                                                                                                                                                                                                                                string = "Brennan"

                                                                                                                                                                                                                                                                        self.assertEqual(max_integer(string), 'r')



                                                                                                                                                                                                                                                                            def test_list_of_strings(self):

                                                                                                                                                                                                                                                                                        """Test a list of strings."""

                                                                                                                                                                                                                                                                                                strings = ["Brennan", "is", "my", "name"]

                                                                                                                                                                                                                                                                                                        self.assertEqual(max_integer(strings), "name")



                                                                                                                                                                                                                                                                                                            def test_empty_string(self):

                                                                                                                                                                                                                                                                                                                        """Test an empty string."""

                                                                                                                                                                                                                                                                                                                                self.assertEqual(max_integer(""), None)



                                                                                                                                                                                                                                                                                                                                if __name__ == '__main__':

                                                                                                                                                                                                                                                                                                                                        unittest.main()#!/usr/bin/python3

                                                                                                                                                                                                                                                                                                                                        """Unittests for max_integer([..])."""



                                                                                                                                                                                                                                                                                                                                        import unittest

                                                                                                                                                                                                                                                                                                                                        max_integer = __import__('6-max_integer').max_integer





                                                                                                                                                                                                                                                                                                                                        class TestMaxInteger(unittest.TestCase):

                                                                                                                                                                                                                                                                                                                                                """Define unittests for max_integer([..])."""



                                                                                                                                                                                                                                                                                                                                                    def test_ordered_list(self):

                                                                                    dered), 4)



                                                                                                                                                                                                                                                                                                                                                                                    def test_unordered_list(self):

                                                                                                                                                                                                                                                                                                                                                                                                """Test an unordered list of integers."""

                                                                                                                                                                                                                                                                                                                                                                                                        unordered = [1, 2, 4, 3]

                                                                                                                                                                                                                                                                                                                                                                                                                self.assertEqual(max_integer(unordered), 4)

??? from here until ???END lines may have been inserted/deleted


                                                                                                                                                                                                                                                                                                                                                                                                                    def test_max_at_begginning(self):

                                                                                                                                                                                                                                                                                                                                                                                                                                """Test a list with a beginning max value."""

                                                                                                                                                                                                                                                                                                                                                                                                                                        max_at_beginning = [4, 3, 2, 1]

                                                                                                                                                                                                                                                                                                                                                                                                                                                self.assertEqual(max_integer(max_at_beginning), 4)



                                                                                                                                                                                                                                                                                                                                                                                                                                                    def test_empty_list(self):

                                                                                                                  empty = []

???END
