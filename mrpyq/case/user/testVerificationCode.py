# coding:utf-8
import unittest, requests
from common.logger import Log

class MyTestCase(unittest.TestCase):
    log = Log()

    def setUp(self):
        self.headers = {"Accept-Encoding": "gzip", "Connection": "Keep-Alive",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Host": "testapi.mrpyq.com", "mpc-mac": "cc%3Aa2%3A23%3Aa4%3A41%3A33", "mpc-network": "none",
                        "mpc-os": "19", "mpc-token": "865166020012616", "mpc-type": "HUAWEI+MT7-TL00", "mpc-ver": "3.1.0",
                        "User-Agent": "MingPeng/3.1.0"}
        self.data = {"access_token": "", "phone_areacode": "+86"}
        self.url = "https://testapi.mrpyq.com/pass/send_phone_code_new"


    def test_VerificationCode_Register(self):
        '''注册页面测试获取验证码'''
        self.headers["Content-Length"] = "63"
        self.data["phone"] = 18872215422
        self.data["action"] = "reg"
        r = requests.post(self.url, headers=self.headers, data=self.data)
        print(r.content)
        result = r.json()
        print(result)
        # 断言：测试结果与期望结果对比
        self.assertEqual(result["result"], 1, msg='验证码发送失败')

    def test_VerificationCode_Login(self):
        '''免密登陆页面测试获取验证码'''
        self.headers["Content-Length"] = "65"
        self.data["phone"] = 13510405322
        self.data["action"] = "login"
        r = requests.post(self.url, headers=self.headers, data=self.data)
        print(r.content)
        result = r.json()
        print(result)
        # 断言：测试结果与期望结果对比
        self.assertEqual(result["result"], 1, msg='验证码发送失败')


if __name__ == '__main__':
    unittest.main()
