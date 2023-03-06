from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from safir313.views import LoginRequiredMixin
from .forms import KidForm
from .utils import validate_code_meli
from .models import Kid


class RegisterView(LoginRequiredMixin, View):

    def get(self, request):
        context = {'form': KidForm}
        print(KidForm)
        return render(request, 'base.html', context=context)

    def post(self, request):
        context = {}
        kid_form = KidForm(request.POST)
        context['form'] = kid_form
        cmc = True if request.POST.get("cmc") == 'on' else False
        print(cmc)
        if kid_form.is_valid():
            code_meli = kid_form.cleaned_data['codmeli']
            phone = kid_form.cleaned_data['phone']
            if len(code_meli) == 10 and len(phone) == 11:
                if validate_code_meli(code_meli):
                    is_duplicate_codemeli = Kid.objects.filter(codmeli=code_meli).exists()
                    is_duplicate_fullname = Kid.objects.filter(name=kid_form.cleaned_data['name'], lastname=kid_form.cleaned_data['lastname']).exists()
                    if not is_duplicate_codemeli or cmc:
                        if not is_duplicate_fullname:
                            save_kid = Kid(
                                codmeli=kid_form.cleaned_data['codmeli'],
                                name=kid_form.cleaned_data['name'],
                                lastname=kid_form.cleaned_data['lastname'],
                                age=kid_form.cleaned_data['age'],
                                gender=kid_form.cleaned_data['gender'],
                            )
                            save_kid.save()

                            context['form'] = KidForm
                            context['message'] = 'شرکت کننده با موفقیت ثبت نام شد'
                            context['kid'] = save_kid
                        else:
                            context['error'] = 'این مشخصات (نام و نام خانوادگی) قبلا ثبت شده'
                            kid_data = Kid.objects.filter(codmeli=code_meli)[0]
                            context['kid'] = kid_data
                    else:
                        context['error'] = 'کد ملی قبلا ثبت شده است'
                        kid_data = Kid.objects.filter(codmeli=code_meli)[0]
                        context['kid'] = kid_data
                else:
                    context['error'] = 'کد ملی وارد شده نامعتبر است، لطفا کد ملی صحیح وارد کنید.'
            else:
                context['error'] = 'کد ملی یا شماره تلفن همراه نادرست وارد شده (کد ملی باید 10 رقم و شماره همراه 11 رقم باشد!)'

        else:
            context['form'] = kid_form

        return render(request, 'base.html', context=context)
