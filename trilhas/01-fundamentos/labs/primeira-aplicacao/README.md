# Lab integrado — Pod → Deployment → Service

[← Camada 01](../../README.md) · [Roadmap](../../../../docs/roadmap.md)

## Objetivo

Acompanhar a evolução de um Pod individual para um Deployment com três réplicas e expor a aplicação via Service. Ao final, observar os processos de agendamento, reconciliação e descoberta de serviços.

**Status:** manifests revisados por inspeção, mas **não executados em um cluster** nesta mudança.

## Pré-requisitos

- Kind e kubectl instalados: [guia existente](../../../../install-kind.md)
- Um cluster funcional e contexto selecionado corretamente
- Acesso a imagens Docker Hub (nginx)

Confira o contexto antes de fazer alterações:

```bash
kubectl config current-context
kubectl get nodes
```

## Etapa 1 — Namespace e Pod individual

Crie um namespace exclusivo:

```bash
kubectl create namespace k8s-lab
```

A partir desta pasta, aplique o Pod:

```bash
kubectl apply -f pod.yaml
kubectl get pods -n k8s-lab -o wide
kubectl describe pod web-pod -n k8s-lab
```

**Observe:** o nó onde o Pod foi agendado, seu endereço IP e os eventos. Este Pod é gerenciado diretamente, sem um controller para recriá-lo automaticamente.

Remova apenas o Pod individual, mantendo o namespace:

```bash
kubectl delete -f pod.yaml
```

## Etapa 2 — Deployment e ReplicaSet

```bash
kubectl apply -f deployment.yaml
kubectl rollout status deployment/web -n k8s-lab --timeout=120s
kubectl get deployment,replicaset,pods -n k8s-lab -o wide
```

**Resultado esperado:** Deployment com três réplicas prontas, um ReplicaSet gerenciando os Pods e três Pods associados a ele (pressupondo recursos e acesso à imagem suficientes).

Agora elimine **um dos Pods controlados pelo Deployment**:

```bash
kubectl get pods -n k8s-lab -l app=web
kubectl delete pod <nome-de-um-pod-do-deployment> -n k8s-lab
kubectl get pods -n k8s-lab -l app=web --watch
```

**Observe:** o ReplicaSet cria outro Pod para recuperar o número desejado de réplicas. Encerre o watch com Ctrl+C.

## Etapa 3 — Service e descoberta

```bash
kubectl apply -f service.yaml
kubectl get service web -n k8s-lab
kubectl get endpointslices -n k8s-lab -l kubernetes.io/service-name=web
```

Testar acesso via port-forward local:

```bash
kubectl port-forward -n k8s-lab service/web 8080:80
```

Em **outro terminal**:

```bash
curl -I http://localhost:8080
```

**Resultado esperado:** resposta HTTP do nginx. Encerre o port-forward com Ctrl+C.

O Service seleciona os Pods via label `app: web`. No cluster, o nome DNS esperado para esse Service é `web.k8s-lab.svc.cluster.local`.

## Etapa 4 — Rollout e rollback

Para observar uma atualização sem depender de uma mudança de versão da aplicação, solicite o reinício controlado do Deployment:

```bash
kubectl rollout restart deployment/web -n k8s-lab
kubectl rollout status deployment/web -n k8s-lab --timeout=120s
kubectl get replicasets,pods -n k8s-lab
```

Para praticar um rollback de revisão, primeiro altere intencionalmente um campo do Pod template, confirme que foi criada uma nova revisão e então execute `kubectl rollout undo deployment/web -n k8s-lab`. Não use rollback sem ter produzido uma revisão anterior.

## Diagnóstico

```bash
kubectl describe deployment web -n k8s-lab
kubectl get events -n k8s-lab --sort-by=.lastTimestamp
kubectl logs -n k8s-lab deployment/web
```

Se o Service não responder, confira as labels dos Pods, o selector e o estado de readiness, além dos EndpointSlices.

## Limpeza

**Somente se o namespace `k8s-lab` tiver sido criado exclusivamente para este exercício** e não contiver outros recursos importantes:

```bash
kubectl delete namespace k8s-lab
```

Alternativamente, remova apenas os manifests do lab:

```bash
kubectl delete -f service.yaml -f deployment.yaml --ignore-not-found
```

## Referências oficiais

- [Pods](https://kubernetes.io/docs/concepts/workloads/pods/)
- [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Services](https://kubernetes.io/docs/concepts/services-networking/service/)
- [Debugging Services](https://kubernetes.io/docs/tasks/debug/debug-application/debug-service/)
