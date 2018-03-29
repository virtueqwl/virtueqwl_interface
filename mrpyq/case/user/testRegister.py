# coding:utf-8
import unittest
import requests
from common.logger import Log
class RegisterTestCase(unittest.TestCase):
    u'''注册'''
    log = Log()

    def setUp(self):
        self.headers = {"Accept-Encoding": "gzip", "Connection": "Keep-Alive",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Host": "testapi.mrpyq.com", "mpc-mac": "68%3Aa0%3Af6%3A08%3Ae3%3A95", "mpc-network": "wifi",
                        "mpc-os": "19", "mpc-token": "A000004F7372FA", "mpc-type": "C8817D", "mpc-ver": "3.1.0",
                        "User-Agent": "MingPeng/3.1.0"}
        self.data = {"access_token": "", "action": "phone_verifycode_reg", "userid": "", "v": "3.1.0",
                     "type": "android",  "token": "A000004F7372FA", "phone_areacode": "+86",
                     "channel": "main"}
        self.url = "https://testapi.mrpyq.com/pass/reg"


    def testRegister_01(self):
        u'''测试注册（已注册号码，正确验证码）'''
        self.headers["Content-Length"] = "548"
        self.data["phone"] = 135104053223
        self.data["code"] = 20177

        r = requests.post(self.url, headers=self.headers, data=self.data)
        print(r.content)
        result = r.json()
        print(result["error"])
        print(result["error_code"])
        # 断言：测试结果与期望结果对比
        self.assertEqual(u"该手机账号已经注册", result["error"], msg='已经注册')
        self.assertEqual(-1, result["error_code"])

    def testRegister_02(self):
        u'''测试注册（已注册号码，错误验证码）'''
        self.headers["Content-Length"] = "548"
        self.data["phone"] = 135104053223
        self.data["code"] = 12345
        url = "https://testapi.mrpyq.com/pass/reg"
        r = requests.post(url, headers=self.headers, data=self.data)
        print(r.content)
        result = r.json()
        print(result["error"])
        # 断言：测试结果与期望结果对比
        self.assertEqual(u"该手机账号已经注册", result["error"], msg='已经注册')

    def testRegister_03(self):
        '''测试注册（未注册号码，正确验证码）'''
        self.headers["Content-Length"] = "548"
        self.data["phone"] = 135104053223
        self.data["code"] = 20177
        url = "https://testapi.mrpyq.com/pass/reg"
        r = requests.post(url, headers=self.headers, data=self.data)
        print(r.content)
        result = r.json()
        print(result["error"])
        # 断言：测试结果与期望结果对比
        self.assertEqual(u"该手机账号已经注册", result["error"], msg='已经注册')

    def testRegister_04(self):
        u'''测试注册（未注册号码，万能验证码）'''
        self.headers["Content-Length"] = "548"
        self.data["phone"] = 135104053223
        self.data["code"] = 20177
        url = "https://testapi.mrpyq.com/pass/reg"
        r = requests.post(url, headers=self.headers, data=self.data)
        print(r.content)
        result = r.json()
        print(result["error"])
        # 断言：测试结果与期望结果对比
        self.assertEqual(u"该手机账号已经注册", result["error"], msg='已经注册')

    def testRegister_05(self):
        u'''测试注册（未注册号码，错误验证码）'''
        self.headers["Content-Length"] = "548"
        self.data["phone"] = 135104053223
        self.data["code"] = 20177
        url = "https://testapi.mrpyq.com/pass/reg"
        r = requests.post(url, headers=self.headers, data=self.data)
        print(r.content)
        result = r.json()
        print(result["error"])
        # 断言：测试结果与期望结果对比
        self.assertEqual(u"该手机账号已经注册", result["error"], msg='已经注册')



if __name__ == '__main__':
    unittest.main()
