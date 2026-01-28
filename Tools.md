# Kubernetes Tooling Lab

Objetivo: servir como base de estudo estruturada e referência prática para pipelines e laboratórios.

Cada ferramenta segue o padrão:
- Nome da ferramenta (título)
- Descrição um pouco mais detalhada
- Link oficial

## Crane (go-containerregistry)

Ferramenta CLI do ecossistema go-containerregistry para interagir com registries de containers. Permite inspecionar imagens, copiar entre registries, assinar artefatos e automatizar tarefas sem depender do Docker daemon.

Link oficial:
https://github.com/google/go-containerregistry

## FreeLens

Interface gráfica gratuita e open source para gerenciar clusters Kubernetes (aplicação standalone). Facilita visualizar recursos, logs e eventos, com acesso rápido a namespaces e contextos, sem exigir licença comercial.

Link oficial:
https://freelens.app

## Kind (Kubernetes in Docker)

Cria clusters Kubernetes locais usando containers Docker. Ideal para testes rápidos, laboratórios e pipelines CI/CD sem necessidade de infraestrutura externa.

Link oficial:
https://kind.sigs.k8s.io/

## kube-linter

Análise estática de manifests Kubernetes e Helm para detectar más práticas e configurações inseguras. Útil para padronização de manifests e prevenção de problemas antes do deploy.

Link oficial:
https://docs.kubelinter.io/

## kubeconform

Valida manifests Kubernetes contra schemas oficiais da API (OpenAPI), incluindo CRDs. Muito usado em pipelines CI para garantir compatibilidade com a versão do cluster.

Link oficial:
https://kubeconform.mandragor.org/

## kubeval

Ferramenta de validação de schema para manifests Kubernetes. Mais comum em pipelines legados, ainda útil para checagens simples.

Link oficial:
https://kubeval.com/

## Trivy

Scanner de segurança para manifests Kubernetes, imagens de containers, dependências e clusters em execução. Detecta CVEs e misconfigurations com relatórios claros.

Link oficial:
https://trivy.dev/

## Checkov

Ferramenta de análise estática de segurança e compliance para Kubernetes YAML, Helm e Infrastructure as Code. Focada em detectar configurações inseguras e reforçar boas práticas.

Link oficial:
https://www.checkov.io/

## KICS (Keeping Infrastructure as Code Secure)

Scanner de segurança focado em IaC (Kubernetes, Helm, Kustomize e outros). Possui catálogo amplo de regras e boa integração com pipelines CI/CD.

Link oficial:
https://docs.kics.io/

## OPA Gatekeeper

Implementa Policy as Code no Kubernetes por meio de um admission controller, validando e bloqueando recursos que violem políticas de governança e compliance no momento da criação.

Link oficial:
https://open-policy-agent.github.io/gatekeeper/

## Kyverno

Engine nativa de políticas Kubernetes que permite validar, mutar e gerar recursos usando políticas declarativas em YAML, facilitando manutenção e adoção.

Link oficial:
https://kyverno.io/

## metrics-server

Coleta métricas básicas de CPU e memória de Pods e Nodes. É dependência do HPA e base para componentes de autoscaling no Kubernetes.

Link oficial:
https://kubernetes-sigs.github.io/metrics-server/

## kube-state-metrics

Exporta métricas sobre o estado dos objetos do cluster (Deployments, Pods, Nodes, etc.). Muito utilizado em conjunto com Prometheus e Grafana para observabilidade.

Link oficial:
https://github.com/kubernetes/kube-state-metrics

## Goldilocks

Sugere valores ideais de requests e limits com base no consumo real de CPU e memória. Ajuda a reduzir desperdício e melhorar previsibilidade de recursos.

Link oficial:
https://goldilocks.docs.fairwinds.com/

## Argo CD

Ferramenta de GitOps que mantém o estado do cluster sincronizado com o Git, monitora drift e automatiza deploys e rollbacks de aplicações Kubernetes.

Link oficial:
https://argoproj.github.io/cd/

## Helm

Gerenciador de pacotes do Kubernetes para instalar, versionar e distribuir aplicações usando charts, facilitando padronização e reutilização.

Link oficial:
https://helm.sh/

## Karpenter

Autoscaler de nodes para Kubernetes que provisiona capacidade de forma dinâmica com base nos Pods pendentes, otimizando custo e performance em ambientes cloud.

Link oficial:
https://karpenter.sh/

## Prometheus

Sistema de monitoramento e alertas baseado em métricas, amplamente adotado no ecossistema Kubernetes para coleta e consulta de séries temporais.

Link oficial:
https://prometheus.io/

## Grafana

Plataforma de visualização de dados e criação de dashboards, comumente utilizada junto ao Prometheus para observabilidade de clusters e aplicações.

Link oficial:
https://grafana.com/
