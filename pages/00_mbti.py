import streamlit as st
import random

# ✅ MBTI 환승 / 재회 추천 데이터셋
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
    total = sum(w for _, w in choices)
    r = random.random() * total
    upto = 0
    for c, w in choices:
        if upto + w >= r:
            return c, w
        upto += w
    return choices[-1]


# ✅ Streamlit UI 구성
st.title("🎬 MBTI 환승연애 예측기")
st.markdown("너의 MBTI를 알려주면...\n**환승할지 재회할지 예측해드립니다 🔮**")

mbti_input = st.text_input("MBTI 입력 (예: ENFP)").upper()

if st.button("운명 확인하기 💘"):
    if mbti_input not in MBTI_MAP:
        st.error("❌ 올바른 MBTI를 입력해주세요! (예: ISTP, ENTP)")
    else:
        transfer, w_t = weighted_choice(MBTI_MAP[mbti_input]['환승'])
        reunion, w_r = weighted_choice(MBTI_MAP[mbti_input]['재회'])

        st.subheader(f"✨ {mbti_input}의 연애 흐름 예측 결과")
        st.write(f"🚀 **환승 추천 MBTI**: `{transfer}` → 신뢰도 {round(w_t * 100)}%")
        st.write(f"💞 **재회 추천 MBTI**: `{reunion}` → 신뢰도 {round(w_r * 100)}%")

        st.caption("※ 재미로만 봐주세요! 실제 연애 결과를 보장하지 않습니다 😆")
