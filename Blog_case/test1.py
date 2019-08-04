import unittest_1

class Test(unittest_1.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01(self):
        a = 6
        b = 7
        self.assertEqual(a,b)
        # return (a + b)

if __name__ == '__main__':
    unittest_1.main()