from django.http import HttpResponse

def index(request):
    return HttpResponse("На данной странице представлено актуальные расписание телепрограммы на 1 день")

