import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

# CACHING IN FUNCTION BASE VIEW

# @cache_page(5 * 60)
# def say_hello(request):
#     key = 'httpbin_result'
#     if cache.get(key) is None:
#         response = request.get('https//httpbin.org/delay/2')
#         data = response.json()
#         return render(request, 'hello.html', {'name': cache.get(key)})


# CACHING IN CLASSBASE VIEW

class HelloView(APIView):
    def get(self, request):
        response = request.get('https//httpbin.org/delay/2')
        data = response.json()
        return render(request, 'hello.html', {'name': 'Mosh'})


@csrf_exempt
def chat(request):
    if request.method != "POST":
        return JsonResponse({"detail": "Method not allowed"}, status=405)

    try:
        body = json.loads(request.body.decode("utf-8") or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"detail": "Invalid JSON"}, status=400)

    prompt = str(body.get("prompt", "")).strip()
    if not prompt:
        return JsonResponse({"detail": "Prompt is required"}, status=400)

    return JsonResponse({
        "message": (
            "Thanks for reaching out to PerfectHomes. "
            "Tell us your preferred location, budget, and property type, "
            "and our team will help match you with available homes."
        )
    })
