import allure

from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


@allure.epic('Registration cases')
class TestUserRegister(BaseCase):
    @allure.description('This test checks that the user has successfully registered')
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post('/user/', data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, 'id')

    @allure.description('This test checks for user registration with an existing email address')
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post('/user/', data=data)

        Assertions.assert_code_status(response, 400)
        assert (response.content.decode('utf-8') ==
                f"Users with email '{email}' already exists"), f'Unexpected response content {response.content}'
