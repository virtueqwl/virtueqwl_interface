# coding:utf-8
import unittest
from common.logger import Log
import requests
class RedPack(unittest.TestCase):
    log = Log()
    '''测试个人发送红包'''
    def setUp(self):
        self.headers = {
            'Accept-Encoding': 'gzip', 'Connection': 'Keep-Alive',
            'Content - Length': '336', 'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'testapi.mrpyq.com',
            'mpc-mac': 'F4%3A09%3AD8%3A10%3A10%3A83',
            'mpc-network': 'wifi',
            'mpc-os': '21',
            'mpc-token': '352621066334654',
            'mpc-type': 'SM-G9006V',
            'mpc-ver': '3.1.1',
            'User-Agent': 'MingPeng/3.1.1'}
        self.url = 'https://testapi.mrpyq.com/redpack/send'
        self.data = {
            'access_token': '5aaa48281893be6a5ceee5fb.1551867432.3bf5c9dbe7bb1d4f19a842d521a2d225',
            'selfno': '506',
            'userid': '55079785fbe78e632112d25f',
            'selfuserid': '55040c10fbe78e5c14de4aa5',
            'no': '1003',
            'total_amount': '1',
            'content': '恭喜发财，大吉大利!',
            'signature': 'b500d736-c2f6-439d-b2b3-7246ad73449d',
            'pack_type': '10'}

    def test_sendPack(self):
        '''sendPack'''
        self.log.info("发送红包")
        r = requests.post(self.url, headers=self.headers, data=self.data)
        result = r.json()
        print(result)
        # 断言：测试结果与期望结果对比
        # self.assertEqual(1, result["result"], msg="红包发送失败")
        # self.log.info("获取测试结果：result{'result'} = %d" % result['result'])
        # self.log.info("----------pass!-------")



if __name__ == '__main__':
    unittest.main()
