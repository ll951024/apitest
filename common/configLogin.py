import requests
class Login():
    def workLogin(self):
        data = '{"mobile":"13283719450","password":"059d38a8c888d5109fa33a9815866013","code":"","fp":"db04e8d4823c1978b16e5d2d6dfeb99e","fid":"","idaasCode":"","strongPassword":false}'
        headers = {"Content-Type": "application/json", "charset": "UTF-8"}
        url = "https://work.bytenew.com/v2/logins/unifiedLogin"
        res = requests.session()
        #res1 = res.post(url=url, data=data, headers=headers)
        return res
        # print(res1.text)
        # print(res1.headers)

        # url2 = "https://work.bytenew.com/v2/project/column/allColumn2/1110357/34913"
        #
        # res2 = res.get(url2)
        # print(res2.text)




