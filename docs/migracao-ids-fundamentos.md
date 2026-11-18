# Migração de IDs — Fundamentos (Camada 01)

A sequência foi reorganizada para seguir **conceito → execução → controladores → rede → configuração → operação**. Os diretórios por assunto e os caminhos dos PNGs **não foram renomeados**, de forma que links antigos por slug continuem funcionando.

| Tema | ID anterior | Novo ID |
| --- | --- | --- |
| Fundamentos Kubernetes | 01.01 | 01.01 |
| Pods | 01.03 | 01.02 |
| Deployments | 01.06 | 01.03 |
| ReplicaSet, DaemonSet e StatefulSet | 01.07 | 01.04 |
| Services | 01.09 | 01.05 |
| Namespaces | 01.02 | 01.06 |
| ConfigMaps | 01.10 | 01.07 |
| Secrets | 01.11 | 01.08 |
| Requests e Limits | 01.04 | 01.09 |
| Probes | 01.05 | 01.10 |
| Volumes | 01.12 | 01.11 |
| Estratégias avançadas de Deployment | 01.08 | 01.12 |
| Ingress | 01.13 | 01.13 |
| HPA | 01.14 | 01.14 |

## Contratos de laboratório

- **Lab 01.01** continua sendo o primeiro contato com a API.
- O antigo **Lab 01.06** (Pod → Deployment → Service) agora é **Lab 01.05**. O caminho da pasta `labs/primeira-aplicacao` não mudou.
- `make lab-up` sem `LAB` agora inicia o **Lab 01.01**. Para repetir a aplicação integrada, use `make lab-up LAB=01.05`.
- Experimento de rollout: `make lab-experiment LAB=01.05 EXPERIMENT=controlled-rollout`.
- Os IDs da Camada 02 em diante não mudaram.

## Verificação após atualizar sua branch

```bash
git pull --ff-only
make validate
python3 -m unittest discover -s tests -p 'test_*.py' -v
make labs
```

Se você tiver comandos salvos no terminal ou suas próprias anotações com IDs antigos, revise-os pela tabela **considerando o assunto**, não apenas o número. Um ID pode passar a identificar outra aula.
