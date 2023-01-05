import unittest
import main

class TestMain(unittest.TestCase):
    def test_PDA(self):
        good_samples = ['000111111111111','01111','0'*100+'1'*400,'0'*101+'1'*404,'0'*1000+'1'*4000]
        bad_samples = ['11','10000','0'*100+'1'*401,'0'*1000+'1'*3999,'0'*10+'1'*46+'0']
        for sample in good_samples:
            result = main.PDA(sample, print_output = False)
            self.assertEqual(result, 0)
        for sample in bad_samples:
            result = main.PDA(sample, print_output = False)
            self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main() # To run the tests directly, instead of python3 -m unittest test_main.py