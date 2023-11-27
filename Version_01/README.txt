python 폴더에 있는 내용은 Docker image

$PYCODE를 불러와 test.py로 만들고 이를 수행해 return값을 출력한다




kube 폴더에 있는 내용은 Yaml 파일 생성기

python3 myjob.py 실행시
내부의 변수를 사용해 myjob.j2 파일을 템플릿삼아
myjob.yaml 파일 생성

minikube kubectl -- apply -t myjob.yaml 
수행시 job 생성
minikube kubectl -- get pods
minikube kubectl -- logs (pod 이름)
으로 로그 확인 가능