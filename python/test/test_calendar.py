# coding: utf-8

"""
    P6 EPPM Rest API

    The Primavera P6 Enterprise Project Portfolio Management (P6 EPPM) API is a flexible interface to P6 EPPM functionality based on the Representational State Transfer (REST) architectural style. Clients can use HTTP enabled technologies to interact with the API and access application features. For example, you can write programs in Javascript, Java, and other languages to create users, view a list of users, update a user's status, or update user details.

    The version of the OpenAPI document: 2022.12.12
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.calendar import Calendar

class TestCalendar(unittest.TestCase):
    """Calendar unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Calendar:
        """Test Calendar
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Calendar`
        """
        model = Calendar()
        if include_optional:
            return Calendar(
                base_calendar_object_id = 56,
                create_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                create_user = '',
                hours_per_day = 1.337,
                hours_per_month = 1.337,
                hours_per_week = 1.337,
                hours_per_year = 1.337,
                is_baseline = True,
                is_default = True,
                is_personal = True,
                is_template = True,
                last_update_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_update_user = '',
                name = '',
                object_id = 56,
                project_id = '',
                project_object_id = 56,
                type = '',
                standard_work_week = openapi_client.models.standard_work_week.StandardWorkWeek(
                    standard_work_hours = [
                        openapi_client.models.standard_work_hours.StandardWorkHours(
                            day_of_week = '', 
                            work_time = [
                                openapi_client.models.work_time.WorkTime(
                                    finish = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], )
                        ], ),
                holiday_or_exceptions = openapi_client.models.holiday_or_exceptions.HolidayOrExceptions(
                    holiday_or_exception = [
                        openapi_client.models.holiday_or_exception.HolidayOrException(
                            date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            work_time = [
                                openapi_client.models.work_time.WorkTime(
                                    finish = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], )
                        ], )
            )
        else:
            return Calendar(
                name = '',
                type = '',
        )
        """

    def testCalendar(self):
        """Test Calendar"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
