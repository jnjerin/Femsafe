from django.shortcuts import render

# Create your views here.
import africastalking
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Set up Africa's Talking API credentials
username = "fgm123"
api_key = "543aee87c11c94508566fcde4e5e9397a0c70410974795ea993852b01b295da9"
africastalking.initialize(username, api_key)

# Create a new USSD service
ussd_service = africastalking.USSD

@csrf_exempt
def ussd_callback(request):
    # Get the user's input from the USSD request
    user_input = request.POST.get('text', '').strip()

    # Define the USSD menu
    menu = {
        '1': {
            'text': 'Chagua lugha yako:\n1. Kiswahili\n2. English\n3. Somali',
            'next': {
                '1': 'Kiswahili',
                '2': 'English',
                '3': 'Somali’'
            }
        },
        'menu_2': {
            'text': 'Chagua kitendo unachotaka kufanya:\n1. Ripoti kisa cha FGM\n2. Pata Skiza tune',
            'next': {
                '1': 'menu_3',
                '2': 'menu_skiza'
            }
        },
        'menu_3': {
            'text': 'Tafadhali chagua eneo ulipo:\n1. Mandera\n2. Mombasa\n3. Kajiado\n4. Isiolo\n5. Narok\n 6. Other',
            'next': {
                '1': 'Mandera',
                '2': 'Mombasa',
                '3': 'Kajiado',
                '4': 'Isiolo',
                '5': 'Narok',
                '6': 'Other',
            }
        },
        'menu_4': {
            'text': 'Tafadhali chagua huduma unayohitaji:\n1. Pata mahali pa kulala\n2. Pata msaada wa matibabu\n3. Piga simu na mtu',
            'next': {
                '1': 'Pata mahali pa kulala',
                '2': 'Pata msaada wa matibabu',
                '3': 'Piga simu na mtu'
            }
        },
        'menu_skiza': {
            'text': 'Unaweza kupata Skiza tune yako kwa kupiga *811#',
            'next': None
        },
        'menu_end': {
            'text': 'Asante kwa kutumia huduma yetu.',
            'next': None
        }
    }

    # Handle the USSD request and get the response
    response = ussd_service.handle(user_input, menu=menu)

    # Return the response as an HTTP response
    return HttpResponse(str(response))
