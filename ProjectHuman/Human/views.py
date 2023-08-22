from django.shortcuts import render, get_object_or_404, redirect

from .models import Human, Profession
from .forms import HumanForm

def index(request):
    human = Human.objects.all()
    professions = Profession.objects.all()
    context = {
        'human': human,
        'name': 'Список профессий',

    }
    return render(request, 'Human/index.html', context=context)

def get_profession(request, profession_id):
    human = Human.objects.filter(profession_id=profession_id)
    professions = Profession.objects.all()
    profession = Profession.objects.get(pk=profession_id)
    context = {
        'human': human,
        'profession': profession
    }
    return render(request, 'Human/profession.html', context=context)


def view_human(request, human_id):
    # human_item = Human.objects.get(pk=human_id)
    human_item = get_object_or_404(Human, pk=human_id)
    context = {
        'human_item': human_item
    }
    return render(request, 'Human/view_human.html', context=context)

def add_human(request):
    if request.method == 'POST':
        form = HumanForm(request.POST)
        if form.is_valid():
            # human = Human.objects.create(**form.cleaned_data)
            human = form.save()
            return redirect(human)
    else:
        form = HumanForm()
    return render(request, 'Human/add_human.html', {'form': form})
