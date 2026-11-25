# Quantum Control Notes

Study notes on qubit measurement and control, written by a C++/Qt instrument-control software engineer with a background in atomic force microscopy (AFM).
Notes are mostly in Korean; code, figures and headings are in English where possible.

정밀 계측 장비(AFM) 제어 소프트웨어 개발자가 큐비트 측정·제어를 공부하며 남기는 공개 학습 노트입니다.

## 목표

- 큐비트 측정·제어의 기본 원리를 직접 계산하고 시뮬레이션해서 설명할 수 있게 된다.
- QCoDeS로 가상 장비 측정을 실행하고 데이터 구조를 이해한다.
- 양자 제어 소프트웨어 오픈소스에 기여한다.

## 진행 현황

| 단계 | 내용 | 기간 | 상태 |
|---|---|---|---|
| 1 | [양자 기초](01-foundations/) | 2026년 12월 | 진행 중 |
| 2 | [큐비트 측정과 제어](02-qubit-control/) | 2027년 1월 | 시작 전 |
| 3 | [QCoDeS 실습](03-qcodes/) | 2027년 1월 말~2월 초 | 시작 전 |
| 4 | 첫 오픈소스 기여 | 2027년 2월 | 시작 전 |

상태는 `시작 전`, `진행 중`, `완료`로 표시합니다. 주간 기록은 [LOG.md](LOG.md)에 있습니다.

## 오픈소스 기여

아직 없습니다. 머지된 PR이 생기면 링크를 추가합니다.

## 폴더 구조

```
01-foundations/    선형대수, 게이트, 밀도행렬, T1/T2
02-qubit-control/  공진기·큐비트 분광, Rabi, Ramsey, I/Q 판독, AFM 대응표
03-qcodes/         QCoDeS 가상 장비 측정, SQLite 데이터 구조
figures/           노트에 쓰는 결과 그래프(PNG)
templates/         노트 양식
```

## 실행 환경

Python 3.12 이상이 필요합니다. 최신 QCoDeS, NumPy, SciPy가 3.12 이상만 지원합니다.

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python check_env.py
```

## 원칙

- 공개 자료와 직접 만든 가상 데이터만 사용합니다. 회사 코드, 장비 사양, 고객 데이터는 넣지 않습니다.
- 요약보다 직접 계산하고 실행한 결과를 남깁니다.
- 틀린 이해를 고친 경우 지우지 않고 고친 내용을 함께 남깁니다.

## License

- Code: [MIT](LICENSE)
- Notes and figures: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
