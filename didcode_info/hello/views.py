from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connections
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
        return render(request, 'about.html')

def contact(request):
    return HttpResponse("<h2>Контакты<h2>")

def get_didcode_info(request, DIDCODE):
    # if request.method == "POST":
    data = ""
    with connections['didcode_db'].cursor() as cursor:
        cursor.execute(f"""
                        SELECT u.ID,  
                               u.DIDCODE,
                               u.PART_NUMBER,
                               u.QTY,
                               u.LOT_ID,
                               u.INSERTION_DATETIME,
                               u.INSERTION_USERID,
                               u.UPDATE_DATETIME,
                               u.UPDATE_USER_ID,
                               u.WAREHOUSE
                        FROM users u
                        WHERE u.DIDCODE = '{DIDCODE}'
                        """)
        data = cursor.fetchall()
        json_kek = {
            "ID": data[0][0], 
            "DIDCODE": data[0][1],
            "PART_NUMBER": data[0][2],
            "QTY": data[0][3],
            "LOT_ID": data[0][4],
            "INSERTION_DATETIME": data[0][5],
            "INSERTION_USERID": data[0][6],
            "UPDATE_DATETIME": data[0][7],
            "UPDATE_USER_ID": data[0][8],
            "WAREHOUSE": data[0][9], 
        }
    return JsonResponse(json_kek)

    