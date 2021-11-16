import os.path
import yaml


def ler_yaml(arquivo):
    with open(arquivo, "r") as f:
        return yaml.safe_load(f)


def configuracao():
    return ler_yaml(os.path.join(os.path.split(os.path.dirname(__file__))[0], "configuracao.yaml"))

