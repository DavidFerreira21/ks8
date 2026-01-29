up:
	kind create cluster --name dev --config kind-config.yaml

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

	
	
	


	
