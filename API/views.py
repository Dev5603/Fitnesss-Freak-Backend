import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import News, Contact, Membership, PT

# Create your views here.
def news(request):
    try:
        news = News.objects.all()
        news = [new.serialize() for new in news]

        return JsonResponse({
            'news': news
        }, status=200)
    except News.DoesNotExist():
        return JsonResponse({
            'error': 'Something went wrong'
        }, status=400)

@csrf_exempt
def contact(request):
    try:
        data = json.loads(request.body)

        name = data.get('name')
        number = data.get('number')
        email = data.get('email')

        if name and number and email:
            newContact = Contact(
                name = name,
                number = number,
                email = email
            )
            newContact.save()


            return JsonResponse({
                'message': 'Contact added successfully'
            }, status=201)
        
        else:
            return JsonResponse({
                'error': 'Data not valid'
            })
    except Contact.DoesNotExist:
        return JsonResponse({
            'error': 'Something went wrong'
        }, status=400)
    
def plans(request):
    try:
        membership_plans = Membership.objects.all()
        membership_plans = [membership.serialize() for membership in membership_plans]

        pt_plans = PT.objects.all()
        pt_plans = [pt_plan.serialize() for pt_plan in pt_plans]

        return JsonResponse({
            'plans': {
                'membership': membership_plans,
                'pt' : pt_plans
            }
        })
    except Membership.DoesNotExist() or PT.DoesNotExist():
        return JsonResponse({
            'error': 'Something went wrong'
        }, status=400)