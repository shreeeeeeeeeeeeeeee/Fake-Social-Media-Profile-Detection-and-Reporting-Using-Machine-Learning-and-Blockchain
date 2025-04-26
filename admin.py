from django.contrib import admin
from .models import ProfileData, Report

class ProfileDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'followers', 'following', 'has_profile_photo', 'is_private')
    search_fields = ('user__username',)

class ReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'reported_profile', 'reason', 'timestamp', 'blockchain_tx_hash')
    search_fields = ('user__username', 'reported_profile')
    list_filter = ('timestamp',)
    
admin.site.register(ProfileData, ProfileDataAdmin)
admin.site.register(Report, ReportAdmin)
