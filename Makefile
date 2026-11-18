SHELL := /bin/bash
.DEFAULT_GOAL := help

CLUSTER_NAME ?= dev
KIND_CONFIG ?= kind-config.yaml
KUBE_CONTEXT ?= kind-$(CLUSTER_NAME)
LAB_DIR := trilhas/01-fundamentos/labs/primeira-aplicacao
LAB_NAMESPACE := k8s-lab

.PHONY: help check-tools check-context up nodes status down validate doctor labs lab-up lab-test lab-down

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

lab-up: check-context ## Aplica Deployment e Service do laboratório integrado
	@kubectl create namespace "$(LAB_NAMESPACE)" --dry-run=client -o yaml | kubectl apply -f -
	@kubectl apply -f "$(LAB_DIR)/deployment.yaml" -f "$(LAB_DIR)/service.yaml"

lab-test: check-context ## Espera o Deployment ficar pronto e verifica Service
	@kubectl rollout status deployment/web -n "$(LAB_NAMESPACE)" --timeout=180s
	@kubectl get deployment web -n "$(LAB_NAMESPACE)"
	@kubectl get service web -n "$(LAB_NAMESPACE)"
	@kubectl get endpointslices -n "$(LAB_NAMESPACE)" -l kubernetes.io/service-name=web

lab-down: check-context ## Remove somente Deployment e Service criados pelo laboratório
	@kubectl delete -f "$(LAB_DIR)/service.yaml" -f "$(LAB_DIR)/deployment.yaml" --ignore-not-found
	@echo "Namespace $(LAB_NAMESPACE) preservado; remova-o manualmente se estiver vazio."

# Interface de descoberta: não modifica recursos do cluster.
doctor: ## Verifica ferramentas e Docker local
	@python3 scripts/labctl.py doctor

labs: ## Lista os laboratórios registrados em lab.yaml
	@python3 scripts/labctl.py labs
