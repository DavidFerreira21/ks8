# Complementar 01.01 — Escolha do ambiente e responsabilidades

[← Aula 01.01](../README.md) · [🧪 Lab 01.01](../../labs/fundamentos-cluster/README.md) · [↑ Camada 01](../../README.md)

> **Leitura opcional:** Use quando precisar diferenciar cluster local, runtime de containers e componentes do Control Plane. Não substitui a aula nem o desafio do laboratório.

## Decisões e sintomas

| Situação | Leitura técnica |
| --- | --- |
| **Docker/OCI** | Executa e empacota containers; não fornece a API Kubernetes. |
| **Kind** | Executa nós Kubernetes como containers, indicado para experimentos descartáveis. |
| **EKS** | Control Plane gerenciado; observabilidade e controle do plano de controle dependem do provedor. |

## Como interpretar as evidências

Quando um objeto existe mas o Pod não está pronto, inspecione API, controller, scheduler e kubelet em etapas — não presuma erro do Docker.

## Referência histórica preservada

O [material complementar original](../../../../1-fundamentos/README.md) permanece acessível, com exemplos e comandos adicionais. Esta página reúne a comparação rápida no padrão editorial das demais camadas, sem duplicar todo o material antigo.

## Referências oficiais

[Documentação Kubernetes — Conceitos](https://kubernetes.io/docs/concepts/) · [Debugging](https://kubernetes.io/docs/tasks/debug/)

---

[↑ Aula 01.01](../README.md) · [↑ Camada 01](../../README.md)
