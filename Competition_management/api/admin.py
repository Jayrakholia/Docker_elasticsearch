from django.contrib import admin
from api.models import User, Competition, Entry
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','name','birth_date','gender','is_active','is_delete','created_at','updated_at']

@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display=['id','name','status','description','user_id','is_active','is_delete','created_at','updated_at']

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display=['id','title','topic','state','country','created_at','updated_at','competition_id']