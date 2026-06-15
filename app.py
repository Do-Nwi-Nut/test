import streamlit as st
import time

# 1. 페이지 기본 설정 및 귀여운 애니메이션 CSS 주입
st.set_page_config(page_title="포켓몬 속성 진단 테스트", page_icon="⚡", layout="centered")

st.markdown("""
    <style>
    /* 전체 폰트 및 배경 애니메이션 */
    @import url('https://fonts.googleapis.com/css2?family=Gamja+Flower&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Gamja+Flower', cursive;
        font-size: 20px;
    }
    
    /* 둥둥 떠다니는 귀여운 애니메이션 효과 */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    
    /* 반짝이는 애니메이션 효과 */
    @keyframes pulse {
        0% { opacity: 0.6; }
        50% { opacity: 1; }
        100% { opacity: 0.6; }
    }
    
    .title-box {
        text-align: center;
        animation: float 3s ease-in-out infinite;
        padding: 20px;
    }
    
    /* 심플하고 귀여운 버튼 스타일링 */
    div.stButton > button {
        width: 100%;
        border-radius: 20px;
        border: 3px solid #333333;
        padding: 15px;
        font-size: 18px !important;
        font-weight: bold;
        background-color: #ffffff;
        transition: all 0.2s ease-in-out;
        box-shadow: 0px 5px 0px #333333;
        margin-bottom: 10px;
    }
    div.stButton > button:hover {
        transform: translateY(3px);
        box-shadow: 0px 2px 0px #333333;
    }
    
    /* 결과 페이지 카드 디자인 애니메이션 */
    .result-card {
        padding: 30px;
        border-radius: 30px;
        border: 4px solid #333333;
        text-align: center;
        box-shadow: 0px 10px 0px #333333;
        animation: float 4s ease-in-out infinite;
        margin-top: 20px;
    }
    
    .loading-text {
        text-align: center;
        font-size: 24px;
        animation: pulse 1.5s infinite;
    }
    </style>
""", unsafe_unsafe_allow_html=True)

# 2. 질문 데이터셋 (12개 문항, 각 선택지는 물, 풀, 불, 전기 순서)
questions = [
    {
        "q": "주말이 찾아왔을 때, 당신이 가장 하고 싶은 것은?",
        "options": [
            ("🌊 조용히 혼자 목욕을 하거나 강가를 산책한다", "물"),
            ("🌱 햇살을 받으며 공원이나 숲길을 걷는다", "풀"),
            ("🔥 친구들을 모아 핫하고 시끌벅적한 곳으로 간다", "불"),
            ("⚡ 밀린 게임을 하거나 테마파크로 짜릿하게 놀러 간다", "전기")
        ]
    },
    {
        "q": "친구가 속상한 일로 울고 있다면 당신의 반응은?",
        "options": [
            ("🌊 말없이 곁에서 눈물을 닦아주며 다독인다", "물"),
            ("🌱 이야기를 가만히 들어주며 따뜻한 차를 타준다", "풀"),
            ("🔥 화를 내며 '누구야? 내가 혼내줄게!'라며 같이 흥분한다", "불"),
            ("⚡ 기분 전환용 재미있는 밈을 보여주거나 맛있는 걸 사준다", "전기")
        ]
    },
    {
        "q": "새로운 취미를 시작할 때 당신의 스타일은?",
        "options": [
            ("🌊 물 흐르듯 자연스럽게 스며드는 취미", "물"),
            ("🌱 식물 키우기, 요가 등 마음이 편해지는 취미", "풀"),
            ("🔥 격렬한 운동이나 열정을 불태울 수 있는 취미", "불"),
            ("⚡ EDM 작곡, 드론 조종 등 트렌디하고 짜릿한 취미", "전기")
        ]
    },
    {
        "q": "조별 과제를 할 때 당신의 역할은?",
        "options": [
            ("🌊 묵묵히 자료를 조사하고 뒤에서 받쳐주는 역할", "물"),
            ("🌱 갈등을 중재하고 팀원들의 멘탈을 케어하는 역할", "풀"),
            ("🔥 앞장서서 발표를 맡고 분위기를 주도하는 리더 역할", "불"),
            ("⚡ 반짝이는 아이디어를 뿜어내며 PPT를 화려하게 만드는 역할", "전기")
        ]
    },
    {
        "q": "화가 났을 때 당신의 모습은?",
        "options": [
            ("🌊 차갑게 가라앉으며 말문을 닫아버린다", "물"),
            ("🌱 웬만하면 참고 넘어가지만 한 번 터지면 무섭다", "풀"),
            ("🔥 그 자리에서 불같이 화를 내고 금방 풀린다", "불"),
            ("⚡ 짜증이 스파크처럼 튀고 이리저리 안절부절못한다", "전기")
        ]
    },
    {
        "q": "미래의 내 집을 꾸민다면 어떤 느낌으로?",
        "options": [
            ("🌊 통창 너머로 바다가 보이는 미니멀한 블루 하우스", "물"),
            ("🌱 베란다 가득 화분이 있고 우드톤의 아늑한 그린 하우스", "풀"),
            ("🔥 화려한 조명과 벽난로가 있는 힙한 레드 하우스", "불"),
            ("⚡ 최신 가전제품과 스마트 홈 시스템이 완비된 옐로우 하우스", "전기")
        ]
    },
    {
        "q": "여행 계획을 세울 때 당신은?",
        "options": [
            ("🌊 목적지만 정하고 발길 닿는 대로 유유자적 떠난다", "물"),
            ("🌱 힐링 스팟 위주로 여유롭게 일정을 짠다", "풀"),
            ("🔥 1분 1초도 쉬지 않는 열정 가득한 액티비티 투어", "불"),
            ("⚡ SNS에서 가장 핫하고 짜릿한 맛집과 명소 정복", "전기")
        ]
    },
    {
        "q": "당신이 가장 좋아하는 계절은?",
        "options": [
            ("🌊 시원한 바다를 즐길 수 있는 여름", "물"),
            ("🌱 새싹이 돋아나고 포근한 봄", "풀"),
            ("🔥 단풍이 붉게 물들고 감성 있는 가을", "불"),
            ("⚡ 눈이 내리고 짜릿한 스포츠를 즐기는 겨울", "전기")
        ]
    },
    {
        "q": "낯선 사람 가득한 파티에 초대받았다면?",
        "options": [
            ("🌊 구석에서 친한 사람 한두 명과 조용히 대화한다", "물"),
            ("🌱 따뜻한 미소로 인사를 건네며 들어준다", "풀"),
            ("🔥 파티 분위기를 하이텐션으로 만들며 주인공이 된다", "불"),
            ("⚡ 이곳저곳 빠르게 돌아다니며 명함을 주고받는다", "전기")
        ]
    },
    {
        "q": "시험 전날, 당신의 행동은?",
        "options": [
            ("🌊 '어떻게든 되겠지' 하며 평정심을 유지한다", "물"),
            ("🌱 미리 해둔 필기를 차분히 복습하며 마음을 가다듬는다", "풀"),
            ("🔥 밤을 새우며 초집중 모드로 에너지를 불태운다", "불"),
            ("⚡ 벼락치기로 핵심만 빠르게 스캔하며 스릴을 즐긴다", "전기")
        ]
    },
    {
        "q": "길을 가다 예쁜 유기동물을 발견했다면?",
        "options": [
            ("🌊 안타까운 눈빛으로 바라보며 조용히 신고 기관을 찾는다", "물"),
            ("🌱 부드럽게 다가가 다친 곳은 없는지 살핀다", "풀"),
            ("🔥 '헉 너무 귀여워!' 소리 지르며 당장 간식을 사 온다", "불"),
            ("⚡ 일단 사진이나 영상을 찍어 커뮤니티에 도움을 요청한다", "전기")
        ]
    },
    {
        "q": "당신의 좌우명과 가장 가까운 것은?",
        "options": [
            ("🌊 유수연화 (물처럼 자연스럽고 유연하게 살자)", "물"),
            ("🌱 대기만성 (뿌리를 깊게 내리고 차분히 성장하자)", "풀"),
            ("🔥 화력전개 (한 번 사는 인생, 뜨겁게 불태우자)", "불"),
            ("⚡ 전광석화 (인생은 타이밍, 빠르게 행동하자)", "전기")
        ]
    }
]

# Session State 초기화 (사용자 선택 데이터 및 진행도 저장)
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'scores' not in st.session_state:
    st.session_state.scores = {"물": 0, "풀": 0, "불": 0, "전기": 0}

# 3. 앱 화면 구성
# 메인 홈 화면
if st.session_state.step == 0:
    st.markdown('<div class="title-box"><h1>✨ 나의 포켓몬 속성 진단 ✨</h1><p>12개의 질문으로 알아보는 나의 숨겨진 타입!</p></div>', unsafe_allow_html=True)
    
    # 귀여운 몬스터볼 이모지 애니메이션 공간
    st.markdown("<h1 style='text-align: center; font-size: 80px; animation: float 2s infinite;'>🔴</h1>", unsafe_allow_html=True)
    
    if st.button("테스트 시작하기! 👉"):
        st.session_state.step = 1
        st.rerun()

# 질문 진행 화면 (1 ~ 12번)
elif 1 <= st.session_state.step <= 12:
    current_idx = st.session_state.step - 1
    q_data = questions[current_idx]
    
    # 진행도 표시 바
    st.progress(st.session_state.step / 12)
    st.write(f"**Q{st.session_state.step}. {q_data['q']}**")
    st.write("")
    
    # 버튼을 클릭하면 스코어를 더하고 즉시 다음 질문 단계로 넘어감
    for option_text, type_attr in q_data['options']:
        if st.button(option_text, key=f"q_{st.session_state.step}_{type_attr}"):
            st.session_state.scores[type_attr] += 1
            st.session_state.step += 1
            st.rerun()

# 4. 결과 분석 및 속성별 커스텀 페이지 출력
else:
    st.markdown('<div class="loading-text">🔮 당신의 에너지를 분석하는 중... 🔮</div>', unsafe_allow_html=True)
    time.sleep(1.5) # 귀여운 로딩 연출
    
    # 가장 높은 점수의 속성 추출
    final_type = max(st.session_state.scores, key=st.session_state.scores.get)
    
    # 속성별 디자인 정의 (물: 파랑, 풀: 초록, 불: 빨강, 전기: 노랑)
    type_styles = {
        "물": {
            "bg": "#E0F2FE", "border": "#0284C7", "text": "#0369A1", "emoji": "🌊", 
            "title": "침착하고 유연한 [물 속성]",
            "desc": "당신은 깊은 바다처럼 차분하고 조용한 성격의 소유자입니다. 갈등을 부드럽게 흘려보낼 줄 알며, 주변 사람들을 편안하게 해주는 포용력이 있어요!"
        },
        "풀": {
            "bg": "#DCFCE7", "border": "#16A34A", "text": "#15803D", "emoji": "🌱", 
            "title": "싱그럽고 따뜻한 [풀 속성]",
            "desc": "당신은 따사로운 햇살을 머금은 숲처럼 평화롭고 상냥한 사람입니다. 경청을 잘하고 공감 능력이 뛰어나 주변에 힐러 역할을 자처하네요!"
        },
        "불": {
            "bg": "#FEE2E2", "border": "#DC2626", "text": "#B91C1C", "emoji": "🔥", 
            "title": "열정적이고 용감한 [불 속성]",
            "desc": "당신은 활활 타오르는 불꽃처럼 에너지가 넘치고 정의로운 리더 타입입니다! 한 번 꽂히면 끝을 보는 열정파이며 분위기 메이커입니다."
        },
        "전기": {
            "bg": "#FEF9C3", "border": "#CA8A04", "text": "#A16207", "emoji": "⚡", 
            "title": "짜릿하고 트렌디한 [전기 속성]",
            "desc": "당신은 언제나 스파크가 튀듯 톡톡 튀는 아이디어와 유머 감각을 가진 사람입니다! 지루한 건 절대 못 참으며, 트렌디하고 빠른 행동력을 자랑해요."
        }
    }
    
    style = type_styles[final_type]
    
    # 속성 맞춤형 결과 카드 HTML 마크업 생성
    st.markdown(f"""
        <div class="result-card" style="background-color: {style['bg']}; border-color: {style['border']}; color: {style['text']};">
            <h1 style="font-size: 80px; margin: 0; animation: float 2.5s infinite;">{style['emoji']}</h1>
            <h2 style="margin-top: 10px;">{style['title']}</h2>
            <hr style="border-top: 2px dashed {style['border']};">
            <p style="font-size: 20px; line-height: 1.6; font-weight: bold;">{style['desc']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    
    # 다시 하기 버튼
    if st.button("🔄 테스트 다시 하기"):
        st.session_state.step = 0
        st.session_state.scores = {"물": 0, "풀": 0, "불": 0, "전기": 0}
        st.rerun()
