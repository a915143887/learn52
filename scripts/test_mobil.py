import app
import json
import utils
import requests
import requests
import unittest
from api.mobile_api import mobile_api


class mobile(unittest.TestCase):
    #前置处理
    def setUp(self):
        self.mobile_api = mobile_api()
        self.session = requests.session()
    #后置处理
    def tearDown(self):
        self.session.close()

    def test001_index(self):
        #请求参数
        request_data = {}
        #对参数加密
        diyou = utils.EncryptUtil.get_diyou(request_data)
        xdmy = utils.EncryptUtil.get_xmdy(diyou)
        #发送请求
        response = self.session.post(url=self.mobile_api.index_url, data={"diyou":diyou, "xmdy":xdmy})
        print("加密的响应数据：{}".format(response.json()))
        #获取响应数据并解密
        diyou = response.json().get("diyou")
        disclocse_data = utils.EncryptUtil.decrypt_data(diyou)
        #将JSON字符串转换成字典
        data = json.loads(disclocse_data)
        print("解密的响应数据：{}".format(data))
        self.assertEqual(200, data.get("code"))
        self.assertEqual("success", data.get("result"))

    def test002_index(self):
        data = utils.encryption_and_disclocse(self.session, url=self.mobile_api.index_url, r_data={})
        self.assertEqual(200, data.get("code"))
        self.assertEqual("success", data.get("result"))

    def test003_login(self):
        #请求参数
        requests_data = {"member_name": "13012345678", "password": "test123"}
        #对请求参数加密
        diyou = utils.EncryptUtil.get_diyou(requests_data)
        xmdy = utils.EncryptUtil.get_xmdy(diyou)
        #发送加密的请求
        response = self.session.post(url=self.mobile_api.login_url, data={"diyou": diyou, "xmdy": xmdy})
        print("加密的响应数据：{}".format(response.json()))
        #获取响应数据并解密
        diyou = response.json().get("diyou")
        disclocse_data = utils.EncryptUtil.decrypt_data(diyou)
        #把JSON字符串转换成字典
        data = json.loads(disclocse_data)
        print("解密的响应数据：{}".format(data))
        self.assertEqual(200, data.get("code"))
        self.assertEqual("success", data.get("result"))
