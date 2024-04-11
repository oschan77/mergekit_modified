import yaml
from huggingface_hub import ModelCard
from jinja2 import Template

USERNAME = "oschan77"
MODEL_NAME = "OpenPipe-7B-slerp"


template_text = """
---
license: apache-2.0
tags:
- merge
- mergekit
{%- for model in models %}
- {{ model }}
{%- endfor %}
---

# {{ model_name }}

{{ model_name }} is a merge of the following models using [mergekit](https://github.com/cg123/mergekit):

{%- for model in models %}
* [{{ model }}](https://huggingface.co/{{ model }})
{%- endfor %}

## 🧩 Configuration

```
{{- yaml_config -}}
```
"""

# Create a Jinja template object
jinja_template = Template(template_text.strip())

# Get list of models from config
with open("config.yaml", "r") as f:
    yaml_config = f.read()

data = yaml.safe_load(yaml_config)
if "models" in data:
    models = [
        data["models"][i]["model"]
        for i in range(len(data["models"]))
        if "parameters" in data["models"][i]
    ]
elif "parameters" in data:
    models = [
        data["slices"][0]["sources"][i]["model"]
        for i in range(len(data["slices"][0]["sources"]))
    ]
elif "slices" in data:
    models = [
        data["slices"][i]["sources"][0]["model"] for i in range(len(data["slices"]))
    ]
else:
    raise Exception("No models or slices found in yaml config")

# Fill the template
content = jinja_template.render(
    model_name=MODEL_NAME,
    models=models,
    yaml_config=yaml_config,
    username=USERNAME,
)

# Save the model card
card = ModelCard(content)
card.save("merge/README.md")
