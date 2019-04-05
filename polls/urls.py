from django.urls import path
from .views import index, detail, retults, vote
from .views import IndexView, Detail_View, ResultsView

app_name = 'polls'
urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path('<int:pk>/', Detail_View.as_view(), name='detail'),
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
]
