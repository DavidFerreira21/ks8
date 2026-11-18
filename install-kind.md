# Guia de ambiente — Kind no WSL2

[← Início](README.md) · [Comandos dos labs](docs/labs.md)

Este documento prepara o laboratório local com Windows + WSL2 (Ubuntu) + Docker Desktop, Kind e kubectl. Confira as versões mais recentes nos links oficiais; o comando de instalação abaixo não fixa uma versão para não perpetuar um release obsoleto.

## 1. Preparar WSL2 no Windows

**Execute no PowerShell do Windows, como Administrador**:

```powershell
wsl --install -d Ubuntu
wsl --set-default-version 2
wsl --set-default Ubuntu
wsl --list --verbose
```

Reinicie o Windows se solicitado. Abra **Ubuntu (WSL)** para os próximos comandos Linux.

## 2. Preparar Docker Desktop

Instale [Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/) e habilite **Settings → Resources → WSL Integration** para Ubuntu.

No terminal do **Ubuntu (WSL)**, confirme:

```bash
docker version
docker ps
```

Os dois comandos precisam funcionar antes de criar o cluster.

## 3. Instalar Kind e kubectl

Siga as instruções oficiais para seu sistema e arquitetura:

- [Kind — Quick Start](https://kind.sigs.k8s.io/docs/user/quick-start/)
- [kubectl — Instalação](https://kubernetes.io/docs/tasks/tools/)

Confirme os binários:

```bash
kind version
kubectl version --client
```

## 4. Criar o cluster

Execute na **raiz do repositório**:

```bash
make help
make up
kubectl config current-context
make nodes
```

O Makefile cria um cluster Kind chamado `dev` (contexto esperado: `kind-dev`) usando [kind-config.yaml](kind-config.yaml). A configuração tem um nó Control Plane, dois Workers e mapeamento das portas 80/443 para experimentos futuros.

Se quiser criar sem o Makefile:

```bash
kind create cluster --name dev --config kind-config.yaml
kubectl get nodes --context kind-dev
```

## 5. Executar o primeiro lab

```bash
python3 -m pip install 'PyYAML>=6,<7'
make validate
make lab-up
make lab-test
bash scripts/lab-diagnostics.sh
make lab-down
```

> `make lab-up` aplica **Deployment e Service**, não o Pod individual. Para seguir a sequência didática completa, veja o [lab Pod → Deployment → Service](trilhas/01-fundamentos/labs/primeira-aplicacao/README.md).

## 6. Limpeza

- `make lab-down` remove somente Deployment e Service do exemplo e preserva `k8s-lab`.
- `make down` **apaga o cluster Kind `dev` inteiro**, incluindo seus recursos e dados. Execute apenas se não precisar mais dele.

## 7. Ingress

O cluster tem portas 80/443 mapeadas, mas **não instala automaticamente um Ingress Controller**. O exercício de Ingress será padronizado em um laboratório separado; não dependa de um antigo alvo `make install-nginx`, pois ele não foi implementado nesta etapa.

Referências: [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) e [Gateway API](https://kubernetes.io/docs/concepts/services-networking/gateway/).
