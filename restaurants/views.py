from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
    context = {
        "my_list":[
            {
                'name':'Macdonalds',
                'food_type':'Junk Food',
            },
            {
                'name':'99 Grill',
                'food_type':'Burgers',
            },
            {
                'name':'Subway',
                'food_type':'Healthy Food',
            },
        ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):
    context = {
        "my_object":{
                        'name':'99 Grill',
                        'food_type':'Burgers.',
                    },
    }
    return render(request, 'detail.html', context)
