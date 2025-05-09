from django.contrib import admin
from .models import *


class ReadOnlyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class StudentAnswerAdmin(ReadOnlyAdmin):
    list_display = ('student_name', 'question_text', 'choice', 'submitted_at')
    search_fields = ('student__name', 'question__question_text', 'choice')
    readonly_fields = ('student', 'question', 'choice')

    def student_name(self, obj):
        return obj.student.name
    student_name.short_description = 'Student Name'

    def question_text(self, obj):
        return obj.question.question_text
    question_text.short_description = 'Question'

    def submitted_at(self, obj):
        return obj.student.submitted_at
    submitted_at.short_description = 'Submitted At'


class StudentAdmin(ReadOnlyAdmin):
    list_display = ('name', 'batch_name',
                    'batch_time', 'submitted_at')
    readonly_fields = ('name', 'batch_name', 'batch_time', 'submitted_at')


class QuestionAdmin(ReadOnlyAdmin):
    list_display = ('question_text',)
    readonly_fields = ('question_text',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(StudentAnswer, StudentAnswerAdmin)
