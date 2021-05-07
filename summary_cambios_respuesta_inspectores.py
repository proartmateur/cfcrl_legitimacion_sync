from dataclasses import dataclass
from typing import List

from cambio_respuesta_inspectores import CambioRespuestaInspectores


@dataclass
class SummaryCambiosRespuestaInspectores:
    total_analizado: int
    total_cambios: int
    cambios: List[CambioRespuestaInspectores]
    no_existentes: List[str]
    mal_formados: List[str]

    def porcentaje_cambios(self):
        return (self.total_cambios * 100) / self.total_analizado

    def porcentaje_cambios_human(self):
        return f"{self.total_cambios} / {self.total_analizado} = {self.porcentaje_cambios()}%"

    def reporte(self):
        return f"""Summary:
    Con cambios: {self.porcentaje_cambios_human()}
    No existentes: {len(self.no_existentes)}
    Mal Formados: {len(self.mal_formados)} 
"""