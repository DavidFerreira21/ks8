# Secrets

o que é o secret

por padrão secrets nao e criptografado ficam em base64

voce  deve criptografar e controlar acesso tanto aos secrets quato aos Pod que estao montando esse secrets 

# tipos de secrets

Tipos de Secrets
Existem vários tipos de Secrets que você pode usar, dependendo de suas necessidades específicas. Abaixo estão alguns dos tipos mais comuns de Secrets:

Opaque Secrets - são os Secrets mais simples e mais comuns. Eles armazenam dados arbitrários, como chaves de API, senhas e tokens. Os Opaque Secrets são codificados em base64 quando são armazenados no Kubernetes, mas não são criptografados. Eles podem ser usados para armazenar dados confidenciais, mas não são seguros o suficiente para armazenar informações altamente sensíveis, como senhas de banco de dados.

kubernetes.io/service-account-token - são usados para armazenar tokens de acesso de conta de serviço. Esses tokens são usados para autenticar Pods com o Kubernetes API. Eles são montados automaticamente em Pods que usam contas de serviço.

kubernetes.io/dockercfg e kubernetes.io/dockerconfigjson - são usados para armazenar credenciais de registro do Docker. Eles são usados para autenticar Pods com um registro do Docker. Eles são montados em Pods que usam imagens de container privadas.

kubernetes.io/tls, kubernetes.io/ssh-auth e kubernetes.io/basic-auth - são usados para armazenar certificados TLS, chaves SSH e credenciais de autenticação básica, respectivamente. Eles são usados para autenticar Pods com outros serviços.

bootstrap.kubernetes.io/token - são usados para armazenar tokens de inicialização de cluster. Eles são usados para autenticar nós com o plano de controle do Kubernetes.


echo -n 'ks8-labs' | base64


echo -n 'a3M4LWxhYnM=' | base64 -d



apiVersion: v1
kind: Secret
metadata:
  name: ks8-secret
type: Opaque
data: # Inicio dos dados
    username: dGVzdHVzZXI=
    password: a3M4LWxhYnM=


kubectl create -f ks8-secret.yaml

kubectl get secret giropops-secret -o yaml

apiVersion: v1
data:
  username: dGVzdHVzZXI=
  password: a3M4LWxhYnM=
kind: Secret
metadata:
  creationTimestamp: "2023-05-21T10:38:39Z"
  name: giropops-secret
  namespace: default
  resourceVersion: "466"
  uid: ac816e95-8896-4ad4-9e64-4ee8258a8cda
type: Opaque

apiVersion: v1
kind: Pod
metadata:
  name: giropops-pod
spec:
  containers:
  - name: ks8-container
    image: nginx
    env: # Inicio da definição das variáveis de ambiente
    - name: USERNAME # Nome da variável de ambiente que será usada no Pod
      valueFrom: # Inicio da definição de onde o valor da variável de ambiente será buscado
        secretKeyRef: # Inicio da definição de que o valor da variável de ambiente será buscado em um Secret, através de uma chave
          name: giroks8pops-secret # Nome do Secret que contém o valor da variável de ambiente que será usada no Pod
          key: username # Nome da chave do campo do Secret que contém o valor da variável de ambiente que será usada no Pod
    - name: PASSWORD # Nome da variável de ambiente que será usada no Pod
      valueFrom: # Inicio da definição de onde o valor da variável de ambiente será buscado
        secretKeyRef: # Inicio da definição de que o valor da variável de ambiente será buscado em um Secret, através de uma chave
          name: ks8-secret # Nome do Secret que contém o valor da variável de ambiente que será usada no Pod
          key: password # Nome da chave do campo do Secret que contém o valor da variável de ambiente que será usada no Pod


kubectl exec ks8-pod -- env

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=kubectl exec ks8-pod -- env
NGINX_VERSION=1.23.4
NJS_VERSION=0.7.11
PKG_RELEASE=1~bullseye
PASSWORD=giropops
USERNAME=CENSURADO
KUBERNETES_PORT_443_TCP_PROTO=tcp
KUBERNETES_PORT_443_TCP_PORT=443
KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1
KUBERNETES_SERVICE_HOST=10.96.0.1
KUBERNETES_SERVICE_PORT=443
KUBERNETES_SERVICE_PORT_HTTPS=443
KUBERNETES_PORT=tcp://10.96.0.1:443
KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443
HOME=/root