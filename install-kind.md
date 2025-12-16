# Guia rápido: Kind no WSL com Docker Desktop

## Pré-requisitos
- Habilitar o WSL no Windows e definir o Ubuntu como distro padrão
- Instalar o Docker Desktop no Windows
- Habilitar o recurso **WSL Integration** do Docker Desktop para a distro Ubuntu

## Instalar o Kind
```bash
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.23.0/kind-linux-amd64
chmod +x kind
sudo mv kind /usr/local/bin/kind
```

## Validar Docker + Kind
```bash
docker ps        # verifica se o Docker Engine está rodando
kind version     # confirma se o Kind está acessível
```
Siga apenas se ambos os comandos executarem sem erros.

## Criar o cluster Kind
1. Confira `kind-config.yaml` (exemplo abaixo) e ajuste se necessário:
   ```yaml
   kind: Cluster
   apiVersion: kind.x-k8s.io/v1alpha4
   nodes:
     - role: control-plane
     - role: worker
     - role: worker
   ```
2. Suba o cluster: `make up` (atalho para `kind create cluster --name dev --config kind-config.yaml`).
3. Valide o contexto `kind-dev`:
   ```bash
   kubectl cluster-info --context kind-dev
   kubectl get nodes
   ```

## Instalar o Ingress NGINX
```bash
make install-nginx    # usa o kustomize em ingress-nginx/
# ou diretamente:
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
```

## Comandos úteis do Makefile
```bash
make nodes   # exibe os nós do cluster
make down    # exclui o cluster (kind delete cluster --name dev)
```
Utilize `make down` ao final dos testes para liberar recursos.
