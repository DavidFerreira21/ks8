# Lab 01.11 — Volumes: persistencia via PVC

[← Camada 01](../../README.md) · [Guia de labs](../../../../docs/labs.md)

## Objetivo e hipótese

Um volume efêmero desaparece com o Pod; um PVC pode preservar dados além do ciclo de vida do Pod. Este lab exige um provisionador local funcional.

**Escopo:** cluster Kind `dev` e namespace `lab-01-11`.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
kubectl get nodes
cat trilhas/01-fundamentos/labs/volumes-basico/resources.yaml
```

Preveja o comportamento dos controladores e componentes envolvidos.

## Fase 2 — Aplicar e testar

```bash
make lab-up LAB=01.11
make lab-test LAB=01.11
make lab-observe LAB=01.11
```

**Observe provisionamento do PVC e o Pod:**

```bash
kubectl get pvc,pv -n lab-01-11
kubectl describe pvc dados-pvc -n lab-01-11
kubectl exec -n lab-01-11 pod/escritor -- cat /dados/mensagem.txt
```

**Experimento — excluir Pod não apaga PVC:**

```bash
kubectl delete pod escritor -n lab-01-11
kubectl get pvc dados-pvc -n lab-01-11
kubectl apply -f trilhas/01-fundamentos/labs/volumes-basico/resources.yaml
kubectl wait --for=condition=Ready pod/escritor -n lab-01-11 --timeout=120s
kubectl exec -n lab-01-11 pod/escritor -- cat /dados/mensagem.txt
```

O arquivo pode ser sobrescrito pelo script de inicialização: para provar persistência, antes de excluir o Pod escreva `kubectl exec ... -- sh -c 'echo marcador > /dados/marcador.txt'` e depois leia `marcador.txt` no novo Pod. O Kind requer um StorageClass funcional, normalmente `standard`.

## Fase 3 — Diagnosticar

```bash
kubectl get events -n lab-01-11 --sort-by=.lastTimestamp
kubectl get all -n lab-01-11
```

Observe eventos, `spec` e `status`; anote evidências do experimento. O check automático não é uma prova de comportamento de ponta a ponta.

## Fase 4 — Limpar

```bash
make lab-down LAB=01.11
make lab-status LAB=01.11
```

O namespace é preservado; não utilize `make down` para limpar um único exercício.

## Checklist

- [ ] Expliquei os objetos do manifesto.
- [ ] Comparei hipótese com observação real.
- [ ] Investiguei eventos e condições relevantes.
- [ ] Limpei os recursos do exercício.
