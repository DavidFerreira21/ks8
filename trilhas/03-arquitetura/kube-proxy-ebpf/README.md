# 03.13 · kube-proxy e eBPF

[⌂ Início](../../../README.md) · [↑ Camada 03](../README.md) · [📚 Catálogo](../../../docs/catalogo.md)

> **Ao concluir esta aula, você será capaz de:** Relacionar Services, EndpointSlices e implementação do dataplane, diferenciando kube-proxy de alternativas baseadas em eBPF.

## 🎨 Infográfico

![03.13 — kube-proxy e eBPF](images/kube-proxy-ebpf.png)

## 📖 Aula teórica

### Responsabilidade na arquitetura

Um Service oferece endereço e nome estáveis enquanto Pods de backend mudam. A implementação de encaminhamento pode depender de kube-proxy com iptables/nftables/IPVS ou de dataplane substituto. eBPF é uma tecnologia usada por alguns projetos, não um componente obrigatório de todo cluster.

### Mecanismo e fluxo de execução

O API Server armazena Service e EndpointSlices. Um controlador publica endpoints conforme selectors/readiness. O dataplane do cluster traduz acessos ao ClusterIP em conexões a backends. O kube-proxy observa essas mudanças e configura regras quando presente; eBPF pode assumir parte ou toda essa função conforme CNI instalado.

### Exemplo interpretado (trecho)

```yaml
apiVersion: v1
kind: Service
spec:
  selector:
    app: web
  ports:
    - port: 80
      targetPort: 80
```

O fragmento é uma representação didática: os campos de status são observados, não editados pelo aluno; os demais exemplos podem exigir objetos adicionais para constituir um manifesto completo.

### Inspeção e sinais observáveis

```bash
kubectl config current-context
kubectl get svc,endpointslices -n lab-03-13
kubectl get daemonsets -n kube-system
kubectl describe svc web -n lab-03-13
```

**Interpretação:** Desconfigure temporariamente o selector do Service e verifique mudança em EndpointSlices. Interprete conectividade separadamente do tipo de dataplane presente.

### Cuidados e limites

Não presuma que kube-proxy é um DaemonSet em todas as distribuições nem que eBPF substitui o dataplane no Kind padrão. Não altere regras de iptables no nó.

## 🧪 Aplicação prática

[🧪 Lab 03.13](../labs/kube-proxy-ebpf-basico/README.md) — desafio YAML, observação e experimento com evidências. Quando um componente não está no Kind, o lab diferencia **analogia local** de teste da implementação real.

**Complementar opcional:** [Aprofundamento sobre kube-proxy e eBPF](complementares/README.md); não é necessário para executar o laboratório.

## ✅ Revisão do aprendizado

- Por que Service criado não implica backends prontos?
- Que parte do comportamento depende de EndpointSlices e qual do dataplane?
- Quando usar eBPF não elimina a necessidade de Service Discovery?

## 🔗 Referências oficiais

- [Documentação oficial do conceito](https://kubernetes.io/docs/reference/networking/virtual-ips/)
- [Arquitetura e componentes](https://kubernetes.io/docs/concepts/overview/components/)

---

[← Aula 03.12](../cni-comunicacao/README.md) · [↑ Camada 03](../README.md) · [🧪 Lab 03.13](../labs/kube-proxy-ebpf-basico/README.md) · [Próxima: Aula 03.14 →](../coredns/README.md)
