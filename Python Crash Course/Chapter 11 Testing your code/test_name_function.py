'''
Unit test
'''

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    ''' Tests for name_function.py '''

    def test_first_last_name(self):
        ''' Do names like Janis Joplin work '''
        formatted_name = get_formatted_name("Janis", "Joplin")
        self.assertEqual(formatted_name, "Janis Joplin1")

if __name__ == "__main__":

    unittest.main()

'''

Example of a failing unittest:

Testing started at 06:42 ...

Ran 1 test in 0.000s

Janis Joplin1 != Janis Joplin

Expected :Janis Joplin
Actual   :Janis Joplin1
 <Click to see difference>

AssertionError: 'Janis Joplin' != 'Janis Joplin1'
- Janis Joplin
+ Janis Joplin1
?             +

'''