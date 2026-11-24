# 3단계 · QCoDeS 실습

완료 기준: 가상 장비로 2D 측정을 실행하고 SQLite 데이터 구조를 설명할 수 있음

## 노트 목록

| 노트 | 상태 |
|---|---|
| `DummyInstrument`로 1D 측정 | 시작 전 |
| Measurement와 DataSet으로 2D 스윕 | 시작 전 |
| 가상 Rabi 데이터 저장과 시각화 | 시작 전 |
| SQLite DB 테이블 구조 | 시작 전 |
| `Parameter`, `Instrument`, DataSet 소스 읽기 | 시작 전 |
| pyvisa-sim으로 가상 SCPI 장비 드라이버 | 시작 전 |

측정 결과 DB 파일(`*.db`)은 용량이 커질 수 있어 저장소에 올리지 않습니다. 필요한 결과는 그래프나 작은 CSV로 남깁니다.

## 참고 자료

- [QCoDeS documentation](https://microsoft.github.io/Qcodes/)
- [Measurement and DataSet example](https://microsoft.github.io/Qcodes/examples/DataSet/Performing-measurements-using-qcodes-parameters-and-dataset.html)
