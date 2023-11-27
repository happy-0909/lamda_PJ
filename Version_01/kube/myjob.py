import yaml
from jinja2 import Template

# 템플릿 로드
with open('myjob.j2', 'r') as file:
    template_content = file.read()

template = Template(template_content)

# 변수 정의
variables = {'pycode': "def main() : \n\tprint('Hello! world')\n\tprint('Goodbye! world')\n\treturn 'byebye'"}

# 변수를 적용하여 YAML 생성
rendered_yaml = template.render(variables)

# 생성된 YAML 출력 또는 파일에 저장
print(rendered_yaml)


with open("./myjob.yaml", "w+") as fw :
    fw.write(rendered_yaml)
