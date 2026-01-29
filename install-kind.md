# Guia rápido: Kind no WSL com Docker Desktop

## Pré-requisitos (Windows)
### 1) Instalar/ativar o WSL e definir o Ubuntu como padrão
Abra o PowerShell como Administrador e execute:
```powershell
wsl --install
wsl --set-default-version 2
wsl --install -d Ubuntu
```
Defina o Ubuntu como distro padrão:
```powershell
wsl --set-default Ubuntu
```
Reinicie o Windows se for solicitado.

### 2) Instalar o Docker Desktop
1. Baixe e instale o Docker Desktop para Windows.
2. Abra o Docker Desktop e finalize o onboarding.

### 3) Habilitar WSL Integration no Docker Desktop
No Docker Desktop:
1. **Settings** → **Resources** → **WSL Integration**
2. Marque **Enable integration with my default WSL distro**
3. Ative a integração para **Ubuntu**
4. Clique em **Apply & Restart**

### 4) Validar WSL + Docker dentro do Ubuntu
Abra o Ubuntu (WSL) e rode:
```bash
wsl --list --verbose
docker version
docker ps
```
Siga adiante somente se o Docker estiver respondendo sem erros dentro do Ubuntu.

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
   nodes:
  - role: control-plane
    kubeadmConfigPatches:
      - |
        kind: InitConfiguration
        nodeRegistration:
          kubeletExtraArgs:
            node-labels: "ingress-ready=true"

    extraPortMappings:
      - containerPort: 80
        hostPort: 80
      - containerPort: 443
        hostPort: 443

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
