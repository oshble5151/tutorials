import iris
# 각 time의 위경도 2차원 값에서 전체 시간축에 대한 평균값 2차원 값을 빼준 값을 계산 가능 
f= iris.load_cube('file_name')
f_mean = f.collapsed('time',iris.analysis.MEAN)

anomaly = f - f_mean 
# 넘파이의 brodcast 규칙을 따름
