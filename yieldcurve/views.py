
from django.shortcuts import render
from django.http import JsonResponse
import plotly.graph_objects as go
from yieldcurve.models import YieldCurve
from scipy.interpolate import interp1d
import numpy as np

def index(request):
    return render(request, 'index.html')

def yield_curve_by_date(request, selected_date):
    data = YieldCurve.objects.filter(date=selected_date).order_by('maturity')
    if not data.exists():
        return JsonResponse({'error': 'No yieldcurves found'}, status=404)

    maturities = [entry.maturity for entry in data]
    yields = [entry.yield_value for entry in data]

    maturities_numeric = np.arange(len(maturities))
    interp = interp1d(maturities_numeric, yields, kind='cubic')
    smooth_maturities = np.linspace(maturities_numeric.min(), maturities_numeric.max(), 100)
    smooth_yields = interp(smooth_maturities)

# Create your views here.

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=maturities, y=yields, mode ='lines+markers', name='Original Points'))
    fig.add_trace(go.Scatter(x=smooth_maturities, y=smooth_yields, mode='lines', name='Smoothed Curve'))
    fig.update_layout(
        title="Кривая доходности на {selected date}",
        xaxis_title="Maturity",
        yaxis_title="Yield (%)",
        template="plotly_white"
    )

    graph_json = fig.to_plotly_json()

    return JsonResponse(graph_json)