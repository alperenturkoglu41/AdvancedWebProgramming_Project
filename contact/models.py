from django.db import models


class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name="Updated Date",
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name="Created Date",
    )

    class Meta:
        abstract = True


class GeneralSetting(AbstractModel):
    name = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="Name",
        help_text="This is variable of the setting.",
    )
    description = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="Description",
    )
    parameter = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="Parameter",
    )

    def __str__(self):
        return f"General Setting: {self.name}"

    class Meta:
        verbose_name = "General Setting"
        verbose_name_plural = "General Settings"
        ordering = ("name",)


class Profile(AbstractModel):
    full_name = models.CharField(max_length=120, default="", verbose_name="Ad Soyad")
    profile_title = models.CharField(max_length=180, default="", blank=True, verbose_name="Profil Başlığı")
    hero_titles = models.CharField(max_length=500, default="", blank=True, verbose_name="Hero Yazıları")
    hero_description = models.CharField(max_length=500, default="", blank=True, verbose_name="Hero Açıklaması")
    summary = models.TextField(default="", blank=True, verbose_name="Özet")
    about_intro = models.TextField(default="", blank=True, verbose_name="Hakkımda 1. Paragraf")
    about_middle = models.TextField(default="", blank=True, verbose_name="Hakkımda 2. Paragraf")
    about_footer = models.TextField(default="", blank=True, verbose_name="Hakkımda 3. Paragraf")
    education_label = models.CharField(max_length=180, default="", blank=True, verbose_name="Eğitim Bilgisi")
    location = models.CharField(max_length=180, default="", blank=True, verbose_name="Konum")
    hero_image = models.CharField(max_length=255, default="img/alperen-main.jpeg", blank=True, verbose_name="Hero Görseli")
    profile_image = models.CharField(max_length=255, default="img/alperen-profile.jpg", blank=True, verbose_name="Profil Görseli")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profil"
        ordering = ("-is_active", "full_name")


class ContactInfo(AbstractModel):
    location = models.CharField(max_length=180, default="", blank=True, verbose_name="Konum")
    institution = models.CharField(max_length=180, default="", blank=True, verbose_name="Bağlı Kurum")
    email = models.EmailField(default="", blank=True, verbose_name="E-posta")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")

    def __str__(self):
        return self.email or "İletişim Bilgisi"

    class Meta:
        verbose_name = "İletişim Bilgisi"
        verbose_name_plural = "İletişim Bilgileri"
        ordering = ("-is_active", "email")


class Skill(AbstractModel):
    name = models.CharField(max_length=120, verbose_name="Beceri")
    percent = models.PositiveSmallIntegerField(default=80, verbose_name="Yüzde")
    order = models.PositiveIntegerField(default=0, verbose_name="Sıra")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Beceri"
        verbose_name_plural = "Beceriler"
        ordering = ("order", "name")


class Education(AbstractModel):
    title = models.CharField(max_length=180, verbose_name="Okul/Bölüm")
    period = models.CharField(max_length=80, default="", blank=True, verbose_name="Tarih")
    subtitle = models.CharField(max_length=180, default="", blank=True, verbose_name="Alt Başlık")
    description = models.TextField(default="", blank=True, verbose_name="Açıklama")
    order = models.PositiveIntegerField(default=0, verbose_name="Sıra")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Eğitim"
        verbose_name_plural = "Eğitimler"
        ordering = ("order", "title")


class Experience(AbstractModel):
    title = models.CharField(max_length=180, verbose_name="Görev")
    period = models.CharField(max_length=80, default="", blank=True, verbose_name="Tarih")
    company = models.CharField(max_length=180, default="", blank=True, verbose_name="Kurum")
    description = models.TextField(default="", blank=True, verbose_name="Açıklama")
    order = models.PositiveIntegerField(default=0, verbose_name="Sıra")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")

    @property
    def bullets(self):
        return [line.strip() for line in self.description.splitlines() if line.strip()]

    def __str__(self):
        return f"{self.title} - {self.company}"

    class Meta:
        verbose_name = "İş Deneyimi"
        verbose_name_plural = "İş Deneyimleri"
        ordering = ("order", "title")


class Service(AbstractModel):
    icon = models.CharField(max_length=80, default="bi bi-check-circle", verbose_name="Bootstrap Icon")
    title = models.CharField(max_length=180, verbose_name="Başlık")
    description = models.TextField(default="", blank=True, verbose_name="Açıklama")
    order = models.PositiveIntegerField(default=0, verbose_name="Sıra")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yetkinlik Kartı"
        verbose_name_plural = "Yetkinlik Kartları"
        ordering = ("order", "title")


class Statistic(AbstractModel):
    value = models.PositiveIntegerField(default=0, verbose_name="Değer")
    label = models.CharField(max_length=120, verbose_name="Etiket")
    order = models.PositiveIntegerField(default=0, verbose_name="Sıra")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")

    def __str__(self):
        return f"{self.value} - {self.label}"

    class Meta:
        verbose_name = "Sayaç"
        verbose_name_plural = "Sayaçlar"
        ordering = ("order", "label")


class PortfolioItem(AbstractModel):
    title = models.CharField(max_length=180, verbose_name="Başlık")
    description = models.TextField(default="", blank=True, verbose_name="Açıklama")
    image = models.CharField(max_length=255, default="", blank=True, verbose_name="Görsel")
    alt_text = models.CharField(max_length=180, default="", blank=True, verbose_name="Görsel Açıklaması")
    order = models.PositiveIntegerField(default=0, verbose_name="Sıra")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Çalışma"
        verbose_name_plural = "Çalışmalar"
        ordering = ("order", "title")


class SocialLink(AbstractModel):
    label = models.CharField(max_length=80, verbose_name="Etiket")
    icon = models.CharField(max_length=80, default="bi bi-link", verbose_name="Bootstrap Icon")
    url = models.CharField(max_length=255, verbose_name="Bağlantı")
    order = models.PositiveIntegerField(default=0, verbose_name="Sıra")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = "Sosyal Bağlantı"
        verbose_name_plural = "Sosyal Bağlantılar"
        ordering = ("order", "label")
