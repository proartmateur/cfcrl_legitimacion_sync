from dataclasses import dataclass


def parse_null(val: str):
    if val is None:
        return None

    if val.upper() == "NULL":
        return None
    if val == '':
        return None


@dataclass
class RespuestaInspector:
    id_respuesta: str
    id_cita: str
    id_pregunta: str
    Respuesta: bool
    Observaciones: str
    no_oficio_designacion: str
    fecha_desginacion: str
    no_trab_derecho_voto: str
    votos_emitidos: str
    votos_a_favor: str
    votos_en_contra: str
    votos_validos: str
    votos_nulos: str
    manifestaron_contrato: str
    no_manifestaron_contrato: str
    total_consultado: str
    file_evidencia: str
    sys_fec_insert: str

    def normalize(self):
        self.Respuesta = bool(self.Respuesta)
        self.Observaciones = parse_null(self.Observaciones)
        self.Observaciones = parse_null(self.Observaciones)
        self.no_oficio_designacion = parse_null(self.no_oficio_designacion)
        self.fecha_desginacion = parse_null(self.fecha_desginacion)
        self.no_trab_derecho_voto = parse_null(self.no_trab_derecho_voto)
        self.votos_emitidos = parse_null(self.votos_emitidos)
        self.votos_a_favor = parse_null(self.votos_a_favor)
        self.votos_en_contra = parse_null(self.votos_en_contra)
        self.votos_validos = parse_null(self.votos_validos)
        self.votos_nulos = parse_null(self.votos_nulos)
        self.manifestaron_contrato = parse_null(self.manifestaron_contrato)
        self.no_manifestaron_contrato = parse_null(self.no_manifestaron_contrato)
        self.total_consultado = parse_null(self.total_consultado)
        self.file_evidencia = parse_null(self.file_evidencia)
        self.sys_fec_insert = parse_null(self.sys_fec_insert)

    def is_equal(self, respuesta_inspector) -> bool:
        conditions = []
        conditions.append(self.id_respuesta == respuesta_inspector.id_respuesta)
        conditions.append(self.id_cita == respuesta_inspector.id_cita)
        conditions.append(self.id_pregunta == respuesta_inspector.id_pregunta)
        conditions.append(self.Respuesta == respuesta_inspector.Respuesta)
        conditions.append(self.Observaciones == respuesta_inspector.Observaciones)
        conditions.append(self.no_oficio_designacion == respuesta_inspector.no_oficio_designacion)
        conditions.append(self.fecha_desginacion == respuesta_inspector.fecha_desginacion)
        conditions.append(self.no_trab_derecho_voto == respuesta_inspector.no_trab_derecho_voto)
        conditions.append(self.votos_emitidos == respuesta_inspector.votos_emitidos)
        conditions.append(self.votos_a_favor == respuesta_inspector.votos_a_favor)
        conditions.append(self.votos_en_contra == respuesta_inspector.votos_en_contra)
        conditions.append(self.votos_validos == respuesta_inspector.votos_validos)
        conditions.append(self.votos_nulos == respuesta_inspector.votos_nulos)
        conditions.append(self.manifestaron_contrato == respuesta_inspector.manifestaron_contrato)
        conditions.append(self.no_manifestaron_contrato == respuesta_inspector.no_manifestaron_contrato)
        conditions.append(self.total_consultado == respuesta_inspector.total_consultado)
        conditions.append(self.file_evidencia == respuesta_inspector.file_evidencia)
        conditions.append(self.sys_fec_insert == respuesta_inspector.sys_fec_insert)

        for condition in conditions:
            if not condition:
                return False

        return True

    def diferencias(self, respuesta_inspector):
        my = self.to_dict()
        other = respuesta_inspector.to_dict()
        diferences = []

        for k in my:
            is_diferent = my[k] != other[k]
            # print(k, " != ", is_diferent)
            if is_diferent:
                diferences.append({
                    "key": k,
                    "self": my[k],
                    "new": other[k]
                })
        return diferences

    # region Serialization
    def to_dict(self):
        return {
            "id_respuesta": self.id_respuesta,
            "id_cita": self.id_cita,
            "id_pregunta": self.id_pregunta,
            "Respuesta": self.Respuesta,
            "Observaciones": self.Observaciones,
            "no_oficio_designacion": self.no_oficio_designacion,
            "fecha_desginacion": self.fecha_desginacion,
            "no_trab_derecho_voto": self.no_trab_derecho_voto,
            "votos_emitidos": self.votos_emitidos,
            "votos_a_favor": self.votos_a_favor,
            "votos_en_contra": self.votos_en_contra,
            "votos_validos": self.votos_validos,
            "votos_nulos": self.votos_nulos,
            "manifestaron_contrato": self.manifestaron_contrato,
            "no_manifestaron_contrato": self.no_manifestaron_contrato,
            "total_consultado": self.total_consultado,
            "file_evidencia": self.file_evidencia,
            "sys_fec_insert": self.sys_fec_insert
        }
    # endregion
