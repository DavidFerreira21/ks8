up:
	kind create cluster --name dev --config kind-config.yaml

down:
	kind delete cluster --name dev

test:
	kubectl apply -f test-deploy.yaml
	

Config-bash:
	sudo apt-get install bash-completion 
	kubectl completion bash | sudo tee /etc/bash_completion.d/kubectl > /dev/null
	echo 'alias k=kubectl' >>~/.bashrc
	echo 'complete -o default -F __start_kubectl k' >>~/.bashrc

install-nginx:
	kubectl apply -f ingress-nginx/ingress-nginx.yaml

	
