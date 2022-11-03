from django.shortcuts import render
from django.views import View


class TestView(View):

    template_name = 'test2.html'

    def get(self, request):
        context = {
            'test': [1, 2, 3, 4, 5, 6, 7]
        }
        return render(request, self.template_name, context)
