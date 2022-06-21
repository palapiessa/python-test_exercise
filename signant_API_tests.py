import unittest
import signant_API_calls

class TestAPI(unittest.TestCase):
    # Token fetched after first test case: 
    # curl -u web-user:rasti http://localhost:8080/api/auth/token
    auth_headers = {
        'content-type': "application/json",
        'token': "MjkzNDI5MjU0NzA5OTAwNjA1MTE5MzAwOTgyMDU0NTA5NTc5MzA2"
    }
    
    user1 = {
        "username": "JukkaK",
        "password": "rasti",
        "firstname": "Jukka",
        "lastname" : "Kivi",
        "phone" : "00512345"
    }

    user2 = {
        "username": "web-user",
        "password": "rasti",
        "firstname": "hei",
        "lastname" : "moi",
        "phone" : "0001"
    }

    # As an API Consumer I can:
    # 1. Register new users
    def test_register_user(self):
       self.assertEqual(signant_API_calls.register_user(self.user1), 201)
       self.assertEqual(signant_API_calls.register_user(self.user2), 201)
       
    # 2. Review users registered in system
    def test_review_users(self):
        json_data = signant_API_calls.retrieve_users(self.auth_headers)
        users= json_data.get('payload')
        self.assertTrue('web-user' in users)
        self.assertTrue('JukkaK' in users)
        self.assertEqual(len(users), 2)

    # # 3. If authenticated I can get personal information of users
    def test_get_user_info(self):
        user_id = self.user1.get('username')
        json_data = signant_API_calls.retrieve_user_info(user_id, self.auth_headers)
        user_info = json_data.get('payload')
        self.assertEqual(self.user1.get('firstname'),user_info['firstname'])
        self.assertEqual(self.user1.get('lastname'),user_info['lastname'])
        self.assertEqual(self.user1.get('phone'),user_info['phone'])
        user_id = self.user2.get('username')
        json_data = signant_API_calls.retrieve_user_info(user_id, self.auth_headers)
        user_info= json_data.get('payload')
        self.assertEqual(self.user2.get('firstname'),user_info['firstname'])
        self.assertEqual(self.user2.get('lastname'),user_info['lastname'])
        self.assertEqual(self.user2.get('phone'),user_info['phone'])
    
    # 4. If authenticated I can update personal information of users
    def test_update_user_info(self):
        user_new = {
            "firstname": "Jouko",
            "lastname" : "Talo",
            "phone" : "04012345"
        }
        user_id = self.user2.get('username')
        signant_API_calls.update_user_info(user_id, self.auth_headers, user_new)
        json_data = signant_API_calls.retrieve_user_info(user_id, self.auth_headers)
        user_info= json_data.get('payload')
        self.assertEqual(user_new.get('firstname'),user_info['firstname'])
        self.assertEqual(user_new.get('lastname'),user_info['lastname'])
        self.assertEqual(user_new.get('phone'),user_info['phone'])

if __name__ == '__main__':
    unittest.main()