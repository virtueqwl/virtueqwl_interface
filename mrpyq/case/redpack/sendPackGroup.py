# coding:utf-8
import unittest
from common.logger import Log
import requests
class RedPack(unittest.TestCase):
    log = Log()
    '''测试群组发送红包'''
    def setUp(self):
        self.headers = {
            'Accept-Encoding': 'gzip',
            'Connection': 'Keep-Alive',
            'Content - Length': '264',
            'Content-Type': 'application/x-www-form-urlencoded',
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
            'access_token': '5aaa48281893be6a5ceee5fb.1551925110.e0f52f23a96b6d1939c7c38a23fbc81a',
            'selfno': '506',
            'total_count': '2',
            'selfuserid': '55040c10fbe78e5c14de4aa5',
            'total_amount': '2',
            'groupid': '5aab2cdb1893be081bdf0f02',
            'content': 'hello',
            'signature': '363fc865-3470-4074-a14c-fa57da725f4b',
            'pack_type': '20'}

    def test_sendPackGroup(self):
        '''sendGroupPack'''
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
