import unittest
import os,sys

from context import IocFile



class TestIocFile(unittest.TestCase):

    def setUp(self):

        self.ioc_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'iocfile.txt'
        )

        self.ioc_file = IocFile(self.ioc_file_path)
        
    
    def tearDown(self):

        self.ioc_file = None

    '''
    def test_ioc_file_path(self):

        print self.ioc_file.file
    '''

    def test_iocfile_domains(self):

        self.assertIn('cmatthewbrooks.com', self.ioc_file.domains)

    def test_neutered_iocfile_domains(self):

        self.assertIn('www.badguy.com', self.ioc_file.domains)

    def test_iocfile_ips(self):
        
        self.assertIn('8.8.8.8', self.ioc_file.ips)

    def test_iocfile_emails(self):

        self.assertIn('me@cmatthewbrooks.com', self.ioc_file.emails)

    def test_iocfile_hashes(self):

        self.assertIn('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', self.ioc_file.hashes)
        self.assertIn('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', self.ioc_file.hashes)

    def test_bad_lines_unparsed(self):
        
        all_indicators = self.ioc_file.all_indicators()
        self.assertEquals(len(all_indicators), 6)

if __name__ == '__main__':
    unittest.main()
