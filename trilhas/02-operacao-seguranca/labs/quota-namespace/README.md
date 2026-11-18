# Lab 02.04 — ResourceQuota e LimitRange

[← Aula 02.04](../../resourcequota-limitrange/README.md) · [↑ Camada 02](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=02.04` cria o namespace e copia um **starter incompleto** para `.labs/02.04/resources.yaml`. Você completa o YAML e executa `kubectl apply -f .labs/02.04/`. Só então use `make lab-test LAB=02.04` e `make lab-observe LAB=02.04`. **`make lab-up` aplica a solução e é reservado à CI.**

## Objetivo e hipótese

Observar defaults de admissão e a rejeição deliberada do segundo Pod ao atingir a quota do namespace.

**Pré-requisitos:** Kind `dev`, contexto `kind-dev`, `kubectl`, `make`; namespace isolado `lab-02-04`. 

## Desafio — o que você vai construir

Escreva ResourceQuota `pod-count` com `pods: '1'`, LimitRange `container-defaults` com defaults CPU/memória e Pod `demo-1` que não declare requests/limits no template.

Antes de olhar `solution/`, formule uma hipótese sobre o comportamento e consulte `kubectl explain` quando necessário.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=02.04
cat .labs/02.04/resources.yaml
```

Descreva quais objetos devem aparecer e qual observação confirmará sua hipótese.

## Fase 2 — Aplicar e observar

Complete os campos TODO no starter e execute:

```bash
kubectl apply -f .labs/02.04/
make lab-test LAB=02.04
make lab-observe LAB=02.04
```

Use `kubectl describe resourcequota pod-count -n lab-02-04` e `kubectl get pod demo-1 -n lab-02-04 -o yaml` para comparar defaults com seu YAML.

## Fase 3 — Experimento controlado

Tente criar um segundo Pod com `kubectl run demo-2 -n lab-02-04 --image=nginx:1.27 --restart=Never`. A criação deve ser rejeitada por quota. Caso seja admitido, remova-o e investigue o estado de `used` e `hard`. Para validar a rejeição de forma reproduzível, também execute `make lab-experiment LAB=02.04 EXPERIMENT=reject-pod`; o contrato usa o mesmo namespace e só considera sucesso quando o erro confirma quota excedida.

## Resultado esperado e evidências

`used: pods: 1` e falha de admissão com motivo de quota. Os defaults definidos pelo LimitRange aparecem no Pod admitido.

**Evidências específicas:** registre os valores `hard`/`used`, requests/limits admitidos e o erro específico de quota na tentativa de criar `demo-2`.

## Fase 4 — Diagnosticar

`kubectl describe quota pod-count -n lab-02-04`; se a criação inesperada tiver sucesso, `kubectl delete pod demo-2 -n lab-02-04`.

Se a observação divergir, identifique primeiro **contexto → namespace → objeto → eventos → hipótese**, sem aplicar soluções aleatórias.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=02.04
make lab-status LAB=02.04
```

A limpeza remove os objetos declarados no contrato e preserva o namespace. Desfaça explicitamente alterações manuais do experimento. **Não execute `make down`**, que remove o cluster Kind.

## Critérios de conclusão

- [ ] Completei o YAML sem copiar a solução e confirmei o contexto esperado.
- [ ] Observei o comportamento específico descrito em **Resultado esperado**.
- [ ] Registrei o resultado do experimento, uma hipótese e a explicação técnica.
- [ ] Removi os recursos do lab e revi qualquer alteração manual.

## Perguntas de diagnóstico e reflexão

- O que o LimitRange injeta em um Pod sem requests definidos?
- Por que a rejeição ocorre na admissão e não no scheduler?

## Aprofunde seus conhecimentos

[Documentação oficial](https://kubernetes.io/docs/concepts/policy/resource-quotas/) · [Aula 02.04](../../resourcequota-limitrange/README.md)

---

[← Lab 02.03](../securitycontext-psa-basico/README.md) · [↑ Camada 02](../../README.md) · [Próximo: Lab 02.05 →](../init-sidecars-basico/README.md)
