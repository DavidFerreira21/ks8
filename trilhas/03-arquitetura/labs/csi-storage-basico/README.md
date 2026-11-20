# Lab 03.15 — CSI e Storage

[← Aula 03.15](../../csi-storage/README.md) · [↑ Camada 03](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=03.15` prepara namespace e starter incompleto. Complete `.labs/03.15/resources.yaml`, aplique com `kubectl apply -f .labs/03.15/`, observe e valide. `make lab-up` usa a solução e é exclusivo da CI.

## Objetivo e hipótese

Verificar PVC Bound e persistência de arquivo quando o Pod consumidor é recriado.

**Pré-requisitos:** `kind-dev`, `kubectl`, `make`, namespace `lab-03-15`. Depende de StorageClass funcional. O Kind pode usar provisionador local, não necessariamente um driver CSI.

## Desafio — o que você vai construir

Crie PVC `dados` solicitando 256Mi ReadWriteOnce e Pod `escritor` BusyBox que monta o PVC em `/dados`, grava um marcador somente se não existir e permanece ativo.

Preveja o resultado antes de consultar `solution/`. A documentação oficial é a referência para esclarecer recursos e campos.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=03.15
cat .labs/03.15/resources.yaml
```

## Fase 2 — Aplicar e observar

Complete os TODOs e execute:

```bash
kubectl apply -f .labs/03.15/
make lab-test LAB=03.15
make lab-observe LAB=03.15
```

Inspecione PVC, PV e StorageClass com `kubectl get pvc dados -n lab-03-15 -o wide` e `kubectl get storageclass`.

## Fase 3 — Experimento controlado

Registre `kubectl exec -n lab-03-15 escritor -- cat /dados/marcador.txt`; exclua somente o Pod com `kubectl delete pod escritor -n lab-03-15` e reaplique o YAML. Compare arquivo e vínculo PVC.

### Comprovar persistência, não apenas vínculo

```bash
kubectl get pvc dados -n lab-03-15 -o wide
kubectl exec -n lab-03-15 escritor -- cat /dados/marcador.txt
kubectl delete pod escritor -n lab-03-15
kubectl apply -f .labs/03.15/resources.yaml
kubectl wait pod/escritor -n lab-03-15 --for=condition=Ready --timeout=120s
kubectl exec -n lab-03-15 escritor -- cat /dados/marcador.txt
```

Se o arquivo persistir, prove o comportamento de volume. **Não declare CSI funcional** sem confirmar `PV.spec.csi.driver`. Para utilizar um driver de exemplo realmente CSI, consulte o [experimento opcional com CSI Hostpath](experiments/README.md), exclusivo do Kind descartável.

## Resultado esperado e evidências

Com provisionador local funcional, PVC chega a Bound e o marcador permanece após recriar apenas o Pod. Se não houver StorageClass, classifique como dependência não atendida.

**Evidências específicas:** registre PVC Bound, PV/StorageClass associado, conteúdo do marcador antes/depois e a distinção entre provisionador CSI e hostPath/local.

## Fase 4 — Diagnosticar

Investigue `kubectl describe`, eventos, status, selectors e dependências do ambiente. Identifique o primeiro sinal causal; não confunda ausência de um addon com erro do YAML principal.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=03.15
make lab-status LAB=03.15
```

O namespace permanece preservado. Reverta recursos temporários não declarados no contrato; não execute `make down`.

## Critérios de conclusão

- [ ] Escrevi o YAML sem copiar a solução.
- [ ] **Critério exclusivo 03.15:** registre PVC Bound, PV/StorageClass associado, conteúdo do marcador antes/depois e a distinção entre provisionador CSI e hostPath/local.
- [ ] Expliquei a diferença entre estado declarado e comportamento comprovado.
- [ ] Reverti experimentos e limpei o laboratório.

## Perguntas de diagnóstico e reflexão

- Qual diferença existe entre PVC, PV e driver CSI?
- Por que o estado Bound sozinho é insuficiente?
- Que risco há na política de reclaim ao excluir o PVC?

## Aprofunde seus conhecimentos

[Documentação Kubernetes](https://kubernetes.io/docs/concepts/storage/volumes/#csi) · [Aula 03.15](../../csi-storage/README.md)

---

[← Lab 03.14](../coredns-basico/README.md) · [↑ Aula 03.15](../../csi-storage/README.md) · [↑ Camada 03](../../README.md) · [Próximo: Lab 03.16 →](../gateway-api-basico/README.md)
