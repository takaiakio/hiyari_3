from django.shortcuts import render, get_object_or_404, redirect
from .models import NearMissReport
from .forms import NearMissReportForm
import csv
from django.http import HttpResponse
import io

def report_list(request):
    reports = NearMissReport.objects.all()
    return render(request, 'survey/report_list.html', {'reports': reports})

def report_detail(request, pk):
    report = get_object_or_404(NearMissReport, pk=pk)
    return render(request, 'survey/report_detail.html', {'report': report})

def report_edit(request, pk):
    report = get_object_or_404(NearMissReport, pk=pk)
    if request.method == 'POST':
        form = NearMissReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('report_list')
    else:
        form = NearMissReportForm(instance=report)
    return render(request, 'survey/report_edit.html', {'form': form})

def report_delete(request, pk):
    report = get_object_or_404(NearMissReport, pk=pk)
    if request.method == 'POST':
        report.delete()
        return redirect('report_list')
    return render(request, 'survey/report_confirm_delete.html', {'report': report})



'''def export_csv(request):
    # BytesIOを使ってメモリ上のバイナリファイルを作成
    output = io.BytesIO()
    
    # CSV writerを作成し、エンコーディングを指定して書き込み
    wrapper = io.TextIOWrapper(output, encoding='utf-8-sig')
    writer = csv.writer(wrapper, dialect='excel')

    # ヘッダーの書き込み
    writer.writerow(['題名', '遭遇場面', '遭遇頻度', 'ミス回避策'])

    # データの取得と書き込み
    reports = NearMissReport.objects.all()
    for report in reports:
        writer.writerow([report.title, report.description, report.frequency, report.mitigation])

    # バッファをフラッシュして、CSV内容をHTTPレスポンスに設定
    wrapper.flush()
    response = HttpResponse(output.getvalue(), content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=near_miss_reports.csv'

    # BytesIOのバッファをクローズ
    output.close()

    return response'''

def export_csv(request):
    # BytesIOを使ってメモリ上のバイナリファイルを作成
    output = io.BytesIO()
    
    # TextIOWrapperを使ってエンコーディングを指定
    wrapper = io.TextIOWrapper(output, encoding='utf-8-sig', newline='')
    writer = csv.writer(wrapper, dialect='excel')

    # ヘッダーの書き込み
    writer.writerow(['題名', '遭遇場面', '遭遇頻度', '回避事由'])

    # データの取得と書き込み
    reports = NearMissReport.objects.all()
    for report in reports:
        writer.writerow([report.title, report.description, report.frequency, report.mitigation])

    # バッファをフラッシュして、CSV内容をHTTPレスポンスに設定
    wrapper.flush()
    response = HttpResponse(output.getvalue(), content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=near_miss_reports.csv'

    # BytesIOのバッファをクローズ
    output.close()

    return response




def report_create(request):
    if request.method == 'POST':
        form = NearMissReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report_list')
    else:
        form = NearMissReportForm()
    return render(request, 'survey/report_form.html', {'form': form})
