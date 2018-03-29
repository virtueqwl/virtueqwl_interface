# coding:utf-8
import unittest
import requests
from common.logger import Log


class CreateFeedTestCase(unittest.TestCase):
    '''发布帖子'''
    log = Log()

    def setUp(self):
        self.headers = {
            "Accept-Encoding": "gzip", "Connection": "Keep-Alive", "Content-Length": "88",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "testapi.mrpyq.com", "mpc-mac": "b4%3A0b%3A44%3A28%3A1a%3A72", "mpc-network": "wifi",
            "mpc-os": "19", "mpc-token": "352621066334654", "mpc-type": "G9006V", "mpc-ver": "3.1.1",
            "User-Agent": "MingPeng/3.1.1"}

        self.url = "https://testapi.mrpyq.com/feed/create"
        self.content = "3月22日上午，广东省广州市中级人民法院公开开庭审理原告广东省消费者委员会" \
                       "（下简称“省消委会”）诉被告广州悦骑信息科技有限公司（下简称“悦骑公司”）" \
                       "民事公益诉讼案。原告省消委会认为，" \
                       "被告悦骑公司在“小鸣单车”经营管理过程中侵害众多不特定消费者的合法权益，" \
                       "依法向广州中院提起消费民事公益诉讼。这是全国首例共享单车民事公益诉讼案。" \
                       "本案由广州中院副院长蒋耀庭担任审判长，" \
                       "由3名法官和2名人民陪审员组成合议庭进行公开开庭审理，庭审全程进行了网络庭审直播。"
        # 12345678900
        self.data = {
            "access_token": "5aaa48281893be6a5ceee5fb.1553073874.43a514f7fb0cecd5a491d98643eb6e3b",
            "roomid": "551e51f8fbe78e6c02be1d89",
            "userid": "55040c10fbe78e5c14de4aa5",
            "tid": "0",
            "content": self.content,
            "copyright": "true"}

    def testcreatefeed(self):
        '''测试发帖'''
        # 发帖热度要做判断
        r = requests.post(self.url, headers=self.headers, data=self.data)
        result = r.json()
        feed = result["feed"]
        print(feed)
        print(feed["liked"])
        self.assertEqual("False", feed["liked"])


if __name__ == '__main__':
    unittest.main()

