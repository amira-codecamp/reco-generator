from django.shortcuts import render
from django.http import HttpResponse
from wkhtmltopdf import render_pdf_from_template

def index(request):
    context = {}
    return render(request, 'reco/templates/index.html', context)

def pdf(request):
    context = {}
    data = request.POST
    context['user'] = data.get('user')
    context['company'] = data.get('company')
    context['email'] = data.get('email')
    context['candidate'] = data.get('candidate')
    context['position'] = data.get('position')
    context['motivation'] = data.get('motivation')
    context['solving'] = data.get('solving')
    context['communication'] = data.get('communication')
    context['teamwork'] = data.get('teamwork')
    context['adaptability'] = data.get('adaptability')
    context['creativity'] = data.get('creativity')
    context['text'] = data.get('text')
    template_name = 'reco/templates/pdf.html'
    cmd_options={'orientation':'Portrait', 'page-size':'A4', 'margin-top':'80px', 'margin-bottom':'80px', 'margin-left':'80px', 'margin-right':'80px'}
    pdf_ = render_pdf_from_template(template_name, header_template=None, footer_template=None, context=context, cmd_options=cmd_options, request=request)
    response = HttpResponse(pdf_, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reference-letter.pdf"'
    return response

def word(request):
    context = {}
    return HttpResponse(request)
