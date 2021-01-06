from unittest import TestCase

from wave_reader.util import UnknownDevice, parse_serial_number


class TestReaderUtils(TestCase):
    def test_parse_serial_number(self):
        """Validate Wave Plus manufacturer data parsing."""
        valid_data = {820: [13, 25, 160, 170, 9, 0]}
        valid_serial = parse_serial_number(valid_data)
        self.assertEqual(valid_serial, 2862618893)

        invalid_data = [
            {},
            None,
            {120: []},
            {120: None},
            {820: [10, 20]},
            {120: [13, 25, 160, 170, 9, 0]}
        ]
        for i in invalid_data:
            self.assertRaises(UnknownDevice, parse_serial_number, i)
