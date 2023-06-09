from rest_framework import serializers
from .models import Quiz, Question, Answer, StudentAnswer, StudentScore


class QuizSerialize(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = ["id","title"]


class QuestionSerialize(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ["id", "quiz", "question", "question_type"]


class AnswerSerialize(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ["id", "question", "answer", "is_correct"]


class StudentAnswerSerialize(serializers.ModelSerializer):

    class Meta:
        model = StudentAnswer
        fields = ["id", "quiz", "question", "answer"]


class StudentScoreSerialize(serializers.ModelSerializer):

    class Meta:
        model = StudentScore
        fields = "__all__"