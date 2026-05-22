from django.shortcuts import render

from contact.models import (
    ContactInfo,
    Education,
    Experience,
    GeneralSetting,
    PortfolioItem,
    Profile,
    Service,
    Skill,
    SocialLink,
    Statistic,
)


def get_general_setting(parameter):
    try:
        obj = GeneralSetting.objects.get(name=parameter).parameter
    except GeneralSetting.DoesNotExist:
        obj = ""
    return obj


def index(request):
    profile = Profile.objects.filter(is_active=True).first()
    contact_info = ContactInfo.objects.filter(is_active=True).first()
    context = {
        "site_title": get_general_setting("site_title") or "Alperen Türkoğlu | Kişisel Web Sitesi",
        "site_keywords": get_general_setting("site_keywords") or "Alperen Türkoğlu, Piri Reis Üniversitesi, BTMteknik, kişisel web sitesi, CV",
        "site_description": get_general_setting("site_description") or "Alperen Türkoğlu'nun eğitim, iş deneyimi, yetkinlik ve iletişim bilgilerini içeren kişisel web sitesi.",
        "profile": profile,
        "contact_info": contact_info,
        "skills": Skill.objects.filter(is_active=True),
        "educations": Education.objects.filter(is_active=True),
        "experiences": Experience.objects.filter(is_active=True),
        "services": Service.objects.filter(is_active=True),
        "statistics": Statistic.objects.filter(is_active=True),
        "portfolio_items": PortfolioItem.objects.filter(is_active=True),
    }
    return render(request, "index.html", context=context)


def contact(request):
    profile = Profile.objects.filter(is_active=True).first()
    contact_info = ContactInfo.objects.filter(is_active=True).first()
    context = {
        "site_title": "İletişim | Alperen Türkoğlu",
        "site_keywords": "Alperen Türkoğlu iletişim, BTMteknik, Piri Reis Üniversitesi",
        "site_description": "Alperen Türkoğlu iletişim sayfası.",
        "profile": profile,
        "contact_info": contact_info,
        "social_links": SocialLink.objects.filter(is_active=True),
    }
    return render(request, "contact.html", context=context)
