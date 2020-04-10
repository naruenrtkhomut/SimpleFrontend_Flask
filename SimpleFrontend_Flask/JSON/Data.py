import json, urllib.request

class Data_JSON_URL:
    def URL_LINK_DATA(Url_Link):
        JSON_DATA = urllib.request.urlopen(Url_Link)
        JSON_GET_DATA = json.loads(JSON_DATA.read().decode())
        return JSON_GET_DATA
    
class GetData:
    def Model():
        return Data_JSON_URL.URL_LINK_DATA('https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimpleModelTypeValue.json')
    def ModelGroup():
        return Data_JSON_URL.URL_LINK_DATA('https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimpleModelTypeList.json')
    def Social():
        return Data_JSON_URL.URL_LINK_DATA('https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimpleSocial.json')
    def PhoneNumber():
        return Data_JSON_URL.URL_LINK_DATA('https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimplePhoneNumber.json')
    def LatestOrder():
        return Data_JSON_URL.URL_LINK_DATA('https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimpleLatestOrder.json')
    def HotestOrder():
        return Data_JSON_URL.URL_LINK_DATA('https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimpleHotestOrder.json')
    def Payment():
        return Data_JSON_URL.URL_LINK_DATA('https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimplePayment.json')
    def Order():
        return Data_JSON_URL.URL_LINK_DATA('https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimpleOrderName_Value.json')
    def ModelName():
        return Data_JSON_URL.URL_LINK_DATA('https://raw.githubusercontent.com/naruenrtkhomut/SimpleJsonData/master/SimpleModelNameList.json')
