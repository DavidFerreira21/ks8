up:
	kind create cluster --name dev --config kind-config.yaml

down:
	kind delete cluster --name dev

install-nginx:
	kubectl apply -k ingress-nginx

	