from django.contrib import admin
# Register your models here.

from .models import Question, Choice


# admin.StackedInline 보다 깔끔하게 출력
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0 # 실제 입력한 내용과 별도로 추가 행 출력


class QuestionAdmin(admin.ModelAdmin):

    # 내용 field 에서의 설정
    fieldsets = [
        ('투표질문', {'fields':['question_text']}),
        ('날짜정보', {'fields':['pub_date']}),
    ]

    # Question admin 출력 필드를 정의 (Default 는 question_text만 출력)
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # foreignkey 내용을 연결
    inlines = [ChoiceInline]
    # 검색용 form 추가
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
