# Mobile Marketing Analytics ML

모바일 마케팅 분석 및 머신러닝 프로젝트

## 프로젝트 구조

```
mobile-marketing-analytics-ml/
├── datasets/              # 데이터셋 저장 디렉토리
├── notebooks/             # 분석 노트북
│   ├── 01_cohort_analysis.ipynb
│   ├── 02_ltv_modeling.ipynb
│   ├── 03_roas_prediction.ipynb
│   ├── 04_high_value_user_prediction.ipynb
│   ├── 05_segmentation_clustering.ipynb
│   └── 06_skan4_attribution.ipynb
├── src/                   # 소스 코드
├── README.md
├── requirements.txt
└── pipeline_diagram.png
```

## 분석 내용

1. **Cohort Analysis** - 코호트 분석
2. **LTV Modeling** - 고객 생애 가치 모델링
3. **ROAS Prediction** - 광고 투자 대비 수익 예측
4. **High Value User Prediction** - 고가치 사용자 예측
5. **Segmentation & Clustering** - 사용자 세그먼테이션 및 클러스터링
6. **SKAN4 Attribution** - SKAdNetwork 4.0 어트리뷰션 분석

## 설치 방법

```bash
pip install -r requirements.txt
```

## 사용 방법

각 노트북은 독립적으로 실행 가능하며, 순차적으로 실행하는 것을 권장합니다.

## 데이터셋

이 프로젝트에서 사용할 수 있는 데이터셋은 다음과 같습니다:

### 1. 샘플 데이터 (테스트용)

프로젝트에 포함된 샘플 데이터 생성 스크립트를 사용할 수 있습니다:

```bash
python src/download_datasets.py
```

선택 옵션 1을 선택하면 다음 샘플 데이터가 생성됩니다:
- `sample_users.csv`: 사용자 기본 정보 (user_id, install_date, platform, country, channel)
- `sample_events.csv`: 사용자 이벤트 데이터 (user_id, event_date, event_type, revenue)
- `sample_campaigns.csv`: 마케팅 캠페인 데이터 (campaign_id, channel, budget, impressions, clicks)

### 2. 추천 공개 데이터셋

이 프로젝트의 분석 목적(코호트 · LTV/ROAS · 고가치 유저 · 세그멘테이션 · SKAN)에 맞춰 **바로 다운로드 가능하고, 제대로 된 분석·모델링이 가능한 공개 데이터셋**을 선별했습니다.

---

## ✅ **1. Cookie Cats Retention Dataset (강력 추천)**

📍 *Kaggle — 바로 다운로드 가능*

**링크:** [https://www.kaggle.com/datasets/yufengsui/cookie-cats](https://www.kaggle.com/datasets/yufengsui/cookie-cats)

### 포함 데이터
- `user_id`: 사용자 ID
- `version` / `test_group`: A/B 테스트 그룹
- `level progress`: 레벨 진행도
- `retention_1` / `retention_7`: 1일/7일 리텐션

### 가능 작업
- ✅ 코호트 분석 (install date 기준)
- ✅ Retention curve 분석
- ✅ 고가치 유저 정의 (retention 기반 proxy)
- ✅ Early behavior → retention 예측
- ✅ A/B 테스트 실습

### 레포 노트북 매핑
- `01_cohort_analysis.ipynb`
- `04_high_value_user_prediction.ipynb`
- `05_segmentation_clustering.ipynb`

※ LTV/ROAS는 없음 → retention 기반 proxy 가능

---

## ✅ **2. Mobile User Behavior Dataset (App Usage / Segmentation)**

📍 *Kaggle — 사용 가능*

**링크:** [https://www.kaggle.com/datasets/loveall/cellular-usage-analytics](https://www.kaggle.com/datasets/loveall/cellular-usage-analytics)

### 포함 데이터
- 세션 길이
- 데이터 사용량
- 앱 사용 패턴
- user category 정보

### 가능 작업
- ✅ 세그멘테이션
- ✅ User behavior clustering
- ✅ Event frequency 기반 고가치 예측

### 레포 노트북 매핑
- `05_segmentation_clustering.ipynb`
- `04_high_value_user_prediction.ipynb` (behavior 기반)

---

## ✅ **3. Mobile Game Telemetry Dataset (게임 이벤트 로그)**

📍 *Kaggle — 사용 가능*

**링크:** [https://www.kaggle.com/datasets/leomauro/mobile-game-telemetry](https://www.kaggle.com/datasets/leomauro/mobile-game-telemetry)

### 포함 데이터
- `user_id`: 사용자 ID
- `session`: 세션 정보
- `event_time`: 이벤트 발생 시간
- `game events`: 게임 이벤트 로그
- `device info`: 디바이스 정보

### 가능 작업
- ✅ 코호트 분석
- ✅ 이벤트 기반 feature engineering
- ✅ Retention / DAU 분석
- ✅ 고가치 유저 정의
- ✅ Segmentation
- ✅ 일부 LTV proxy 가능 (engagement 기반)

### 레포 노트북 매핑
- `01_cohort_analysis.ipynb`
- `04_high_value_user_prediction.ipynb`
- `05_segmentation_clustering.ipynb`
- `02_ltv_modeling.ipynb` (engagement 기반 proxy)

---

## ✅ **4. Steam Games Playtime Dataset (유저 가치 기반 예측 가능)**

📍 *Kaggle — 사용 가능*

**링크:** [https://www.kaggle.com/datasets/nikdavis/steam-games-complete-dataset](https://www.kaggle.com/datasets/nikdavis/steam-games-complete-dataset)

### 포함 데이터
- 유저별 플레이타임
- 구매 여부/가격
- 스팀 행동 데이터

### 가능 작업
- ✅ LTV proxy (시간 기반 가치)
- ✅ 고가치 유저 예측
- ✅ 세그멘테이션

### 레포 노트북 매핑
- `02_ltv_modeling.ipynb`
- `04_high_value_user_prediction.ipynb`
- `05_segmentation_clustering.ipynb`

---

## ✅ **5. Adjust / Meta SKAN Sample Dataset (SKAN 전용)**

⚠️ *Kaggle에는 SKAN 데이터셋이 없습니다. 공식 문서의 샘플 데이터를 활용하세요.*

### Adjust SKAN Sample
**링크:** [https://www.adjust.com/resources/](https://www.adjust.com/resources/)

### Meta SKAN Sample
**링크:** [https://developers.facebook.com/docs/marketing-api/](https://developers.facebook.com/docs/marketing-api/)

### 가능 작업
- ✅ `06_skan4_attribution.ipynb`
  - Conversion value → revenue 추정
  - Postback delay / lock window 처리
  - SKAN 4.0 3개 postback 활용해 attribution reconstruct

---

## ✅ **6. E-commerce Behavior Data (LTV/ROAS Revenue 기반 대체 옵션)**

📍 *Kaggle — 사용 가능*

**링크:** [https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store)

### 포함 데이터
- User session
- Event (view, cart, purchase)
- **Revenue 존재** (실제 매출 데이터)

### 가능 작업
- ✅ LTV/ROAS와 구조 80% 유사 (모바일이 아니라 웹이지만 모델 구조 동일)
- ✅ 실제 revenue 기반 LTV 모델링
- ✅ ROAS 예측

### 레포 노트북 매핑
- `02_ltv_modeling.ipynb`
- `03_roas_prediction.ipynb`

---

## 🔥 **최적 데이터셋 조합 (추천)**

이 프로젝트의 모든 노트북을 완성하기 위한 **최적 세트**:

### ⭐ **Best Set (3개 조합)**

1. **Cookie Cats Dataset** → 코호트 / retention / 고가치 / segmentation
2. **Mobile Game Telemetry Dataset** → 이벤트 기반 feature engineering + user clustering
3. **Adjust/Meta SKAN Sample** → attribution

이 조합으로 노트북 6개가 모두 완성됩니다:

| 노트북 | 데이터셋 |
|--------|----------|
| `01_cohort_analysis` | Cookie Cats + Game Telemetry |
| `02_ltv_modeling` | Game Telemetry (engagement→LTV proxy) |
| `03_roas_prediction` | Telemetry 기반 ad_proxy 또는 synthetic data 사용 |
| `04_high_value_user_prediction` | Cookie Cats or Telemetry |
| `05_segmentation_clustering` | Telemetry |
| `06_skan4_attribution` | Adjust + Meta SKAN samples |

---

### 📥 **데이터셋 다운로드 방법**

#### Kaggle 데이터셋 다운로드

1. Kaggle 계정 생성 및 로그인
2. Kaggle API 설정:
   ```bash
   pip install kaggle
   # ~/.kaggle/kaggle.json에 API 토큰 설정
   ```
3. 데이터셋 다운로드:
   ```bash
   kaggle datasets download -d yufengsui/cookie-cats -p datasets/
   kaggle datasets download -d leomauro/mobile-game-telemetry -p datasets/
   unzip datasets/*.zip -d datasets/
   ```

#### SKAN 샘플 데이터

- Adjust/Meta 공식 문서에서 샘플 데이터 및 예제 코드 다운로드
- `datasets/skan/` 디렉토리에 저장

---

### 📋 **데이터셋 구조 권장사항**

프로젝트의 각 노트북에서 사용하기 위해 다음 컬럼들이 포함된 데이터를 권장합니다:

**사용자 데이터:**
- `user_id`: 사용자 고유 ID
- `install_date`: 앱 설치일
- `platform`: 플랫폼 (iOS/Android)
- `country`: 국가 코드
- `channel`: 유입 채널

**이벤트 데이터:**
- `user_id`: 사용자 ID
- `event_date`: 이벤트 발생일시
- `event_type`: 이벤트 유형 (session_start, purchase, view_item 등)
- `revenue`: 수익 (해당하는 경우)

**캠페인 데이터:**
- `campaign_id`: 캠페인 ID
- `channel`: 채널명
- `date`: 날짜
- `budget`: 예산
- `impressions`: 노출 수
- `clicks`: 클릭 수
- `conversions`: 전환 수
- `revenue`: 수익

