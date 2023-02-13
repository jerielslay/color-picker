from django.shortcuts import render
from django.views import View
from paint_app.forms import ColorPickerForm

class ColorPickerView(View):
    def get(self, request):
        color_form = ColorPickerForm()
        
        red_value=255,
        green_value=255,
        blue_value=255,

        context = {
            'form': color_form,
            'red': red_value,
            'green': green_value,
            'blue': blue_value
        }
        return render(
            request=request, 
            template_name='color_picker.html', 
            context = context
            )

    def post(self, request):
        color_form = ColorPickerForm() #can pur request.POST and the numbers will stay in the boxs 
        red_value= int(request.POST('red_amount'))
        green_value= int(request.POST('green_amount'))
        blue_value= int(request.POST('blue_amount'))

        context = {
            'form': color_form,
            'red': red_value,
            'green': green_value,
            'blue': blue_value
        }
        return render(
            request=request, 
            template_name='color_picker.html', 
            context = context
            )