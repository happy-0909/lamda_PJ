import os

# 특정 환경변수의 값을 가져오기
my_variable_value = os.environ.get('PYCODE')

# 값 출력
print(f"{my_variable_value}")

with open("/app/test.py" , "w+") as fw :
    fw.write(my_variable_value)
