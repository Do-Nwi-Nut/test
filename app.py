import streamlit as st
import random

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="포켓몬 속성 심리테스트 ✨",
    page_icon="🌟",
    layout="centered"
)

# 2. 글로벌 CSS 및 애니메이션 설정 (중괄호 충돌이 없도록 일반 문자열 처리)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Gamja+Flower&display=swap');

* { font-family: 'Gamja+Flower', 'Nunito', sans-serif; }

html, body, [class*="css"] {
    background: #1a1a2e;
    color: #fff;
}

.stApp {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    min-height: 100vh;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem; }

@keyframes twinkle {
    0%, 100% { opacity: 0.2; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.3); }
}
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-12px); }
}
@keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-15px); }
}
@keyframes waveBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
@keyframes fireFlicker {
    0%, 100% { transform: scale(1) rotate(-1deg); filter: brightness(1); }
    50% { transform: scale(1.05) rotate(1deg); filter: brightness(1.2); }
}
@keyframes leafSway {
    0%, 100% { transform: rotate(-4deg); }
    50% { transform: rotate(4deg); }
}
@keyframes electricZap {
    0%, 100% { opacity: 1; transform: skewX(0deg); }
    50% { opacity: 0.8; transform: skewX(-2deg); }
}

.hero-section {
    text-align: center;
    padding: 2rem 1rem;
    animation: float 4s ease-in-out infinite;
}
.hero-title {
    font-size: 3rem;
    font-weight: 900;
    background: linear-gradient(90deg, #ff6b6b, #ffd700, #4ecdc4, #95e17d, #667eea);
    background-size: 300% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: waveBG 3s linear infinite;
    margin-bottom: 0.5rem;
}
.hero-sub {
    font-size: 1.2rem;
    color: #aac4ff;
    margin-bottom: 1.5rem;
}
.pokeball-anim {
    font-size: 4.5rem;
    display: inline-block;
    animation: bounce 2s ease-in-out infinite;
}
.stars-container {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}
.star {
    position: absolute;
    color: #fff;
    animation: twinkle var(--dur) ease-in-out infinite var(--delay);
}

.q-card {
    background: rgba(255,255,255,0.07);
    border: 2px solid rgba(255,255,255,0.15);
    border-radius: 24px;
    padding: 2rem;
    margin: 1rem 0;
    backdrop-filter: blur(10px);
    text-align: center;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}
.q-number {
    font-size: 0.9rem;
    color: #aac4ff;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 0.5rem;
}
.q-text {
    font-size: 1.5rem;
    font-weight: 800;
    color: #fff;
    line-height: 1.4;
}
.q-emoji {
    font-size: 3rem;
    margin-bottom: 0.5rem;
    display: inline-block;
    animation: float 3s ease-in-out infinite;
}

.progress-container {
    background: rgba(255,255,255,0.1);
    border-radius: 20px;
    height: 12px;
    margin: 1rem 0;
    overflow: hidden;
}
.progress-fill {
    height: 100%;
    border-radius: 20px;
    background: linear-gradient(90deg, #667eea, #764ba2);
    transition: width 0.4s ease;
    box-shadow: 0 0 10px rgba(102,126,234,0.7);
}

div.stButton > button {
    width: 100%;
    background: rgba(255,255,255,0.08) !important;
    border: 2px solid rgba(255,255,255,0.2) !important;
    border-radius: 16px !important;
    color: #ffffff !important;
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    padding: 1rem 1.5rem !important;
    transition: all 0.2s ease !important;
    text-align: left !important;
    margin-bottom: 0.6rem !important;
    backdrop-filter: blur(5px) !important;
}
div.stButton > button:hover {
    background: rgba(255,255,255,0.25) !important;
    border-color: rgba(255,255,255,0.6) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3) !important;
}

/* 결과창 전용 클래스 */
.result-card {
    border-radius: 32px;
    padding: 3rem 2rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    border: 4px solid rgba(255,255,255,0.3);
    box-shadow: 0 15px 35px rgba(0,0,0,0.4);
    animation: float 4s ease-in-out infinite;
}
.result-title {
    font-size: 3.2rem;
    font-weight: 900;
    margin-bottom: 0.5rem;
    text-shadow: 0 2px 15px rgba(0,0,0,0.2);
}
.result-subtitle {
    font-size: 1.4rem;
    margin-bottom: 1.5rem;
    font-weight: 700;
    opacity: 0.9;
}
.trait-list {
    text-align: left;
    margin: 1.5rem 0;
    padding: 0;
    list-style: none;
}
.trait-list li {
    padding: 0.7rem 1rem;
    font-size: 1.1rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
    border-radius: 12px;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: #333333 !important;
    background: rgba(255, 255, 255, 0.6) !important;
    border: 1px solid rgba(0,0,0,0.05);
}

.water-bubble { display: inline-block; animation: float 2.5s ease-in-out infinite; }
.fire-flicker { display: inline-block; animation: fireFlicker 0.6s ease-in-out infinite; }
.leaf-sway { display: inline-block; animation: leafSway 1.8s ease-in-out infinite; }
.electric-zap { display: inline-block; animation: electricZap 1.2s ease-in-out infinite; }

.restart-btn > button {
    background: rgba(255,255,255,0.2) !important;
    border: 2px solid rgba(255,255,255,0.5) !important;
    border-radius: 50px !important;
    font-size: 1.2rem !important;
    padding: 0.8rem 2.5rem !important;
    text-align: center !important;
    color: #fff !important;
}
.restart-btn > button:hover {
    background: rgba(255,255,255,0.4) !important;
}
</style>
""", unsafe_allow_html=True)

# 3. 별빛 고정 효과
if 'stars_html' not in st.session_state:
    stars = '<div class="stars-container">'
    star_chars = ["★", "✦", "✧", "⊹", "✩", "⋆"]
    for _ in range(25):
        x, y = random.randint(0, 100), random.randint(0, 100)
        size = random.uniform(0.6, 1.3)
        dur = random.uniform(2, 5)
        delay = random.uniform(0, 3)
        char = random.choice(star_chars)
        stars += f'<div class="star" style="left:{x}%;top:{y}%;font-size:{size}rem;--dur:{dur}s;--delay:{delay}s;">{char}</div>'
    stars += '</div>'
    st.session_state.stars_html = stars

st.markdown(st.session_state.stars_html, unsafe_allow_html=True)

# 4. 질문 데이터 (12문항)
questions = [
    {
        "emoji": "🌅", "text": "주말 오전, 눈을 떴을 때 나는 보통...",
        "options": [
            ("조용히 커피 한잔하며 여유를 즐겨요", "water"),
            ("가벼운 산책을 하면서 돌아다녀요", "grass"),
            ("친구들과 약속을 잡고 밖으로 튀어나가요", "fire"),
            ("밀린 게임이나 힙한 트렌드를 서치해요", "electric"),
        ]
    },
    {
        "emoji": "💭", "text": "친구가 눈물을 흘리며 고민을 털어놓을 때 나는...",
        "options": [
            ("감정을 오롯이 들어주며 깊이 공감해줘요", "water"),
            ("마음을 차분하게 달래줄 따뜻한 대안을 줘요", "grass"),
            ("내 일처럼 같이 화내고 으르렁거려요", "fire"),
            ("핵심을 빠르게 짚어내고 해결책을 제시해요", "electric"),
        ]
    },
    {
        "emoji": "🎨", "text": "예상치 못한 일이 생기면?",
        "options": [
            ("일단 상황을 지켜보며 침착하게 판단한다", "water"),
            ("주변 사람들과 협력할 방법을 찾는다", "grass"),
            ("빠르게 행동하며 문제를 돌파한다"", "fire"),
            ("새로운 아이디어로 색다른 해결책을 낸다", "electric"),
        ]
    },
    {
        "emoji": "🏖️", "text": "상상만 해도 행복한 나만의 여행 스타일은?",
        "options": [
            ("넓은 바다를 보며 멍때리는 유유자적 힐링 투어", "water"),
            ("자연의 소리 가득한 숲속 글램핑 스팟", "grass"),
            ("페스티벌과 핫플레이스를 정복하는 액티비티 투어", "fire"),
            ("첨단 미래 도시의 화려한 조명과 야경 투어", "electric"),
        ]
    },
    {
        "emoji": "😤", "text": "극심한 스트레스를 받았을 때 탈출구는?",
        "options": [
            ("따뜻한 목욕이나 샤워로 생각을 깨끗이 씻어내요", "water"),
            ("한적한 공원 벤치에서 머리를 식혀요", "grass"),
            ("땀을 쫙 흘리거나 수다를 떨며 다 태워버려요", "fire"),
            ("도파민 터지는 취미나 게임에 미친 듯이 몰두해요", "electric"),
        ]
    },
    {
        "emoji": "🍽️", "text": "음식을 고를 때 내가 가장 끌리는 기준은?",
        "options": [
            ("깔끔하고 정갈하게 입안을 채워주는 맛", "water"),
            ("몸도 마음도 정화되는 건강하고 깨끗한 맛", "grass"),
            ("땀이 쏙 빠질 만큼 화끈하고 자극적인 맛", "fire"),
            ("간편하고 빠르면서도 트렌디하게 맛있는 최신 푸드", "electric"),
        ]
    },
    {
        "emoji": "🌙", "text": "늦은 밤 잠들기 직전, 침대 위에서의 내 모습은?",
        "options": [
            ("감성 넘치는 잔잔한 플리나 음악에 심취한다", "water"),
            ("오늘 하루를 되돌아보며 다이어리를 쓴다", "grass"),
            ("시간 가는 줄 모르고 쇼츠/유튜브를 릴레이 시청한다", "fire"),
            ("내일 할 일이나 기발한 영감이 끊임없이 도진다", "electric"),
        ]
    },
    {
        "emoji": "🦁", "text": "내가 생각하는 나의 가장 매력적인 무기는?",
        "options": [
            ("누구보다 넓은 포용력과 깊은 감수성", "water"),
            ("흔들리지 않는 뚝심과 한결같은 성실함", "grass"),
            ("빠른 추진력과 무한 긍정 에너지", "fire"),
            ("번뜩이는 두뇌 회전과 쾌활한 유머 감각", "electric"),
        ]
    },
    {
        "emoji": "🎵", "text": "평소 내 플레이리스트를 장악한 장르는?",
        "options": [
            ("듣기만 해도 몽글몽글해지는 인디, Lo-fi", "water"),
            ("마음 안정을 돕는 쿨재즈, 어쿠스틱 팝", "grass"),
            ("텐션을 급상승시키는 댄스, 힙합, 락", "fire"),
            ("리드미컬하고 세련된 테크노, EDM, 신스팝", "electric"),
        ]
    },
    {
        "emoji": "🌟", "text": "인생에서 가장 가치 있게 생각하는 모토는?",
        "options": [
            ("부드러움이 강함을 이긴다.", "water"),
            ("꾸준함이 결과를 바꾼다.", "grass"),
            ("다시 돌아올 힘을 남기지 않는다.", "fire"),
            ("달라지지 않으면 살아남을 수 없다.", "electric"),
        ]
    },
    {
        "emoji": "👥", "text": "새로운 조별 과제나 팀 프로젝트에 투입되었을 때 나는?",
        "options": [
            ("팀원들의 의견을 묵묵히 조율하며 서포트한다", "water"),
            ("마찰이 생기지 않도록 중간에서 부드럽게 중재한다", "grass"),
            ("팀의 사기를 올리며 앞장서서 리드해 나간다", "fire"),
            ("템플릿 제작이나 기발한 아이디어 피칭을 도맡는다", "electric"),
        ]
    },
    {
        "emoji": "🎁", "text": "소중한 사람에게 선물을 줄 때 나의 선택은?",
        "options": [
            ("정성 어린 편지와 마음이 뭉클해지는 선물", "water"),
            ("오랫동안 곁에 두고 쓸 수 있는 아늑한 물건", "grass"),
            ("요즘 가장 핫하고 모두가 부러워할 만한 화려한 선물", "fire"),
            ("상대방이 깜짝 놀랄 만한 기발하고 스마트한 아이템", "electric"),
        ]
    }
]

results = {
    "water": {
        "name": "물 타입 🌊", "subtitle": "깊고 유연한 바다의 영혼",
        "bg_color": "linear-gradient(135deg, #0077b6 0%, #00b4d8 50%, #90e0ef 100%)",
        "text_color": "#0369A1", "card_bg": "#E0F2FE", "border_color": "#0284C7",
        "main_pokemon": "🐳", "anim_class": "water-bubble",
        "traits": [
            "어떤 그릇에도 맞춰 변하는 유연하고 포용력 있는 성격입니다.",
            "타인의 상처를 묵묵히 어루만져 주는 따뜻한 감수성의 소유자입니다.",
            "겉으로는 고요해 보이지만, 내면에는 아주 깊고 단단한 주관이 서려 있어요.",
            "복잡한 상황 속에서도 직관적으로 정답을 부드럽게 찾아냅니다."
        ],
        "compatible": "💕 환상의 케미: 풀 타입(🌿)과 함께하면 최고의 심리적 안정감을 느껴요!",
        "pokemon_examples": "꼬부기, 라프라스, 샤미드", "particles": "🌊💧💙🫧"
    },
    "grass": {
        "name": "풀 타입 🌿", "subtitle": "치유와 평화를 선사하는 대지의 숲",
        "bg_color": "linear-gradient(135deg, #1b4332 0%, #2d6a4f 50%, #52b788 100%)",
        "text_color": "#15803D", "card_bg": "#DCFCE7", "border_color": "#16A34A",
        "main_pokemon": "🌿", "anim_class": "leaf-sway",
        "traits": [
            "급하게 서두르지 않고 묵묵히 자신만의 뿌리를 내리는 성실파입니다.",
            "주변 사람들의 마음을 편안하게 힐링해주는 인간 비타민 같은 존재입니다.",
            "갈등을 싫어하며 대가 없는 친절과 조화를 베풀 줄 압니다.",
            "인내심이 무척 뛰어나 신뢰감을 주는 든든한 버팀목 역할을 해냅니다."
        ],
        "compatible": "💕 환상의 케미: 물 타입(🌊)과 만나면 서로를 무한히 성장시켜 주는 상생의 관계가 됩니다!",
        "pokemon_examples": "이상해씨, 치코리타, 샤로다", "particles": "🌿🍃🌱💚"
    },
    "fire": {
        "name": "불 타입 🔥", "subtitle": "세상을 밝히는 찬란한 불꽃",
        "bg_color": "linear-gradient(135deg, #7f1d1d 0%, #dc2626 50%, #f97316 100%)",
        "text_color": "#B91C1C", "card_bg": "#FEE2E2", "border_color": "#DC2626",
        "main_pokemon": "🔥", "anim_class": "fire-flicker",
        "traits": [
            "가슴속에 꺼지지 않는 뜨거운 열정과 에너지를 품고 있습니다.",
            "실패를 두려워하지 않고 과감하게 도전하는 타고난 개척자입니다.",
            "솔직하고 뒤끝 없는 성격으로 주변의 분위기를 리드하는 대장 부엉이입니다.",
            "목표가 생기면 그 누구보다 폭발적인 집중력과 추진력을 발휘합니다."
        ],
        "compatible": "💕 환상의 케미: 전기 타입(⚡)과 만나면 멈추지 않는 도파민과 시너지가 폭발합니다!",
        "pokemon_examples": "파이리, 리자몽, 윈디", "particles": "🔥💥✨❤️"
    },
    "electric": {
        "name": "전기 타입 ⚡", "subtitle": "짜릿하고 영리한 섬광의 혁신가",
        "bg_color": "linear-gradient(135deg, #713f12 0%, #ca8a04 50%, #eab308 100%)",
        "text_color": "#A16207", "card_bg": "#FEF9C3", "border_color": "#CA8A04",
        "main_pokemon": "⚡", "anim_class": "electric-zap",
        "traits": [
            "스파크가 튀듯 남들이 생각지 못한 기발한 아이디어를 뿜어냅니다.",
            "지루한 일상을 싫어하며 언제나 새롭고 트렌디한 것에 안테나를 켭니다.",
            "두뇌 회전과 행동력이 전광석화처럼 빨라 위기 대처 능력이 만렙입니다.",
            "특유의 센스와 위트 넘치는 성격으로 모임의 활력소 역할을 톡톡히 합니다."
        ],
        "compatible": "💕 환상의 케미: 불 타입(🔥)과 함께할 때 가장 지루하지 않고 짜릿한 파트너가 됩니다!",
        "pokemon_examples": "피카츄, 에레브, 쥬피썬더", "particles": "⚡💡✨💛"
    }
}

# 5. 세션 상태 초기화
if 'page' not in st.session_state:
    st.session_state.page = 'intro'
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
if 'scores' not in st.session_state:
    st.session_state.scores = {"water": 0, "grass": 0, "fire": 0, "electric": 0}
if 'shuffled_options' not in st.session_state:
    st.session_state.shuffled_options = {}

def reset():
    st.session_state.page = 'intro'
    st.session_state.current_q = 0
    st.session_state.scores = {"water": 0, "grass": 0, "fire": 0, "electric": 0}
    st.session_state.shuffled_options = {}

# ---- [PAGE] INTRO ----
if st.session_state.page == 'intro':
    st.markdown("""
    <div class="hero-section">
        <div class="pokeball-anim">🔮</div>
        <h1 class="hero-title">포켓몬 속성<br>심리테스트</h1>
        <p class="hero-sub">당신은 어떤 타입의 트레이너인가요?<br>12가지 문항으로 잠재된 속성을 깨워보세요! ✨</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1.5rem 0;">
        <div style="background:linear-gradient(135deg,#0077b6,#00b4d8);border-radius:20px;padding:1.2rem;text-align:center;">
            <div style="font-size:2rem;" class="water-bubble">🌊</div>
            <div style="color:#fff;font-weight:800;font-size:1.1rem;margin-top:5px;">물 타입</div>
        </div>
        <div style="background:linear-gradient(135deg,#2d6a4f,#52b788);border-radius:20px;padding:1.2rem;text-align:center;">
            <div style="font-size:2rem;" class="leaf-sway">🌿</div>
            <div style="color:#fff;font-weight:800;font-size:1.1rem;margin-top:5px;">풀 타입</div>
        </div>
        <div style="background:linear-gradient(135deg,#dc2626,#f97316);border-radius:20px;padding:1.2rem;text-align:center;">
            <div style="font-size:2rem;" class="fire-flicker">🔥</div>
            <div style="color:#fff;font-weight:800;font-size:1.1rem;margin-top:5px;">불 타입</div>
        </div>
        <div style="background:linear-gradient(135deg,#ca8a04,#eab308);border-radius:20px;padding:1.2rem;text-align:center;">
            <div style="font-size:2rem;" class="electric-zap">⚡</div>
            <div style="color:#fff;font-weight:800;font-size:1.1rem;margin-top:5px;">전기 타입</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    _, col_btn, _ = st.columns([0.5, 2, 0.5])
    with col_btn:
        if st.button("✨ 진단 시작하기!", key="start_game"):
            reset()
            st.session_state.page = 'quiz'
            st.rerun()

# ---- [PAGE] QUIZ ----
elif st.session_state.page == 'quiz':
    q_idx = st.session_state.current_q
    q = questions[q_idx]
    total = len(questions)
    progress_pct = int((q_idx / total) * 100)

    st.markdown(f"""
    <div style="margin:0.5rem 0;">
        <div style="display:flex;justify-content:space-between;color:#aac4ff;font-weight:700;font-size:1rem;margin-bottom:0.3rem;">
            <span>문항 {q_idx+1} / {total}</span>
            <span>{progress_pct}% 완료</span>
        </div>
        <div class="progress-container">
            <div class="progress-fill" style="width:{progress_pct}%;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="q-card">
        <span class="q-emoji">{q['emoji']}</span>
        <div class="q-number">Q U E S T I O N &nbsp; {q_idx+1:02d}</div>
        <div class="q-text">{q['text']}</div>
    </div>
    """, unsafe_allow_html=True)

    # 셔플 고정
    if q_idx not in st.session_state.shuffled_options:
        st.session_state.shuffled_options[q_idx] = random.sample(q['options'], len(q['options']))
    
    current_options = st.session_state.shuffled_options[q_idx]

    # KeyError 완전 해결 로직
    for opt_text, opt_type in current_options:
        if st.button(opt_text, key=f"btn_{q_idx}_{opt_text[:15]}"):
            st.session_state.scores[opt_type] += 1
            if q_idx + 1 < total:
                st.session_state.current_q += 1
                st.rerun()
            else:
                st.session_state.page = 'result'
                st.rerun()

# ---- [PAGE] RESULT ----
elif st.session_state.page == 'result':
    winner = max(st.session_state.scores, key=st.session_state.scores.get)
    r = results[winner]

    # 배경 동적 주입
    st.markdown(f"""
    <style>
    .stApp {{
        background: {r['bg_color']} !important;
        background-size: 400% 400% !important;
        animation: waveBG 6s ease infinite !important;
    }}
    </style>
    """, unsafe_allow_html=True)

    # 파티클 데코레이션
    deco_emojis = r['particles']
    deco_html = '<div style="position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;overflow:hidden;z-index:0;">'
    for i in range(12):
        emoji = deco_emojis[i % len(deco_emojis)]
        x, y = random.randint(0, 100), random.randint(0, 100)
        size = random.uniform(1.5, 2.5)
        dur = random.uniform(3, 6)
        deco_html += f'<div style="position:absolute;left:{x}%;top:{y}%;font-size:{size}rem;opacity:0.2;animation:float {dur}s ease-in-out infinite;">{emoji}</div>'
    deco_html += '</div>'
    st.markdown(deco_html, unsafe_allow_html=True)

    total_answers = sum(st.session_state.scores.values())
    if total_answers == 0: total_answers = 1
    score_pct = int((st.session_state.scores[winner] / total_answers) * 100)

    # [핵심 변경 사항]: f-string 문자열 안에서 중괄호로 인한 깨짐을 방지하기 위해 HTML 구조를 하드코딩식으로 안전하게 분할 렌더링합니다.
    st.markdown(f'<div class="result-card" style="background: {r["card_bg"]} !important; border-color: {r["border_color"]} !important;">', unsafe_allow_html=True)
    st.markdown(f'<div style="font-size:5rem; display:inline-block;" class="{r["anim_class"]}">{r["main_pokemon"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="font-size:1rem; letter-spacing:3px; font-weight:800; color: {r["text_color"]} !important; margin:0.5rem 0;">당신의 매칭 속성은</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="result-title" style="color: {r["text_color"]} !important;">{r["name"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="result-subtitle" style="color: {r["text_color"]} !important; opacity:0.85;">{r["subtitle"]}</div>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="background:rgba(0,0,0,0.05); border-radius:50px; padding:0.6rem 1.5rem; margin:1.2rem 0; font-size:1.1rem; font-weight:800; color: {r['text_color']} !important; display:inline-block;">
        💡 싱크로율 {score_pct}%
    </div>
    """, unsafe_allow_html=True)

    # 특징 리스트 출력
    st.markdown('<ul class="trait-list">', unsafe_allow_html=True)
    for trait in r['traits']:
        st.markdown(f'<li>{trait}</li>', unsafe_allow_html=True)
    st.markdown('</ul>', unsafe_allow_html=True)
    
    # 파트너 및 케미
    st.markdown(f"""
    <div style="background:rgba(255,255,255,0.7); border-radius:16px; padding:1.1rem 1.5rem; margin:1rem 0; text-align:left; border:1px solid rgba(0,0,0,0.06);">
        <div style="font-weight:800; font-size:1.1rem; color:{r['text_color']} !important; margin-bottom:0.3rem;">🎮 대표적인 파트너 포켓몬</div>
        <div style="color:#222222 !important; font-size:1rem; font-weight:600;">{r['pokemon_examples']}</div>
    </div>
    <div style="background:rgba(255,255,255,0.4); border-radius:16px; padding:0.9rem 1.5rem; margin:0.5rem 0; font-size:1rem; color:{r['text_color']} !important; font-weight:700; border:1px solid rgba(0,0,0,0.04);">
        {r['compatible']}
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True) # result-card 종료

    # 6. 하단 멀티 에너그래프 스코어 보드
    st.markdown("""
    <div style="background:rgba(0,0,0,0.4); border-radius:24px; padding:1.5rem; margin:1.5rem 0; backdrop-filter:blur(10px); border: 1px solid rgba(255,255,255,0.1);">
        <div style="font-size:1.2rem; font-weight:800; margin-bottom:1.2rem; text-align:center; color:#fff;">📊 내 속성 멀티 에너그래프</div>
    """, unsafe_allow_html=True)

    type_info = [
        ("water", "🌊 물 타입", "#00b4d8"),
        ("grass", "🌿 풀 타입", "#52b788"),
        ("fire", "🔥 불 타입", "#f97316"),
        ("electric", "⚡ 전기 타입", "#eab308"),
    ]
    for t, label, color in type_info:
        pct = int((st.session_state.scores.get(t, 0) / total_answers) * 100)
        st.markdown(f"""
        <div style="margin:0.6rem 0;">
            <div style="display:flex; justify-content:space-between; margin-bottom:0.3rem; font-size:0.95rem; font-weight:700; color:#fff;">
                <span>{label}</span><span>{pct}%</span>
            </div>
            <div style="background:rgba(255,255,255,0.1); border-radius:20px; height:10px;">
                <div style="width:{pct}%; height:100%; border-radius:20px; background:{color}; box-shadow:0 0 10px {color}; transition:width 1s ease;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # 리스타트 버튼
    _, col_reset, _ = st.columns([1, 2, 1])
    with col_reset:
        st.markdown('<div class="restart-btn" style="text-align:center; margin-top:1rem;">', unsafe_allow_html=True)
        if st.button("🔄 처음부터 다시 하기", key="final_restart_btn"):
            reset()
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
