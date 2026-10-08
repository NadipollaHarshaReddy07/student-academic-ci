import unittest

from student_result_logic import predict_result


class TestStudentResultLogic(unittest.TestCase):

    def test_pass_case(self):
        result = predict_result(70, 85)
        self.assertEqual(result, "PASS")

    def test_fail_due_to_marks(self):
        result = predict_result(30, 85)
        self.assertEqual(result, "FAIL")

    def test_fail_due_to_attendance(self):
        result = predict_result(70, 60)
        self.assertEqual(result, "FAIL")


if __name__ == "__main__":
    unittest.main()
