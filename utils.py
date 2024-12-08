def config_par(config_path):
    with open(config_path) as config_file:
        config = dict()
        lines = config_file.readlines()
        for line in lines:
            k, v = line.split(' = ')
            config[k] = v.split('\n')[0].replace(' ', '')
        return config
    