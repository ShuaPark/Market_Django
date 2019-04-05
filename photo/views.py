from django.shortcuts import render

# Create your views here.
from .models import Photo

# Photo List뷰 만들기 : GenericView 의 ListView와 동일
def photo_list(request):
    photos = Photo.objects.all()
    content = {'photos':photos}
    return render(request, 'photo/list.html', content)


from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class PhotoUploadView(CreateView):

    model  = Photo
    fields = ['photo','text']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        # form 입력이 정상 처리시
        if form.is_valid():
            form.instance.save()
            return redirect('photo:list') # 작업 완료 후 연결 url
        else:
            return self.render_to_response({'form':form})



class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photo/detail.html'


class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'


class PhotoUpdateView(UpdateView):
    model = Photo
    fields= ['photo', 'text']
    template_name = 'photo/update.html'