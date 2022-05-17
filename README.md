# Pelvics_detection

프로젝트 구조는 https://data-newbie.tistory.com/614 를 참고하였습니다. 

```
project   
  |----- data   
  |        |----- external   <- Third party data 
  |        |----- interim     <- Transformed intermediate data, not ready for modeling 
  |        |----- processed   <- Prepared data, ready for modeling
  |        |----- raw         <- 불변의 original data 
  |    
  |----- models              <- Serialized model 
  |----- notebooks           <- 재현성을 위해 ipynb 파일은 해당 디렉토리에서 관리(step-user-description.ipynb 형태로 저장할 것)
  |----- test                <- Folder containing scrips to test the code
  |----- src
           |----- data       <- Folder containing scripts to download/generate data 
           |----- features   <- Folder containing scripts to transform data for modeling
           |----- model      <- Folder containing scripts to train and predict 
```

## src
`data` : 이 디렉터리에는 데이터가 생성되는 모든 위치에서 데이터를 수집하고 추가 기능 엔지니어링이 발생할 수 있는 상태가 되도록 데이터를 변환하는 script를 저장함. 

`feature` : 이 디렉터리에는 데이터를 조작하고 기계학습 모델에서 사용할 수 있는 형식으로 저장하는 script를 저장함. 

`models` : 모델을 빌드하고 훈련하는데 사용되는 script를 포함함. 

> 본 프로젝트는 KDD 방식으로 이루어지며 notebook 저장할 때 역시, 이 스텝을 기준으로 파일 이름을 만들어줌 

STEP 1. 데이터 선택  
STEP 2. 데이터 준비   
STEP 3. 데이터 변환  
STEP 4. 데이터 마이닝  
STEP 5. 데이터 마이닝 결과 평가   

