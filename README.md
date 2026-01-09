# Ornek Flask API

## Proje Amacı
Bu proje, basit bir REST API geliştirilmesi, GitHub üzerinden versiyon kontrolü,
Postman ile test edilmesi ve GitHub Actions ile otomatik testlerin çalıştırılmasını
göstermek amacıyla hazırlanmıştır.

## Kullanılan Teknolojiler
- Python
- Flask
- Git / GitHub
- Postman
- GitHub Actions (CI/CD)

## API Endpointleri

### GET /
Ana endpoint, basit bir mesaj döner.

### GET /users
Sistemdeki kullanıcı listesini JSON formatında döner.

## Kurulum ve Çalıştırma

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

##Test
API testleri Postman kullanılarak yapılmıştır.
Testler GitHub Actions ile otomatik olarak çalıştırılmaktadır.