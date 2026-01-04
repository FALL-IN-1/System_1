from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def every_place(request):
    """List all restaurant"""

    return HttpResponse(
        """
        <h1>Restaurant List<h1>
        <ul>
        <li>Pizza Bari</li>
        <li> Meatbox Bari </li>
        </ul>
        """
    )