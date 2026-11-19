# 02.03 · SecurityContext e Pod Security Admission

[⌂ Início](../../../README.md) · [↑ Camada 02](../README.md) · [📚 Catálogo](../../../docs/catalogo.md)

> **Ao concluir esta aula, você será capaz de:** Distinguir configurações de segurança do container das políticas de admissão e interpretar uma criação negada por PSA.

## 🎨 Infográfico

![02.03 — SecurityContext e Pod Security Admission](images/securitycontext-pod-security.png)

## 📖 Aula teórica

### O problema que este recurso resolve

O SecurityContext configura propriedades de execução, como usuário não-root, capacidades Linux, sistema de arquivos somente leitura e escalonamento de privilégios. Pod Security Admission (PSA) avalia Pods em namespaces conforme níveis `privileged`, `baseline` e `restricted`.

### Como funciona no Kubernetes

O PSA pode atuar em modos `enforce`, `audit` e `warn` via labels de namespace. `enforce` pode rejeitar um Pod antes do agendamento; `warn` alerta, mas não bloqueia. SecurityContext por si só não ativa uma política no namespace.

### Exemplo interpretado (trecho)

SecurityContext do container e a política PSA no namespace atuam em pontos diferentes. O trecho não substitui um Pod completo.

```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 10001
  seccompProfile:
    type: RuntimeDefault
```

Este é um **trecho ilustrativo**, não um manifesto para aplicar isoladamente. A implementação completa será escrita pelo aluno no laboratório.

### Exemplo de inspeção

Os comandos abaixo são exemplos para um cluster de estudo. Substitua os nomes ilustrativos e confirme o contexto antes de executar.

```bash
kubectl config current-context
kubectl label namespace NAMESPACE pod-security.kubernetes.io/warn=restricted --overwrite
kubectl get namespace NAMESPACE --show-labels
kubectl describe pod POD -n NAMESPACE
```

**O que observar:** Em `warn`, um manifesto incompatível pode gerar aviso de PodSecurity; em `enforce`, pode ocorrer rejeição por admissão. A política de namespace precisa ser inspecionada junto com o Pod.

### Cuidados e limitações

Nunca aplique `enforce=restricted` indiscriminadamente em namespaces de sistema. `runAsNonRoot` não substitui análise de permissões de arquivo, seccomp, capabilities e imagem.

## 🧪 Aplicação prática

**[🧪 Lab 02.03](../labs/securitycontext-psa-basico/README.md):** escreva o YAML do exercício, execute no Kind, registre evidências e explique as divergências. O complementar não é pré-requisito.

**Complementar opcional:** [Consultar aprofundamento 02.03](complementares/README.md). Referência adicional; não é necessária para executar o lab.

## ✅ Revisão do aprendizado

- Qual diferença existe entre `runAsNonRoot` e a política PSA `restricted`?
- Quando `warn` produz aviso sem rejeição?
- Como diferenciar um Pod barrado pela admissão de um Pod Pending pelo scheduler?

## 🔗 Referências oficiais

- [Documentação oficial do conceito](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)
- [Documentação oficial do conceito](https://kubernetes.io/docs/concepts/security/pod-security-admission/)

---

[← Aula 02.02 — RBAC e ServiceAccount](../rbac-serviceaccount/README.md) · [↑ Camada 02](../README.md) · [🧪 Lab 02.03](../labs/securitycontext-psa-basico/README.md) · [Próxima: Aula 02.04 — ResourceQuota e LimitRange →](../resourcequota-limitrange/README.md)
