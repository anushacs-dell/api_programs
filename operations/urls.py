from django.urls import path
from .views import *

urlpatterns = [
    path('calculator',CalculatorView.as_view()),
    path('substract',SubstractView.as_view()),
    path('multi',MultipleView.as_view()),
    path('division',DivisionView.as_view()),
    path('fact',FactorialView.as_view()),
    path('prime',PrimeNumberView.as_view()),
    path('largest',AddinView.as_view()),
]
