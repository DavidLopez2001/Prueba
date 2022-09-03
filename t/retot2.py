
SalarioBase, CantidadHorasExtra, Bonificaciones = input().split()
SalarioBase = float(SalarioBase)
CantidadHorasExtra = int(CantidadHorasExtra)
Bonificaciones = int(Bonificaciones)

ValorHoraTrabajo = SalarioBase/192
ValorHorasExtra = (CantidadHorasExtra * (ValorHoraTrabajo*0.25))+(ValorHoraTrabajo * CantidadHorasExtra)

ValorBonificaciones = 0

if(Bonificaciones == 1):
    ValorBonificaciones = SalarioBase * 0.05

SalarioTotal = SalarioBase + ValorHorasExtra + ValorBonificaciones

PlanObligatorioSalud = SalarioTotal * 0.035
AportePension = SalarioTotal * 0.04
CajaCompensacion = SalarioTotal * 0.01

Total =SalarioTotal- (PlanObligatorioSalud + AportePension + CajaCompensacion)

print(round(Total, 1))