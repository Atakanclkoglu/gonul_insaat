from django.db import models

# banner
class Slider(models.Model):
    title = models.CharField(
        max_length=200, 
        verbose_name="Başlık", 
        blank=True  # Boş bırakılmasına izin verilmez
    )
    description = models.TextField(
        verbose_name="Açıklama", 
        blank=True  # Boş bırakılmasına izin verilmez
    )
    image = models.ImageField(
        upload_to='carousel_images/', 
        verbose_name="Resim", 
        blank=True  # Boş bırakılmasına izin verilmez
    )
   
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Oluşturulma Tarihi"
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name="Güncellenme Tarihi"
    )

    class Meta:
        verbose_name = "Afiş"
        verbose_name_plural = "Afişler"

    def __str__(self):
        return self.title
    


# hakkında

class AboutUs(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Başlık",
        blank=True
    )
    heading = models.CharField(
        max_length=255,
        verbose_name="Alt Başlık",
        blank=True
    )
    description = models.TextField(
        verbose_name="Açıklama",
        blank=True
    )
    short_description = models.TextField(
        verbose_name="Kısa Açıklama",
        blank=True  # Bu alan opsiyonel
    )
    years_of_experience = models.PositiveIntegerField(
        verbose_name="Deneyim Yılı",
        blank=False
    )
    image_1 = models.ImageField(
        upload_to='about_images/',
        verbose_name="Görsel 1",
        blank=True
    )
    image_2 = models.ImageField(
        upload_to='about_images/',
        verbose_name="Görsel 2",
        blank=True
    )

    class Meta:
        verbose_name = "Hakkımızda"
        verbose_name_plural = "Hakkımızda"    

    def __str__(self):
        return self.title
    



#  hizmetlerimiz

class Service(models.Model):   
    name = models.CharField(
        max_length=255,
        verbose_name="Başlık",
        blank=True
    )
    
    description = models.TextField(
        verbose_name="Açıklama",
        blank=True
    )
   
   
    image = models.ImageField(
        upload_to='about_images/',
        verbose_name="Görsel ",
        blank=True
    )
    icon = models.ImageField(
        upload_to='about_images/',
        verbose_name="İcon Görsel",
        blank=True
    )

    class Meta:
        verbose_name = "Hizmetlerimiz"
        verbose_name_plural = "Hizmetlerimiz"    

    def __str__(self):
        return self.name
    




# sosyal medya
class SocialMedia(models.Model):
    name = models.CharField(max_length=50, verbose_name="Sosyal Medya Platformu")
    icon_image = models.ImageField(upload_to='social_media_icons/', verbose_name="İkon Resmi", default='social_media_icons/default_image.jpg')
    url = models.URLField(max_length=200, verbose_name="Link")
    

    class Meta:
        verbose_name = "Sosyal Medya"
        verbose_name_plural = "Sosyal Medya"

    def __str__(self):
        return self.name    


# logo
class Logo(models.Model):
    name = models.CharField(max_length=50, verbose_name="Logo Adı")
    image = models.ImageField(upload_to='logo/', verbose_name="Logo Resmi", default='logo/default_image.jpg')
    

    class Meta:
        verbose_name = "Logo"
        verbose_name_plural = "Logolar"

    def __str__(self):
        return self.name


# projeler


class Project(models.Model):
    # Proje adı
    project_name = models.CharField(
        max_length=200, 
        verbose_name="Proje Sloganınız", 
         
        
    )
    
    # Proje açıklaması
    project_description = models.TextField(
        verbose_name="Proje Açıklaması", 
        help_text="Proje hakkında açıklama.", 
        null=True, 
        blank=True,  # Boş bırakılabilir
    )
    
    # Proje resmi (media'den)
    project_image = models.ImageField(
        upload_to='projects/', 
        verbose_name="Proje Resmi", 
        help_text="Proje ile ilgili resim", 
        null=True, 
        blank=True  # Boş bırakılabilir

    )
    
    # Projeye ait bina adları (bir projeye birden fazla bina olabilir)
    building_name = models.CharField(
        max_length=200, 
        verbose_name="Bina Adı", 
        help_text="Projede yer alan bina adı.", 
        null=True, 
        blank=True,  # Boş bırakılabilir
        default=""  # Varsayılan değer

    )
    
    # Bina özellikleri
    building_features1 = models.TextField(
        max_length=100,
        verbose_name="Bina Özelliği 1", 
        help_text="Bina ile ilgili özellikler.", 
        null=True, 
        blank=True,  # Boş bırakılabilir
        default=""  # Varsayılan değer

    )
    building_features2 = models.TextField(
        max_length=100,
        verbose_name="Bina Özelliği 2", 
        help_text="Bina ile ilgili özellikler.", 
        null=True, 
        blank=True,  # Boş bırakılabilir
        default=""  # Varsayılan değer

    )    
    building_features3 = models.TextField(
        max_length=100,
        verbose_name="Bina Özelliği 3", 
        help_text="Bina ile ilgili özellikler.", 
        null=True, 
        blank=True,  # Boş bırakılabilir
        default=""  # Varsayılan değer

    )    

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = "Proje"
        verbose_name_plural = "Projeler"




class ServiceVideo(models.Model):
    title = models.CharField(max_length=255, verbose_name="Başlık")
    video = models.FileField(upload_to='videos/', verbose_name="Video Dosyası")
    logo = models.ImageField(upload_to='logos/', verbose_name="Logo Görseli")
    description = models.TextField(blank=True, null=True, verbose_name="Açıklama")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Hizmet Videosu"
        verbose_name_plural = "Hizmet Videoları"
