# mockを使ったテスト

import unittest
from unittest.mock import MagicMock
from unittest import mock

import salary


class TestSalary(unittest.TestCase):
    def test_calculation_salary(self):
        s = salary.Salary(year=2017)
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        self.assertEqual(s.calculation_salary(), 101)
        # magicmockであるbonus_api.bonus_price()APIが本当に呼ばれたかテストもできる
        s.bonus_api.bonus_price.assert_called()
        # magicmockであるbonus_api.bonus_price()APIが一度だけ呼ばれたかテストできる
        s.bonus_api.bonus_price.assert_called_once()
        # magicmockであるbonus_api.bonus_price()APIの引数yearがちゃんと渡されていrうかテストできる
        s.bonus_api.bonus_price.assert_called_with(year=2017)
        # magicmockであるbonus_api.bonus_price()APIが一度だけ呼ばれ、かつ引数が2017かテストできる
        s.bonus_api.bonus_price.assert_called_once_with(year=2017)
        # magicmockであるbonus_api.bonus_price()APIが何回呼ばれたかもわかる
        self.assertEqual(s.bonus_api.bonus_price.call_count, 1)

    def test_calculation_salary_no_salary(self):
        s = salary.Salary(year=2050)
        s.bonus_api.bonus_price = MagicMock(return_value=0)
        self.assertEqual(s.calculation_salary(), 100)
        # magicmockであるbonus_api.bonus_price()APIが呼ばれないこともテストできる
        s.bonus_api.bonus_price.assert_not_called()

    # 1. デコレーターでパスを指定すると、わざわざMagicMock()としなくてよい
    @mock.patch('salary.ThirdPartyBonusRestApi.bonus_price')
    def test_calculation_salary_patch(self, mock_bonus):
        mock_bonus.return_value = 1

        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(s.calculation_salary(), 101)
        mock_bonus.assert_called()

    # 2. デコレーターではなく、with ステートメントでもできる
    def test_calculation_salary_patch_with(self):
        # withステートメントの中だけ、mock_bonusが有効である
        with mock.patch('salary.ThirdPartyBonusRestApi.bonus_price') as mock_bonus:
            mock_bonus.return_value = 1

            s = salary.Salary(year=2017)
            salary_price = s.calculation_salary()

            self.assertEqual(s.calculation_salary(), 101)
            mock_bonus.assert_called()

    # 3. パッチャーを使ってもできる
    def test_calculation_salary_patch_patcher(self):
        patcher = mock.patch('salary.ThirdPartyBonusRestApi.bonus_price')
        # patcher.start() ~ stop()の間だけ、mock_bonusが有効である
        mock_bonus = patcher.start()
        mock_bonus.return_value = 1

        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(s.calculation_salary(), 101)
        mock_bonus.assert_called()
        patcher.stop()