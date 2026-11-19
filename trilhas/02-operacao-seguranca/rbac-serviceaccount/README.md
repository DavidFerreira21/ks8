# 02.02 · RBAC e ServiceAccount

[⌂ Início](../../../README.md) · [↑ Camada 02](../README.md) · [📚 Catálogo](../../../docs/catalogo.md)

> **Ao concluir esta aula, você será capaz de:** Criar uma identidade com menor privilégio e demonstrar permissões autorizadas e negadas por RBAC.

## 🎨 Infográfico

![02.02 — RBAC e ServiceAccount](images/rbac-serviceaccount.png)

## 📖 Aula teórica

### O problema que este recurso resolve

Autenticação identifica quem faz a requisição. Autorização determina o que pode ser executado. ServiceAccount é identidade de workload; Role define regras em um namespace e RoleBinding concede tais regras a um sujeito.

### Como funciona no Kubernetes

`Role` e `RoleBinding` trabalham no namespace. Um `RoleBinding` também pode referenciar uma `ClusterRole`, mas a concessão continua limitada ao namespace do binding. `ClusterRoleBinding` concede regras de cluster. Uma regra não nega explicitamente: falta de autorização normalmente resulta em `forbidden` quando nenhum autorizador concede o acesso.

### Exemplo interpretado (trecho)

A Role define regras; a permissão só existe para o sujeito depois da associação por binding.

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: somente-leitura
rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get", "list"]
```

Este é um **trecho ilustrativo**, não um manifesto para aplicar isoladamente. A implementação completa será escrita pelo aluno no laboratório.

### Exemplo de inspeção

Os comandos abaixo são exemplos para um cluster de estudo. Substitua os nomes ilustrativos e confirme o contexto antes de executar.

```bash
kubectl config current-context
kubectl auth can-i list pods -n lab-ops-rbac --as=system:serviceaccount:lab-ops-rbac:lab-reader
kubectl auth can-i list secrets -n lab-ops-rbac --as=system:serviceaccount:lab-ops-rbac:lab-reader
kubectl describe rolebinding pod-reader-binding -n lab-ops-rbac
```

**O que observar:** A identidade deve conseguir listar Pods e não listar Secrets. Os testes com `--as` exigem que o usuário que executa tenha permissão de impersonation.

### Cuidados e limitações

Evite verbos e resources com `*` sem justificativa; não associe ServiceAccounts ao `cluster-admin` para simplificar o lab. Auto-mount de tokens e permissões de acesso são preocupações separadas.

## 🧪 Aplicação prática

**[🧪 Lab 02.02](../labs/rbac-minimo/README.md):** escreva o YAML do exercício, execute no Kind, registre evidências e explique as divergências. O complementar não é pré-requisito.

**Complementar opcional:** [Consultar aprofundamento 02.02](complementares/README.md). Referência adicional; não é necessária para executar o lab.

## ✅ Revisão do aprendizado

- Qual papel de ServiceAccount, Role e RoleBinding no mesmo fluxo de autorização?
- Por que uma ClusterRole referenciada por RoleBinding não implica acesso em todos os namespaces?
- Como demonstrar uma permissão negada sem criar credenciais de serviço?

## 🔗 Referências oficiais

- [Documentação oficial do conceito](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- [Documentação oficial do conceito](https://kubernetes.io/docs/concepts/security/service-accounts/)

---

[← Aula 02.01 — Labels, Selectors e Annotations](../labels-selectors-annotations/README.md) · [↑ Camada 02](../README.md) · [🧪 Lab 02.02](../labs/rbac-minimo/README.md) · [Próxima: Aula 02.03 — SecurityContext e Pod Security Admission →](../securitycontext-pod-security/README.md)
