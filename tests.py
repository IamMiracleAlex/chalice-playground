from unittest import TestCase
from unittest.mock import patch
import random
import string

from chalice.test import Client
from app import app, periodic_task

from section_one import calculator, Users


class CalculatorTest(TestCase):
    def setUp(self):
        self.first = 10
        self.second = 20

    def test_addition(self):
        '''Assert that addition works as expected'''

        actual = self.first + self.second
        result = calculator(a=self.first, b=self.second, operator="add")
        self.assertEqual(actual, result)

    def test_subtraction(self):
        '''Assert that subtraction works'''

        actual = self.first - self.second
        result = calculator(a=self.first, b=self.second, operator="-")
        self.assertEqual(actual, result)

    def test_multiplication(self):
        '''Assert that multiplication works'''

        actual = self.first * self.second
        result = calculator(a=self.first, b=self.second, operator="*")
        self.assertEqual(actual, result)

    def test_division(self):
        '''Assert that division works as expected'''

        actual = self.first / self.second
        result = calculator(a=self.first, b=self.second, operator="divide")    



class UsersTest(TestCase):

    def setUp(self):
        self.password = "".join(random.sample(string.ascii_lowercase, 8))
        self.username = "".join(random.sample(string.ascii_lowercase, 4))

    def test_users(self):
        '''Assert that users are stored and passwords can be retrieved'''

        # store user and password
        users = Users()
        users.store_users(username=self.username, password=self.password)

        # search for password
        found_password = users.verify_password(password=self.password)

        # assert password was found
        self.assertEqual(self.password, found_password)
        

class PeriodicTaskTest(TestCase):

    def test_periodic_task(self):
        '''Test periodic task'''

        result = None
        actual = {"success": "true"}

        # mock api get request
        with patch('app.requests.get') as get_request:
            get_request.json.return_value = {
                    "data": {
                        "totalSamplesTested": "1977,479",
                        "totalConfirmedCases": 165515,
                        "totalActiveCases": 7092,
                        "discharged": 156358,
                        "death": 2065,
                        "states": [{
                            "state": "Lagos",
                            "_id": "D-Ynje52j",
                            "confirmedCases": 58615,
                            "casesOnAdmission": 1186,
                            "discharged": 56990,
                            "death": 439
                        }, {
                            "state": "Kogi",
                            "_id": "MeIgm9TSJ3K",
                            "confirmedCases": 5,
                            "casesOnAdmission": 0,
                            "discharged": 3,
                            "death": 2
                        }]
                    }
                }

            # mock boto3 resource    
            with patch('app.boto3.resource') as upload_file:  
                upload_file.Bucket.upload_file.return_value = None

                # mock boto3 client
                with patch('app.boto3.client') as upload_to_dynamodb:

                    upload_to_dynamodb.put_item.return_value = None 

                    # mock aws event
                    event={'version': '2.0',
                            'account': 'AWS_ACCOUNT',
                            'region': 'us-east-1',
                            'detail': {},
                            'detail-type': 'dict',
                            'source': 'AWS',
                            'time': '2020-05-13',
                            'id': 2,
                            'resources': 'resources',
                            }
                    result  = periodic_task(event=event, context={})

        # assert the result is accurate
        self.assertEqual(actual, result)


if __name__ == '__main__':
    unittest.main()