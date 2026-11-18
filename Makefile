SHELL := /bin/bash
.DEFAULT_GOAL := help

CLUSTER_NAME ?= dev
KIND_CONFIG ?= kind-config.yaml
KUBE_CONTEXT ?= kind-$(CLUSTER_NAME)
LAB ?= 01.01
EXPERIMENT ?= controlled-rollout
LAB_ID ?= 01.07
LAB_SLUG ?= configmaps-basico
LAB_TITLE ?= Estudando ConfigMaps
LAB_NAMESPACE := k8s-lab

.PHONY: help check-tools check-context up nodes status down validate doctor labs lab-prepare lab-reset lab-solution lab-up lab-test lab-status lab-observe lab-experiment lab-down new-lab

help: ## Exibe os alvos disponíveis
	@awk 'BEGIN {FS = ":.*## "}; /^[a-zA-Z_-]+:.*## / {printf "  %-18s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

check-tools: ## Verifica as ferramentas necessárias
	@command -v kind >/dev/null || (echo "kind não encontrado" >&2; exit 1)
	@command -v kubectl >/dev/null || (echo "kubectl não encontrado" >&2; exit 1)
	@command -v docker >/dev/null || (echo "docker não encontrado" >&2; exit 1)
	@docker info >/dev/null 2>&1 || (echo "Docker não está respondendo" >&2; exit 1)

check-context: ## Confere o contexto Kubernetes antes de alterar workloads
	@command -v kubectl >/dev/null || (echo "kubectl não encontrado" >&2; exit 1)
	@current="$$(kubectl config current-context 2>/dev/null)"; \
	  if [[ "$$current" != "$(KUBE_CONTEXT)" ]]; then \
	    echo "Contexto $$current inesperado; esperado: $(KUBE_CONTEXT)" >&2; \
	    exit 1; \
	  fi

up: check-tools ## Cria o cluster Kind local, se ainda não existir
	@if kind get clusters | grep -Fxq "$(CLUSTER_NAME)"; then \
	  echo "Cluster Kind $(CLUSTER_NAME) já existe"; \
	else \
	  kind create cluster --name "$(CLUSTER_NAME)" --config "$(KIND_CONFIG)"; \
	fi

nodes: check-context ## Mostra os nós do cluster do lab
	@kubectl get nodes -o wide

status: check-context ## Lista Pods e Services do namespace de lab
	@kubectl get pods,services -n "$(LAB_NAMESPACE)" --ignore-not-found

down: ## Remove somente o cluster Kind identificado por CLUSTER_NAME
	@command -v kind >/dev/null || (echo "kind não encontrado" >&2; exit 1)
	@if kind get clusters | grep -Fxq "$(CLUSTER_NAME)"; then \
	  kind delete cluster --name "$(CLUSTER_NAME)"; \
	else \
	  echo "Cluster Kind $(CLUSTER_NAME) não encontrado"; \
	fi

validate: ## Validação estática dos manifests do lab (sem cluster)
	@python3 scripts/labctl.py validate
	@python3 scripts/validate_manifests.py
	@python3 scripts/validate_lab_resources.py

lab-prepare: check-context ## Prepara namespace, apoio e arquivos para o aluno (sem aplicar a solução)
	@CLUSTER_NAME="$(CLUSTER_NAME)" python3 scripts/labctl.py lab-prepare --lab "$(LAB)"

lab-reset: check-context ## Reinicia recursos declarados, preservando seus arquivos de estudo
	@CLUSTER_NAME="$(CLUSTER_NAME)" python3 scripts/labctl.py lab-reset --lab "$(LAB)"

lab-solution: ## Mostra caminhos das soluções sem aplicar nada
	@CLUSTER_NAME="$(CLUSTER_NAME)" python3 scripts/labctl.py lab-solution --lab "$(LAB)"

lab-up: check-context ## Apenas CI: aplica a solução de referência para LAB
	@CLUSTER_NAME="$(CLUSTER_NAME)" python3 scripts/labctl.py lab-up --lab "$(LAB)"

lab-test: check-context ## Valida checks do LAB selecionado
	@CLUSTER_NAME="$(CLUSTER_NAME)" python3 scripts/labctl.py lab-test --lab "$(LAB)"

lab-status: check-context ## Mostra recursos do lab selecionado
	@CLUSTER_NAME="$(CLUSTER_NAME)" python3 scripts/labctl.py lab-status --lab "$(LAB)"

lab-observe: check-context ## Mostra eventos, recursos, estados e perguntas de observação
	@CLUSTER_NAME="$(CLUSTER_NAME)" python3 scripts/labctl.py lab-observe --lab "$(LAB)"

lab-experiment: check-context ## Executa experimento controlado após confirmação explícita
	@CLUSTER_NAME="$(CLUSTER_NAME)" python3 scripts/labctl.py lab-experiment --lab "$(LAB)" --experiment "$(EXPERIMENT)" --confirm

lab-down: check-context ## Remove recursos declarados, mas preserva o namespace
	@CLUSTER_NAME="$(CLUSTER_NAME)" python3 scripts/labctl.py lab-down --lab "$(LAB)"

# Interface de descoberta: não modifica recursos do cluster.
doctor: ## Verifica ferramentas e Docker local
	@python3 scripts/labctl.py doctor

labs: ## Lista os laboratórios registrados em lab.yaml
	@python3 scripts/labctl.py labs

new-lab: ## Gera esqueleto: make new-lab LAB_ID=01.07 LAB_SLUG=configmaps-basico
	@python3 scripts/new_lab.py --id "$(LAB_ID)" --slug "$(LAB_SLUG)" --title "$(LAB_TITLE)"
