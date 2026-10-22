import unittest

from autorecon import validate_target


class TestTargetValidation(unittest.TestCase):
    def test_valid_ipv4(self):
        self.assertTrue(validate_target("192.168.56.101"))

    def test_valid_ipv6(self):
        self.assertTrue(validate_target("2001:db8::1"))

    def test_valid_hostname(self):
        self.assertTrue(validate_target("example.com"))

    def test_valid_lab_hostname(self):
        self.assertTrue(validate_target("metasploitable.local"))

    def test_rejects_invalid_ipv4(self):
        self.assertFalse(validate_target("999.999.999.999"))

    def test_rejects_spaces(self):
        self.assertFalse(validate_target("bad target"))

    def test_rejects_empty_target(self):
        self.assertFalse(validate_target(""))

    def test_rejects_hostname_starting_with_hyphen(self):
        self.assertFalse(validate_target("-invalid.example"))


if __name__ == "__main__":
    unittest.main()
