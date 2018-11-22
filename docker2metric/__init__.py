from os import popen, environ
from json import loads, dumps
import socket

__version__ = "1.0.0"

def get_docker_metrics():
    fields = dumps(
        {
            "container": "{{ .Container }}",
            "id": "{{.ID}}",
            "name": "{{.Name}}",
            "cpu.percent": "{{.CPUPerc}}",
            "mem.usage": "{{.MemUsage}}",
            "mem.percent": "{{.MemPerc}}",
            "net.io": "{{.NetIO}}",
            "block.io": "{{.BlockIO}}",
        }
    )
    command = "docker stats --no-stream --format '{}'".format(fields)
    stats = loads("[{}]".format(",".join(popen(command).readlines())))


    def toByte(value):
        value = value.lower()
        if "gib" in value or "gb" in value:
            exp = 1024 ** 3
        elif "mib" in value or "mb" in value:
            exp = 1024 ** 2
        elif "kib" in value or "kb" in value:
            exp = 1024
        else:
            exp = 1
        value = float("".join([s for s in value if s.isdigit() or s == "."]))
        return int(value * exp)

    metrics = []
    for stat in stats:
        mem = stat["mem.usage"].replace(" ", "").split("/")
        network = stat["net.io"].replace(" ", "").split("/")
        disk = stat["block.io"].replace(" ", "").split("/")
        metrics.append({
            "origin": socket.gethostname(),
            "type": "docker-stats-{}".format(stat["name"]),
            "metrics": [
                {
                    "metric": "memory.percent",
                    "value": float(stat["mem.percent"].replace("%", "")),
                    "unit": "%",
                },
                {
                    "metric": "cpu",
                    "value": float(stat["cpu.percent"].replace("%", "")),
                    "unit": "%",
                },
                {"metric": "memory.usage", "value": toByte(mem[0]), "unit": "o"},
                {"metric": "network", "value": toByte(network[0]), "unit": "o"},
                {"metric": "disk", "value": toByte(disk[0]), "unit": "o"},
            ],
        })
    return metrics
