totalsequencias = str(input('Digite todas as sequêcias separadas por espaço, para comparação:'))
divisequencias = totalsequencias.split()

sequenciaatual = 'Null'
numsequencias = len(divisequencias)

for c in range (0,numsequencias):
    sequenciacomp = divisequencias[c]
    if c==0:
        sequenciaatual = divisequencias[0]
    else:
        for i in range(0,len(divisequencias[c])):
            if sequenciaatual.find((sequenciacomp[0:i])) == -1:
                sequenciasep = sequenciacomp[i-1:len(sequenciacomp)]
                if sequenciaatual.find((sequenciasep))== -1:
                    sequenciaatual = sequenciaatual + sequenciasep



print(sequenciaatual)