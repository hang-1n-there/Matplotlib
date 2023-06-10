## plt.plot()
```python
plt.plot([x값의 좌표], [y값의 좌표])
```
- 그래프의 좌표를 표시해주는 함수
---
## plt.xlabel & plt.ylabel
```python
plt.xlabel('x축의 이름')
plt.xlabel('y축의 이름')
```
- x축과 y축의 이름을 표시해주는 함수
---
## plt.legend
```python
plt.legend(loc='범례 위치', ncol = 그래프의 수, frameon = True, shadow = True)
```
- 그래프의 범례와 개수를 표시하는 함수
- plt.plot(label='그래프의 이름')을 추가해줘야 함
- fontsize : 폰트 크기 지정
- frameon : 범례 테두리 표시
- shadow : 범례 그림자 표시
---
## plt.axis
```python
 #축 범위 지정
plt.axis([xmin,xmax,ymin,ymax])
plt.xlim([xmin,xmax]) # x축범위
plt.ylim([ymin,ymax]) # y축범위

plt.axis('square') # 옵션 지정
```
- x와 y의 최솟값과 최댓값을 그래프에 적용하는 함수
- 아래와 같은 옵션 지정 가능

| 값 | 설명 |
|------:|--------|
|on     |축과 라벨을 켠다        |
|  off     |   축과 라벨을 끈다     |
|    equal   |  축의 범위와 스케일을 동일하게 설정      |
|   scaled    |    플롯 박스의 차원과 동일하게 스케일을 설정    |
| tight      |     모든 데이터를 볼 수 있도록 범위 설정   |
|    auto,normal   |     축의 스케일을 자동 설정   |
|   image   |  데이터 범위에 대해 축의 범위를 적용한 scaled      |
| square | xmax - xmin = ymax - ymin 이 되도록 설정|
---


