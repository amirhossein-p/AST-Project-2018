import unittest
import ObjectListMerger_v3 as code

class testCase(unittest.TestCase):
    """Tests for ObjectListMerger_v1.py"""
    def test_getInput(self):
        #test 1 ---> input1
        input1 = [("knife",1, 99), ("scissor", 2, 65), ("spoon", 3, 33), ("spoon", 4, 80), ("keys", 5, 95)]
        self.assertEqual(code.getInput(1,input1)[0].dataNum, 1) #should be from input1
        self.assertEqual(code.getInput(1,input1)[0].objName, 'knife') #should be knife
        self.assertEqual(code.getInput(1,input1)[0].objNum, 1) #should be 1
        self.assertEqual(code.getInput(1,input1)[0].prec, 99) #should be 99

        #test 1 ---> input2
        input2 = [ ("keys", 5, 95), ("spoon", 4, 99),("fork", 3, 99), ("scissor", 2, 95), ("knife",1, 55)]
        self.assertEqual(code.getInput(2,input2)[0].dataNum, 2) #should be from input2
        self.assertEqual(code.getInput(2,input2)[0].objName, 'keys') #should be keys
        self.assertEqual(code.getInput(2,input2)[0].objNum, 5) #should be 5
        self.assertEqual(code.getInput(2,input2)[0].prec, 95) #should be 95


        #test 2 ---> input1
        #throws error that list index is out of range
        input1 = []
        self.assertNotEqual(code.getInput(1,input1)[0].dataNum, 1)
        self.assertNotEqual(code.getInput(1,input1)[0].objName, 'knife')
        self.assertNotEqual(code.getInput(1,input1)[0].objNum, 1)
        self.assertNotEqual(code.getInput(1,input1)[0].prec, 99)

        #test 2 ---> input2
        input2 = []
        self.assertNotEqual(code.getInput(2,input2)[0].dataNum, 2)
        self.assertNotEqual(code.getInput(2,input2)[0].objName, 'keys')
        self.assertNotEqual(code.getInput(2,input2)[0].objNum, 5)
        self.assertNotEqual(code.getInput(2,input2)[0].prec, 99)



        #test 3 ---> input1
        input1 = [("knife",1, 99), ("scissor", 2, 65), ("spoon", 3, 33)]
        self.assertEqual(code.getInput(1,input1)[0].dataNum, 1)
        self.assertEqual(code.getInput(1,input1)[0].objName, 'knife')
        self.assertEqual(code.getInput(1,input1)[0].objNum, 1)
        self.assertEqual(code.getInput(1,input1)[0].prec, 99)

        #test 3 ---> input2
        input2 = []
        self.assertNotEqual(code.getInput(2,input2)[0].dataNum, 1)
        self.assertNotEqual(code.getInput(2,input2)[0].objName, 'keys')
        self.assertNotEqual(code.getInput(2,input2)[0].objNum, 5)
        self.assertNotEqual(code.getInput(2,input2)[0].prec, 99)


        #test 4 ---> input1
        input1 = [("knife",1, 99), ("scissor", 2, 65), ("spoon", 3, 33)]
        self.assertEqual(code.getInput(1,input1)[0].dataNum, 1)
        self.assertEqual(code.getInput(1,input1)[0].objName, 'knife')
        self.assertEqual(code.getInput(1,input1)[0].objNum, 1)
        self.assertEqual(code.getInput(1,input1)[0].prec, 99)

        #test 4 ---> input2
        input2 = [("KNIFE",1, 99), ("SCISSOR", 2, 65), ("SPOON", 3, 33)]
        self.assertEqual(code.getInput(2,input2)[0].dataNum, 2)
        self.assertEqual(code.getInput(2,input2)[0].objName, 'KNIFE')
        self.assertEqual(code.getInput(2,input2)[0].objNum, 1)
        self.assertEqual(code.getInput(2,input2)[0].prec, 99)



        #test 5 ---> input1
        input1 = [("knife",1, 99), ("scissor", 2, 65)]
        self.assertEqual(code.getInput(1,input1)[0].dataNum, 1)
        self.assertEqual(code.getInput(1,input1)[0].objName, 'knife')
        self.assertEqual(code.getInput(1,input1)[0].objNum, 1)
        self.assertEqual(code.getInput(1,input1)[0].prec, 99)

        #test 5 ---> input2
        input2 = [("fork", 3, 99), ("spoon", 4, 99)]
        self.assertEqual(code.getInput(2,input2)[0].dataNum, 2)
        self.assertEqual(code.getInput(2,input2)[0].objName, 'fork')
        self.assertEqual(code.getInput(2,input2)[0].objNum, 3)
        self.assertEqual(code.getInput(2,input2)[0].prec, 99)


        #test 6 ---> input1
        input1 = [("knife",1, 94),("knife",1, 69),("knife",1, 89)]
        self.assertEqual(code.getInput(1,input1)[0].dataNum, 1)
        self.assertEqual(code.getInput(1,input1)[0].objName, 'knife')
        self.assertEqual(code.getInput(1,input1)[0].objNum, 1)
        self.assertEqual(code.getInput(1,input1)[0].prec, 94)

        #test 6 ---> input2
        input2 = [("knife",1, 99),("fork", 3, 99)]
        self.assertEqual(code.getInput(2,input2)[0].dataNum, 2)
        self.assertEqual(code.getInput(2,input2)[0].objName, 'knife')
        self.assertEqual(code.getInput(2,input2)[0].objNum, 1)
        self.assertEqual(code.getInput(2,input2)[0].prec, 99)


    # def test_selector(self):
    #     #test 1
    #     #Should throw error because keys and knife are not the same. Development code should consider whether items being compared are the same items
    #     input1 = [("knife",1, 99), ("scissor", 2, 65), ("spoon", 3, 33), ("spoon", 4, 80), ("keys", 5, 95)]
    #     input2 = [ ("keys", 5, 95), ("spoon", 4, 99),("fork", 3, 99), ("scissor", 2, 95), ("knife",1, 55)]
    #     in1 = code.getInput(1,input1)
    #     in2 = code.getInput(2,input2)
    #     self.assertEqual(code.selector(in1[0], in2[0]).prec,99)
    #     self.assertEqual(code.selector(in1[0], in2[0]).dataNum, 1)
    #
    #     #test 2: Throws error that list index is out of range.
    #     input1 = []
    #     input2 = []
    #     in1 = code.getInput(1,input1)
    #     in2 = code.getInput(2,input2)
    #     self.assertNotEqual(code.selector(in1[0], in2[0]).prec,95)
    #     self.assertNotEqual(code.selector(in1[0], in2[0]).dataNum, 1)
    #
    #     #test 3:
    #     input1 = [("knife",1, 99), ("scissor", 2, 65), ("spoon", 3, 33)]
    #     input2 = []
    #     in1 = code.getInput(1,input1)
    #     in2 = code.getInput(2,input2)
    #     self.assertEqual(code.selector(in1[0], in2[0]).prec,99)
    #     self.assertEqual(code.selector(in1[0], in2[0]).dataNum, 1)
    #
    #
    #     #test 4:
    #     input1 = [("knife",1, 99), ("scissor", 2, 65), ("spoon", 3, 33)]
    #     input2 = [("KNIFE",1, 99), ("SCISSOR", 2, 65), ("SPOON", 3, 33)]
    #     in1 = code.getInput(1,input1)
    #     in2 = code.getInput(2,input2)
    #     self.assertEqual(code.selector(in1[0], in2[0]).prec,99)
    #     self.assertEqual(code.selector(in1[0], in2[0]).dataNum, 1)
    #
    #
    #
    #     #test 5: should throw error because the second input doesn't have knife to compare to.
    #     input1 = [("knife",1, 99), ("scissor", 2, 65)]
    #     input2 = [("fork", 3, 99), ("spoon", 4, 99)]
    #     in1 = code.getInput(1,input1)
    #     in2 = code.getInput(2,input2)
    #     self.assertEqual(code.selector(in1[0], in2[0]).prec,99)
    #     self.assertEqual(code.selector(in1[0], in2[0]).dataNum, 1)
    #
    #
    #     #test 6:
    #     input1 = [("knife",1, 94),("knife",1, 69),("knife",1, 89)]
    #     input2 = [("knife",1, 99),("fork", 3, 99)]
    #     in1 = code.getInput(1,input1)
    #     in2 = code.getInput(2,input2)
    #     self.assertEqual(code.selector(in1[0], in2[0]).prec,99)
    #     self.assertEqual(code.selector(in1[0], in2[0]).dataNum, 2)


#getoutput calls the selector function inside so this code below tests both functions.
    def test_getOutput(self):
        #test 1:
        input1 = [("knife",1, 99), ("scissor", 2, 65)]
        input2 = [("fork", 3, 99), ("spoon", 4, 99)]
        in1 = code.getInput(1,input1)
        in2 = code.getInput(2,input2)
        self.assertEqual(code.getOutput(in1,in2),[])



        #test 2:
        input1 = [("knife",1, 94),("knife",1, 69),("knife",1, 89)]
        input2 = [("knife",1, 99),("fork", 3, 99)]
        in1 = code.getInput(1,input1)
        in2 = code.getInput(2,input2)
        self.assertEqual(code.getOutput(in1,in2)[0].dataNum,2)


        #test 3:
        input1 = [("knife",1, 99), ("scissor", 2, 65), ("spoon", 3, 33), ("spoon", 4, 80), ("keys", 5, 95)]
        input2 = [ ("keys", 5, 95), ("spoon", 4, 99),("fork", 3, 99), ("scissor", 2, 95), ("knife",1, 55)]
        in1 = code.getInput(1,input1)
        in2 = code.getInput(2,input2)
        self.assertEqual(code.getOutput(in1,in2)[3].prec,99)
        self.assertEqual(code.getOutput(in1,in2)[3].objName,"spoon")

        #test 4:
        input1 = []
        input2 = []
        in1 = code.getInput(1,input1)
        in2 = code.getInput(2,input2)
        self.assertEqual(code.getOutput(in1,in2),[])



        #test 5:
        input1 = [("knife",1, 99), ("scissor", 2, 65), ("spoon", 3, 33)]
        input2 = []
        in1 = code.getInput(1,input1)
        in2 = code.getInput(2,input2)
        self.assertEqual(code.getOutput(in1,in2),[])



        #test 6:
        input1 = [("knife",1, 99), ("scissor", 2, 65), ("spoon", 3, 33)]
        input2 = [("KNIFE",1, 99), ("SCISSOR", 2, 65), ("SPOON", 3, 33)]
        in1 = code.getInput(1,input1)
        in2 = code.getInput(2,input2)
        self.assertEqual(code.getOutput(in1,in2)[0].dataNum,1)



        def test_multiSelect(self):
            #test 1:
            input11 = [['knife',1, 89]]
            input21 = [['knife',1, 35]]
            input21 = [['knife',1, 69]]
            input22 = [['knife',1, 80]]

            in11 = code.getInput(1,input11)
            in21 = code.getInput(2,input21)
            in12 = code.getInput(1,input12)
            in22 = code.getInput(2,input22)
            self.assertEqual(code.multiSelect([in11,in21,in12,in22])[0].data.prec,89)




if __name__ == '__main__':
    unittest.main()
