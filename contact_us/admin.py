from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Contact

@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):

    list_display = ['name', 'email', 'subject', 'message','contact_date', 'replied', 'resolved']
    search_fields = ['name', 'email', 'subject',  'message']
    list_filter = ['contact_date', 'replied', 'resolved']

    summernote_fields = ('message',)

    actions = ['mark_as_replied', 'mark_as_not_replied', 'mark_as_resolved', 'mark_as_not_resolved']

    def mark_as_replied(self, request, queryset):
        """
        Allows admin to mark contact as replied.
        """
        queryset.update(replied=True)
        self.message_user(request, 'Selected contacts have been marked as replied.')
    
    def mark_as_not_replied(self, request, queryset):
        """
        Allows admin to mark contact as not replied.
        """
        queryset.update(replied=False)
        self.message_user(request, 'Selected contacts have been marked as not replied too.')
    
    
    def mark_as_resolved(self, request, queryset):
        """
        Allows admin to mark contact as resolved.
        """
        queryset.update(resolved=True)
        self.message_user(request, 'Selected contacts have been marked as resolved.')

    def mark_as_not_resolved(self, request, queryset):
        """
        Allows admin to mark contact as not resolved.
        """
        queryset.update(resolved=False)
        self.message_user(request, 'Selected contacts have been marked as not resolved.')

