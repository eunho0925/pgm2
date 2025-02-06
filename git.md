
# Git 기본 명령어

## git 설정 관련

```bash
    git config --gloabl user.name "user name" # 사용자 이름
    git config --gloabl user.email "user@email.com" #이메일
    git config --list # 현재 설정된 git 정보 조회
```

## 레포지토리 초기화 및 상태 

```bash
    git init # 새로운 git 레포지토리 생성
    git clone <url> #원격 레포지토리 복제
    git status # 상태 확인
    git log    # 커밋 로그 확인
```
## 스테이징 및 커밋

```bash
    git add <파일명> # 특정 파일 스테이징
    git add .       # 현재 디렉토리의 모든  변경 사항 스테이징
    git commit -m "메세지" # 파일 커밋 및 메세지작성
    git diff # 변경 사항 확인 
```

## 원격 저장소 관련
```bash
    git remote add origin <URL> # 원격 레포지토리 추가 
    git remote -v # 설정된 원격 저장소 확인
    git push origin <브랜치명> # 변경 사항을 원격 저장소에 ~
    git pull origin <브랜치명> # 원격 저장소로 부터 변경사항 가져오기 
```

