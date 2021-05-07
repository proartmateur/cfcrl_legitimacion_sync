import pandas as pd

memo_db=pd.read_csv("venv/memo_tabla_respuesta_inspectores.csv", encoding="latin8")
cfcrl_db=pd.read_csv("venv/cfcrl_tabla_respuesta_inspectores.csv", encoding="latin8")

Filas1=len(memo_db.index)
Filas2=len(cfcrl_db)

print('memo: '+str(Filas1)+'  cfcrl:'+str(Filas2))

