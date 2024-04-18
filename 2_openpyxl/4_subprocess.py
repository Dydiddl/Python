import os
import subprocess

# 1. 주민등록번호로 나이 계산
subprocess.run("python", "1_jumin_with.py")

# 2. 민증 없는 사람 밑으로 보내기
subprocess.run("python", "2_organizelInformation.py")

# 3. numbering 
subprocess.run("python", "3_numbering.py")
