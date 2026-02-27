.PHONY: all up down test-deploy config-bash install-nginx install-argocd configure-argocd-ingress apply-argocd-test-app

all:
	$(MAKE) up
	$(MAKE) install-nginx
	$(MAKE) install-argocd
	$(MAKE) configure-argocd-ingress
	$(MAKE) apply-argocd-test-app

up:
	@if kind get clusters | grep -qx "dev"; then \
		echo "Cluster 'dev' ja existe. Pulando criacao."; \
	else \
		kind create cluster --name dev --config kind-config.yaml; \
	fi

down:
	kind delete cluster --name dev

test-deploy:
	kubectl apply -f test-deploy.yaml
	kubectl get pods -l app=http-echo
	kubectl get endpoints http-echo-svc
	

config-bash:
	sudo apt-get install bash-completion 
	kubectl completion bash | sudo tee /etc/bash_completion.d/kubectl > /dev/null
	echo 'alias k=kubectl' >>~/.bashrc
	echo 'complete -o default -F __start_kubectl k' >>~/.bashrc

install-nginx:
	kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
	kubectl -n ingress-nginx patch deploy ingress-nginx-controller --type='json' -p='[{"op":"add","path":"/spec/template/spec/nodeSelector","value":{"ingress-ready":"true","kubernetes.io/os":"linux"}}]'
	kubectl -n ingress-nginx patch deploy ingress-nginx-controller --type='json' -p='[{"op":"add","path":"/spec/template/spec/containers/0/ports/0/hostPort","value":80},{"op":"add","path":"/spec/template/spec/containers/0/ports/1/hostPort","value":443}]'
	kubectl wait --namespace ingress-nginx --for=condition=Ready pod --selector=app.kubernetes.io/component=controller --timeout=180s

install-argocd:
	kubectl create namespace argocd --dry-run=client -o yaml | kubectl apply -f -
	kubectl apply --server-side -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
	kubectl -n argocd patch configmap argocd-cmd-params-cm --type merge -p '{"data":{"server.insecure":"true"}}'
	kubectl -n argocd rollout restart deployment argocd-server
	@echo "Aguardando pods do Argo CD serem criados..."
	@attempts=0; \
	until [ $$attempts -ge 150 ] || kubectl -n argocd get pods -o name | grep -q .; do \
		attempts=$$((attempts+1)); \
		sleep 2; \
	done; \
	if [ $$attempts -ge 150 ]; then \
		echo "Timeout aguardando pods do Argo CD no namespace argocd."; \
		kubectl -n argocd get all; \
		exit 1; \
	fi
	kubectl -n argocd wait --for=condition=Ready pod --all --timeout=600s
	kubectl -n argocd rollout status deployment/argocd-server --timeout=300s
	@echo "Aguardando secret inicial do Argo CD..."
	@until kubectl -n argocd get secret argocd-initial-admin-secret >/dev/null 2>&1; do sleep 2; done
	@echo "Argo CD admin password:"
	@kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo

configure-argocd-ingress:
	kubectl apply -f argo/argocd-ingress.yaml

apply-argocd-test-app:
	kubectl apply -f argo/test-app-application.yaml

	
	
	


	
