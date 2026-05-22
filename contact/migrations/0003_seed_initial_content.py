from django.db import migrations


def seed_initial_content(apps, schema_editor):
    GeneralSetting = apps.get_model("contact", "GeneralSetting")
    Profile = apps.get_model("contact", "Profile")
    ContactInfo = apps.get_model("contact", "ContactInfo")
    Skill = apps.get_model("contact", "Skill")
    Education = apps.get_model("contact", "Education")
    Experience = apps.get_model("contact", "Experience")
    Service = apps.get_model("contact", "Service")
    Statistic = apps.get_model("contact", "Statistic")
    PortfolioItem = apps.get_model("contact", "PortfolioItem")
    SocialLink = apps.get_model("contact", "SocialLink")

    settings = {
        "site_title": "Alperen Türkoğlu | Kişisel Web Sitesi",
        "site_keywords": "Alperen Türkoğlu, Piri Reis Üniversitesi, BTMteknik, kişisel web sitesi, CV",
        "site_description": "Alperen Türkoğlu'nun eğitim, iş deneyimi, yetkinlik ve iletişim bilgilerini içeren kişisel web sitesi.",
    }
    for name, parameter in settings.items():
        GeneralSetting.objects.update_or_create(
            name=name,
            defaults={"description": name, "parameter": parameter},
        )

    Profile.objects.update_or_create(
        full_name="Alperen Türkoğlu",
        defaults={
            "profile_title": "Üniversite mezunu, teknik ekip destek personeli",
            "hero_titles": "Piri Reis Üniversitesi Mezunu, BTMteknik Part-Time Çalışanı, Gelişime Açık Takım Arkadaşı",
            "hero_description": "BTMteknik'te part-time görev alan, gelişime açık ve sorumluluk sahibi takım arkadaşı.",
            "summary": "Üniversite eğitimi boyunca sorumluluk alan, staj deneyimlerini gerçek iş süreçlerine dönüştüren ve teknik ekip içinde gelişimini sürdüren aday.",
            "about_intro": "2021 yılında Piri Reis Üniversitesi'nde öğrenim hayatıma başladım ve 2026 yılında mezun oldum. Üniversite sürecinde akademik bilgiyle birlikte çalışma disiplinimi geliştirmeye, sorumluluk almaya ve profesyonel hayata güçlü bir başlangıç yapmaya odaklandım.",
            "about_middle": "2023-2026 yılları arasında Piri Reis Üniversitesi bünyesinde stajyer öğrenci olarak görev aldım. Bu süreç, düzenli takip, iletişim, ekip içi koordinasyon ve iş süreçlerine uyum konularında sağlam bir deneyim kazandırdı.",
            "about_footer": "2025 yaz döneminde BTMteknik'te staj programımı tamamladım ve performansım doğrultusunda BTMteknik bünyesinde part-time olarak görev yapmaya devam ediyorum.",
            "education_label": "Piri Reis Üniversitesi mezunu",
            "location": "İstanbul, Türkiye",
            "hero_image": "img/alperen-main.jpeg",
            "profile_image": "img/alperen-profile.jpg",
            "is_active": True,
        },
    )

    ContactInfo.objects.update_or_create(
        email="info@alperenturkoglu.com",
        defaults={"location": "İstanbul, Türkiye", "institution": "BTMteknik", "is_active": True},
    )

    for order, name, percent in [
        (1, "Takım Çalışması", 95),
        (2, "Operasyonel Takip", 90),
        (3, "Raporlama ve Düzen", 85),
        (4, "Öğrenme Hızı", 92),
    ]:
        Skill.objects.update_or_create(name=name, defaults={"percent": percent, "order": order, "is_active": True})

    Education.objects.update_or_create(
        title="Piri Reis Üniversitesi",
        defaults={
            "period": "2021 - 2026",
            "subtitle": "Üniversite Eğitimi",
            "description": "Akademik eğitim sürecinde teknik bakış açısı, disiplinli çalışma alışkanlığı ve profesyonel iletişim becerileri geliştirildi.",
            "order": 1,
            "is_active": True,
        },
    )

    experiences = [
        (
            "Part-Time Çalışan",
            "2025 - Devam Ediyor",
            "BTMteknik",
            "Staj sürecinde edinilen deneyimi şirket içi görevlerde aktif olarak kullanma.\nTeknik ekip iş akışlarına destek verme ve günlük operasyonların düzenli ilerlemesine katkı sağlama.\nVerilen sorumlulukları takip ederek zamanında ve özenli şekilde tamamlama.",
            1,
        ),
        (
            "Stajyer",
            "2025 Yaz Dönemi",
            "BTMteknik",
            "Profesyonel iş ortamında uygulamalı deneyim kazanma.\nEkip içi iletişim, görev takibi ve iş disiplini konularında gelişim gösterme.",
            2,
        ),
        (
            "Stajyer Öğrenci",
            "2023 - 2026",
            "Piri Reis Üniversitesi",
            "Üniversite bünyesinde akademik ve idari süreçlere destek olma.\nDüzenli çalışma, sorumluluk bilinci ve kurumsal iletişim becerilerini güçlendirme.",
            3,
        ),
    ]
    for title, period, company, description, order in experiences:
        Experience.objects.update_or_create(
            title=title,
            company=company,
            defaults={"period": period, "description": description, "order": order, "is_active": True},
        )

    services = [
        ("Görev Takibi", "bi bi-kanban", "Verilen işleri önceliklendirir, süreci düzenli takip eder ve sonucu net şekilde raporlar.", 1),
        ("Ekip Uyumu", "bi bi-people", "Takım içi iletişimi güçlü tutar, ortak hedeflere katkı sağlar ve sorumluluk paylaşımına uyum gösterir.", 2),
        ("Teknik Destek", "bi bi-tools", "Teknik süreçlerde öğrenmeye açık, dikkatli ve çözüm odaklı bir yaklaşımla destek sağlar.", 3),
        ("Raporlama", "bi bi-journal-check", "İş adımlarını düzenli kayıt altına alır, takip edilebilir ve anlaşılır çıktılar oluşturur.", 4),
        ("Hızlı Öğrenme", "bi bi-lightning-charge", "Yeni süreçlere kısa sürede adapte olur ve öğrendiklerini uygulamaya dönüştürür.", 5),
        ("Sorumluluk Bilinci", "bi bi-shield-check", "Güvenilir, planlı ve dikkatli çalışarak görevlerin sürdürülebilir biçimde ilerlemesini sağlar.", 6),
    ]
    for title, icon, description, order in services:
        Service.objects.update_or_create(
            title=title,
            defaults={"icon": icon, "description": description, "order": order, "is_active": True},
        )

    for order, value, label in [
        (1, 2021, "Üniversite Başlangıcı"),
        (2, 2023, "İlk Staj Deneyimi"),
        (3, 2025, "BTMteknik Başlangıcı"),
        (4, 2026, "Mezuniyet"),
    ]:
        Statistic.objects.update_or_create(label=label, defaults={"value": value, "order": order, "is_active": True})

    portfolio = [
        ("Piri Reis Üniversitesi", "2021-2026 eğitim ve 2023-2026 stajyer öğrenci deneyimi.", "img/pru-logo.jpeg", "Piri Reis Üniversitesi logosu", 1),
        ("BTMteknik", "2025 yaz stajı ve devam eden part-time görev.", "img/btm-logo.png", "BTMteknik logosu", 2),
        ("Kişisel Profil", "Profesyonel CV, hakkımda ve iletişim bilgileri için tek sayfalı portfolyo.", "img/alperen-profile.jpg", "Alperen Türkoğlu profil çalışması", 3),
    ]
    for title, description, image, alt_text, order in portfolio:
        PortfolioItem.objects.update_or_create(
            title=title,
            defaults={"description": description, "image": image, "alt_text": alt_text, "order": order, "is_active": True},
        )

    for order, label, icon, url in [
        (1, "E-posta", "bi bi-envelope", "/contact/"),
        (2, "CV", "bi bi-file-earmark-person", "/#resume"),
        (3, "Çalışmalar", "bi bi-briefcase", "/#portfolio"),
    ]:
        SocialLink.objects.update_or_create(
            label=label,
            defaults={"icon": icon, "url": url, "order": order, "is_active": True},
        )


class Migration(migrations.Migration):

    dependencies = [
        ("contact", "0002_contactinfo_education_experience_portfolioitem_and_more"),
    ]

    operations = [
        migrations.RunPython(seed_initial_content, migrations.RunPython.noop),
    ]
