import unittest
import assignment_seven


class MyTestCase(unittest.TestCase):

    def test_encode_one(self):
        self.assertEqual("sbwkrq", assignment_seven.encode("python", 3))
        self.assertEqual("bgdtc", assignment_seven.encode("zebra",2))

    # def test_encode_two(self):
    #     self.assertEqual("wcescjdpek", assignment_seven.encode("hello world", "python"))
    #
    # def test_option_three(self):
    #     pass



if __name__ == '__main__':
    unittest.main()
