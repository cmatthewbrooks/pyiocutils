import unittest
import os,sys

from context import IocArgs



class TestIocArgs(unittest.TestCase):

    def setUp(self):

        self.args = []

    def tearDown(self):

        self.args = []

    def test_file_args_to_set(self):

        self.args.append(os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'iocfile.txt'
        ))

        indicators = IocArgs.args_to_set(self.args)

        self.assertEqual(len(indicators), 6)
        self.assertIn('cmatthewbrooks.com', indicators)
        self.assertIn('www.badguy.com', indicators)

    def test_csv_args_to_set(self):
        
        self.args.append('cmatthewbrooks.com,me@cmatthewbrooks.com,8.8.8.8')

        indicators = IocArgs.args_to_set(self.args)

        self.assertEqual(len(indicators), 3)
        self.assertIn('cmatthewbrooks.com', indicators)
        self.assertIn('me@cmatthewbrooks.com', indicators)
        self.assertIn('8.8.8.8', indicators)

    def test_list_args_to_set(self):
        
        new_args = ['cmatthewbrooks.com','www.badguy.com','8.8.8.8']
        
        self.args.extend(new_args)

        indicators = IocArgs.args_to_set(self.args)

        self.assertEqual(len(indicators), 3)
        self.assertIn('cmatthewbrooks.com', indicators)
        self.assertIn('www.badguy.com', indicators)
        self.assertIn('8.8.8.8', indicators)



if __name__ == '__main__':
    unittest.main()
