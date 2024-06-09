import requests

headers = {
    # 오현택
    # "x-nxopen-api-key": "test_9392c67b8e3b9222db966f58be5b70297ee60e6180d5d3b6f11cae8d38de16ccefe8d04e6d233bd35cf2fabdeb93fb0d"
    # 박우진
    "x-nxopen-api-key": "test_fcbb644b0795b15c260e79b797ec02e806a33c2ce838123d345055cccda69e185ac61399047147932c90a12d833bc382"
}


class MapleInfo:
    def __init__(self, name=None, date=None):
        self.setInfo(name, date)

    def setInfo(self, name=None, date=None):
        self.ocid = self.setOcid(name)
        if self.ocid == None:
            pass
        self.basic = self.setBasic(self.ocid, date)
        self.stat = self.setStat(self.ocid, date)
        self.hyperStat = self.setHyperStat(self.ocid, date)
        self.ability = self.setAbility(self.ocid, date)
        self.union = self.setUnion(self.ocid, date)
        self.Mu_Lung_Dojo = self.setMu_Lung_Dojo(self.ocid, date)
        self.popularity = self.setPopularity(self.ocid, date)


    def setOcid(self, name=None):
        if name == None: return None
        self.name = name
        urlString = "https://open.api.nexon.com/maplestory/v1/id?character_name=" + name
        response = requests.get(urlString, headers=headers)

        if response.status_code != 200:
            print("존재하지 않는 캐릭터명입니다.")
            return None

        return response.json()['ocid']

    def setBasic(self, ocid=None, date=None):
        if ocid == None:
            return None
        urlString = "https://open.api.nexon.com/maplestory/v1/character/basic?ocid=" + ocid
        if date != None:
            urlString += "&date=" + date
        response = requests.get(urlString, headers=headers)
        self.basic = response.json()

        return self.basic

    def setStat(self, ocid=None, date=None):
        if ocid == None:
            return None
        urlString = "https://open.api.nexon.com/maplestory/v1/character/stat?ocid=" + ocid
        if date != None:
            urlString += "&date=" + date
        response = requests.get(urlString, headers=headers)
        self.stat = response.json()

        return self.stat

    def setHyperStat(self, ocid=None, date=None):
        if ocid == None:
            return None
        urlString = "https://open.api.nexon.com/maplestory/v1/character/hyper-stat?ocid=" + ocid
        if date != None:
            urlString += "&date=" + date
        response = requests.get(urlString, headers=headers)
        self.hyperStat = response.json()

        return self.hyperStat

    def setAbility(self, ocid=None, date=None):
        if ocid == None:
            return None
        urlString = "https://open.api.nexon.com/maplestory/v1/character/ability?ocid=" + ocid
        if date != None:
            urlString += "&date=" + date
        response = requests.get(urlString, headers=headers)
        self.ability = response.json()

        return self.ability

    def setExpHistory(self):
        pass

    def setLevelHistory(self):
        pass

    def setUnion(self, ocid=None, date=None):
        if ocid == None:
            return None
        urlString = "https://open.api.nexon.com/maplestory/v1/user/union?ocid=" + ocid
        if date != None:
            urlString += "&date=" + date
        response = requests.get(urlString, headers=headers)

        return response.json()

    def setMu_Lung_Dojo(self, ocid=None, date=None):
        if ocid == None:
            return None
        urlString = "https://open.api.nexon.com/maplestory/v1/character/dojang?ocid=" + ocid
        if date != None:
            urlString += "&date=" + date
        response = requests.get(urlString, headers=headers)

        return response.json()

    def setPopularity(self, ocid=None, date=None):
        if ocid == None:
            return None
        urlString = "https://open.api.nexon.com/maplestory/v1/character/popularity?ocid=" + ocid
        if date != None:
            urlString += "&date=" + date
        response = requests.get(urlString, headers=headers)

        return response.json()

if __name__ == "__main__":
    c1 = MapleInfo("아델")

    print(c1.basic['character_exp_rate'])
    print(c1.stat)
    print(c1.hyperStat)
    print(c1.ability)
    print(c1.union)
    print(c1.Mu_Lung_Dojo)
    print(c1.popularity)
