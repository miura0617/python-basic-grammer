# pytestのコマンドライン引数によって、処理させたい場合
# > pytest test_calculation_class6.py --os-name=mac
# 結果： 動作しない！！
# 考察： 動画はpytest 3.2.1、自分はpytest 6.1.1でだいぶ違うため、動作しないのでは
import os
import pytest
import calculation


class TestCal(object):
    # setup_class/teardown_class
    # classを生成する前後で実行される
    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calculation.Cal()
        cls.test_file_name = 'test.txt'

    def test_add_num_and_double(self):
        assert self.cal.add_num_and_double(1, 1) == 4

    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(
            tmpdir, test_file_name
        )
        assert os.path.exists(test_file_path) is True