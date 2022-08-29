import app
import json
import utils
import requests
import unittest
from api.mobile_api import mobile_api

class mobile(unittest.TestCase):
    session = None

    #前置处理
    @classmethod
    def setUpClass(cls):
        cls.mobile_api = mobile_api()
        cls.session = requests.session()
    #后置处理
    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    #首页
    def test001_index(self):
        #请求参数
        requests_data = {}
        #对参数加密
        diyou = utils.EncryptUtil.get_diyou(requests_data)
        xmdy = utils.EncryptUtil.get_xmdy(diyou)
        #发送参数加密的请求
        response = self.session.post(url=self.mobile_api.index_url, data={"diyou": diyou,"xmdy": xmdy})
        print("加密的响应数据：{}".format(response.json()))
        #获取响应数据并解密
        diyou = response.json().get("diyou")
        disclocse_data = utils.EncryptUtil.decrypt_data(diyou)
        #把JSON字符串转换成字典
        data = json.loads(disclocse_data)
        print("解密的响应数据：{}".format(data))
        self.assertEqual(200, data.get("code"))
        self.assertEqual("success", data.get("result"))

    #登录
    def test002_login(self):
        #请求参数
        requests_data = {"member_name": "13012345678", "password": "test123"}
        #对参数加密
        diyou = utils.EncryptUtil.get_diyou(requests_data)
        xmdy = utils.EncryptUtil.get_xmdy(diyou)
        #发送参数加密的请求
        response = requests.post(url=self.mobile_api.login_url, data={"diyou": diyou, "xmdy": xmdy})
        print("加密的响应数据：{}".format(response.json()))
        #获取响应数据并解密
        diyou = response.json().get("diyou")
        disclocse_data = utils.EncryptUtil.decrypt_data(diyou)
        #把JSON字符串转换成字典
        data = json.loads(disclocse_data)
        print("解密的响应数据：{}".format(data))
        self.assertEqual(200, data.get("code"))
        self.assertEqual("success", data.get("result"))
