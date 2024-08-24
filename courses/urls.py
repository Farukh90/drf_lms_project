from django.urls import path, include
from rest_framework.routers import SimpleRouter
from courses.views import (
    CourseViewSet,
    LessonCreateApiView,
    LessonListApiView,
    LessonRetrieveApiView,
    LessonUpdateApiView,
    LessonDestroyApiView,
    PaymentListView, SubscriptionView,
)

app_name = "courses"

router = SimpleRouter()
router.register(r"", CourseViewSet)  # Регистрируем маршруты для курса

urlpatterns = [
    path(
        "<int:course_id>/lessons/", LessonCreateApiView.as_view(), name="lessons_create"
    ),
    path(
        "<int:course_id>/lessons/list/",
        LessonListApiView.as_view(),
        name="lessons_list",
    ),
    path(
        "<int:course_id>/lessons/<int:pk>/",
        LessonRetrieveApiView.as_view(),
        name="lessons_retrieve",
    ),
    path(
        "<int:course_id>/lessons/<int:pk>/destroy/",
        LessonDestroyApiView.as_view(),
        name="lessons_destroy",
    ),
    path(
        "<int:course_id>/lessons/<int:pk>/update/",
        LessonUpdateApiView.as_view(),
        name="lessons_update",
    ),
    path("payments/", PaymentListView.as_view(), name="payment-list"),

    path('subscriptions/', SubscriptionView.as_view(), name='subscription_view'),

    path("", include(router.urls)),


]

# Включаем маршруты из роутера для курсов
urlpatterns += router.urls
