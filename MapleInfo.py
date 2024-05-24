import requests

headers = {
    "x-nxopen-api-key": "test_9392c67b8e3b9222db966f58be5b70297ee60e6180d5d3b6f11cae8d38de16ccefe8d04e6d233bd35cf2fabdeb93fb0d"
}


class MapleInfo:
    def __init__(self, characterName=None):
        self.ocid = self.getOcid(characterName)

    def getOcid(self, characterName=None):
        if characterName == None: return None
        self.characterName = characterName
        urlString = "https://open.api.nexon.com/maplestory/v1/id?character_name=" + characterName
        response = requests.get(urlString, headers=headers)

        return response.json()['ocid']

    def getBasicInfo(self, ocid=None, date=None):
        if ocid == None:
            return None
        urlString = "https://open.api.nexon.com/maplestory/v1/character/basic?ocid=" + ocid
        if date != None:
            urlString += "&date=" + date
        response = requests.get(urlString, headers=headers)
        self.basicInfo = response.json()

        return self.basicInfo


c1 = MapleInfo("아델")
c1.getBasicInfo(c1.ocid, '2024-01-01')

print(c1.basicInfo)
