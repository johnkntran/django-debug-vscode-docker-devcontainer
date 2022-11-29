from django.http import JsonResponse


def some_endpoint(request):
    msg = 'Hello, World!' # TODO: Set breakpoint here to test debugging
    return JsonResponse({'msg': msg})
