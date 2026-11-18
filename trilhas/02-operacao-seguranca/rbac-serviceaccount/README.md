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

## ✅ Revisão do aprendizado

- Qual papel de ServiceAccount, Role e RoleBinding no mesmo fluxo de autorização?
- Por que uma ClusterRole referenciada por RoleBinding não implica acesso em todos os namespaces?
- Como demonstrar uma permissão negada sem criar credenciais de serviço?

## 🔗 Referências oficiais

- [Documentação Kubernetes](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- [Documentação Kubernetes](https://kubernetes.io/docs/concepts/security/service-accounts/)

---

[↑ Camada 02](../README.md) · [🧪 Lab 02.02](../labs/rbac-minimo/README.md) · [← Aula 02.01](../labels-selectors-annotations/README.md) · [Próxima: 02.03 →](../securitycontext-pod-security/README.md)
