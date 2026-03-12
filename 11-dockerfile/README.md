# Dockerfile

## O que e Dockerfile?

Dockerfile e um arquivo de texto com instrucoes para construir uma imagem de container.
Ele define:

- imagem base
- arquivos que entram na imagem
- dependencias instaladas
- comando de inicializacao

Com isso, o build fica reprodutivel e versionado no Git.

## Estrutura basica

Instrucoes mais comuns:

- `FROM`: imagem base
- `WORKDIR`: diretorio de trabalho dentro da imagem
- `COPY`: copia arquivos locais para a imagem
- `RUN`: executa comandos no build
- `EXPOSE`: documenta porta usada pela aplicacao
- `CMD` ou `ENTRYPOINT`: comando de inicializacao do container

## Exemplo simples

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000
CMD ["python", "app.py"]
```

Build e execucao:

```bash
docker build -t minha-api:1.0 .
docker run --rm -p 8000:8000 minha-api:1.0
```

## Dockerfile multi-stage

Multi-stage build reduz tamanho da imagem final separando fase de build e fase de runtime.

Vantagens:

- imagem menor
- menos superficie de ataque
- menos dependencias em producao

Exemplo com Go:

```dockerfile
# stage 1: build
FROM golang:1.24 AS builder
WORKDIR /src
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o app ./cmd/api

# stage 2: runtime
FROM gcr.io/distroless/static-debian12
WORKDIR /
COPY --from=builder /src/app /app
USER nonroot:nonroot
ENTRYPOINT ["/app"]
```

## O que e Distroless?

Imagens distroless incluem apenas o necessario para rodar a aplicacao (sem shell, sem gerenciador de pacotes, sem utilitarios extras).

Beneficios:

- menor tamanho
- menos CVEs
- menor risco operacional

Ponto de atencao:

- debug fica mais dificil (normalmente se usa sidecar/debug container quando necessario)

## O que e Trivy?

Trivy e um scanner de seguranca para:

- imagens de container
- filesystem/projetos
- manifestos IaC (Kubernetes, Terraform etc.)
- SBOM

Comandos principais:

```bash
# Scan de imagem
trivy image nginx:1.27

# Scan de codigo/arquivos locais
trivy fs .

# Scan de manifests (Kubernetes/Terraform)
trivy config .

# Gerar SBOM (CycloneDX)
trivy image --format cyclonedx --output sbom.json nginx:1.27
```

## O que e Docker Scout?

Docker Scout analisa imagens, gera inventario de pacotes (SBOM) e cruza com base de vulnerabilidades para priorizar correcao.

Comandos principais:

```bash
# Visao geral de seguranca
docker scout quickview minha-api:1.0

# Lista CVEs da imagem
docker scout cves minha-api:1.0

# Sugestao de melhorias (ex.: trocar imagem base)
docker scout recommendations minha-api:1.0

# Comparar duas imagens/tags
docker scout compare minha-api:1.0 --to minha-api:1.1
```

## O que e Cosign?

Cosign assina e verifica artefatos OCI (imagens e assinaturas) para garantir autenticidade e integridade.

Comandos principais:

```bash
# Gerar par de chaves
cosign generate-key-pair

# Assinar imagem com chave
cosign sign --key cosign.key registry.exemplo.com/minha-api:1.0

# Verificar assinatura
cosign verify --key cosign.pub registry.exemplo.com/minha-api:1.0
```

### Por que assinar imagem?

- prova de origem (quem publicou)
- garantia de integridade (imagem nao foi alterada)
- suporte a politicas de admissao no cluster (exigir imagem assinada)
- melhora de rastreabilidade e compliance

## Fluxo recomendado (build seguro)

```bash
# 1) Build
docker build -t registry.exemplo.com/minha-api:1.0 .

# 2) Scan local
trivy image registry.exemplo.com/minha-api:1.0
docker scout cves registry.exemplo.com/minha-api:1.0

# 3) Push
docker push registry.exemplo.com/minha-api:1.0

# 4) Assinatura
cosign sign --key cosign.key registry.exemplo.com/minha-api:1.0

# 5) Verificacao
cosign verify --key cosign.pub registry.exemplo.com/minha-api:1.0
```

## Boas praticas rapidas

- usar imagem base minima (`alpine`, `slim`, `distroless` quando possivel)
- fixar versoes de dependencias
- evitar rodar como `root`
- usar multi-stage
- escanear imagem no CI
- assinar imagem antes de promover para producao
