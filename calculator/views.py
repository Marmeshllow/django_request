from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def omlet(request):
    servings = int(request.GET.get('servings', 1))
    recipe = {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5
    }
    for key, val in recipe.items():
        recipe[key] = val * servings
    context = {
        'recipe': recipe,
        'name': 'Омлет',
    }
    return render(request, 'calculator/index.html', context)


def pasta(request):
    servings = int(request.GET.get('servings', 1))
    recipe = {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    }
    for key, val in recipe.items():
        recipe[key] = val * servings
    context = {
        'recipe': recipe,
        'name': 'Паста',
    }
    return render(request, 'calculator/index.html', context)


def buter(request):
    servings = int(request.GET.get('servings', 1))
    recipe = {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }
    for key, val in recipe.items():
        recipe[key] = val * servings
    context = {
        'recipe': recipe,
        'name': 'Бутербродик',
    }
    return render(request, 'calculator/index.html', context)
