'''
import mock, unittest, requests
class Num:
    def __init__(self, number):
        self.number = number
class Exponential2(Num):
    def run(self):
        return int(self.number**2)



class TestExponential2(unittest.TestCase):
    def test_run(self):
        mock_func = mock.Mock()
        mock_func.return_value = 3
        with mock.patch.object(Exponential2, 'run', mock_func):
            check = Exponential2(number=3).run()
            self.assertEqual(3, check)

        with mock.patch.object(Exponential2, 'run') as mock_func:
            mock_func.return_value = 4
            check = Exponential2(number=3).run()
            self.assertEqual(4, check)
        
        with mock.patch.object(requests, 'get') as get_mock:
            get_mock.return_value = 200
            self.assertTrue(requests.get("valid_endpoint") == 200)

if __name__ == "__main__":
    unittest.main()
    '''