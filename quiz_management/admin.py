from django.contrib import admin
from .models import Quiz, Question, Answer, StudentAnswer, StudentScore

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(StudentAnswer)
admin.site.register(StudentScore)

