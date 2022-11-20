import os

from django.test import TestCase

from frontend.old.current_grades_dan import get_current_grades


class Test01(TestCase):
    def setUp(self):
        os.environ["AERIES_API_KEY"] = "477abe9e7d27439681d62f4e0de1f5e1"

    #
    # def test_current_grades01(self):
    #     api = Api("815", "ReportCard")
    #     out = api.get_current_grades_csv()
    #     print("Running test_current_grades")

    def test_current_grades02(self):
        get_current_grades(
            aeries_base_url='https://demo.aeries.net/aeries',
            aeries_api_token='477abe9e7d27439681d62f4e0de1f5e1',
            school_code='994',
            student_ids=['99400002'],
        )
