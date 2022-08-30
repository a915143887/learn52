import unittest
from tools.HTMLTestRunner_PY3 import HTMLTestRunner
from scripts.test_mobil import mobile

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(mobile))

report = "./report/report.html"

with open(report, "wb") as e:
    runner = HTMLTestRunner(e, title="mobile测试报告")
    runner.run(suite)

