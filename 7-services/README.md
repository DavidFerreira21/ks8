# Services

Services são recursos do Kubernetes que expõem um conjunto de Pods de forma estável. Eles resolvem dois problemas comuns:
- IPs de Pod são efêmeros e mudam quando o Pod é recriado.
- É necessário ter um ponto de acesso único e balanceado para vários Pods.

Em resumo, um Service cria um IP virtual (ClusterIP) e um DNS para acessar os Pods que combinam com um seletor de labels.

## Conceitos básicos

- Seletor: define quais Pods fazem parte do Service (match por labels).
- Port / TargetPort: porta exposta pelo Service e a porta no container.
- DNS interno: `meu-service.meu-namespace.svc.cluster.local`.
- Balanceamento: o kube-proxy distribui as conexões entre os Pods saudáveis.

## Tipos de Service

### ClusterIP (padrão)

Exposição interna ao cluster. Ideal para comunicação entre serviços dentro do Kubernetes.

Expor com:

```bash
kubectl expose deploy minha-app --name=app-clusterip --port=80 --target-port=8080 --type=ClusterIP
```

ou

```yaml
apiVersion: v1
kind: Service
metadata:
  name: app-clusterip
spec:
  type: ClusterIP
  selector:
    app: minha-app
  ports:
    - name: http
      port: 80
      targetPort: 8080
```

### NodePort

Expõe o Service em uma porta fixa em todos os nós. Útil para testes ou acesso externo simples.

Expor com:

```bash
kubectl expose deploy minha-app --name=app-nodeport --port=80 --target-port=8080 --type=NodePort
```

ou

```yaml
apiVersion: v1
kind: Service
metadata:
  name: app-nodeport
spec:
  type: NodePort
  selector:
    app: minha-app
  ports:
    - name: http
      port: 80
      targetPort: 8080
      nodePort: 30080
```

### LoadBalancer

Cria um balanceador de carga externo via provedor cloud (ou via MetalLB em clusters locais).

Expor com:

```bash
kubectl expose deploy minha-app --name=app-loadbalancer --port=80 --target-port=8080 --type=LoadBalancer
```

ou

```yaml
apiVersion: v1
kind: Service
metadata:
  name: app-loadbalancer
spec:
  type: LoadBalancer
  selector:
    app: minha-app
  ports:
    - name: http
      port: 80
      targetPort: 8080
```

### ExternalName

Cria um alias DNS para um serviço externo. Não cria endpoints.

Criar com:

```bash
kubectl create service externalname db-externa --external-name=db.exemplo.com
```

ou

```yaml
apiVersion: v1
kind: Service
metadata:
  name: db-externa
spec:
  type: ExternalName
  externalName: db.exemplo.com
```

## Endpoints

Endpoints são os IPs e portas dos Pods que o Service está apontando. Eles são gerados automaticamente com base no selector (exceto no ExternalName).

```bash
kubectl get endpoints app-clusterip
```

Para inspecionar os endpoints detalhados:

```bash
kubectl describe endpoints app-clusterip
```

## Headless Service (ClusterIP: None)

Quando você define `clusterIP: None`, o Service não cria IP virtual e expõe diretamente os IPs dos Pods via DNS. Isso é útil em StatefulSets.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: app-headless
spec:
  clusterIP: None
  selector:
    app: minha-app
  ports:
    - name: http
      port: 80
      targetPort: 8080
```

## Comandos úteis

```bash
# listar services
kubectl get svc

# ver detalhes
kubectl describe svc app-clusterip

# testar DNS do service dentro do cluster (exemplo com pod temporário)
kubectl run -it --rm dns-test --image=busybox --restart=Never -- nslookup app-clusterip
```
