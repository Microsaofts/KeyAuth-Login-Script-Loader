# KeyAuth Login Script

KeyAuth API kullanarak kullanıcı lisanslarını doğrulayan bir Python uygulamasıdır. Bu uygulama ayrıca basit bir yükleme çubuğu, kullanıcı bilgilerini görüntüleme ve lisans doğrulaması gibi özellikler sunar.

### Gereksinimler

- Python 3.x
- Gerekli Python kütüphanesi:
  - `pyautogui`

- Projeyi Klonlayın
- Gerekli Bağımlılıkları Yükleyin

Aşağıdaki komut ile gerekli kütüphaneleri yükleyin:

```bash
pip install pyautogui
```

- API Bilgilerinizi Girin

Proje dosyasının içindeki KeyAuth API bilgilerinizi aşağıdaki alanlara girin:

```python
keyauthapp = api(
    name = "YourAppName",
    ownerid = "YourOwnerID",
    secret="YourSecretKey",
    version = "1.0",
    hash_to_check = getchecksum()
)
```

### Test Etme 

Tüm İşlemler Tamamlandıktan sonra Test Etemk için şu komutu kullanabilirsiniz:

```bash
python main.py
```

## Kullanım

- Uygulama başlatıldığında, bir lisans anahtarı girmeniz gerekecek.
- Doğru lisans anahtarı girildikten sonra, kullanıcı bilgilerinizi ve aktif aboneliklerinizi görüntüleyebilirsiniz.


**Note:** Bu Kod Sadece Giriş Kısmını Ele Alır. Kullanıcı Giriş Yaptıktan Sonra Farklı Eylemler Gerçekleştire Bilirsiniz. Örnek Olarak Basit Bir Konsol Aracının Doğrulama Kısmı Olarak Kullanıla Bilirsiniz.

## Katkıda Bulunma

Projeye katkıda bulunmak isterseniz, lütfen bir yıldız bırakın. Her türlü katkı için minnettar oluruz!

## Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.