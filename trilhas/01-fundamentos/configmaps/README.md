# 01.07 · ConfigMaps

[⌂ Início](../../../README.md) · [↑ Camada 01](../README.md) · [📚 Catálogo](../../../docs/catalogo.md)

> **Ao concluir esta aula, você será capaz de:** Explicar como configuração não sensível é separada da imagem e por que atualizações não afetam automaticamente variáveis de ambiente existentes.

## 🎨 Infográfico

![01.07 — ConfigMaps](images/configmaps.png)

## 📖 Aula teórica

## Separar configuração do artefato de aplicação

Um **ConfigMap** armazena configurações **não sensíveis**, geralmente em pares chave-valor ou arquivos. Isso permite publicar uma mesma imagem de aplicação em ambientes diferentes, variando parâmetros sem reconstruí-la.

É um objeto com escopo de namespace; referências a ConfigMaps feitas por Pods normalmente precisam apontar para ConfigMaps do mesmo namespace.

## Como os containers consomem valores?

| Forma | Como funciona | Atualização |
| --- | --- | --- |
| `env` com `configMapKeyRef` | Injeta uma chave como variável de ambiente | Não altera a variável de um processo já iniciado |
| `envFrom` | Injeta múltiplas chaves como variáveis | Requer reiniciar/recriar o Pod para atualizar as variáveis |
| Volume de ConfigMap | Monta chaves como arquivos | Pode refletir alterações eventualmente, com restrições; `subPath` não atualiza automaticamente |

## Exemplo de definição

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_MODE: "dev"
  API_URL: "https://api.example.invalid"
```

## Exemplo de uso no Pod

```yaml
env:
  - name: APP_MODE
    valueFrom:
      configMapKeyRef:
        name: app-config
        key: APP_MODE
```

O segundo trecho pertence a um container, em `spec.containers[].env`. A API não injeta valores em containers arbitrários: a configuração deve estar referenciada no template do Pod.

## Cuidados e diagnóstico

Não coloque senhas, tokens ou chaves em ConfigMap. Para esses dados, estude Secrets e o gerenciamento seguro de credenciais. Evite depender de atualização imediata de arquivos montados, sobretudo quando o aplicativo mantém configurações em cache.

```bash
kubectl get configmaps
kubectl describe configmap app-config
kubectl get configmap app-config -o yaml
```

O objeto `app-config` precisa existir. Se a variável não aparece no Pod, confira namespace, chave, referência e se o Pod foi recriado após a alteração.

## 🧪 Aplicação prática

**🧪 Lab 01.07:** [🧪 Lab 01.07](../labs/configmaps-basico/README.md). Execute as etapas no seu Kind, observe os eventos e registre sua hipótese antes do experimento.

## ✅ Revisão do aprendizado

- O que muda quando um ConfigMap consumido via `envFrom` é atualizado?
- Por que reiniciar os Pods pode ser necessário para consumir um novo valor de variável de ambiente?
- Quando usar ConfigMap em vez de Secret?

## 🔗 Referências oficiais

[Documentação Kubernetes — ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)

---

[← Aula 01.06 — Namespaces](../namespaces/README.md) · [↑ Camada 01](../README.md) · [🧪 Lab 01.07](../labs/configmaps-basico/README.md) · [Próxima: Aula 01.08 — Secrets →](../secrets/README.md)
