# 02.05 · Init Containers e Sidecars

[⌂ Início](../../../README.md) · [↑ Camada 02](../README.md) · [📚 Catálogo](../../../docs/catalogo.md)

> **Ao concluir esta aula, você será capaz de:** Explicar a ordem de inicialização e identificar a diferença entre init containers comuns e sidecars nativos.

## 🎨 Infográfico

![02.05 — Init Containers e Sidecars](../init-containers-sidecars/images/init-containers-sidecars.png)

## 📖 Aula teórica

### O problema que este recurso resolve

Init containers comuns executam e terminam antes dos containers principais. Um sidecar nativo é definido em `initContainers` com `restartPolicy: Always`: inicia no fluxo de init e permanece ativo enquanto a aplicação opera.

### Como funciona no Kubernetes

Os init containers comuns precisam concluir com sucesso; falhas são retentadas segundo as políticas aplicáveis. O sidecar nativo permanece em execução e seu status aparece em `initContainerStatuses`. Containers adicionais comuns em `containers` também podem fazer papel auxiliar, mas têm semântica de ciclo de vida diferente.

### Exemplo interpretado (trecho)

Sidecar nativo usa `restartPolicy: Always` sob `initContainers`, ao contrário do init comum que precisa terminar.

```yaml
initContainers:
  - name: auxiliar
    image: busybox:1.36
    restartPolicy: Always
    command: ["sh", "-c", "sleep 3600"]
```

Este é um **trecho ilustrativo**, não um manifesto para aplicar isoladamente. A implementação completa será escrita pelo aluno no laboratório.

### Exemplo de inspeção

Os comandos abaixo são exemplos para um cluster de estudo. Substitua os nomes ilustrativos e confirme o contexto antes de executar.

```bash
kubectl config current-context
kubectl get pod POD -n NAMESPACE -o jsonpath='{.status.initContainerStatuses}'
kubectl logs POD -n NAMESPACE -c init-prepare
kubectl describe pod POD -n NAMESPACE
```

**O que observar:** Registre a sequência dos init containers e a permanência do sidecar nativo. A aplicação só deve iniciar quando os init containers necessários satisfizerem suas condições.

### Cuidados e limitações

Um sidecar nativo não é um Job; processos eternos como init containers comuns impedem o Pod de iniciar. Verifique compatibilidade da versão do Kubernetes.

## 🧪 Aplicação prática

**[🧪 Lab 02.05](../labs/init-sidecars-basico/README.md):** escreva o YAML do exercício, execute no Kind, registre evidências e explique as divergências. O complementar não é pré-requisito.

## ✅ Revisão do aprendizado

- Por que um init container comum que nunca termina impede a aplicação de iniciar?
- Qual campo identifica um sidecar nativo na definição do Pod?
- Que status comprova a ordem dos init containers?

## 🔗 Referências oficiais

- [Documentação Kubernetes](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/)
- [Documentação Kubernetes](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/)

---

[↑ Camada 02](../README.md) · [🧪 Lab 02.05](../labs/init-sidecars-basico/README.md) · [← Aula 02.04](../resourcequota-limitrange/README.md) · [Próxima: 02.06 →](../jobs-cronjobs/README.md)
