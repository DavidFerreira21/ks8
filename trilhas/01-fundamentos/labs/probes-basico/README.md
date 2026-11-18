# Lab 01.10 — Probes

[← Aula 01.10](../../probes/README.md) · [↑ Camada 01](../../README.md) · [🧪 Índice dos labs](../../../../docs/labs.md)

> **MODO DESAFIO:** execute `make lab-prepare LAB=01.10`, complete `.labs/01.10/resources.yaml` e execute **`kubectl apply -f .labs/01.10/`**. Só depois valide com `make lab-test LAB=01.10`. `make lab-up` aplica a solução completa e fica reservado à CI; `make lab-solution LAB=01.10` revela seus arquivos para estudo posterior.


## Objetivo e hipótese

Uma aplicação Running pode estar NotReady. O experimento cria uma falha de readiness e restaura via rollback, sem atribuir a falha à liveness.

**Escopo:** cluster Kind `dev`, namespace exclusivo `lab-01-10`.

## Desafio — o que você vai construir

Escreva o Deployment `web` com nginx e configure **readinessProbe** e **livenessProbe** HTTP na porta 80. Inicialmente ambas devem verificar `/`. Depois aplique a alteração controlada da readiness para um caminho inválido e observe a nova revisão.

**Antes de aplicar:** use o arquivo incompleto em `.labs/01.10/` como ponto de partida. Confira campos com `kubectl explain`; não abra a solução antes de formular uma tentativa.

## Fase 1 — Preparar

```bash
kubectl config current-context
kubectl get nodes
make lab-prepare LAB=01.10
cat .labs/01.10/resources.yaml
```

Preveja os objetos criados e seus estados.

## Fase 2 — Executar

```bash
# Preencha os arquivos de trabalho
kubectl apply -f .labs/01.10/
make lab-test LAB=01.10
make lab-observe LAB=01.10
```

**Observe as condições:**

```bash
kubectl get pods -n lab-01-10 -w
kubectl describe deployment web -n lab-01-10
```

**Experimento — readiness inválida sem derrubar a réplica anterior:** aplique um patch no template do Deployment, criando nova revisão com caminho inválido:

```bash
kubectl patch deployment web -n lab-01-10 --type=strategic -p '{"spec":{"template":{"spec":{"containers":[{"name":"nginx","readinessProbe":{"httpGet":{"path":"/nao-existe","port":80}}}]}}}}'
kubectl get pods -n lab-01-10 -w
```

Interrompa o watch com Ctrl+C. Compare o novo Pod (não Ready) e o Pod da revisão anterior. Veja detalhes com `kubectl describe pod`. **Recupere o rollout:**

```bash
kubectl rollout undo deployment/web -n lab-01-10
kubectl rollout status deployment/web -n lab-01-10 --timeout=120s
make lab-test LAB=01.10
```

Repare que readiness controla elegibilidade ao tráfego e progressão do rollout; liveness decide quando reiniciar o container.

## Resultado esperado e evidências

- Inicialmente o Pod do Deployment fica `Ready` com sucesso nas verificações HTTP.
- Uma revisão com readiness em `/nao-existe` tem novo Pod `Running`, mas **NotReady**; o rollout pode ficar travado porque o Pod não é elegível para tráfego.
- `kubectl rollout undo` recupera a revisão saudável. Falhar readiness não equivale a reinício por liveness; compare `READY` e `RESTARTS`.

**Se o resultado divergir:** confirme contexto, namespace, eventos e o YAML escrito. Diferencie comportamento intencional do experimento e erro na sua configuração.

## Fase 3 — Diagnosticar

```bash
kubectl get events -n lab-01-10 --sort-by=.lastTimestamp
kubectl get all -n lab-01-10
```

Leia `describe`, compare `spec` e `status` e explique eventos. Testes automatizados conferem existência e readiness quando indicado, não o experimento pedagógico.

## Fase 4 — Limpeza

```bash
make lab-down LAB=01.10
make lab-status LAB=01.10
```

Namespace preservado intencionalmente. Nunca apague o cluster inteiro para limpar só um lab.

## Critérios de conclusão

- [ ] Configurei readiness e liveness com funções diferentes.
- [ ] Observei o novo Pod Running/NotReady no experimento.
- [ ] Expliquei por que readiness inválida bloqueia disponibilidade sem necessariamente reiniciar o container.
- [ ] Executei rollback, vi o rollout saudável e limpei o lab.

## Perguntas de diagnóstico e reflexão

- Qual efeito observado diferencia falha de readiness de falha de liveness?
- Que configuração evitaria reinícios prematuros em aplicações com startup demorada?

**Evidências específicas:** registre condições Ready, eventos e contagem de reinícios antes e depois de provocar as falhas de probes; explique o efeito de liveness versus readiness.

## Aprofunde seus conhecimentos

[Probes](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/) · [Configurar probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/) · [Deployments e rollback](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#rolling-back-a-deployment).

Releia a [aula teórica](../../probes/README.md) e compare os exemplos com o que você observou no cluster.

---

[← Lab 01.09](../requests-limits-basico/README.md) · [↑ Aula 01.10](../../probes/README.md) · [Próximo: Lab 01.11 →](../volumes-basico/README.md)
