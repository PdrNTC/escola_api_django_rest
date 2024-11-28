from rest_framework.throttling import AnonRateThrottle

## Criando Classe para personalizar os limites de requisição da matricula ##
class MatriculaAnonRateThrottle(AnonRateThrottle):
    rate = '5/day'