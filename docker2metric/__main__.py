from docker2metric.docker2metric import get_docker_metrics
from json import dumps
print(dumps(get_docker_metrics(), indent=4))
