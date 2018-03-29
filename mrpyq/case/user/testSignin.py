# coding:utf-8
import unittest
import requests
from common.logger import Log
class SignInTestCase(unittest.TestCase):
    '''签到'''
    log = Log()

    def setUp(self):
        self.headers = {
            "Accept-Encoding": "gzip", "Connection": "Keep-Alive", "Content-Length": "88",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "testapi.mrpyq.com", "mpc-mac": "b4%3A0b%3A44%3A28%3A1a%3A72", "mpc-network": "wifi",
            "mpc-os": "19", "mpc-token": "352621066334654", "mpc-type": "G9006V", "mpc-ver": "3.1.1",
            "User-Agent": "MingPeng/3.1.1"}


        self.url = "https://testapi.mrpyq.com/member/signin"
        self.url2 = "https://testapi.mrpyq.com/mission/daily/signin"
        # 12345678900
        self.data = {"access_token": "5aaa48281893be6a5ceee5fb.1552805711.144a99fcf0051bfdbe6178e6f0afa2aa", "userid": "55040c10fbe78e5c14de4aa5"}
        self.data2 = {"access_token": "5aaa48281893be6a5ceee5fb.1552805711.144a99fcf0051bfdbe6178e6f0afa2aa"}

    def test_signin(self):
        '''角色签到'''
        r = requests.post(self.url, headers=self.headers, data=self.data)
        result = r.json()
        print(result)
        self.assertEqual(1, result["result"])

    def test_daily_signin(self):
        '''每日签到领圈币'''
        r = requests.post(self.url2, headers=self.headers, data=self.data2)
        result = r.json()
        print(result)




if __name__ == '__main__':
    unittest.main()
