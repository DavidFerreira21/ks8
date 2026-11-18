# Lab 02.03 — SecurityContext e admissão PSA

[← Aula 02.03](../../securitycontext-pod-security/README.md) · [↑ Camada 02](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=02.03` cria o namespace e copia um **starter incompleto** para `.labs/02.03/resources.yaml`. Você completa o YAML e executa `kubectl apply -f .labs/02.03/`. Só então use `make lab-test LAB=02.03` e `make lab-observe LAB=02.03`. **`make lab-up` aplica a solução e é reservado à CI.**

## Objetivo e hipótese

Configurar execução sem root e observar o efeito de um namespace com perfil de Pod Security.

**Pré-requisitos:** Kind `dev`, contexto `kind-dev`, `kubectl`, `make`; namespace isolado `lab-02-03`. O experimento não eleva privilégios nem altera namespaces de sistema.

## Desafio — o que você vai construir

Defina um Pod `seguro` com BusyBox, `runAsNonRoot: true`, `runAsUser: 10001`, `allowPrivilegeEscalation: false` e capabilities `drop: [ALL]`. Ele deve dormir por tempo suficiente para observação.

Antes de olhar `solution/`, formule uma hipótese sobre o comportamento e consulte `kubectl explain` quando necessário.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=02.03
cat .labs/02.03/resources.yaml
```

Descreva quais objetos devem aparecer e qual observação confirmará sua hipótese.

## Fase 2 — Aplicar e observar

Complete os campos TODO no starter e execute:

```bash
kubectl apply -f .labs/02.03/
make lab-test LAB=02.03
make lab-observe LAB=02.03
```

Inspecione `kubectl get pod seguro -n lab-02-03 -o yaml` e `kubectl describe pod seguro -n lab-02-03` para conferir os campos de segurança e status.

## Fase 3 — Experimento controlado

No Kind local, aplique `kubectl label namespace lab-02-03 pod-security.kubernetes.io/warn=restricted --overwrite`. Reaplique seu YAML para observar avisos, se houver. Remova a label após o teste com `kubectl label namespace lab-02-03 pod-security.kubernetes.io/warn-`. **Não use `enforce` sem antes verificar o impacto.**

## Resultado esperado e evidências

Os campos de securityContext aparecem no objeto. O modo `warn` pode avisar requisitos ausentes sem necessariamente impedir a criação.

**Evidências específicas:** registre securityContext, status do Pod, labels PSA do namespace e qualquer aviso gerado sem inserir credenciais.

## Fase 4 — Diagnosticar

`kubectl describe pod seguro -n lab-02-03`; diferencie falha de admissão, container sem privilégio e erro de imagem.

Se a observação divergir, identifique primeiro **contexto → namespace → objeto → eventos → hipótese**, sem aplicar soluções aleatórias.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=02.03
make lab-status LAB=02.03
```

A limpeza remove os objetos declarados no contrato e preserva o namespace. Desfaça explicitamente alterações manuais do experimento. **Não execute `make down`**, que remove o cluster Kind.

## Critérios de conclusão

- [ ] Completei o YAML sem copiar a solução e confirmei o contexto esperado.
- [ ] Observei o comportamento específico descrito em **Resultado esperado**.
- [ ] Registrei o resultado do experimento, uma hipótese e a explicação técnica.
- [ ] Removi os recursos do lab e revi qualquer alteração manual.

## Perguntas de diagnóstico e reflexão

- Por que `runAsNonRoot` não equivale a uma política PSA?
- Por que avisos no modo `warn` não significam bloqueio?

## Aprofunde seus conhecimentos

[Documentação oficial](https://kubernetes.io/docs/concepts/security/pod-security-admission/) · [Aula 02.03](../../securitycontext-pod-security/README.md)

---

[← Lab 02.02](../rbac-minimo/README.md) · [↑ Camada 02](../../README.md) · [Próximo: Lab 02.04 →](../quota-namespace/README.md)
