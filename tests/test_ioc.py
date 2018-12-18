import unittest

from context import Ioc
import data


class TestIOC(unittest.TestCase):

    def test_is_domain(self):

        for domain in data.TEST_DOMAINS_GOOD:
    
            self.assertTrue(
                Ioc.is_domain(domain)
            )

    def test_is_not_domain(self):

        for domain in data.TEST_DOMAINS_BAD:

            self.assertFalse(
                Ioc.is_domain(domain)
            )

    def test_is_ip(self):
        
        for ip in data.TEST_IPS_GOOD:

            self.assertTrue(
                Ioc.is_ip(ip)
            )

    def test_is_not_ip(self):

        for ip in data.TEST_IPS_BAD:

            self.assertFalse(
                Ioc.is_ip(ip)
            )

    def test_is_md5(self):

        for hash in data.TEST_MD5_GOOD:

            self.assertTrue(
                Ioc.is_md5(hash)
            )

    def test_is_not_md5(self):

        for hash in data.TEST_MD5_BAD:

            self.assertFalse(
                Ioc.is_md5(hash)
            )

    def test_is_sha1(self):

        for hash in data.TEST_SHA1_GOOD:

            self.assertTrue(
                Ioc.is_sha1(hash)
            )

    def test_is_not_sha1(self):

        for hash in data.TEST_SHA1_BAD:

            self.assertFalse(
                Ioc.is_sha1(hash)
            )

    def test_is_sha256(self):

        for hash in data.TEST_SHA256_GOOD:

            self.assertTrue(
                Ioc.is_sha256(hash)
            )

    def test_is_not_sha256(self):

        for hash in data.TEST_SHA256_BAD:

            self.assertFalse(
                Ioc.is_sha256(hash)
            )

    def test_is_hash(self):

        for hash in data.TEST_MD5_GOOD:

            self.assertTrue(
                Ioc.is_hash(hash)
            )

        for hash in data.TEST_SHA1_GOOD:

            self.assertTrue(
                Ioc.is_hash(hash)
            )

        for hash in data.TEST_SHA256_GOOD:

            self.assertTrue(
                Ioc.is_hash(hash)
            )

    def test_is_not_hash(self):

        for hash in data.TEST_MD5_BAD:

            self.assertFalse(
                Ioc.is_hash(hash)
            )

        for hash in data.TEST_SHA1_BAD:

            self.assertFalse(
                Ioc.is_hash(hash)
            )

        for hash in data.TEST_SHA256_BAD:

            self.assertFalse(
                Ioc.is_hash(hash)
            )

    def test_is_email(self):

        for email in data.TEST_EMAILS_GOOD:

            self.assertTrue(
                Ioc.is_email(email)
            )

    def test_is_not_email(self):

        for email in data.TEST_EMAILS_BAD:

            self.assertFalse(
                Ioc.is_email(email)
            )

    def test_is_indicator(self):

        for indicator in data.ALL_INDICATORS_GOOD:

            self.assertTrue(
                Ioc.is_indicator(indicator)
            )

    def test_get_indicator_type(self):

        for indicator in data.TEST_DOMAINS_GOOD:
            self.assertEqual(Ioc.get_indicator_type(indicator), Ioc.DOMAIN)
    
        for indicator in data.TEST_IPS_GOOD:
            self.assertEqual(Ioc.get_indicator_type(indicator), Ioc.IP)

        for indicator in data.TEST_MD5_GOOD:
            self.assertEqual(Ioc.get_indicator_type(indicator), Ioc.MD5)

        for indicator in data.TEST_SHA1_GOOD:
            self.assertEqual(Ioc.get_indicator_type(indicator), Ioc.SHA1)

        for indicator in data.TEST_SHA256_GOOD:
            self.assertEqual(Ioc.get_indicator_type(indicator), Ioc.SHA256)

        for indicator in data.TEST_EMAILS_GOOD:
            self.assertEqual(Ioc.get_indicator_type(indicator), Ioc.EMAIL)
            
    def test_clean_indicator(self):

        for indicator in data.TEST_NEUTERED_INDICATORS:
            self.assertTrue(
                Ioc.is_indicator(Ioc.clean_indicator(indicator))
            )

if __name__ == '__main__':
    unittest.main()
