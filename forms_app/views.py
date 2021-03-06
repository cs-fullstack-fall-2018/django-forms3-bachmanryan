from django.shortcuts import render, redirect, get_object_or_404
from .forms import Forms, OtherForms
from .models import FormModel, NonProfitModel


def index(request):
    form_list = FormModel.objects.all()
    context = {'form_list': form_list}
    return render(request, 'forms_app/index.html', context)


def otherindex(request):
    other_form_list = NonProfitModel.objects.all()
    other_context = {'other_form_list': other_form_list}
    return render(request, 'forms_app/index.html', other_context)


def otheradd(request):
    if(request.method == 'POST'):
        form = OtherForms(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('otherindex')
    else:
        form = OtherForms()
    return render(request, 'forms_app/addRecipe.html', {'form': form})


def add(request):
    if (request.method == 'POST'):
        form = Forms(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect("index")
    else:
        form = Forms()
    return render(request, 'forms_app/addRecipe.html', {'form': form})


def edit(request, pk):
    theModel = get_object_or_404(FormModel, pk=pk)

    if (request.method == 'POST'):
        form = Forms(request.POST, instance=theModel)
        if (form.is_valid()):
            form.save()
            return redirect("index")
        else:
            print("Hey buddy. It looks like your form was invalid. Sorry about that...")
            return redirect("edit", pk=pk)
    else:
        form = Forms(instance=theModel)
    return render(request, 'forms_app/addRecipe.html', {'form': form})


def otheredit(request, pk):
    myModel = get_object_or_404(NonProfitModel, pk=pk)

    if (request.method == 'POST'):
        form = OtherForms(request.POST, instance=myModel)
        if (form.is_valid()):
            form.save()
            return redirect("base")
        else:
            print("invalid")
            return redirect("otheredit", pk=pk)
    else:
        form = OtherForms(instance=myModel)
    return render(request, 'forms_app/addRecipe.html', {'form': form})
