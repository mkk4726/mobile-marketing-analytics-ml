# Mobile Marketing Analytics ML

모바일 마케팅 데이터를 분석하고 머신러닝 모델을 개발하는 프로젝트입니다.

---

## 📊 데이터셋

### 기본 데이터셋

#### 1. Cookie Cats Retention Dataset
- **설명**: 모바일 게임 A/B 테스팅 데이터
- **링크**: [Kaggle](https://www.kaggle.com/datasets/mursideyarkin/mobile-games-ab-testing-cookie-cats)

#### 2. Mobile User Behavior Dataset
- **설명**: 앱 사용 및 세그먼테이션 데이터
- **링크**: [Kaggle](https://www.kaggle.com/datasets/suraj520/cellular-network-analysis-dataset)

#### 3. Mobile Game Telemetry Dataset
- **설명**: 게임 이벤트 로그 데이터
- **링크**: [Kaggle](https://www.kaggle.com/datasets/debs2x/gamelytics-mobile-analytics-challenge)

#### 4. Steam Games Playtime Dataset
- **설명**: 유저 가치 기반 예측 가능한 게임 플레이타임 데이터
- **링크**: [Kaggle](https://www.kaggle.com/datasets/trolukovich/steam-games-complete-dataset)

#### 5. E-commerce Behavior Data
- **설명**: LTV/ROAS Revenue 기반 대체 옵션
- **링크**: [Kaggle](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store)

---

### ✅ 추천 데이터셋 목록

**CLV / LTV / ROAS** 같은 지표 예측에 적합한 데이터셋을 정리했습니다.

| 이름 | 설명 | 활용 가능성 |
| --- | --- | --- |
| [FinTech Customer Life Time Value (LTV) Dataset][1] | 약 7,000개 샘플, 20여개 피처로 고객 인구통계·거래이력·앱 사용패턴 등이 담겨 있음 | LTV 회귀모델 연습에 적합 |
| [Customer Life Time Value][2] | 사용자 및 정책(보험?) 데이터를 기반으로 CLTV 예측용 | 비금융/보험 영역에서 모델링 경험 확보 가능 |
| [CAC‑LTV Model][3] | 가상의 SaaS 사업을 모델링한 합성 데이터셋으로 "Customer Acquisition Cost(CAC)", LTV, 유지율까지 포함됨 | 광고/마케팅 비용과 LTV 연관성을 탐구할 때 유용 |
| [Advertising Spend vs Sales][4] | 여러 채널(TV, 라디오, 신문 등) 광고지출과 매출의 관계가 담긴 데이터셋 | ROAS(광고비 대비 수익)나 마케팅 채널 효율 분석에 적합 |
| [Sales and Advertising Clean Dataset][5] | 광고지출 및 마케팅 활동, 판매성과 관련된 클린 데이터셋 | 마케팅 캠페인 성과 예측 또는 채널별 스펜드 최적화에 활용 가능 |
| [Sample Media Spend Data][6] | 여러 미디어 채널의 지출 및 판매 데이터가 다수 주차(weeks)로 제공됨 | 시계열 + 마케팅 spend 모델링 연습 가능 |

---

## 🎯 연습 과제 제안

### LTV & ROAS 예측 과제

1. **고객 단위 LTV 예측**
   - 기존 거래이력 + 앱/웹 사용패턴 → **향후 N개월/년 매출예측**

2. **광고비 대비 수익(ROAS) 분석**
   - 채널별 광고지출 → 수익/매출 산출 → **효율이 낮은 채널 식별 및 최적화 시뮬레이션**

3. **CAC vs LTV 비교 분석**
   - 신규 고객 획득 비용 대비 기대 고객가치 산정 → **마케팅 투자 의사결정 지원**

4. **시계열/패널데이터 모델링**
   - 매체지출 주차별/월별 데이터로 → **지출 결정이 매출에 미치는 지연효과(lag) 탐구**

5. **세그먼트화 + 예측**
   - 고가치 고객군을 식별하고, 이들의 행동패턴 기반으로 **향후 CLV 상위 고객 예측**

---

## 📚 참고자료

[1]: https://www.kaggle.com/datasets/harunrai/fintech-customer-life-time-value-ltv-dataset?utm_source=chatgpt.com "FinTech Customer Life Time Value (LTV) Dataset"
[2]: https://www.kaggle.com/datasets/shibumohapatra/customer-life-time-value?utm_source=chatgpt.com "Customer Life Time Value"
[3]: https://www.kaggle.com/datasets/ameernassar/cac-ltv-model?utm_source=chatgpt.com "CAC-LTV Model Analysis for SaaS Business Insights"
[4]: https://www.kaggle.com/datasets/brsahan/advertising-spend-vs-sales?utm_source=chatgpt.com "Advertising Spend vs Sales"
[5]: https://www.kaggle.com/datasets/mahmoudshaheen1134/sales-and-advertising-clean-dataset?utm_source=chatgpt.com "Sales and advertising clean dataset"
[6]: https://www.kaggle.com/datasets/yugagrawal95/sample-media-spends-data?utm_source=chatgpt.com "Sample Media Spends Data"
이 