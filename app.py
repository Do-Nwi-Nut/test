import streamlit as st
import time

st.set_page_config(
    page_title="포켓몬 속성 심리테스트",
    page_icon="⚡",
    layout="wide"
)

# -------------------
# CSS
# -------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

html, body, [class*="css"] {
    font-family: 'Jua', sans-serif;
}

.stApp{
    background: linear-gradient(
        135deg,
        #fff6cc,
        #ffd9d9,
        #d9f5ff,
        #e5ffd9
    );
}

/* 떠다니는 포켓볼 */

.pokeball{
    position: fixed;
    font-size:40px;
    animation: float 5s ease-in-out infinite;
    opacity:0.2;
    z-index:0;
}

.ball1{
    top:10%;
    left:5%;
}

.ball2{
    top:70%;
    right:10%;
}

.ball3{
    top:35%;
    right:20%;
}

@keyframes float{
    0%{
        transform:translateY(0px);
    }
    50%{
        transform:translateY(-20px);
    }
    100%{
        transform:translateY(0px);
    }
}

.title{
    text-align:center;
    font-size:55px;
    font-weight:bold;
    animation: glow 2s infinite;
}

@keyframes glow{
    0%{
        text-shadow:0 0 10px white;
    }
    50%{
        text-shadow:0 0 30px gold;
    }
    100%{
        text-shadow:0 0 10px white;
    }
}

.glass{
    background: rgba(255,255,255,0.35);
    backdrop-filter: blur(15px);
    padding:30px;
    border-radius:25px;
    box-shadow:0 8px 32px rgba(0,0,0,0.15);
}

.result-card{
    padding:30px;
    border-radius:25px;
    color:white;
    text-align:center;
    animation: popup 0.8s;
}

@keyframes popup{
    from{
        transform:scale(0.7);
        opacity:0;
    }
    to{
        transform:scale(1);
        opacity:1;
    }
}

/* 물 */

.water{
    background:linear-gradient(
        135deg,
        #4FC3F7,
        #0288D1
    );
}

/* 풀 */

.grass{
    background:linear-gradient(
        135deg,
        #66BB6A,
        #2E7D32
    );
}

/* 불 */

.fire{
    background:linear-gradient(
        135deg,
        #FF7043,
        #D84315
    );
}

/* 전기 */

.electric{
    background:linear-gradient(
        135deg,
        #FFD54F,
        #F9A825
    );
}

.water-icon{
    animation: wave 2s infinite;
}

.grass-icon{
    animation: leaf 2s infinite;
}

.fire-icon{
    animation: flame 1s infinite;
}

.electric-icon{
    animation: electric 1s infinite;
}

@keyframes wave{
    50%{
        transform:translateY(-10px);
    }
}

@keyframes leaf{
    50%{
        transform:rotate(8deg);
    }
}

@keyframes flame{
    50%{
        transform:scale(1.2);
    }
}

@keyframes electric{
    50%{
        opacity:0.4;
    }
}

</style>

<div class="pokeball ball1">⚪🔴</div>
<div class="pokeball ball2">⚪🔴</div>
<div class="pokeball ball3">⚪🔴</div>

""", unsafe_allow_html=True)

# -------------------
# 질문
# -------------------

questions = [
    {
        "question":"새로운 모임에 갔을 때 나는?",
        "options":{
            "먼저 다가간다":"fire",
            "분위기를 관찰한다":"water",
            "친해질 시간을 가진다":"grass",
            "재밌는 이벤트를 만든다":"electric"
        }
    },
    {
        "question":"친구들이 나를 보는 모습은?",
        "options":{
            "열정적":"fire",
            "차분함":"water",
            "다정함":"grass",
            "엉뚱함":"electric"
        }
    },
    {
        "question":"좋아하는 휴일은?",
        "options":{
            "액티비티":"fire",
            "집에서 휴식":"water",
            "공원 산책":"grass",
            "새로운 장소 탐험":"electric"
        }
    },
    {
        "question":"위기 상황에서는?",
        "options":{
            "밀어붙인다":"fire",
            "냉정히 분석":"water",
            "주변을 챙긴다":"grass",
            "새로운 방법 시도":"electric"
        }
    },
    {
        "question":"가장 중요한 가치는?",
        "options":{
            "도전":"fire",
            "공감":"water",
            "성장":"grass",
            "창의성":"electric"
        }
    }
]

# -------------------
# 세션 초기화
# -------------------

if "finished" not in st.session_state:
    st.session_state.finished = False

if not st.session_state.finished:

    st.markdown(
        '<div class="title">⚡ 포켓몬 속성 심리테스트 🌱</div>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    scores = {
        "water":0,
        "grass":0,
        "fire":0,
        "electric":0
    }

    answers = []

    with st.form("test_form"):

        for q in questions:

            answer = st.radio(
                q["question"],
                list(q["options"].keys()),
                key=q["question"]
            )

            answers.append((q,answer))

        submit = st.form_submit_button("✨ 결과 보기")

    if submit:

        for q,answer in answers:

            element = q["options"][answer]
            scores[element] += 1

        st.session_state.scores = scores
        st.session_state.finished = True
        st.rerun()

# -------------------
# 결과 페이지
# -------------------

else:

    scores = st.session_state.scores

    result = max(scores, key=scores.get)

    progress = st.progress(0)

    messages = [
        "⚡ 전투 데이터 수집중...",
        "🌱 성향 분석중...",
        "💧 감정 패턴 계산중...",
        "🔥 최종 결과 생성중..."
    ]

    holder = st.empty()

    for i,msg in enumerate(messages):

        holder.info(msg)
        progress.progress((i+1)*25)
        time.sleep(0.8)

    holder.success("분석 완료!")

    st.balloons()

    info = {
        "water":{
            "emoji":"💧",
            "class":"water",
            "icon":"water-icon",
            "title":"물 타입",
            "desc":"차분하고 공감 능력이 뛰어난 성향",
            "pokemon":"꼬부기 · 라프라스 · 밀로틱"
        },
        "grass":{
            "emoji":"🌱",
            "class":"grass",
            "icon":"grass-icon",
            "title":"풀 타입",
            "desc":"배려심 많고 꾸준히 성장하는 성향",
            "pokemon":"이상해씨 · 나무지기 · 샤로다"
        },
        "fire":{
            "emoji":"🔥",
            "class":"fire",
            "icon":"fire-icon",
            "title":"불 타입",
            "desc":"열정적이고 목표 지향적인 성향",
            "pokemon":"파이리 · 마그마 · 번치코"
        },
        "electric":{
            "emoji":"⚡",
            "class":"electric",
            "icon":"electric-icon",
            "title":"전기 타입",
            "desc":"창의적이고 호기심이 넘치는 성향",
            "pokemon":"피카츄 · 라이츄 · 렌트라"
        }
    }

    data = info[result]

    st.markdown(
        f"""
        <div class="result-card {data['class']}">
            <h1 class="{data['icon']}">
            {data['emoji']}
            </h1>

            <h1>
            당신은 {data['title']}!
            </h1>

            <h3>
            {data['desc']}
            </h3>

            <br>

            <h2>
            추천 포켓몬
            </h2>

            <h3>
            {data['pokemon']}
            </h3>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## 📊 속성 게이지")

    total = sum(scores.values())

    st.progress(scores["water"]/total)
    st.write("💧 물")

    st.progress(scores["grass"]/total)
    st.write("🌱 풀")

    st.progress(scores["fire"]/total)
    st.write("🔥 불")

    st.progress(scores["electric"]/total)
    st.write("⚡ 전기")

    if st.button("🔄 다시 하기"):

        st.session_state.finished = False
        st.rerun()
