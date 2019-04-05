from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Bookmark
import json

# 내용을 살펴보는 view 함수
class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 3   # ListView 페이지에서 Paginate 기능 활성화

    # generic view 에 get_context_data 를 활용하여 내용을 추가합니다
    # Master Core Django 336페이지

    # context["temp"] : 템플릿에서 temp 객체로 호출이 가능
    def get_context_data(self, **kwargs):
        data = [
            {"year": '2008', "value": 20},
            {"year": '2009', "value": 10},
            {"year": '2010', "value": 5},
            {"year": '2011', "value": 5},
            {"year": '2012', "value": 20} 
        ]
        context = super(BookmarkListView, self).get_context_data(**kwargs)
        context["temp"] = json.dumps(data) 
        return context
    

# 새로운 Bookmark 추가함수
class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']   # Bookmark 테이블에서 연결할 Field 목록
    # success_url = reverse_lazy('bookmark:list') # 작업 완료 후 연결 link name
    template_name_suffix = '_create'  #  모델클래스_create.html 와 연결


# 북마크 확인기능
class BookmarkDetailView(DetailView):
    model = Bookmark


# 수정 기능
class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']  # Bookmark 테이블에서 연결할 Field 목록
    template_name_suffix = "_update" # 모델클래스_update.html 와 연결
    # success_url = reverse_lazy('bookmark:list')

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy("bookmark:list")