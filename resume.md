# Resumo do projeto

Este arquivo reune os principais conceitos e objetos vistos no repositorio ate agora, com explicacoes curtas para consulta rapida.

## Fundamentos de containers

- Container Engine: gerencia imagens, rede e volumes (ex: Docker, Podman, CRI-O).
- OCI: padrao aberto para formatos de imagem e runtime de containers.
- Container Runtime: executa containers nos nos (ex: containerd, CRI-O, runc).

## Cluster e arquitetura

- Cluster Kubernetes: conjunto de nos control-plane e workers.
- Control plane: API Server, Scheduler, Controller Manager e etcd.
- API Server: porta de entrada do cluster para comandos via kubectl.
- etcd: banco chave-valor do estado do cluster.
- Scheduler: escolhe em qual no cada Pod sera executado.
- Controller Manager: mantem o estado atual alinhado ao estado desejado.
- Kubelet: agente nos workers que cria e monitora Pods.
- Kube-proxy: roteamento e balanceamento local de trafego.
- Namespaces: isolamento logico de recursos dentro do cluster.

## Objetos e workloads

- Pod: menor unidade do Kubernetes; pode ter um ou mais containers.
- Pod multi-container: varios containers compartilhando rede e volumes.
- ReplicaSet: garante a quantidade desejada de replicas de Pods.
- Deployment: gerencia o ciclo de vida dos Pods via ReplicaSet.
- Rollout/Rollback: atualizacoes controladas de Deployments.
- Estrategias de deployment: RollingUpdate e Recreate (inclui maxSurge e maxUnavailable).
- DaemonSet: garante um Pod por no (ex: agentes de monitoramento).
- StatefulSet: identidade fixa, ordem de criacao/remocao e volumes exclusivos por replica.

## Rede e exposicao

- Service: endpoint estavel para Pods (ClusterIP, NodePort, LoadBalancer).
- Ingress: regras HTTP/HTTPS para expor servicos.
- Ingress Controller: componente que implementa o Ingress (ex: ingress-nginx).
- ingress-nginx: manifestos para subir o controller no Kind.

## Saude e observabilidade

- Probes: liveness, readiness e startup para vida, prontidao e inicializacao.
- Logs: saida dos Pods para diagnostico.
- Events: eventos do cluster para troubleshooting.

## Recursos e armazenamento

- Requests e limits: minimo e maximo de CPU e memoria para containers.
- Volumes: mecanismos de armazenamento para Pods (temporarios ou persistentes).
- StorageClass: define classes de armazenamento e provisionamento.
- volumeBindingMode: controla quando o PV e associado ao PVC (ex: WaitForFirstConsumer).
- PersistentVolume (PV): recurso de armazenamento no cluster.
- PersistentVolumeClaim (PVC): pedido de armazenamento feito por Pods.
- AccessModes: RWO, ROX e RWX conforme o tipo de uso.
- ReclaimPolicy: Retain/Delete define o que ocorre ao remover o PVC.
- EmptyDir: volume temporario para compartilhamento entre containers.
- HostPath: monta diretorios do no dentro do Pod (ex: /proc e /sys no DaemonSet).
- NFS: armazenamento compartilhado via servidor NFS.

## Politicas de agendamento e rede do no

- Labels e selectors: ligam Deployments/ReplicaSets/DaemonSets aos Pods.
- NodeSelector: direciona Pods para nos especificos.
- Tolerations: permite agendar Pods em nos com taints.
- HostNetwork: Pod usa a rede do no (exige cuidado).

## Ferramentas e manifests

- kubectl: CLI para aplicar manifests e inspecionar recursos.
- Manifests YAML: descrevem objetos para criar/atualizar via `kubectl apply -f`.
- Kustomize: compoe manifests e aplica patches (ex: ingress-nginx).
- Kind/Minikube: criacao de clusters locais para estudo e testes.
- kind-config.yaml: define o cluster local (control-plane e workers).
- Makefile: atalhos para subir, validar e remover o cluster Kind.
- install-kind.md: guia de instalacao do Kind no WSL.
- Tools.md: referencia rapida de ferramentas externas (ex: Crane, FreeLens).

## Operacao basica

- apply/get/describe: criar e inspecionar recursos.
- logs/exec/attach: diagnosticar Pods e containers.
- delete: remover recursos por nome ou manifesto.
