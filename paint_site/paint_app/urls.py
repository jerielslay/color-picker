from django.urls import path
from paint_app.views import ColorPickerView

urlpatterns=[
    path('', ColorPickerView.as_view(), name='paint'),
]