# python-test_exercise
This repo is for exercise to create API and Robot Framework tests.
The instructions and the demo app can be found from: https://github.com/SH-interview/Flasky

Run tests against empty DB.
Fetch token after running first test case and add token to "auth_headers" class variable.

Run API tests from cmd-line:
- python -m unittest signant_API_tests.TestAPI.test_register_user
- python -m unittest signant_API_tests.TestAPI.test_review_users
- python -m unittest signant_API_tests.TestAPI.test_get_user_info
- python -m unittest signant_API_tests.TestAPI.test_update_user_info
