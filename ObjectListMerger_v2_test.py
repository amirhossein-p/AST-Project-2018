
import unittest
import ObjectListMerger_v1 as code

class testCase(unittest.TestCase):
    """Tests for ObjectListMerger_v1.py"""
    def test_getInput(self):
        #test 1 ---> resulted in failure
        input1 = [['knife',1, 99], ['scissor', 2, 65], ['fork', 3, 33], ['spoon', 4, 80], ['keys', 5, 95]]
        self.assertEqual(code.getInput(1,input1)[0].dataNum, 1) #should be from input1
        self.assertNotEqual(code.getInput(1,input1)[0].objName, 'spoon') #should be knife
        self.assertEqual(code.getInput(1,input1)[0].objNum, 1) #should be 1
        self.assertNotEqual(code.getInput(1,input1)[0].prec, 100) #should be 99


        #test 2 ---> success
        input2 = [['scissor',1, 99], ['spoon', 2, 65], ['keys', 3, 33], ['spoon', 4, 80], ['knife', 5, 95]]
        self.assertEqual(code.getInput(2,input2)[0].dataNum, 2) #should be from input2
        self.assertEqual(code.getInput(2,input2)[0].objName, 'scissor') #should be scissor
        self.assertEqual(code.getInput(2,input2)[0].objNum, 1) #should be 1
        self.assertEqual(code.getInput(2,input2)[0].prec, 99) #should be 99

    def test_selector(self):
        #test 1 --->failure
        input1 = [['knife',1, 99], ['scissor', 2, 65], ['fork', 3, 33], ['spoon', 4, 80], ['keys', 5, 95]]
        input2 = [['knife',1, 55], ['scissor', 2, 95], ['fork', 3, 99], ['spoon', 4, 99], ['keys', 5, 95] ]
        in1 = code.getInput(1,input1)
        in2 = code.getInput(2,input2)
        self.assertNotEqual(code.selector(in1[0], in2[0]).prec, 55) #data selected should have the highest precision
        self.assertNotEqual(code.selector(in1[0], in2[0]).dataNum, 2) #data from input 1 should be selected

        #test 2 ---> success
        input1 = [['knife',1, 20], ['scissor', 2, 99], ['fork', 3, 25], ['spoon', 4, 80], ['keys', 5, 95]]
        input2 = [['knife',1, 55], ['scissor', 2, 95], ['fork', 3, 99], ['spoon', 4, 70], ['keys', 5, 95] ]
        in1 = code.getInput(1,input1)
        in2 = code.getInput(2,input2)
        self.assertEqual(code.selector(in1[4], in2[4]).prec, 95) #data selected should have the highest precision
        self.assertEqual(code.selector(in1[4], in2[4]).dataNum, 1) #data from input 1 should be selected

if __name__ == '__main__':
    unittest.main()
