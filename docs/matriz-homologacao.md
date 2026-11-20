# Matriz de homologação dos 50 laboratórios

[⌂ Início](../README.md) · [🧪 Execução](labs.md) · [📜 Contrato](padrao-editorial.md)

> **Critério:** a existência do contrato, teste estático, CI Kind e experimento funcional são quatro coisas diferentes. **Nenhum lab de addon é declarado homologado sem evidência de execução.**

## Status desta revisão

- **52 aulas / 50 labs documentados:** 04.04 (ESO) e 04.05 (Karpenter) permanecem aulas teóricas, sem lab; os outros 50 temas possuem contratos práticos.
- **Cobertura CI de base:** 12 da Camada 01 + 13 da Camada 02 + 17 da Camada 03 = **42 labs**, conforme scripts `ci-kind-smoke.sh` e `ci-kind-layer03.sh`.
- **8 labs fora da CI básica:** 2 da Camada 01, 1 da Camada 02 (02.13: enforcement depende do CNI) e 5 labs da Camada 04 que exigem addons. Os IDs 04.04/04.05 não são labs.
- **¹ Base CI aprovada:** refere-se à execução concluída da base anterior à revisão pedagógica. **A ampliação 02.09/02.12/02.14 só será aprovada após executar o novo HEAD.** A CI do **HEAD da auditoria** deve passar novamente antes de afirmar aprovação desta versão. Mesmo CI verde não prova todos os passos manuais.
- **Evidência pendente:** significa que ainda não há artefato reproduzível de execução funcional do cenário avançado no repositório; não significa necessariamente que o manifesto esteja incorreto.

## Como registrar uma homologação reproduzível

Para cada lab, guarde: data/hora, versão do Kubernetes e do addon, contexto/cluster, commit Git, comandos usados, estado inicial, evento ou tráfego observado, resultado esperado versus real, cleanup e link para logs/screenshot **sem segredos**.

Status sugeridos: `Editorial aprovado`, `Contrato validado`, `CI Kind aprovado`, `Funcional validado`, `Dependência ausente` ou `Falhou com evidência`. Não use a palavra "aprovado" sozinha sem informar nível.

## Matriz curricular

| Lab | Cobertura automática | Dependência/limite | Evidência específica requerida | Estado registrado |
| --- | --- | --- | --- | --- |
| [01.01](../trilhas/01-fundamentos/labs/fundamentos-cluster/README.md) | CI Kind, cobertura de base | CI cobre solução e checks; experimento manual deve ser documentado | Spec/status e nós do Kind | Base CI aprovada¹; experimento manual não registrado |
| [01.02](../trilhas/01-fundamentos/labs/pods-basico/README.md) | CI Kind, cobertura de base | CI cobre solução e checks; experimento manual deve ser documentado | Recriação de Pod avulso | Base CI aprovada¹; experimento manual não registrado |
| [01.03](../trilhas/01-fundamentos/labs/deployments-basico/README.md) | CI Kind, cobertura de base | CI cobre solução e checks; experimento manual deve ser documentado | ReplicaSet restaura Pods | Base CI aprovada¹; experimento manual não registrado |
| [01.04](../trilhas/01-fundamentos/labs/controladores-basico/README.md) | CI Kind, cobertura de base | CI cobre solução e checks; experimento manual deve ser documentado | DaemonSet/StatefulSet e identidade | Base CI aprovada¹; experimento manual não registrado |
| [01.05](../trilhas/01-fundamentos/labs/services-basico/README.md) | CI Kind, cobertura de base | CI cobre solução e checks; experimento manual deve ser documentado | Selector e EndpointSlices + HTTP | Base CI aprovada¹; experimento manual não registrado |
| [01.06](../trilhas/01-fundamentos/labs/namespaces-basico/README.md) | CI Kind, cobertura de base | CI cobre solução e checks; experimento manual deve ser documentado | Escopo de namespaces | Base CI aprovada¹; experimento manual não registrado |
| [01.07](../trilhas/01-fundamentos/labs/configmaps-basico/README.md) | CI Kind, cobertura de base | CI cobre solução e checks; experimento manual deve ser documentado | Mudança de ConfigMap env + restart | Base CI aprovada¹; experimento manual não registrado |
| [01.08](../trilhas/01-fundamentos/labs/secrets-basico/README.md) | CI Kind, cobertura de base | CI cobre solução e checks; experimento manual deve ser documentado | Secret consumido sem exibição | Base CI aprovada¹; experimento manual não registrado |
| [01.09](../trilhas/01-fundamentos/labs/requests-limits-basico/README.md) | CI Kind, cobertura de base | CI cobre solução e checks; experimento manual deve ser documentado | Requests, limits e QoS | Base CI aprovada¹; experimento manual não registrado |
| [01.10](../trilhas/01-fundamentos/labs/probes-basico/README.md) | CI Kind, cobertura de base | CI cobre solução e checks; experimento manual deve ser documentado | Readiness/liveness e restartCount | Base CI aprovada¹; experimento manual não registrado |
| [01.11](../trilhas/01-fundamentos/labs/volumes-basico/README.md) | CI Kind, cobertura de base | CI cobre solução e checks; experimento manual deve ser documentado | PVC Bound e marcador persistente | Base CI aprovada¹; experimento manual não registrado |
| [01.12](../trilhas/01-fundamentos/labs/estrategias-deployment-basico/README.md) | CI Kind, cobertura de base | CI cobre solução e checks; experimento manual deve ser documentado | Rollout e rollback comparados | Base CI aprovada¹; experimento manual não registrado |
| [01.13](../trilhas/01-fundamentos/labs/ingress-basico/README.md) | Fora do smoke Kind | Ingress Controller + teste Host HTTP | Host HTTP via Ingress Controller | Pendente addon |
| [01.14](../trilhas/01-fundamentos/labs/hpa-basico/README.md) | Fora do smoke Kind | Metrics Server + carga CPU | HPA CPU/replicas com carga | Pendente addon |
| [02.01](../trilhas/02-operacao-seguranca/labs/labels-selectors-basico/README.md) | CI Kind, cobertura de base | CI cobre contrato e cenários integrados selecionados | Labels vs annotations | Base CI aprovada¹; experimento manual não registrado |
| [02.02](../trilhas/02-operacao-seguranca/labs/rbac-minimo/README.md) | CI Kind, cobertura de base | CI cobre contrato e cenários integrados selecionados | RBAC can-i allow/deny | Base CI aprovada¹; experimento manual não registrado |
| [02.03](../trilhas/02-operacao-seguranca/labs/securitycontext-psa-basico/README.md) | CI Kind, cobertura de base | CI cobre contrato e cenários integrados selecionados | PSA warn/enforce dry-run | Base CI aprovada¹; experimento manual não registrado |
| [02.04](../trilhas/02-operacao-seguranca/labs/quota-namespace/README.md) | CI Kind, cobertura de base | CI cobre contrato e cenários integrados selecionados | Quota nega segundo Pod | Base CI aprovada¹; experimento manual não registrado |
| [02.05](../trilhas/02-operacao-seguranca/labs/init-sidecars-basico/README.md) | CI Kind, cobertura de base | CI cobre contrato e cenários integrados selecionados | Init e sidecar nativo | Base CI aprovada¹; experimento manual não registrado |
| [02.06](../trilhas/02-operacao-seguranca/labs/jobs-cronjobs-basico/README.md) | CI Kind, cobertura de base | CI cobre contrato e cenários integrados selecionados | Job concluído e CronJob | Base CI aprovada¹; experimento manual não registrado |
| [02.07](../trilhas/02-operacao-seguranca/labs/scheduling-basico/README.md) | CI Kind, cobertura de base | CI cobre contrato e cenários integrados selecionados | Taint e toleration com reversão | Base CI aprovada¹; experimento manual não registrado |
| [02.08](../trilhas/02-operacao-seguranca/labs/topology-spread-basico/README.md) | CI Kind, cobertura de base | CI cobre contrato e cenários integrados selecionados | Topology Spread 2 Ready + 1 Pending | Base CI aprovada¹; experimento manual não registrado |
| [02.09](../trilhas/02-operacao-seguranca/labs/priorityclass-basico/README.md) | CI Kind, nova cobertura | Comparação de prioridade sem preempção | PriorityClass sem preempção real | Execução do HEAD pendente |
| [02.10](../trilhas/02-operacao-seguranca/labs/qos-eviction-basico/README.md) | CI Kind, cobertura de base | CI cobre contrato e cenários integrados selecionados | QoS classes e Burstable | Base CI aprovada¹; experimento manual não registrado |
| [02.11](../trilhas/02-operacao-seguranca/labs/pdb-basico/README.md) | CI Kind, cobertura de base | CI cobre contrato e cenários integrados selecionados | PDB disruptionsAllowed | Base CI aprovada¹; experimento manual não registrado |
| [02.12](../trilhas/02-operacao-seguranca/labs/node-maintenance-basico/README.md) | CI Kind, nova cobertura | Nó Kind isolado, cordon e reversão | Cordon/uncordon, sem drain | Execução do HEAD pendente |
| [02.13](../trilhas/02-operacao-seguranca/labs/networkpolicy-basico/README.md) | Fora do smoke Kind | CNI que aplica NetworkPolicy | NetworkPolicy enforcement real | Pendente cenário específico |
| [02.14](../trilhas/02-operacao-seguranca/labs/troubleshooting-basico/README.md) | CI Kind, nova cobertura | Diagnóstico e recuperação em execução | Falha de imagem + correção | Execução do HEAD pendente |
| [03.01](../trilhas/03-arquitetura/labs/arquitetura-cluster-basico/README.md) | CI Kind, 17 labs | CI cobre solução/check; comparar fase manual | Réplica e UID gerenciados | Base CI aprovada¹; experimento manual não registrado |
| [03.02](../trilhas/03-arquitetura/labs/kube-apiserver-basico/README.md) | CI Kind, 17 labs | CI cobre solução/check; comparar fase manual | Dry-run server válido/inválido | Base CI aprovada¹; experimento manual não registrado |
| [03.03](../trilhas/03-arquitetura/labs/etcd-basico/README.md) | CI Kind, 17 labs | CI cobre solução/check; comparar fase manual | resourceVersion antes/depois | Base CI aprovada¹; experimento manual não registrado |
| [03.04](../trilhas/03-arquitetura/labs/admission-controllers-basico/README.md) | CI Kind, 17 labs | CI cobre solução/check; comparar fase manual | Admission quota rejeitada | Base CI aprovada¹; experimento manual não registrado |
| [03.05](../trilhas/03-arquitetura/labs/kube-controller-manager-basico/README.md) | CI Kind, 17 labs | CI cobre solução/check; comparar fase manual | Controller reconcilia Pod | Base CI aprovada¹; experimento manual não registrado |
| [03.06](../trilhas/03-arquitetura/labs/crds-custom-resources-basico/README.md) | CI Kind, 17 labs | CI cobre solução/check; comparar fase manual | CRD Established/schema rejeita CR | Base CI aprovada¹; experimento manual não registrado |
| [03.07](../trilhas/03-arquitetura/labs/custom-controllers-operators-basico/README.md) | CI Kind, 17 labs | Controller Python customizado opcional | Reconciler nativo vs controller próprio | Base CI aprovada¹; avançado opcional pendente |
| [03.08](../trilhas/03-arquitetura/labs/kube-scheduler-basico/README.md) | CI Kind, 17 labs | CI cobre solução/check; comparar fase manual | Unschedulable por selector | Base CI aprovada¹; experimento manual não registrado |
| [03.09](../trilhas/03-arquitetura/labs/cloud-controller-manager-basico/README.md) | CI Kind, 17 labs | Cloud Controller Manager real (fora do Kind) | LoadBalancer sem cloud | Base CI aprovada¹; avançado opcional pendente |
| [03.10](../trilhas/03-arquitetura/labs/kubelet-basico/README.md) | CI Kind, 17 labs | CI cobre solução/check; comparar fase manual | Readiness controlada pelo kubelet | Base CI aprovada¹; experimento manual não registrado |
| [03.11](../trilhas/03-arquitetura/labs/container-runtime-basico/README.md) | CI Kind, 17 labs | CI cobre solução/check; comparar fase manual | Erro de pull vs container iniciado | Base CI aprovada¹; experimento manual não registrado |
| [03.12](../trilhas/03-arquitetura/labs/cni-comunicacao-basico/README.md) | CI Kind, 17 labs | CI cobre solução/check; comparar fase manual | HTTP por Pod IP | Base CI aprovada¹; experimento manual não registrado |
| [03.13](../trilhas/03-arquitetura/labs/kube-proxy-ebpf-basico/README.md) | CI Kind, 17 labs | Cilium dataplane real opcional | EndpointSlice e dataplane | Base CI aprovada¹; avançado opcional pendente |
| [03.14](../trilhas/03-arquitetura/labs/coredns-basico/README.md) | CI Kind, 17 labs | CI cobre solução/check; comparar fase manual | FQDN vs backend sem endpoints | Base CI aprovada¹; experimento manual não registrado |
| [03.15](../trilhas/03-arquitetura/labs/csi-storage-basico/README.md) | CI Kind, 17 labs | CSI Hostpath real opcional | Arquivo persistente via PVC | Base CI aprovada¹; avançado opcional pendente |
| [03.16](../trilhas/03-arquitetura/labs/gateway-api-basico/README.md) | CI Kind, 17 labs | Gateway API + Envoy Gateway opcional | Service nativo vs HTTPRoute | Base CI aprovada¹; avançado opcional pendente |
| [03.17](../trilhas/03-arquitetura/labs/kustomize-helm-basico/README.md) | CI Kind, 17 labs | CI cobre solução/check; comparar fase manual | Kustomize base/overlay | Base CI aprovada¹; experimento manual não registrado |
| [04.01](../trilhas/04-platform-engineering/labs/argo-cd-basico/README.md) | Somente contrato estático | Argo CD instalado e AppProject | Application Synced/Healthy e drift | Funcional pendente: addon/ambiente específico |
| [04.02](../trilhas/04-platform-engineering/labs/crossplane-basico/README.md) | Somente contrato estático | Crossplane v2 + Function + Composition | XRD, Function, XR e ConfigMap composto | Funcional pendente: addon/ambiente específico |
| [04.03](../trilhas/04-platform-engineering/labs/kyverno-basico/README.md) | Somente contrato estático | Kyverno CEL/webhook | Policy CEL nega/admite | Funcional pendente: addon/ambiente específico |
| [04.06](../trilhas/04-platform-engineering/labs/cilium-basico/README.md) | Somente contrato estático | Kind Cilium dedicado | Cilium ingress permitido/negado | Funcional pendente: addon/ambiente específico |
| [04.07](../trilhas/04-platform-engineering/labs/prometheus-grafana-basico/README.md) | Somente contrato estático | Prometheus Operator + Grafana | Target UP + PromQL + painel Grafana | Funcional pendente: addon/ambiente específico |

**Cobertura adicional nesta revisão:** 02.09 agora verifica PriorityClass/Pod sem preempção, 02.12 confirma cordon/uncordon com agendamento bloqueado e recuperado e 02.14 observa falha de pull e recuperação. **02.13 permanece fora do smoke** para evitar alegação falsa de enforcement no Kind padrão; seu [roteiro opcional com Cilium](../trilhas/02-operacao-seguranca/labs/networkpolicy-basico/experiments/README.md) documenta o teste real.

## Prioridades para ampliar a homologação

1. **Kind com addons:** Ingress, Metrics Server e Cilium NetworkPolicy.
2. **Controladores em Kind dedicado:** Argo CD, Crossplane v2, Kyverno e Prometheus Operator/Grafana (mais Cilium no cluster específico).
3. **Avançados da Camada 03:** reconciler real, Cilium dataplane, CSI driver e Gateway Controller, cada qual com roteiro opcional.
4. **Conteúdo teórico:** ESO e Karpenter permanecem disponíveis nas aulas 04.04 e 04.05, sem tarefas de provisionamento, segredos ou recursos cloud.

[Preparação dos cinco ambientes de labs da Camada 04](ambientes/README.md) · [Execução e segurança](labs.md)
