############################################
# pytestでスキップした関数を表示するには -rs オプションをつけて、実行確認できます
# > pytest <.py> -rs
############################################
import pytest
import calculation

release_ver = '1.0.0'

class TestCal(object):
    # setup_class/teardown_class
    # classを生成する前後で実行される
    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calculation.Cal()

    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.cal

    # setup_method/teardown_method
    # 各テストを実行する前後に実行される
    def setup_method(self, method):
        print('method = {}'.format(method.__name__))
        # self.cal = calculation.Cal()

    def teardown_method(self, method):
        print('method = {}'.format(method.__name__))
        # del self.cal

    def test_add_num_and_double(self):
        assert self.cal.add_num_and_double(1, 1) == 4

    # @pytest.mark.skip(reason='skip!')
    @pytest.mark.skipif(release_ver=='1.0.0', reason='skip!')
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')
