# pip install PyYAML
import yaml

config = None
with open("config.yml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

if config is None:
    print("Error: no configs found :(")
    exit(-1111)

with open("template.html", "r", encoding="utf-8") as tf:
    template = tf.read()
    for c in config:
        x = config[c]
        print(f"Replacing: {{{c}}} -> {str(x)}")
        template = template.replace(f"{{{c}}}", str(x))

with open("index.html", "w", encoding="utf-8") as idf:
    idf.write(template)