from django.shortcuts import render


# Main page
def head_page(request):
    return render(request, 'base.html')


# Shop
def puzzles_dict(request):
    title = 'Магазин головоломок'

    puzzle_products = {
        '1': 'Головоломка No1',
        '2': 'Головоломка No2',
        '3': 'Головоломка No3',
        '4': 'Головоломка No4',
    }
    return render(request, 'puzzle_shop.html', {'title': title, 'puzzle_products': puzzle_products})


# Basket
def basket(request):
    # Basket
    initial_info = "В корзине пока пусто. Головоломки ждут вас!"
    return render(request, 'puzzle.html', {'initial_information': initial_info})
