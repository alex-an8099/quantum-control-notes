# 선형대수 복습: 복소벡터, 유니터리, 에르미트 행렬, 텐서곱

> 작성일: 2026-11-25 · 단계: 1

## 질문

큐비트 상태와 게이트를 다루려면 어떤 선형대수가 필요한가?
특히 "유니터리"와 "에르미트"는 각각 무엇을 보장하는가?

## 핵심 정리

> 아래는 학습용 요약입니다. 손 계산을 마친 뒤 내 말로 다시 고쳐 씁니다.

### 1. 상태 = 길이 1인 복소벡터

- 큐비트 상태: $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle = \begin{pmatrix}\alpha\\\beta\end{pmatrix}$, $\alpha, \beta \in \mathbb{C}$
- 브라 $\langle\psi|$ 는 켓의 **켤레 전치**: $\langle\psi| = (\alpha^*, \beta^*)$
- 내적 $\langle\phi|\psi\rangle = \sum_i \phi_i^* \psi_i$. 켤레를 빼먹으면 $(1, i)$ 의 "길이 제곱"이 0이 되는 이상한 결과가 나온다.
- 정규화: $\langle\psi|\psi\rangle = |\alpha|^2 + |\beta|^2 = 1$
- 측정 확률(보른 규칙): $P(0) = |\langle 0|\psi\rangle|^2 = |\alpha|^2$
- 전체 위상 $e^{i\theta}|\psi\rangle$ 는 측정으로 구분할 수 없다. 상대 위상(α와 β 사이 위상차)은 구분할 수 있다.

### 2. 유니터리: 게이트

- $U^\dagger U = I$ ($U^\dagger$ = 켤레 전치)
- 의미: 내적(그래서 길이, 확률의 합)을 보존한다. 닫힌 계의 시간 진화와 모든 게이트는 유니터리다.
- 역연산이 $U^\dagger$ 로 항상 존재한다 → 게이트는 되돌릴 수 있다. 측정은 되돌릴 수 없다(유니터리가 아님).

### 3. 에르미트: 관측량

- $A = A^\dagger$
- 고윳값이 모두 실수다 → 측정값으로 쓸 수 있다.
- 서로 다른 고윳값의 고유벡터는 직교한다 → 측정 결과들이 서로 확실히 구분된다.
- 예: $Z$ 의 고윳값 +1, −1, 고유벡터 $|0\rangle, |1\rangle$. "Z축으로 측정한다"는 말의 뜻.
- X, Y, Z, H는 유니터리이면서 에르미트다(그래서 자기 자신이 역연산: $H H = I$). S는 유니터리지만 에르미트가 아니다.

### 4. 텐서곱: 여러 큐비트

- $|a\rangle \otimes |b\rangle$: 2차원 × 2차원 → 4차원. 순서는 $|00\rangle, |01\rangle, |10\rangle, |11\rangle$.
- $(A \otimes B)(|a\rangle \otimes |b\rangle) = A|a\rangle \otimes B|b\rangle$ → 한 큐비트에만 작용하는 게이트는 $X \otimes I$ 처럼 쓴다.
- 텐서곱으로 쪼갤 수 없는 상태 = **얽힘**. 예: $\frac{1}{\sqrt2}(|00\rangle + |11\rangle)$
- 판별 요령: 4성분 벡터를 2×2 행렬로 접었을 때 rank 1이면 곱 상태, rank 2면 얽힘.

## 손 계산 문제

종이에 먼저 풀고, 답을 아래 빈칸에 적은 뒤 코드로 확인합니다.

1. $|\psi\rangle = (1, i)$
   - a. $\langle\psi|\psi\rangle$ =
   - b. 정규화한 $|\psi\rangle$ =
   - c. $P(0)$, $P(1)$ =
2. 행렬 성질
   - a. X, Y, Z, H, S = diag(1, i) 각각 유니터리인가? 에르미트인가?
   - b. $H|0\rangle$ =
   - c. $HH$ =
3. $X$ 의 고윳값과 고유벡터 =
4. 텐서곱
   - a. $|0\rangle \otimes |1\rangle$ =
   - b. $X \otimes I$ (4×4) =
   - c. $\mathrm{CNOT}\,(H|0\rangle \otimes |0\rangle)$ = , 곱 상태인가 얽힘 상태인가?

## 코드와 실행

[linear_algebra_check.py](linear_algebra_check.py)

```
python 01-foundations/linear_algebra_check.py
```

핵심: 브라는 켤레 전치이므로 내적은 `np.vdot`(첫 인자를 켤레)으로, 텐서곱은 `np.kron`으로 계산한다.

```python
np.vdot(psi, psi)                 # <psi|psi>, 켤레 포함
np.allclose(U.conj().T @ U, I)    # 유니터리 판별
np.kron(ket0, ket1)               # |0> (x) |1>
```

## 결과

손 계산과 코드 출력이 다른 문항과 이유를 적습니다.

| 문항 | 손 계산 | 코드 | 일치 / 틀린 이유 |
|---|---|---|---|
|  |  |  |  |

참고: `np.linalg.eigh`가 돌려준 고유벡터는 부호(전체 위상)가 손 계산과 다를 수 있다. 위의 1번 정리대로 전체 위상은 물리적으로 같은 상태다.

## AFM과 비교

| AFM | 큐비트 | 닮은 점 / 다른 점 |
|---|---|---|
| 록인 증폭기의 X, Y(진폭·위상) 출력을 복소수 하나로 다룸 | 상태 성분 α, β가 복소수 | 둘 다 진폭과 위상을 복소수로 표현. 큐비트는 전체 위상이 관측되지 않음 |
| 스캐너 좌표 변환(회전 행렬, 직교 행렬) | 게이트(유니터리 행렬) | 둘 다 길이를 보존하는 변환. 유니터리는 복소수 버전의 회전 |
|  |  |  |

## 아직 모르는 점

- 

## 참고 자료

- [IBM Quantum Learning — Basics of quantum information](https://quantum.cloud.ibm.com/learning)
- Nielsen & Chuang, *Quantum Computation and Quantum Information*, 2.1절
