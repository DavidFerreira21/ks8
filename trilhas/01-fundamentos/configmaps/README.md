# 01.07 · ConfigMaps

[⌂ Início](../../../README.md) · [↑ Camada 01](../README.md) · [📚 Catálogo](../../../docs/catalogo.md)

> **Objetivo:** compreender o conceito, interpretar seu comportamento no cluster e conectar a teoria à prática.

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

**🧪 Lab 01.07:** [abrir exercício guiado](../labs/configmaps-basico/README.md). Execute as etapas no seu Kind, observe os eventos e registre sua hipótese antes do experimento.

## ✅ Revisão do aprendizado

- Qual problema este conceito resolve?
- Que campos ou estados da API permitem verificar o comportamento real?
- Que erro ou decisão equivocada você conseguiria diagnosticar após esta aula?

## 🔗 Referência oficial

[Documentação Kubernetes — ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)

---

[↑ Índice da camada](../README.md) · [Próxima: Secrets →](../secrets/README.md)
