# py-minerstatsd-docker

Set the container hostname to be the same as the Docker host name?

Need to downcase import Queue to import queue in module collectd.py

cfg = {
    'interval': '20',
    'url': 'http://localhost:3333',
    'host_name': 'server.monitored.com',
    'collectd_name': 'server.collectd.net',
    'collectd_port': '25826'
}

collectd configuration goes like this:
    ModulePath "/home/imil/bin"
    Import "claymorestats"
        interval "20"
        url "http://127.0.0.1:3333/"

/sw/code/dockers/cultclassik/py-minerstatsd-docker/app/app.py -interval 20 -url http://localhost:3333 -host_name miner03 -collectd_name dagon.diehlabs.lan -collectd_port 25826

python3 -m venv ~/minerstatsd

source ~/envs/minerstatsd/bin/activate

pip install --no-cache-dir -r /sw/code/dockers/cultclassik/py-minerstatsd-docker/app/requirements.txt