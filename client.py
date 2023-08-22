from socket import *
import os
import sys

serverName = '192.168.20.22'
serverPort = 5021
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# 현재 디렉토리의 경로를 가져옵니다.
current_dir = os.getcwd()

# 현재 디렉토리 내의 client 폴더에 Received_data.txt 파일을 이진 쓰기 모드로 생성(또는 열기)합니다.
f = open(current_dir + "/client/Received_data.txt" , "wb")

try:
    # 서버로부터 데이터를 수신받아 data 변수에 저장합니다.
    data = clientSocket.recv(1024)
    
    # 수신받은 데이터를 위에서 생성한 파일에 씁니다.
    
    f.write(data)
    
    # 수신받은 데이터를 출력합니다.
    print(data)
    
# 예외 상황을 처리합니다.
except Exception:
    print(Exception)

# 소켓 연결을 종료합니다.
clientSocket.close()


