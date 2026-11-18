# Lab 01.11 — Volumes

[← Aula 01.11](../../volumes/README.md) · [↑ Camada 01](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)
> **MODO DESAFIO:** execute `make lab-prepare LAB=01.11`, complete `.labs/01.11/claim.yaml` e `.labs/01.11/pod.yaml` e execute **`kubectl apply -f .labs/01.11/`**. Só depois valide com `make lab-test LAB=01.11`. `make lab-up` aplica a solução completa e fica reservado à CI; `make lab-solution LAB=01.11` revela seus arquivos para estudo posterior.


## Objetivo e hipótese

Um volume efêmero desaparece com o Pod; um PVC pode preservar dados além do ciclo de vida do Pod. Este lab exige um provisionador local funcional.

**Escopo:** cluster Kind `dev` e namespace `lab-01-11`.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
kubectl get nodes
make lab-prepare LAB=01.11
cat .labs/01.11/claim.yaml
cat .labs/01.11/pod.yaml
```

Preveja o comportamento dos controladores e componentes envolvidos.

## Fase 2 — Aplicar e testar

```bash
make lab-prepare LAB=01.11
# Preencha os arquivos de trabalho
kubectl apply -f .labs/01.11/
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
kubectl exec -n lab-01-11 pod/escritor -- sh -c 'echo marcador > /dados/marcador.txt'
kubectl delete pod escritor -n lab-01-11
kubectl get pvc dados-pvc -n lab-01-11
kubectl apply -f .labs/01.11/claim.yaml
kubectl apply -f .labs/01.11/pod.yaml
kubectl wait --for=condition=Ready pod/escritor -n lab-01-11 --timeout=120s
kubectl exec -n lab-01-11 pod/escritor -- cat /dados/marcador.txt
```

O arquivo inicial pode ser sobrescrito pelo script de inicialização. Para comprovar persistência, **antes de excluir o Pod**, execute `kubectl exec -n lab-01-11 pod/escritor -- sh -c 'echo marcador > /dados/marcador.txt'`. Após recriar o Pod, execute `kubectl exec -n lab-01-11 pod/escritor -- cat /dados/marcador.txt` e confirme que o marcador permaneceu. O Kind requer um StorageClass funcional, normalmente `standard`.

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

---

[← Lab 01.10](../probes-basico/README.md) · [↑ Aula 01.11](../../volumes/README.md) · [Próximo: Lab 01.12 →](../estrategias-deployment-basico/README.md)
