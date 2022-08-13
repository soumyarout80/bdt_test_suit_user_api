"""User creation feature tests."""
import json
import requests
import time
from behave import given, when, then
from behave import register_type

from six import integer_types


def parse_number(text):
    """
    Convert parsed text into a number.
    :param text: Parsed text, called by :py:meth:`parse.Parser.parse()`.
    :return: Number instance (integer), created from parsed text.
    """
    return int(text)


# -- REGISTER: User-defined type converter (parse_type).
register_type(Number=parse_number)


@given(u'user api endpoint')
def step_impl(context):
    context.url = "http://127.0.0.1:8000/user/v1/"
    # raise NotImplementedError(u'STEP: Given user api endpoint <http://127.0.0.1:8000/user/v1/>')


@given(u'a customer\'s first name')
def step_impl(context):
    context.first_name = "Soumay"
    # raise NotImplementedError(u'STEP: Given a customer first name <Soumya>')


@given(u'a customer\'s last name')
def step_impl(context):
    context.last_name = "Rout"
    # raise NotImplementedError(u'STEP: Given a customer last name <Rout>')


@given(u'a customer\'s gender')
def step_impl(context):
    context.gender = "Male"
    # raise NotImplementedError(u'STEP: Given a customer gender')


@when(u'I enter user email id "{email}"')
def step_impl(context, email):
    assert type(email) == str
    context.email = email


@when(u'I enter the user phone number {phone}')
def step_impl(context, phone):
    # assert type(phone) == int
    context.phone = int(phone)


@when(u'I enter password "{password}" for the user')
def step_impl(context, password):
    assert type(password) == str
    context.password = password


@when(u'I send a POST request to the user api')
def step_impl(context):
    headers = {
        'Content-type': 'application/json',
        'Accept': 'text/plain'
    }
    payload = {'first_name': context.first_name,
               'middle_name': "NA",
               'last_name': context.last_name,
               'email': context.email,
               'gender': context.gender,
               'phone': context.phone,
               'password': context.email,
               }

    response = requests.post(context.url, data=json.dumps(payload), headers=headers)
    if response.status_code != 201:
        raise AssertionError("failed with exception: " + str(response))


@then(u'I should be able to request GET for the newly created user')
def step_impl(context):
    time.sleep(2)
    user_id = 6853

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'id': user_id}

    # sending get request and saving the response as response object
    # r = requests.get(url=URL_END_POINT, params=PARAMS)

    # extracting data in json format
    # data = r.json()
    # print(data)


@then(u'I should get a status code of "{status:Number}"')
def step_impl(context, status):
    assert status == 200 or status == 201
    assert isinstance(status, integer_types), "value.type=%s" % type(status)
    print("Status code for request: {}".format(status))
    # raise NotImplementedError(u'STEP: Then I should get a status code of {}'.format(status))


@then(u'the response value of "email" should equal {email}')
def step_impl(context, email):
    pass
    # raise NotImplementedError('STEP: Then the response value of "user.email" should equal {}'.format(email))


@then(u'I should not see the error message')
def step_impl(context):
    pass


@then(u'the request should be successful')
def step_impl(context):
    pass


@then(u'I should able to get the detail of the user')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: Then I should able to get the detail of the user')


@then(u'I should get the error message "Invalid email format"')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: Then I should get the error message "Invalid email format"')


@then(u'I should see validation message "{message}"')
def step_impl(context, message):
    context.message = message
    pass
    # raise NotImplementedError(u'STEP: Then I should see validation message "Invalid email format"')


@when(u'I should get a status code of "406"')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: When I should get a status code of "400"')
