# Complementar 04.01 — GitOps: sync, health e projetos

[← Aula 04.01](../README.md) · [🧪 Lab 04.01](../../labs/argo-cd-basico/README.md) · [↑ Camada 04](../../README.md)

> **Leitura opcional:** matriz de decisão e diagnóstico para consulta. Não é pré-requisito para executar o laboratório.

## Quando consultar

Ao diagnosticar aplicação `OutOfSync`, repositório inacessível ou divergência entre recursos presentes e Healthy.

| Estado | Significado | Investigação |
| --- | --- | --- |
| `Synced` | Live corresponde ao Git renderizado | Pode haver Pod não pronto |
| `OutOfSync` | Há diferença declarativa | Diff, revision, selfHeal |
| `Healthy` | Recursos satisfazem health checks | Probes e controlador |
| `Degraded` | Recurso com health ruim | Events, conditions, logs |

## Requisitos de isolamento

Instalar Argo CD no namespace `lab-04-01` permite Application local em instalação dedicada. Quando instalado em outro namespace, habilitar *Applications in any namespace* e permitir o namespace no AppProject são passos de administração que não devem ser omitidos.

```bash
kubectl get applications.argoproj.io -n lab-04-01
kubectl get deploy -n lab-04-01
```

**Evite** configurar auto-prune sem revisar exclusões, releases e recursos compartilhados. GitOps não substitui testes de build.

## Referências oficiais

[Argo CD](https://argo-cd.readthedocs.io/en/stable/)

---

[↑ Aula 04.01](../README.md) · [↑ Camada 04](../../README.md)
