import os
import pprint

from klov_reports import Reports


class TestClass1:

    def test_method1(self):
        print("")
        print("********************** ")
        print("This is Test Method")
        print("This is Test Method 123")
        print("********************** ")
        print(" ")

        # obj = Reports("PythonTestProject", "MyPythonReport", "172.29.1.77", 27017, "http://localhost:8080")
        # obj.init_extent_test("TC0014")
        # obj.add_system_info("Window 10 Pro", "QA ", "NARESH KUMAR")
        # obj.testcase_result("Pass", "", "")
        # obj.info_log("My testcase Test001 is Passed Now Great !!!! ")
        # obj.flush_report()
        # obj.shutdown_JVM()

        print("This is My Env Varibles")
        env_var = os.environ
        # print(os.environ['sky'])
        # print(os.environ['M3_HOME'])
        # print(os.environ['nky'])
        pprint.pprint(dict(env_var), width=1)
        print("   ")
        print("   ")
        print("   ")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("   ")
        print("   ")
        print(os.environ['JAVA_HOME'])

        print("   ")
        print("   ")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")