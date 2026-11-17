# Services

[← Camada 01](../README.md) · [Roadmap](../../../docs/roadmap.md) · [Início](../../../README.md)

> **Material de apoio:** este guia organiza o estudo do conceito. Veja também as anotações, os comandos e os exercícios em [7-services/README.md](../../../7-services/README.md).

## Objetivo

Conectar clientes a Pods por um ponto de acesso estável, com descoberta via DNS.

## Ao concluir, você deverá conseguir

- Criar Services e observar seus tipos
- Inspecionar seletores e EndpointSlices
- Consultar DNS interno e entender Headless Services

## Estude o conceito

Consulte as [anotações e exemplos práticos](../../../7-services/README.md), que contém os exemplos, explicações e comandos já presentes na trilha.

**Infográfico:** espaço reservado; o PNG será incluído em um PR posterior, após revisão editorial/técnica.

## Laboratório e observação

**Pré-requisito:** [Kind configurado](../../../install-kind.md) e contexto correto selecionado. Confira `kubectl config current-context` antes de executar comandos que alterem o cluster.

Utilize os manifests e exemplos das [anotações e exemplos práticos](../../../7-services/README.md). Para observar o cluster:

```bash
kubectl get services
kubectl describe service <nome>
kubectl get endpointslices -l kubernetes.io/service-name=<nome>
kubectl get pods --show-labels
```

> Substitua os valores entre `<...>` pelos recursos realmente criados. Os comandos acima são referências para estudo; a execução não foi testada neste PR.

Também há um [lab integrado Pod → Deployment → Service](../labs/primeira-aplicacao/README.md) com arquivos completos e procedimentos de validação.

## Documentação oficial

- [Kubernetes — Services](https://kubernetes.io/docs/concepts/services-networking/service/)

**Próximo passo:** revise [os demais tópicos da camada](../README.md) e avance para [Operação e Segurança](../../02-operacao-seguranca/README.md).


---

### Navegação

[← Anterior](../probes/README.md) · [↑ Voltar à camada](../README.md) · Fim da camada ✓
