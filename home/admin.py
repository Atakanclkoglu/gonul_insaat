from django.contrib import admin

from .models import *

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)



@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'heading', 'years_of_experience')
    search_fields = ('heading', 'title')
    list_editable = ('heading', 'years_of_experience')  # 'title' değil, düzenlenebilir alanlar
    list_display_links = ('title',)  # 'title' tıklanabilir olacak
    list_filter = ('years_of_experience',)
    ordering = ('-years_of_experience',)



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'icon')
    search_fields = ('name',)
    list_editable = ('description', 'icon')  

# sosyal medya admini

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "icon_image")
    search_fields = ("name",)

# proje admini

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # Görünümde hangi alanların görüneceğini belirleyin
    list_display = ('project_name', 'building_name', 'project_description', 'building_features1', 'building_features2', 'building_features3', 'project_image')
    
    # Filtreleme seçenekleri
    list_filter = ('building_name',)
    
    # Arama kutusunu etkinleştirme
    search_fields = ('project_name', 'building_name', 'project_description', 'building_features1', 'building_features2', 'building_features3')
    
    # Admin formunda hangi alanları göstereceğimizi seçiyoruz
    fieldsets = (
        (None, {
            'fields': ('project_name', 'project_description', 'project_image',)
        }),
        ('Bina Bilgileri', {
            'fields': ('building_name', 'building_features1', 'building_features2', 'building_features3',)
        }),
    )
    
    # Görünümü özelleştirme
    ordering = ('project_name',)  # Varsayılan sıralama

    # 'project_description' alanı için uzun bir metin girilmesi gerektiği için bu alanda textarea gösterilecektir
    formfield_overrides = {
        models.TextField: {'widget': admin.widgets.AdminTextareaWidget(attrs={'rows': 4, 'cols': 40})},
    }


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name',)

admin.site.register(ServiceVideo)   
class ServiceVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video', 'logo', 'description')
    search_fields = ('title',)
    list_editable = ('video', 'description') 