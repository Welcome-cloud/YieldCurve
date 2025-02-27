
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import plotly.graph_objects as go
from yieldcurve.models import YieldCurve


def index(request):

    return render(request, "index.html")

#def index(request):
    #return HttpResponse("Hello, Django is working!")

def yield_curve_by_date(request):
    try:
        dates = request.GET.getlist('dates[]')
        if not dates:
            print("Список дат пустой")
            return JsonResponse({"error": "Не выбрана ни одна дата"}, status=400)

        print(f"Полученные даты: {dates}")


        fig = go.Figure()
        for date in dates:
            try:
                record = YieldCurve.objects.get(date=date)
                print(f"Данные для даты {date}: {record}")
                maturities_in_years = [
                    1/365, 7/365, 14/365, 28/365, 91/365,
                    182/365, 1, 2, 3, 5, 7, 10
                ]


                yields= [
                    record.ytm_1d, record.ytm_7d, record.ytm_14d, record.ytm_28d, record.ytm_91d,
                    record.ytm_182d, record.ytm_12m, record.ytm_2y, record.ytm_3y,
                    record.ytm_5y, record.ytm_7y, record.ytm_10y,
                ]

                name_for_legend=f"{str(date)}"
                print(f"Добавляю график с именем: {name_for_legend}")

                yields =[y if y is not None else 0 for y in yields]

                print(f"Доходности для {date}: {yields}")

   #
                fig.add_trace(go.Scatter(x=maturities_in_years, y=yields, mode ='lines+markers', name=name_for_legend))
            except YieldCurve.DoesNotExist:
                print (f"Данные для даты {date} отсутствуют")
                continue
        #fig.add_trace(go.Scatter(x=x_new, y=y_smooth, mode='lines', name='Smoothed Curve'))
        fig.update_layout(
            xaxis_title="Срок до погашения",
            yaxis_title="Доходность (%)",
            template="plotly_white",
            #weidth=700,
            #height=400,
            xaxis=dict(
                tickvals=[
                    1/365, 7/365, 14/365, 28/365, 91/365,
                    182/365, 1, 2, 3, 5, 7, 10
                ],
                ticktext=[
                    "1д", " ", " ", " ", "3м",
                    "6м", "1г", "2г", "3г", "5л", "7л", "10л"
                ],
                tickangle=30,
                tickfont=dict(
                    family="Arial, sans-serif",
                    size=12,
                    color="black"
                )
            )
        )

        return JsonResponse(fig.to_plotly_json(), safe=False)
    except Exception as e:
        print(f"Ошибка: {e}")
        return JsonResponse({'error': str(e)}, status=500)
