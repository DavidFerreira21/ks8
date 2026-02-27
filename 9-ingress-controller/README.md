# Ingress Controllers

O que é o Ingress?

O Ingress é um recurso do Kubernetes que gerencia o acesso externo aos serviços dentro de um cluster. Ele funciona como uma camada de roteamento HTTP/HTTPS, permitindo a definição de regras para direcionar o tráfego externo para diferentes serviços back-end. O Ingress é implementado através de um controlador de Ingress, que pode ser alimentado por várias soluções, como NGINX, Traefik ou Istio, para citar alguns.

Tecnicamente, o Ingress atua como uma abstração de regras de roteamento de alto nível que são interpretadas e aplicadas pelo controlador de Ingress. Ele permite recursos avançados como balanceamento de carga, SSL/TLS, redirecionamento, reescrita de URL, entre outros.

Principais Componentes e Funcionalidades:
Controlador de Ingress: É a implementação real que satisfaz um recurso Ingress. Ele pode ser implementado através de várias soluções de proxy reverso, como NGINX ou HAProxy.

Regras de Roteamento: Definidas em um objeto YAML, essas regras determinam como as requisições externas devem ser encaminhadas aos serviços internos.

Backend Padrão: Um serviço de fallback para onde as requisições são encaminhadas se nenhuma regra de roteamento for correspondida.

Balanceamento de Carga: Distribuição automática de tráfego entre múltiplos pods de um serviço.

Terminação SSL/TLS: O Ingress permite a configuração de certificados SSL/TLS para a terminação de criptografia no ponto de entrada do cluster.

Anexos de Recurso: Possibilidade de anexar recursos adicionais como ConfigMaps ou Secrets, que podem ser utilizados para configurar comportamentos adicionais como autenticação básica, listas de controle de acesso etc.

AWS (Amazon Web Services)
Na AWS, o ingress controller é exposto através de um Network Load Balancer (NLB). O comando para instalação é:
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/aws/deploy.yaml
Você também pode configurar a terminação TLS no Load Balancer da AWS, editando o arquivo deploy.yaml com as informações do seu Certificate Manager (ACM).


Bare Metal
Para instalações em Bare Metal ou VMs "cruas", você pode usar um NodePort para testes rápidos:
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/baremetal/deploy.yaml
Este comando mapeará o ingress controller para uma porta no intervalo de 30000-32767.

