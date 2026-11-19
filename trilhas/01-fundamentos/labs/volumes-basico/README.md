# Lab 01.11 — Volumes

[← Aula 01.11](../../volumes/README.md) · [↑ Camada 01](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** execute `make lab-prepare LAB=01.11`, complete `.labs/01.11/claim.yaml` e `.labs/01.11/pod.yaml` e execute **`kubectl apply -f .labs/01.11/`**. Só depois valide com `make lab-test LAB=01.11`. `make lab-up` aplica a solução completa e fica reservado à CI; `make lab-solution LAB=01.11` revela seus arquivos para estudo posterior.


## Objetivo e hipótese

Um volume efêmero desaparece com o Pod; um PVC pode preservar dados além do ciclo de vida do Pod. Este lab exige um provisionador local funcional.

**Escopo:** cluster Kind `dev` e namespace `lab-01-11`.

## Desafio — o que você vai construir

Escreva **dois arquivos**: `claim.yaml` com PVC `dados-pvc`, acesso `ReadWriteOnce` e solicitação de `100Mi`; e `pod.yaml` com Pod `escritor`, container BusyBox e montagem do PVC em `/dados`. O container escreve um arquivo e permanece ativo. Confira antes se existe StorageClass com provisionamento funcional no Kind.

**Antes de aplicar:** confirme os pré-requisitos, complete o YAML em `.labs/01.11/` e faça uma hipótese sobre o resultado. Recorra a `kubectl explain` ou às referências abaixo; não copie a solução antes de tentar.

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
# Preencha os arquivos de trabalho
kubectl apply -f .labs/01.11/claim.yaml
kubectl apply -f .labs/01.11/pod.yaml
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

O arquivo inicial pode ser sobrescrito pelo script de inicialização. Para comprovar persistência, antes de excluir o Pod, grave um marcador em `/dados/` como no bloco acima. Depois de recriá-lo com o mesmo PVC, leia o marcador para conferir a persistência. O Kind requer um StorageClass funcional, normalmente `standard`. Confira com `kubectl get storageclass` antes do exercício.

## Resultado esperado e evidências

- O PVC chega ao estado **Bound** e o Pod ao estado **Ready**. Com provisionamento dinâmico, um PV é associado ao PVC.
- Antes de excluir o Pod, grave `/dados/marcador.txt` com um texto próprio. Ao recriar **somente o Pod** usando o mesmo PVC, o arquivo precisa continuar legível.
- Se o PVC permanecer `Pending`, investigue o `StorageClass`/provisionador e os eventos. `make lab-down` remove também o PVC; **não considere este exercício backup ou persistência permanente**.

**Se o resultado divergir:** investigue `describe`, eventos e componentes de suporte. Um check que aprova o manifesto não substitui a observação funcional.

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

## Critérios de conclusão

- [ ] Criei o PVC e o Pod com referência ao mesmo claim.
- [ ] Confirmei `Bound` no PVC e a montagem em `/dados`.
- [ ] Mantive `marcador.txt` após excluir e recriar o Pod.
- [ ] Expliquei a diferença entre apagar Pod, PVC e PV e limpei o lab.

## Perguntas de diagnóstico e reflexão

- Se o PVC permanecer em `Pending`, quais evidências em `kubectl describe pvc` e `kubectl get storageclass` ajudam a identificar o problema?
- Por que excluir somente o Pod preservou `marcador.txt`, enquanto remover o PVC pode ter consequências diferentes conforme a política de reclaim do PV?
- Como `persistentVolumeReclaimPolicy` muda o risco de perda de dados quando você exclui o PVC, mesmo que a aplicação tenha sido removida?

**Evidências específicas:** registre PVC `Bound`, PV associado, Pod e conteúdo de `marcador.txt` antes e após recriar somente o Pod; explique o papel do PVC na persistência.

## Aprofunde seus conhecimentos

[Volumes](https://kubernetes.io/docs/concepts/storage/volumes/) · [Persistent Volumes e PVCs](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) · [Storage Classes](https://kubernetes.io/docs/concepts/storage/storage-classes/).

Volte à [aula teórica](../../volumes/README.md) e relacione os mecanismos com os eventos e estados vistos no Kind.

---

[← Lab 01.10](../probes-basico/README.md) · [↑ Aula 01.11](../../volumes/README.md) · [Próximo: Lab 01.12 →](../estrategias-deployment-basico/README.md)
