# import sys
# import os
# import time
#
# from HTMLTestRunnerNew import HTMLTestRunner
#
# curPath = os.path.abspath(os.path.dirname(r'C:\Users\Administrator\PycharmProjects\autosuyuansys\run\discover.py'))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)
#
#
# import unittest
# class pao():
#     def run(self) -> object:
#
#         test_dir = r'./'
#         discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
#         return discover
#
# if __name__ == '__main__':
#     a=pao()
#     b=a.run()
#     runner = unittest.TextTestRunner()
#     runner.run(b)



import sys
import os
curPath = os.path.abspath(os.path.dirname(r'C:\Users\Administrator\PycharmProjects\autosuyuansys\run\discover.py'))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest
from HTMLTestRunnerNew import HTMLTestRunner
import time



def run():
   reportpath = "../report"
   test_dir = './'
   suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test_*.py')
   now = time.strftime('%Y-%m-%d_%H_%M_%S')
   reportname = reportpath + '\\' + 'TestResult' + now + '.html'
   with open(reportname, 'wb') as f:
      runner = HTMLTestRunner(
         stream=f,
         title='测试报告',
         verbosity = 2,
         tester = "寇旭珂",
         description='Test the import testcase'
      )
      runner.run(suite)
   time.sleep(1)



if __name__ == '__main__':

   run()