from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    image = models.ImageField(upload_to='posts/', verbose_name="Gönderi Resmi")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellenme Tarihi")

    class Meta:
        verbose_name = "Gönderi"
        verbose_name_plural = "Gönderiler"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Gönderi"
        verbose_name_plural = "Gönderiler"
        ordering = ['-created_at']