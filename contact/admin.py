from django.contrib import admin

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


@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "parameter", "updated_date", "created_date"]
    search_fields = ["name", "description", "parameter"]
    list_editable = ["description", "parameter"]

    class Meta:
        model = GeneralSetting


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name", "profile_title", "education_label", "location", "is_active", "updated_date"]
    list_editable = ["profile_title", "education_label", "location", "is_active"]
    search_fields = ["full_name", "profile_title", "education_label", "location"]
    list_filter = ["is_active"]


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "location", "institution", "email", "is_active", "updated_date"]
    list_editable = ["location", "institution", "email", "is_active"]
    search_fields = ["location", "institution", "email"]
    list_filter = ["is_active"]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "percent", "order", "is_active"]
    list_editable = ["percent", "order", "is_active"]
    search_fields = ["name"]
    list_filter = ["is_active"]
    ordering = ["order", "name"]


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "period", "subtitle", "order", "is_active"]
    list_editable = ["period", "subtitle", "order", "is_active"]
    search_fields = ["title", "period", "subtitle", "description"]
    list_filter = ["is_active"]
    ordering = ["order", "title"]


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "company", "period", "order", "is_active"]
    list_editable = ["company", "period", "order", "is_active"]
    search_fields = ["title", "company", "period", "description"]
    list_filter = ["is_active"]
    ordering = ["order", "title"]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "icon", "order", "is_active"]
    list_editable = ["icon", "order", "is_active"]
    search_fields = ["title", "description", "icon"]
    list_filter = ["is_active"]
    ordering = ["order", "title"]


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ["id", "value", "label", "order", "is_active"]
    list_editable = ["value", "label", "order", "is_active"]
    search_fields = ["label"]
    list_filter = ["is_active"]
    ordering = ["order", "label"]


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "image", "order", "is_active"]
    list_editable = ["image", "order", "is_active"]
    search_fields = ["title", "description", "image", "alt_text"]
    list_filter = ["is_active"]
    ordering = ["order", "title"]


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ["id", "label", "icon", "url", "order", "is_active"]
    list_editable = ["icon", "url", "order", "is_active"]
    search_fields = ["label", "icon", "url"]
    list_filter = ["is_active"]
    ordering = ["order", "label"]
