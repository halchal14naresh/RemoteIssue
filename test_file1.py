from klov_reports import Reports


class TestClass1:

    def test_method1(self):
        print("")
        print("********************** ")
        print("This is Test Method")
        print("This is Test Method 123")
        print("********************** ")
        print(" ")

        obj = Reports("PythonTestProject", "MyPythonReport", "172.29.1.77", 27017, "http://172.29.1.77:8443")
        obj.init_extent_test("TC0014")
        obj.add_system_info("Window 10 Pro", "QA ", "NARESH KUMAR")
        obj.testcase_result("Pass", "", "")
        obj.info_log("My testcase Test001 is Passed Now Great !!!! ")
        obj.flush_report()
        obj.shutdown_JVM()
