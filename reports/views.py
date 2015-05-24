from django.shortcuts import redirect, render
from reports.models import Report

def home_page(request):
    return render(request, 'home.html')

def view_report(request):
    reports = Report.objects.all()
    return render(request, 'report.html', {'reports': reports})

def new_report(request):
    Report.objects.create(text=request.POST['report_text'])
    return redirect('/reports/the-only-report-in-the-world/')