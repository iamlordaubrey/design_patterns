from kpis import KPIs
from current_kpis import CurrentKPIs
from forecast_kpis import ForecastKPIs

kpis = KPIs()
currentKPIs = CurrentKPIs(kpis)
forecastKPIs = ForecastKPIs(kpis)

kpis.set_kpis(25, 10, 5)
kpis.set_kpis(100, 50, 30)
kpis.set_kpis(50, 10, 20)

print('\n***Detaching the currentKPIs observer.***\n')
kpis.detach(currentKPIs)

kpis.set_kpis(150, 110, 120)

