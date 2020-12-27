import unittest
from nate_auto import auto_sending as aus

class TestEnd2end(unittest.TestCase):
    
    # def setUp(self)
        # self.macro  = aus.send_auto()

    def test_execute(self):
        self.macro  = aus.send_auto()
        self.assertEqual(0, self.macro.start() )

if __name__ == "__main__":
    unittest.main()