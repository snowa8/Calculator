from django.shortcuts import render
import math
import sympy as sp


def calculate(request):
    result = None
    error = None

    if request.method == "POST":
        expression = request.POST.get("expression", "")

        try:
            if expression.isdigit():
                result = math.sqrt(float(expression))
            else:
                x = sp.symbols('x')
                expr = sp.sympify(expression)
                result = expr.evalf()
        except Exception as e:
            error = f"Так нельзя, я тебе запрещаю, потому что: {str(e)}"

    return render(request, 'app/index.html', {'result': result, 'error': error})
