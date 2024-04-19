#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
import requests
from fastapi import FastAPI
from ray import serve


# 1: Defina um aplicativo FastAPI e envolva-o em um Deployment com um route handler:
app = FastAPI()


@serve.deployment
@serve.ingress(app)
class FastAPIDeployment:
    # FastAPI analisará automaticamente a solicitação HTTP para nós:
    @app.get("/hello")
    def say_hello(self, name: str) -> str:
        return f"Olá, {name}!"


# 2: Deploy the deployment.
serve.run(FastAPIDeployment.bind(), route_prefix="/")

# 3: Consulte o Deployment e imprima o resultado:
print(requests.get("http://localhost:8000/hello", params={"name": "Theodore"}).json())
# "Hello Theodore!"