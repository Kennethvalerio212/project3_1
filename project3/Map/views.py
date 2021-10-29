from django.shortcuts import render
import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?" 
key = "yPfDRcQKBMOkOjMAG3WtXIzcCmmI0t5j"



def home(request):
    InputOrig=request.POST.get('inputlocation')
    InputDest=request.POST.get('inputDestination')
    

    url = main_api + urllib.pterarse.urlencode({"key": key, "from":InputOrig, "to":InputDest})
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        Trip_Duration=json_data["route"]["formattedTime"] 
        KM=str("{:.2f}".format((json_data["route"]["distance"])*1.61))
        Fuel=str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78))
        
            'loc':InputOrig,
            'dest':InputDest,
            'Trip':Trip_Duration,
            'KM': KM,
            'Fuel':Fuel
        return render(request, 'maps/home.html',context)


def about(request):
    return render(request, 'maps/about.html', {'title': 'About'})