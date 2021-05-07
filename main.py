import csv
import os
import shelve
from pathlib import Path
from dataclasses import dataclass
from typing import List

from RespuestaInspector import RespuestaInspector
from cambio_respuesta_inspectores import CambioRespuestaInspectores
from summary_cambios_respuesta_inspectores import SummaryCambiosRespuestaInspectores


def traverse_large_file(file_path):
    with open(file_path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            yield RespuestaInspector(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                row[8],
                row[9],
                row[10],
                row[11],
                row[12],
                row[13],
                row[14],
                row[15],
                row[16],
                row[17],
            )


def traverse_large_file_full(file_path):
    with open(file_path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        items = []
        for row in spamreader:
            item = RespuestaInspector(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                row[8],
                row[9],
                row[10],
                row[11],
                row[12],
                row[13],
                row[14],
                row[15],
                row[16],
                row[17],
            )
            items.append(item)

        return items


def index_large_file_by_id(respuesta_inspector: RespuestaInspector, db_name: str):
    with shelve.open(f'{db_name}') as db:
        db[str(respuesta_inspector.id_respuesta)] = respuesta_inspector


def analize_csv(csv: str):
    stps_version_file = csv
    stps_items = traverse_large_file(stps_version_file)
    not_null = []
    for respuesta_inspector in stps_items:
        if respuesta_inspector.no_trab_derecho_voto != "NULL":
            not_null.append(respuesta_inspector.no_trab_derecho_voto)
    print(f"Se encontró {len(not_null)} valores")


def buscar_cambios_cfcrl_vs_stps(csv_cfcrl: str, db_name_stps: str,
                                 max_items: int) -> SummaryCambiosRespuestaInspectores:
    stps_version_file = csv_cfcrl
    stps_items = traverse_large_file(stps_version_file)
    not_null = []
    count = 0
    max_items = max_items
    cambios_log: List[CambioRespuestaInspectores] = []
    no_existentes: List[str] = []
    mal_formados: List[str] = []

    for respuesta_inspector in stps_items:
        respuesta_inspector.normalize()
        if count > 0:
            # Buscar el item
            # print(respuesta_inspector.id_respuesta)
            try:
                item = find_respuesta(respuesta_inspector.id_respuesta, db_name_stps)
                item.normalize()
            except:
                print(f"---Mal Formado: {count}---")
                print("     ", respuesta_inspector.id_respuesta)
                mal_formados.append(respuesta_inspector.id_respuesta)

            if item.id_respuesta is not None:
                # print(f"Existe {item.id_respuesta}")
                es_igual = respuesta_inspector.is_equal(item)
                es_igual2 = respuesta_inspector == item
                # print(f" Es igual: {es_igual} - {es_igual2}")
                if not es_igual:
                    # print(f" Es igual: {es_igual}")
                    cambios = respuesta_inspector.diferencias(item)
                    change = CambioRespuestaInspectores(respuesta_inspector.id_respuesta, cambios)
                    cambios_log.append(change)
                    # print("   ",change)
            else:
                print(f"No Existe: {respuesta_inspector.id_respuesta}")
                no_existentes.append(respuesta_inspector.id_respuesta)

        count += 1
        if count > max_items:
            break

    return SummaryCambiosRespuestaInspectores(
        count,
        len(cambios_log),
        cambios_log,
        no_existentes,
        mal_formados
    )


def make_indexed_db(csv: str):
    stps_version_file = csv
    stps_items = traverse_large_file(stps_version_file)
    name_db_shelve = db_name_from_file(stps_version_file)
    max_items = 1000_000_000_000_000
    count = 0
    for respuesta_inspector in stps_items:
        if count > 0:
            # print(respuesta_inspector)
            index_large_file_by_id(respuesta_inspector, name_db_shelve)
        count += 1
        if count > max_items:
            break


def db_name_from_file(file_name: str):
    f_ext = Path(file_name).suffix
    f_name = os.path.basename(file_name).replace(f_ext, "")
    return f_name + ".db"


def find_respuesta(id, db_name) -> RespuestaInspector:
    with shelve.open(db_name) as shelf:
        return shelf[str(id)]

    return RespuestaInspector(
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None
    )


if __name__ == "__main__":
    csv_name_stps = "memo_tabla_respuesta_inspectores.csv"
    # make_indexed_db(csv_name)
    #
    # respuesta = find_respuesta("500", db_name_from_file(csv_name))
    # print(respuesta)

    db_indexed = db_name_from_file(csv_name_stps)
    csv_name_cfcrl = "cfcrl_respuesta_inspectores_2.csv"
    summary = buscar_cambios_cfcrl_vs_stps(csv_name_cfcrl, db_indexed, 250_000)
    print(summary.reporte())
