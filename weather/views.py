from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def result(request):
    result = None
    if request.method == 'POST':
        temp_max = float(request.POST.get('temp_max'))

        # Simple logic based on patterns from seattle-weather.csv
        if temp_max > 30:
            result = 'sun'
        elif temp_max > 20:
            result = 'drizzle'
        elif temp_max > 10:
            result = 'rain'
        else:
            result = 'snow'

    return render(request, 'result.html', {'result': result})