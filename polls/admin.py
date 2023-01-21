from django.contrib import admin

from .models import Choice, Question


# Allows Choice fields to be displayed when creating Question
# Defines the number of default Choice fields when creating a Question
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# Sets order of the fields on the admin page so 'question_text' is listed first
# Adds a header over the published date via 'fieldsets'
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']         # Adds ability to filter based on 'pub_date' field
    search_fields = ['question_text']  # Adds ability to search based on 'question_text' field


admin.site.register(Question, QuestionAdmin)  # Tells admin that Question objects have an admin interface
