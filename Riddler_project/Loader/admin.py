from django.contrib import admin
from .models import *


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass

@admin.register(Marks_Of_User)
class Marks_Of_UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Marks_Of_User_item)
class Marks_Of_User_itemAdmin(admin.ModelAdmin):
    pass