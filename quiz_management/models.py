from django.db import models
from django.contrib.auth import get_user_model
from .enums import QuestionTypes


User = get_user_model()

class Quiz(models.Model):

    #relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes')

    # fields
    title = models.CharField(max_length=255)

    #timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'quizzes'
    

class Question(models.Model):

    #relationship
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')

    # fields
    question = models.CharField(max_length=255)
    question_type = models.CharField(max_length=100, choices=QuestionTypes.choices, default=QuestionTypes.SINGLE_CORRECT)

    #timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.question
    
    class Meta:
        db_table = 'questions'


class Answer(models.Model):

    #relationship
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    #fields
    answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer
    
    class Meta:
        db_table = 'answers'


class StudentAnswer(models.Model):

    #relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_answers')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    #fields
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer
    
    class Meta:
        db_table = 'student_answers'


class StudentScore(models.Model):

    #relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    #fields
    total_question = models.IntegerField(default=0)
    attempt_question = models.IntegerField(default=0)
    correct_question = models.IntegerField(default=0)

    class Meta:
        db_table = 'student_scores'