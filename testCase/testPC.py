import unittest
import requests
from common.configApi import API,ZS
from common.configLogin import Login

class PC(unittest.TestCase):
    def test_search(self):
        url =API.work_url+ZS.pending_task_list
        print(url)
        headers = {"Content-Type": "application/json", "charset": "UTF-8"}
        data = {"appId":"35859","tableId":1716207,"bizCondition":"{\"processCode\":\"3zg6sbhu22g000\",\"queryType\":1,\"status\":1}","workSheetCondition":"[]","repeatCondition":"[]","pageNum":1,"pageSize":10}
        res = Login.workLogin(self)
        response = res.post(url=url, data=data, headers=headers)
        print(response)


# if __name__ == '__main__':
#     PC.test_search()