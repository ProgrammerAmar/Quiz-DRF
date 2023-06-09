from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'quizzes', views.Quizzes)
router.register(r'questions', views.Questions)
router.register(r'answers', views.Answers)
router.register(r'quiz-attempt', views.QuizAttemptView, basename="quiz-attempt")


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]