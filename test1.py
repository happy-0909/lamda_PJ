import re
import json

def extract_imports_from_json_file(file_path):
    # JSON 파일에서 사용자 입력 읽어오기
    # 후에 웹에서 데이터를 가져올수 있도록 수정해야함.
    with open(file_path, 'r') as json_file:
        json_input = json_file.read()

    # JSON을 파이썬 딕셔너리로 변환
    input_data = json.loads(json_input)

    # "code" 키에 해당하는 값 가져오기
    code = input_data.get("code", "")

    # 정규 표현식 패턴
    pattern = re.compile(r'\bimport\s+(\w+)(\s+as\s+\w+)?(\s*,\s*\w+(\s+as\s+\w+)?)?\b|\bfrom\s+(\w+)\s+import\s+(\w+)(\s+as\s+\w+)?(\s*,\s*\w+(\s+as\s+\w+)?)?\b')

    # 정규 표현식 패턴과 매칭되는 모든 결과
    matches = pattern.findall(code)

    # 모듈 이름을 저장할 집합
    imported_modules = set()

    # 각 매칭 결과를 순회하면서 모듈 이름 추출
    for match in matches:
        for module in match:
            if module:
                imported_modules.add(module)

    return imported_modules

# 테스트를 위해 예제 JSON 파일의 경로
json_file_path = 'test1.json'

# JSON 파일에서 모듈 추출  
# 후에 웹에서 데이터를 가져올수 있도록 수정해야함.
result = extract_imports_from_json_file(json_file_path)
print("Imported modules:", result)

#tmp 변수를 선언해 파싱한 json 값을 하나씩 꺼내온다 \n 으로 줄바꿈
tmp = ""
for im in result :
    tmp += f'{im}\n'
    
#requirements.txt 파일을 생성해서 꺼내온 값을 파일에 넣어준다
with open('requirements.txt', 'w+') as fw :
    fw.write(tmp)