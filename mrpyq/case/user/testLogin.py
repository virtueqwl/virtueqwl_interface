
# coding:utf-8
import unittest
import requests
from common.logger import Log

class LoginTestCase(unittest.TestCase):
    '''登陆'''
    log = Log()

    def setUp(self):
        self.headers = {"Accept-Encoding": "gzip", "Connection": "Keep-Alive",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Host": "testapi.mrpyq.com", "mpc-mac": "68%3Aa0%3Af6%3A08%3Ae3%3A95", "mpc-network": "wifi",
                        "mpc-os": "19", "mpc-token": "A000004F7372FA", "mpc-type": "C8817D", "mpc-ver": "3.1.0",
                        "User-Agent": "MingPeng/3.1.0"}
        self.data = {"access_token": " ", "userid": "", "v": "3.1.0",
                     "type": "android",  "phone_areacode": "+86","channel": "main"}
        self.url = "https://testapi.mrpyq.com/pass/reg"

    def testLogin_01(self):
        '''测试登陆（已注册号码，正确验证码）'''
        self.log.info("------测试登陆（已注册号码，正确验证码）：start!---------")
        self.data["action"] = "phone_verifycode_login"
        self.data["phone"] = 18872215422
        self.data["code"] = 20177
        self.log.info("------输入已注册号码：%s ,验证码: %s 。"%(self.data["phone"],self.data["code"]))
        r = requests.post(self.url, headers=self.headers, data=self.data)
        print(r.content)
        result = r.json()
        print(result["user"])
        user = result["user"]
        print(result["user"])
        # 断言：测试结果与期望结果对比
        self.assertEqual(True, user["me"], msg='验证码登陆失败')
        self.log.info("获取测试结果：%s" % user["me"])
        self.log.info("----------pass!-------")
    # self.log.info("------测试登陆（已注册号码，正确验证码）：start!---------")
    # self.log.info("------输入已注册号码：%s ,验证码: %s 。" % (self.data["phone"], self.data["code"]))
    # self.log.info("获取测试结果：%s" % user["me"])
    # self.log.info("----------pass!-------")

    def testLogin_02(self):
        '''测试登陆（已注册号码，错误验证码）'''
        self.log.info("------测试登陆（已注册号码，错误验证码）：start!---------")
        self.data["action"] = "phone_verifycode_login"
        self.data["phone"] = 18872215422
        self.data["code"] = 12345
        self.log.info("------输入已注册号码：%s ,验证码: %s 。" % (self.data["phone"], self.data["code"]))
        r = requests.post(self.url, headers=self.headers, data=self.data)
        print(r.content)
        result = r.json()
        print(result["error"])
        print(result["error_code"])
        # 断言：测试结果与期望结果对比
        self.assertEqual(u"该手机验证码不正确或已使用过", result["error"], msg='验证码登陆失败')
        self.assertEqual(-1, result["error_code"], msg='验证码登陆失败')
        self.log.info("获取测试结果：%s" % result["error"])
        self.log.info("----------pass!-------")

    def testLogin_03(self):
        '''测试登陆（已注册号码，正确密码）'''
        self.log.info("------测试登陆（已注册号码，正确密码）：start!---------")
        self.data["action"] = "phone_login"
        self.data["phone"] = 18872215422
        self.data["password"] = 13114328435
        self.log.info("------输入已注册号码：%s ,正确密码: %s 。" % (self.data["phone"], self.data["password"]))
        r = requests.post(self.url, headers=self.headers, data=self.data)
        print(r.content)
        result = r.json()
        user = result["user"]
        print(result["user"])

        # 断言：测试结果与期望结果对比
        self.assertEqual(True, user["me"], msg='密码登陆失败')
        self.log.info("获取测试结果：user{me:} = %s" % user["me"])
        self.log.info("----------pass!-------")

    def testLogin_04(self):
        '''测试登陆（已注册号码，错误密码）'''
        self.log.info("------测试登陆（已注册号码，错误密码）：start!---------")
        self.data["action"] = "phone_login"
        self.data["phone"] = 18872215422
        self.data["password"] = 13114328433
        self.log.info("------输入已注册号码：%s ,错误密码: %s 。" % (self.data["phone"], self.data["password"]))
        r = requests.post(self.url, headers=self.headers, data=self.data)
        print(r.content)
        result = r.json()
        print(result["error"])
        print(result["error_code"])
        # 断言：测试结果与期望结果对比
        self.assertEqual(u"您的手机号或密码不正确", result["error"], msg='验证码登陆失败')
        self.assertEqual(-1, result["error_code"], msg='验证码登陆失败')
        self.log.info("获取测试结果：error = %s,error_code = %s" % (result["error"],result["error_code"]))
        self.log.info("----------pass!-------")




if __name__ == '__main__':
    unittest.main()
