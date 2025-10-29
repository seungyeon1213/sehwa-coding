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


transfer_lines = [
    "💥 그 사람? 너 없이도 잘 사는 척 하지만… 사실 너무 궁금해함.",
    "🎯 새로운 설렘이 찾아오고 말았다… 빠져든다…",
    "🔥 전 애인은 이미 추억 속 캐릭터!",
    "🌪️ 너의 매력에 휘말린 사람 등장!"
]

reunion_lines = [
    "💘 서로의 빈자리가 너무 크게 느껴졌다…",
    "📞 우연히 온 연락 한 통… 다시 시작되는 감정선!",
    "🧲 티격태격했는데… 결국은 서로였다!",
    "🌙 그 사람도 사실 계속 생각하고 있었음."
]

advice_lines = [
    "✨ 자신감 장착하고 나가라!",
    "😎 밀당 금지! 솔직함이 최고의 무기.",
    "🧊 쿨한 척? 하지마! 마음을 드러내!",
    "🍀 이번엔 너가 행복해지는 방향으로 가자."
]

def weighted_choice(choices):
    total = sum(w for _, w in choices)
    r = random.random() * total
    upto = 0
    for c, w in choices:
        if upto + w >= r:
            return c, w
        upto += w
    return choices[-1]

st.title("💔 환승연애 MBTI 운명 판독기 🎬")
st.caption("※ 실존 인물과 닮았다면…그건 운명입니다 😌")

mbti_input = st.text_input("MBTI 입력 (예: ENFP)").upper()

if st.button("운명 공개!"):

    if mbti_input not in MBTI_MAP:
        st.error("😡 MBTI 맞게 쓰라고! (예: ISTP, ENTP)")
    else:
        transfer, w_t = weighted_choice(MBTI_MAP[mbti_input]['환승'])
        reunion, w_r = weighted_choice(MBTI_MAP[mbti_input]['재회'])

        st.subheader(f"👀 {mbti_input}의 연애 운명 시나리오")

        mode = random.choice(["환승", "재회"])
        
        if mode == "환승":
            st.info("🚀 **환승 엔딩 예측**")
            st.write(f"👉 상대 MBTI: **{transfer}**")
            st.write(f"📈 신뢰도: **{round(w_t*100)}%**")
            st.write("🎬 시나리오:")
            st.write(random.choice(transfer_lines))
        else:
            st.success("💞 **재회 엔딩 예측**")
            st.write(f"👉 상대 MBTI: **{reunion}**")
            st.write(f"📈 신뢰도: **{round(w_r*100)}%**")
            st.write("🎬 시나리오:")
            st.write(random.choice(reunion_lines))

        st.write("---")
        st.write("📌 오늘의 연애 조언:")
        st.write(random.choice(advice_lines))

        st.caption("※ *당신의 전남친/전여친이 이걸 보고 있다면 긴장해라.* 🤫")
