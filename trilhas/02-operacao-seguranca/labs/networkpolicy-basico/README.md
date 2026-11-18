# Lab 02.13 — NetworkPolicy declarativa e limites do CNI

[← Aula 02.13](../../networkpolicy/README.md) · [↑ Camada 02](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=02.13` cria o namespace e copia o starter **incompleto** em `.labs/02.13/resources.yaml`. Complete-o, execute `kubectl apply -f .labs/02.13/`, depois `make lab-test LAB=02.13` e `make lab-observe LAB=02.13`. **`make lab-up` aplica a solução e é exclusivo da CI.**

## Objetivo e hipótese

Definir default-deny ingress por namespace e diferenciar validação do objeto de enforcement real de rede.

**Pré-requisitos:** Kind `dev`, contexto `kind-dev`, `kubectl` e `make`; namespace exclusivo `lab-02-13`. O Kind padrão não garante implementação de NetworkPolicy; a validação de rede requer um CNI com enforcement e experimento separado.

## Desafio — o que você vai construir

Crie Pod `alvo` BusyBox com label `app: alvo` e NetworkPolicy `isolar-ingress` que seleciona esse Pod e declara `policyTypes: [Ingress]` com lista `ingress: []`.

Preveja o que deve acontecer antes de abrir `solution/`. Use `kubectl explain` e a aula para esclarecer a API.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=02.13
cat .labs/02.13/resources.yaml
```

## Fase 2 — Aplicar e observar

Complete os TODOs e execute:

```bash
kubectl apply -f .labs/02.13/
make lab-test LAB=02.13
make lab-observe LAB=02.13
```

`kubectl get networkpolicy isolar-ingress -n lab-02-13 -o yaml` deve exibir o selector e política; `kubectl get pods -n lab-02-13 --show-labels` mostra a seleção.

## Fase 3 — Experimento controlado

Compare os campos da política com a label do Pod e explique o tráfego que **seria** bloqueado com um CNI que implemente policies. Em Kind padrão, não afirme bloqueio sem instalar/verificar CNI apropriado e executar prova de conectividade.

## Resultado esperado e evidências

O API Server aceita o objeto. **Isso não valida enforcement.** Com Kind padrão, o teste funcional de bloqueio fica pendente.

**Evidências específicas:** registre Pod labels, selector e política na API; anote explicitamente que enforcement de tráfego não foi comprovado sem CNI compatível.

## Fase 4 — Diagnosticar

`kubectl describe networkpolicy isolar-ingress -n lab-02-13`; verifique se o CNI instalado realmente suporta políticas antes de confiar no isolamento.

Quando a observação não corresponder à hipótese, compare contexto, objetos, eventos e condições antes de modificar os manifests.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=02.13
make lab-status LAB=02.13
```

O namespace é preservado; desfaça **separadamente** alterações manuais de nó, policies, Pods temporários e outros recursos criados fora do contrato. Não execute `make down`.

## Critérios de conclusão

- [ ] **Evidência funcional do Lab 02.13:** a seleção da NetworkPolicy foi conferida e a ausência de enforcement sem CNI apropriado foi explicitamente registrada.
- [ ] Completei o YAML sem copiar a solução e validei o contexto `kind-dev`.
- [ ] Observei a condição específica descrita no resultado esperado.
- [ ] Registrei a hipótese inicial, evidências e explicação técnica.
- [ ] Fiz a limpeza e desmanchei todas as alterações manuais.

## Perguntas de diagnóstico e reflexão

- Por que a existência de NetworkPolicy não prova bloqueio?
- Qual diferença entre isolar ingress e egress?

- Qual verificação seria necessária para provar enforcement pelo CNI?

## Aprofunde seus conhecimentos

[Documentação Kubernetes](https://kubernetes.io/docs/concepts/services-networking/network-policies/) · [Aula 02.13](../../networkpolicy/README.md)

---

[← Lab 02.12](../node-maintenance-basico/README.md) · [↑ Camada 02](../../README.md) · [Próximo: Lab 02.14 →](../troubleshooting-basico/README.md)
