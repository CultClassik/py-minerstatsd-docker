# py-minerstatsd-docker


cfg = {
    'interval': '20',
    'url': 'http://localhost:3333'
}

collectd configuration goes like this:
    ModulePath "/home/imil/bin"
    Import "claymorestats"
        interval "20"
        url "http://127.0.0.1:3333/"