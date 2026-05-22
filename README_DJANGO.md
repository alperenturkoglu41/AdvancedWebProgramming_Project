# AWP Django Kişisel Web Sitesi

Bu proje, DevFolio temasının Django altyapısına taşınmış halidir.

## Çalıştırma

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Site: `http://127.0.0.1:8000/`

Admin paneli: `http://127.0.0.1:8000/admin/`

## TODO Uyumu

- Django proje yapısı: `manage.py`, `awp_site/settings.py`, `awp_site/urls.py`
- App yapısı: `contact`
- URL router: ana proje `include`, app içinde `contact/urls.py`
- Template yapısı: `templates/layout.html`, `templates/includes/head.html`, `templates/includes/navbar.html`
- Sayfalar: `templates/index.html`, `templates/contact.html`
- Static dosyalar: `static/assets`
- Media dosyaları: `media/img`
- `.env` ayarları: `django-environ` ile okunur
- Admin paneli: `GeneralSetting` modeli admin paneline kayıtlıdır
- Docker: `Dockerfile` ve `docker-compose.yml`
- Requirements: `requirements.txt` ve `requirement.txt`

## Admin İçerik Yönetimi

Admin panelinde `General Settings` alanından şu değerler yönetilebilir:

- `site_title`
- `site_keywords`
- `site_description`
- `home_banner_name`
- `home_banner_title`
- `home_banner_description`
- `about_myself_welcome`
- `about_myself_footer`
