"""
데이터셋 다운로드 스크립트

사용 가능한 데이터셋:
1. E-commerce Customer Behavior Dataset
2. Mobile App User Behavior Dataset
3. Marketing Campaign Dataset
"""

import os
import requests
import zipfile
from pathlib import Path
import pandas as pd

# 데이터셋 디렉토리
DATASETS_DIR = Path(__file__).parent.parent / "datasets"
DATASETS_DIR.mkdir(exist_ok=True)


def download_file(url: str, filename: str, chunk_size: int = 8192):
    """파일 다운로드 함수"""
    filepath = DATASETS_DIR / filename
    
    if filepath.exists():
        print(f"✓ {filename} 이미 존재합니다.")
        return filepath
    
    print(f"다운로드 중: {filename}...")
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    with open(filepath, 'wb') as f:
        for chunk in response.iter_content(chunk_size=chunk_size):
            f.write(chunk)
    
    print(f"✓ {filename} 다운로드 완료!")
    return filepath


def extract_zip(zip_path: Path, extract_to: Path = None):
    """ZIP 파일 압축 해제"""
    if extract_to is None:
        extract_to = zip_path.parent
    
    print(f"압축 해제 중: {zip_path.name}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"✓ 압축 해제 완료!")


def generate_sample_data():
    """샘플 데이터 생성 (테스트용)"""
    print("\n샘플 데이터 생성 중...")
    
    # 샘플 사용자 행동 데이터
    import numpy as np
    from datetime import datetime, timedelta
    
    np.random.seed(42)
    n_users = 10000
    start_date = datetime(2023, 1, 1)
    
    # 사용자 데이터
    user_data = {
        'user_id': [f'user_{i:05d}' for i in range(1, n_users + 1)],
        'install_date': [start_date + timedelta(days=np.random.randint(0, 365)) for _ in range(n_users)],
        'platform': np.random.choice(['iOS', 'Android'], n_users),
        'country': np.random.choice(['US', 'KR', 'JP', 'GB', 'DE'], n_users, p=[0.3, 0.25, 0.2, 0.15, 0.1]),
        'channel': np.random.choice(['organic', 'facebook', 'google', 'apple_search', 'tiktok'], n_users),
    }
    
    df_users = pd.DataFrame(user_data)
    df_users.to_csv(DATASETS_DIR / 'sample_users.csv', index=False)
    print("✓ sample_users.csv 생성 완료")
    
    # 이벤트 데이터
    events = []
    for user_id in df_users['user_id']:
        install_date = df_users[df_users['user_id'] == user_id]['install_date'].values[0]
        n_events = np.random.poisson(5)  # 평균 5개 이벤트
        
        for i in range(n_events):
            event_date = install_date + timedelta(days=np.random.randint(0, 30))
            events.append({
                'user_id': user_id,
                'event_date': event_date,
                'event_type': np.random.choice(['session_start', 'purchase', 'view_item', 'add_to_cart'], 
                                               p=[0.4, 0.1, 0.3, 0.2]),
                'revenue': np.random.exponential(10) if np.random.random() < 0.1 else 0,
            })
    
    df_events = pd.DataFrame(events)
    df_events.to_csv(DATASETS_DIR / 'sample_events.csv', index=False)
    print("✓ sample_events.csv 생성 완료")
    
    # 마케팅 캠페인 데이터
    campaign_data = {
        'campaign_id': [f'camp_{i:03d}' for i in range(1, 51)],
        'campaign_name': [f'Campaign {i}' for i in range(1, 51)],
        'channel': np.random.choice(['facebook', 'google', 'apple_search', 'tiktok'], 50),
        'start_date': [start_date + timedelta(days=np.random.randint(0, 300)) for _ in range(50)],
        'end_date': [start_date + timedelta(days=np.random.randint(300, 365)) for _ in range(50)],
        'budget': np.random.uniform(1000, 50000, 50),
        'impressions': np.random.randint(10000, 1000000, 50),
        'clicks': np.random.randint(100, 10000, 50),
    }
    
    df_campaigns = pd.DataFrame(campaign_data)
    df_campaigns['end_date'] = df_campaigns.apply(
        lambda x: x['start_date'] + timedelta(days=np.random.randint(7, 30)), axis=1
    )
    df_campaigns.to_csv(DATASETS_DIR / 'sample_campaigns.csv', index=False)
    print("✓ sample_campaigns.csv 생성 완료")
    
    print("\n모든 샘플 데이터 생성 완료!")


def main():
    """메인 함수"""
    print("=" * 50)
    print("데이터셋 다운로드 스크립트")
    print("=" * 50)
    
    print("\n사용 가능한 옵션:")
    print("1. 샘플 데이터 생성 (테스트용)")
    print("2. Kaggle 데이터셋 다운로드 (수동)")
    
    choice = input("\n선택하세요 (1 또는 2, 기본값: 1): ").strip() or "1"
    
    if choice == "1":
        generate_sample_data()
    elif choice == "2":
        print("\nKaggle 데이터셋은 수동으로 다운로드해야 합니다.")
        print("README.md의 '데이터셋' 섹션을 참고하세요.")
    else:
        print("잘못된 선택입니다.")


if __name__ == "__main__":
    main()

