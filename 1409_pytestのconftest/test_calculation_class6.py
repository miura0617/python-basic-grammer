# pytestのコマンドライン引数によって、処理させたい場合
# > pytest test_calculation_class6.py --os-name=mac
# 結果： 動作しない！！
# 考察： 動画はpytest 3.2.1、自分はpytest 6.1.1でだいぶ違うため、動作しないのでは
import pytest
import calculation


class TestCal(object):
    # setup_class/teardown_class
    # classを生成する前後で実行される
    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calculation.Cal()

    def test_add_num_and_double(self, request):
        os_name = request.config.getoption('--os-name')
        print(os_name)
        if os_name == 'mac':
            print('ls')
        elif os_name == 'windows':
            print('dir')
        assert self.cal.add_num_and_double(1, 1) == 4
