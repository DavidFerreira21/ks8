# 02.01 · Labels, Selectors e Annotations

[⌂ Início](../../../README.md) · [↑ Camada 02](../README.md) · [📚 Catálogo](../../../docs/catalogo.md)

> **Ao concluir esta aula, você será capaz de:** Relacionar labels, selectors e annotations e diagnosticar por que uma seleção inclui ou exclui objetos.

## 🎨 Infográfico

![02.01 — Labels, Selectors e Annotations](images/labels-selectors-annotations.png)

## 📖 Aula teórica

### O problema que este recurso resolve

Labels são pares chave/valor destinados à identificação e seleção. Selectors determinam o conjunto de objetos compatíveis. Annotations guardam metadados descritivos para ferramentas e automações, sem participar de selectors. Um selector incorreto pode remover todos os backends de um Service sem alterar o Service em si.

### Como funciona no Kubernetes

Selectors de igualdade usam `matchLabels` ou expressões; selectors de conjunto podem usar `In`, `NotIn`, `Exists` e `DoesNotExist` onde suportados. Labels são mutáveis, mas selectors em alguns controladores são imutáveis após criação. `kubectl get -l` filtra pelo valor observado, não pela intenção descrita no Git.

### Exemplo de inspeção

Os comandos abaixo são exemplos para um cluster de estudo. Substitua os nomes ilustrativos e confirme o contexto antes de executar.

```bash
kubectl config current-context
kubectl get pods -A --show-labels
kubectl get pods -n NAMESPACE -l app=web
kubectl get pods -n NAMESPACE -l 'tier in (frontend,api)'
```

**O que observar:** Compare a quantidade de Pods selecionados com os labels mostrados por `--show-labels`. Uma annotation com o mesmo texto não é selecionada por `-l`.

### Cuidados e limitações

Não armazene credenciais em annotations; elas não são um cofre. Diferencie selector do controlador e label do template; labels de Pod devem corresponder ao selector do Deployment.

## 🧪 Aplicação prática

**[🧪 Lab 02.01](../labs/labels-selectors-basico/README.md):** escreva o YAML do exercício, execute no Kind, registre evidências e explique as divergências. O complementar não é pré-requisito.

## ✅ Revisão do aprendizado

- Por que alterar uma annotation não faz um Service selecionar outro Pod?
- O que muda nos EndpointSlices quando o label usado pelo Service deixa de coincidir?
- Qual diferença existe entre `matchLabels` e `matchExpressions`?

## 🔗 Referências oficiais

- [Documentação Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)
- [Documentação Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)

---

[↑ Camada 02](../README.md) · [🧪 Lab 02.01](../labs/labels-selectors-basico/README.md) · [← Camada 01](../../01-fundamentos/README.md) · [Próxima: 02.02 →](../rbac-serviceaccount/README.md)
