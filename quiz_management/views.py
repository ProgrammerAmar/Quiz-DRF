from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from .serializers import QuizSerialize, QuestionSerialize, AnswerSerialize, StudentAnswerSerialize, StudentScoreSerialize
from .models import Quiz, Question, Answer, StudentAnswer, StudentScore


class Quizzes(viewsets.ModelViewSet):
    serializer_class = QuizSerialize
    queryset = Quiz.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        
        #save data
        serializer.save(user=user)


class Questions(viewsets.ModelViewSet):
    serializer_class = QuestionSerialize
    queryset = Question.objects.all()


class Answers(viewsets.ModelViewSet):
    serializer_class = AnswerSerialize
    queryset = Answer.objects.all()


class QuizAttemptView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = StudentAnswerSerialize

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        #save data
        user = self.request.user
        student_answer = serializer.save(user=user)
        
        #check student answer is correct
        answer = student_answer.answer
        if answer.is_correct:
            student_answer.is_correct = True
            student_answer.save()

        #update student score
        student_score = StudentScore.objects.filter(user=user, quiz=student_answer.quiz).first()
        if student_score:
            student_score.attempt_question += 1
            if student_answer.is_correct:
                student_score.correct_question += 1

            student_score.save()
        else:
            quiz = student_answer.quiz
            attempt_question = 1
            correct_question = 1 if student_answer.is_correct else 0
            StudentScore.objects.create(user=user, quiz=student_answer.quiz, total_question=quiz.questions.count(), attempt_question=attempt_question, correct_question=correct_question)

        #response student score
        score_serializer = StudentScoreSerialize(student_score)
        return Response(score_serializer.data, status=status.HTTP_201_CREATED)