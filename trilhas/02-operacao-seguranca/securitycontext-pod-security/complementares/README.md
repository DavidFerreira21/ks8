# Complementar 02.03 — PSA: níveis e admissão

[← Aula 02.03](../README.md) · [🧪 Lab 02.03](../../labs/securitycontext-psa-basico/README.md) · [↑ Camada 02](../../README.md)

> **Leitura opcional.** Referência para consulta após a aula e o lab; não é pré-requisito e não repete o desafio YAML.

## Quando consultar

Ao aplicar políticas de segurança de Pods ou interpretar rejeições na admissão.

## Matriz

| Nível | Aplicação |
| --- | --- |
| `privileged` | Poucas restrições; apenas situações justificadas |
| `baseline` | Protege contra elevação de privilégios conhecida |
| `restricted` | Controles mais rigorosos para Pods |

| Modo | Comportamento |
| --- | --- |
| `enforce` | Rejeita Pod não conforme |
| `warn` | Emite aviso |
| `audit` | Sinaliza violações para auditoria |

```bash
kubectl get ns NAMESPACE --show-labels
kubectl label ns NAMESPACE pod-security.kubernetes.io/warn=restricted --overwrite
kubectl label ns NAMESPACE pod-security.kubernetes.io/warn-
```

Não altere `kube-system` nem namespaces compartilhados para experimentar `enforce`. SecurityContext do Pod e PSA no namespace têm papéis diferentes.

## Referências oficiais

[Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/) · [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)

---

[↑ Aula 02.03](../README.md) · [↑ Camada 02](../../README.md)
