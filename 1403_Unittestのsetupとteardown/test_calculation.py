import unittest

import calculation


class CalTest(unittest.TestCase):
    # テストの前後に処理を入れるsetupとteardown
    def setUp(self):
        print('setup')
        self.cal = calculation.Cal()

    def tearDown(self):
        print('clean up')
        del self.cal

    def test_add_num_and_double(self):
        self.assertEqual(
            self.cal.add_num_and_double(1, 1),
            4
        )

    # 例外処理のテスト
    # withステートメントでassertRaisesメソッドを使う
    def test_add_num_and_double_raise(self):
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1', '1')


if __name__ == '__main__':
    unittest.main()
