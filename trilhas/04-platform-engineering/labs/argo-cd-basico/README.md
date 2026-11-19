# Lab 04.01 — Argo CD

[← Aula 04.01](../../argo-cd/README.md) · [↑ Camada 04](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** `make lab-prepare LAB=04.01` cria o namespace e copia um starter incompleto para `.labs/04.01/resources.yaml`. **Instale previamente o controlador/CRD do produto** de acordo com o procedimento documentado; complete o YAML e execute `kubectl apply --dry-run=server --validate=strict -f .labs/04.01/
kubectl apply -f .labs/04.01/`. O comando `make lab-up` usa a solução e é exclusivo de CI com os addons adequados.

## Objetivo e hipótese

Criar uma Application real e comparar o estado sincronizado com o destino no Kubernetes.

**Contexto:** `kind-dev` ou cluster de sandbox explicitamente autorizado, namespace de estudo `lab-04-01`. `make lab-test` verifica objetos, **não prova sozinho a funcionalidade do controller**.

## Pré-requisitos da ferramenta

**Guia de instalação, versões e reversão:** [🛠️ Preparar Argo CD](../../../../docs/ambientes/04-argo-cd.md). Siga-o antes de aplicar Custom Resources; a CI padrão não instala esse controlador.

**Instale Argo CD no próprio namespace `lab-04-01` com o procedimento oficial de instalação (ou configure Applications in any namespace se a instalação estiver em outro namespace).** Confirme `kubectl api-resources --api-group=argoproj.io` e o controller Ready antes do apply. O projeto default deve permitir o repositório e o destino do lab.

**Segurança:** **Exige Argo CD real**, controlador e CRD. O Kind padrão não homologa este lab automaticamente. Instalação e remoção do Argo CD são tarefas administrativas separadas.

## Desafio — o que você vai construir

Escreva Application `guestbook-estudo`, namespace `lab-04-01`, source do repositório público `argoproj/argocd-example-apps`, path `guestbook`, targetRevision `HEAD` e destino nesse namespace. Comece com sincronização manual.

Defina sua hipótese antes de consultar `solution/`. Se o tipo não aparecer em `kubectl api-resources`, registre dependência ausente e não tente contornar com recursos fictícios.

## Fase 1 — Preparar e prever

```bash
kubectl config current-context
make lab-prepare LAB=04.01
cat .labs/04.01/resources.yaml
```

Confirme disponibilidade da API específica da ferramenta e o namespace alvo antes de aplicar.

## Fase 2 — Aplicar e observar

Complete os TODOs:

```bash
kubectl apply -f .labs/04.01/
make lab-test LAB=04.01
make lab-observe LAB=04.01
```

`kubectl get application guestbook-estudo -n lab-04-01 -o yaml` exibe sync.status e health.status. Acesse Argo CD via procedimento oficial e sincronize manualmente; observe os recursos criados.

## Fase 3 — Experimento controlado

Altere um campo do Deployment gerenciado por Argo CD diretamente via `kubectl` e observe OutOfSync; depois execute Sync pela interface/CLI autorizada. Se a Application não for reconhecida, confirme o namespace de instalação e a configuração do controller.

## Resultado esperado e evidências

Argo CD compara Git e cluster, sinaliza drift e sincroniza quando solicitado. A criação da Application não substitui a operação de Sync nem prova Health.

**Evidências específicas:** registre repo/path/revisão, Sync status antes/depois, Health e o objeto efetivamente reconciliado; mantenha observações de erro se o controller não estiver instalado.

## Fase 4 — Diagnosticar

Investigue CRDs, condições dos custom resources, logs do controller instalado e permissões. Diferencie **rejeição de API**, **ausência de controller**, **reconciliação não pronta** e **falta de dependência externa**.

## Fase 5 — Limpar com segurança

```bash
make lab-down LAB=04.01
make lab-status LAB=04.01
```

A limpeza remove os objetos declarados neste contrato, **não desinstala automaticamente o addon**. Revise recursos filhos, credenciais e qualquer custo externo antes de excluir a instalação. Na ausência do addon, não tente remoção indiscriminada.

## Critérios de conclusão

- [ ] Escrevi o manifesto principal sem copiar a solução e validei as APIs necessárias.
- [ ] **Critério exclusivo 04.01:** registre repo/path/revisão, Sync status antes/depois, Health e o objeto efetivamente reconciliado; mantenha observações de erro se o controller não estiver instalado.
- [ ] Diferenciei validação declarativa de comportamento funcional realmente observado.
- [ ] Reverti mudanças temporárias e executei a limpeza segura.

## Perguntas de diagnóstico e reflexão

- Que diferença existe entre Application criada, Synced e Healthy?
- Por que drift manual pode gerar OutOfSync?
- Qual configuração autoriza Applications em namespace fora da instalação?

## Aprofunde seus conhecimentos

[Documentação oficial](https://argo-cd.readthedocs.io/en/stable/getting_started/) · [Aula 04.01](../../argo-cd/README.md)

---

[← Camada 03](../../../03-arquitetura/README.md) · [↑ Aula 04.01](../../argo-cd/README.md) · [↑ Camada 04](../../README.md) · [Próximo: Lab 04.02 →](../crossplane-basico/README.md)
