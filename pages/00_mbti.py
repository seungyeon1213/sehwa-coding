# mbti_hwanseung_prediction.py
# MBTI를 입력하면 '환승연애'에서 어느 유형으로 환승하거나 재회할 가능성이 높은지 예측해주는 간단한 스크립트
# (학습된 모델이 아니라 규칙 기반의 재미용 예측입니다. 실제 연애 결과와 다를 수 있음)

import random
import sys

# MBTI별로 환승 대상 및 재회 대상 추천과 가중치(0~1)
# 직관적/재미적 매핑: 보통 성향이 보완되는 유형 혹은 감정표현 방식이 맞는 유형을 추천
MBTI_MAP = {
    'ISTJ': {
        '환승': [('ESFP', 0.35), ('ENFP', 0.25), ('ISFJ', 0.15), ('ENTJ', 0.10), ('INFP', 0.15)],
        '재회': [('ISFJ', 0.35), ('ISTP', 0.25), ('ESFJ', 0.20), ('ESTJ', 0.20)]
    },
    'ISFJ': {
        '환승': [('ENFP', 0.30), ('ESFP', 0.25), ('ISFP', 0.20), ('ISTJ', 0.25)],
        '재회': [('ISTJ', 0.35), ('ISFP', 0.25), ('ESFJ', 0.20), ('INFJ', 0.20)]
    },
    'INFJ': {
        '환승': [('ENTP', 0.30), ('ENFP', 0.30), ('INTP', 0.20), ('ISFJ', 0.20)],
        '재회': [('ENFP', 0.35), ('INFJ', 0.25), ('ENFJ', 0.20), ('INTJ', 0.20)]
    },
    'INTJ': {
        '환승': [('ENFP', 0.35), ('ENTP', 0.25), ('INTP', 0.20), ('ESTJ', 0.20)],
        '재회': [('INTP', 0.30), ('ENTJ', 0.30), ('INFJ', 0.20), ('ISTJ', 0.20)]
    },
    'ISTP': {
        '환승': [('ESFJ', 0.30), ('ESTP', 0.25), ('ISFP', 0.25), ('ENTP', 0.20)],
        '재회': [('ISFP', 0.30), ('ISTP', 0.25), ('ESTP', 0.20), ('ISTJ', 0.25)]
    },
    'ISFP': {
        '환승': [('ESTJ', 0.30), ('ESFJ', 0.25), ('INFP', 0.25), ('ESFP', 0.20)],
        '재회': [('ISFP', 0.30), ('ISFJ', 0.25), ('INFP', 0.25), ('ESFP', 0.20)]
    },
    'INFP': {
        '환승': [('ENFJ', 0.30), ('ENFP', 0.30), ('INFJ', 0.20), ('ISFP', 0.20)],
        '재회': [('INFJ', 0.35), ('ENFP', 0.25), ('INFP', 0.20), ('ISFP', 0.20)]
    },
    'INTP': {
        '환승': [('ENTJ', 0.30), ('ENFP', 0.25), ('INTJ', 0.25), ('INFP', 0.20)],
        '재회': [('INTJ', 0.30), ('ENTP', 0.25), ('INTP', 0.25), ('INFP', 0.20)]
    },
    'ESTP': {
        '환승': [('ISFJ', 0.30), ('ISTJ', 0.25), ('ESFP', 0.25), ('ENFP', 0.20)],
        '재회': [('ESFP', 0.35), ('ESTP', 0.25), ('ISFP', 0.20), ('ISTP', 0.20)]
    },
    'ESFP': {
        '환승': [('ISTJ', 0.30), ('ISFJ', 0.25), ('ENFJ', 0.25), ('ESFP', 0.20)],
        '재회': [('ESTP', 0.35), ('ISFP', 0.25), ('ESFJ', 0.20), ('ENFP', 0.20)]
    },
    'ENFP': {
        '환승': [('ISTJ', 0.30), ('INTJ', 0.25), ('ENFJ', 0.25), ('INFP', 0.20)],
        '재회': [('INFP', 0.35), ('ENFP', 0.25), ('INFJ', 0.20), ('ENTP', 0.20)]
    },
    'ENTP': {
        '환승': [('INFJ', 0.30), ('INTJ', 0.25), ('ENTJ', 0.25), ('ENFP', 0.20)],
        '재회': [('ENTJ', 0.30), ('ENFP', 0.25), ('ENTP', 0.25), ('INTP', 0.20)]
    },
    'ESTJ': {
        '환승': [('ISFP', 0.30), ('ISTP', 0.25), ('ESFJ', 0.25), ('ENFP', 0.20)],
        '재회': [('ISTJ', 0.35), ('ESTJ', 0.25), ('ESFJ', 0.20), ('ENTJ', 0.20)]
    },
    'ESFJ': {
        '환승': [('INTP', 0.30), ('ISTP', 0.25), ('ENFP', 0.25), ('ISFJ', 0.20)],
        '재회': [('ISFJ', 0.35), ('ESFJ', 0.25), ('ENFJ', 0.20), ('ESTJ', 0.20)]
    },
    'ENFJ': {
        '환승': [('ISFP', 0.30), ('INFP', 0.30), ('ENTP', 0.20), ('ESFJ', 0.20)],
        '재회': [('ENFP', 0.35), ('ENFJ', 0.25), ('INFJ', 0.20), ('ESFJ', 0.20)]
    },
    'ENTJ': {
        '환승': [('ISFP', 0.30), ('INFP', 0.25), ('INTP', 0.25), ('ENFP', 0.20)],
        '재회': [('ENTP', 0.30), ('INTJ', 0.25), ('ENTJ', 0.25), ('ESTJ', 0.20)]
    }
}


def weighted_choice(choices):
    """choices: list of (item, weight). returns an item selected by normalized weights."""
    total = sum(w for _, w in choices)
    if total == 0:
        return random.choice([c for c, _ in choices])
    r = random.random() * total
    upto = 0
    for c, w in choices:
        if upto + w >= r:
            return c
        upto += w
    return choices[-1][0]


def predict(mbti: str, seed: int | None = None):
    """주어진 MBTI에 대해 환승 상대와 재회 상대를 하나씩 추천한다.
    seed를 주면 결정적 결과를 얻을 수 있다.
    Returns dict with keys: 'mbti', '환승추천', '재회추천'.
    """
    if seed is not None:
        random.seed(seed)
    m = mbti.upper()
    if m not in MBTI_MAP:
        raise ValueError('유효한 MBTI를 입력해 (예: "INFJ").')

    transfer = weighted_choice(MBTI_MAP[m]['환승'])
    reunion = weighted_choice(MBTI_MAP[m]['재회'])

    # 간단한 신뢰도(가중치 기반) 계산: 추천된 상대의 가중치를 찾아서 퍼센트로 변환
    def get_confidence(category, chosen):
        for c, w in MBTI_MAP[m][category]:
            if c == chosen:
                return round(w * 100)
        return 0

    return {
        'mbti': m,
        '환승추천': transfer,
        '환승신뢰도(%)': get_confidence('환승', transfer),
        '재회추천': reunion,
        '재회신뢰도(%)': get_confidence('재회', reunion)
    }


if __name__ == '__main__':
    # CLI 사용 예시: python mbti_hwanseung_prediction.py INFJ 42
    if len(sys.argv) < 2:
        print('사용법: python mbti_hwanseung_prediction.py <MBTI> [seed]')
        sys.exit(1)
    mbti_input = sys.argv[1]
    seed = int(sys.argv[2]) if len(sys.argv) >= 3 else None
    try:
        result = predict(mbti_input, seed)
        print(f"너의 MBTI: {result['mbti']}")
        print(f"환승(가능성 높은 상대): {result['환승추천']} (신뢰도: {result['환승신뢰도(%)']}%)")
        print(f"재회(가능성 높은 상대): {result['재회추천']} (신뢰도: {result['재회신뢰도(%)']}%)")
    except ValueError as e:
        print(e)
