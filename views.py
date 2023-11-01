from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
from .forms import UserForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .analyser import TextAnalyser

users = ['Вася Питонов', 'Петя Гадюкин']  # TODO: удалить


def index(request):
    context = {
        'users': users
    }
    return render(request, 'app/index.html', context)


def add(request):
    if request.method == 'GET':
        form_fields = UserForm()
        context = {
            'form_fields': form_fields
        }
        return render(request, 'app/add.html', context)
    elif request.method == 'POST':
        form_fields = UserForm(request.POST, request.FILES)
        if form_fields.is_valid():
            file = request.FILES['file']
            file_system = FileSystemStorage()
            file_name = file_system.save(file.name, file)
            file_url = file_system.url(file_name)

            # здесь создать вордклауд
            wc_width = int(request.POST['wc_width'])
            wc_height = int(request.POST['wc_height'])
            parts_of_speech = request.POST.getlist('pos')  # FIXME: должен быть списком
            print(parts_of_speech)
            print(type(parts_of_speech))
            input("!!!!!!!!!!!!!!!!!!!!!")

            TextAnalyser(
                source_file=None,
                destination_file='wordcloud.png',
                parts_of_speech=['NOUN'],
                words_ammount=100,
                wc_width=800,
                wc_height=600,
                wc_background='black',
                wc_margin=10
            )

            context = {
                'url': file_url
            }
            return render(request, 'app/download.html', context)
    else:
        return HttpResponseNotAllowed(
            ['POST', 'GET'],
            content='Ошибка Этот метод не разрешен!'
        )