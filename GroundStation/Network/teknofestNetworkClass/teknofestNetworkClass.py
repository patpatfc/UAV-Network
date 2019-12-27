import requests


class API:

    def __init__(self):
        self.sunucuAdresi = 'http://212.68.57.202:52196'
        self.session = requests.Session()

    def telemetriGonder(self, takim_numarasi, key, IHA_enlem, IHA_boylam, IHA_irtifa, IHA_dikilme, IHA_yonelme,
                        IHA_yatis, IHA_hiz, IHA_batarya, IHA_otonom, IHA_kilitlenme, Hedef_merkez_X, Hedef_merkez_Y,
                        Hedef_genislik, Hedef_yukseklik):
        loop = True
        sunucuAdresi = self.sunucuAdresi + '/api/telemetri_gonder'
        while loop:
            sistemSaati = self.sunucuSaati()
            json = {
                "takim_numarasi": takim_numarasi,
                "key": key,
                "IHA_enlem": IHA_enlem,
                "IHA_boylam": IHA_boylam,
                "IHA_irtifa": IHA_irtifa,
                "IHA_dikilme": IHA_dikilme,
                "IHA_yonelme": IHA_yonelme,
                "IHA_yatis": IHA_yatis,
                "IHA_hiz": IHA_hiz,
                "IHA_batarya": IHA_batarya,
                "IHA_otonom": IHA_otonom,
                "IHA_kilitlenme": IHA_kilitlenme,
                "Hedef_merkez_X": Hedef_merkez_X,
                "Hedef_merkez_Y": Hedef_merkez_Y,
                "Hedef_genislik": Hedef_genislik,
                "Hedef_yukseklik": Hedef_yukseklik,
                "sistemSaati": sistemSaati
            }
            response = self.session.post(url=sunucuAdresi, json=json)
            loop = self.statusCheck(response)

    def telemetrileriAl(self):
        loop = True
        sunucuAdresi = self.sunucuAdresi + '/api/telemetri_gonder'
        while loop:
            response = self.session.get(url=sunucuAdresi)
            json = response.json()
            return json

    def sunucuSaati(self):
        loop = True
        sunucuAdresi = self.sunucuAdresi + '/api/sunucusaati'
        while loop:
            response = self.session.get(url=sunucuAdresi)
            json = response.json()
            return json

    def kilitlenmeBilgisi(self, baslangıcZamanı, bitisZamanı, takımNo, kilitlenmeNo):  # bura nasıl olucak cok net degil
        loop = True
        sunucuAdresi = self.sunucuAdresi + '/api/kilitlenme_bilgisi'
        while loop:
            json = {
                "kilitlenmeBaslangicZamani": baslangıcZamanı,
                "kilitlenmeBitisZamani": bitisZamanı,
                "takim_numarasi": takımNo,
                "kilitlenme_numarasi": kilitlenmeNo
            }
            response = self.session.post(url=sunucuAdresi, json=json)
            loop = self.statusCheck(response)

    def giris(self, takimadi, takimsifresi):  # yarışma başlamadan önce yapılacak
        print("sending LogIn request")
        sunucuAdresi = self.sunucuAdresi + '/api/giris'
        loop = True
        while loop:
            json = {
                "kadi": takimadi,
                "sifre": takimsifresi
            }
            response = self.session.post(url=sunucuAdresi, json=json)
            print(response)
            print(sunucuAdresi)
            loop = self.statusCheck(response)

    def customGet(self, link):
        response = self.session.get(url=link)
        json = response.json()
        return json

    def customPost(self, link, json):
        loop = True
        while loop:
            response = self.session.post(url=link, json=json)
            loop = self.statusCheck(response)

    def statusCheck(self, response):
        responseStatus = response.status_code  # notationdan emin değilim bunu kontrol etmek gerekiyo ama hedeflenen geri dönüşte verdiği numaraya bakmak
        if responseStatus == 200:
            print("İstek başarılı")
            return False

        if responseStatus == 400:  # içerigine bakılması gerekiyor ancak sadece 3 olabildiği içn ileri bi islem yazmadım
            print("Telemetri hızı çok yüksek")
            return

        if responseStatus == 401:
            print("Oturum Aç")
            self.giris()  # parametre nasıl vericez
            return

        if responseStatus == 403:
            print("takım no veya key yanlış")
            return

        if responseStatus == 404:
            print("geçersiz URL")
            return

        if responseStatus == 500:
            print("sunucu içi hata")
            return
