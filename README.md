# assignment

Install minikube:
https://minikube.sigs.k8s.io/docs/start/

curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube


Start your Cluster:
minikube start


# Setup FastAPI

sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate

python3 -m pip install "FastAPI[all]"

deactivate

Run Locally:
uvicorn app:app --reload

Assignment: https://mail.google.com/mail/u/1/#sent/FMfcgzGtxSqKxSlbMnqlMXzDdMCjtvjs?projector=1&messagePartId=0.1