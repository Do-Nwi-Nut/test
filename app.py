import streamlit as st

st.set_page_config(
    page_title="포켓몬 속성 심리테스트 ✨",
    page_icon="🌟",
    layout="centered"
)

# Global CSS & animations
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap');

* { font-family: 'Nunito', sans-serif; }

html, body, [class*="css"] {
    background: #1a1a2e;
    color: #fff;
}

.stApp {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    min-height: 100vh;
}

/* Hide streamlit elements */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1rem; }

/* Floating stars background */
@keyframes twinkle {
    0%, 100% { opacity: 0.2; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.3); }
}
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-15px); }
}
@keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}
@keyframes pulse {
    0%, 100% { transform: scale(1); box-shadow: 0 0 20px currentColor; }
    50% { transform: scale(1.05); box-shadow: 0 0 40px currentColor; }
}
@keyframes slideIn {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes shimmer {
    0% { background-position: -200% center; }
    100% { background-position: 200% center; }
}
@keyframes bounce {
    0%, 100% { transform: translateY(0); }
    25% { transform: translateY(-10px); }
    75% { transform: translateY(-5px); }
}
@keyframes waterWave {
    0% { transform: translateX(0) scaleY(1); }
    50% { transform: translateX(-10px) scaleY(1.1); }
    100% { transform: translateX(0) scaleY(1); }
}
@keyframes fireFlicker {
    0%, 100% { transform: scale(1) rotate(-2deg); filter: brightness(1); }
    25% { transform: scale(1.1) rotate(2deg); filter: brightness(1.3); }
    75% { transform: scale(0.95) rotate(-1deg); filter: brightness(0.9); }
}
@keyframes leafSway {
    0%, 100% { transform: rotate(-5deg); }
    50% { transform: rotate(5deg); }
}
@keyframes electricZap {
    0%, 100% { opacity: 1; transform: skewX(0deg); }
    10% { opacity: 0.7; transform: skewX(-3deg); }
    20% { opacity: 1; transform: skewX(3deg); }
    30% { opacity: 0.8; transform: skewX(-2deg); }
    40% { opacity: 1; transform: skewX(0deg); }
}
@keyframes particleFly {
    0% { transform: translate(0, 0) scale(1); opacity: 1; }
    100% { transform: translate(var(--tx), var(--ty)) scale(0); opacity: 0; }
}
@keyframes orbitRing {
    from { transform: rotate(0deg) translateX(60px) rotate(0deg); }
    to { transform: rotate(360deg) translateX(60px) rotate(-360deg); }
}

.hero-section {
    text-align: center;
    padding: 2rem 1rem;
    animation: slideIn 0.8s ease-out;
}
.hero-title {
    font-size: 2.8rem;
    font-weight: 900;
    background: linear-gradient(90deg, #ff6b6b, #ffd700, #4ecdc4, #95e17d, #667eea);
    background-size: 300% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: shimmer 3s linear infinite;
    margin-bottom: 0.5rem;
    line-height: 1.2;
}
.hero-sub {
    font-size: 1.1rem;
    color: #aac4ff;
    margin-bottom: 1.5rem;
}
.pokeball-anim {
    font-size: 4rem;
    display: inline-block;
    animation: bounce 1.5s ease-in-out infinite;
    cursor: pointer;
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

/* Question card */
.q-card {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 24px;
    padding: 2rem;
    margin: 1rem 0;
    backdrop-filter: blur(10px);
    animation: slideIn 0.5s ease-out;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}
.q-number {
    font-size: 0.85rem;
    color: #aac4ff;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}
.q-text {
    font-size: 1.4rem;
    font-weight: 800;
    color: #fff;
    margin-bottom: 1.5rem;
    line-height: 1.4;
}
.q-emoji {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    display: block;
    animation: float 3s ease-in-out infinite;
}

/* Progress bar */
.progress-container {
    background: rgba(255,255,255,0.1);
    border-radius: 20px;
    height: 10px;
    margin: 1rem 0;
    overflow: hidden;
}
.progress-fill {
    height: 100%;
    border-radius: 20px;
    background: linear-gradient(90deg, #667eea, #764ba2);
    transition: width 0.5s ease;
    box-shadow: 0 0 10px rgba(102,126,234,0.7);
}

/* Option buttons */
.stButton > button {
    width: 100%;
    background: rgba(255,255,255,0.08) !important;
    border: 2px solid rgba(255,255,255,0.2) !important;
    border-radius: 16px !important;
    color: #fff !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 1rem !important;
    font-weight: 700 !important;
    padding: 0.8rem 1.2rem !important;
    transition: all 0.3s ease !important;
    text-align: left !important;
    margin-bottom: 0.5rem !important;
    backdrop-filter: blur(5px) !important;
}
.stButton > button:hover {
    background: rgba(255,255,255,0.2) !important;
    border-color: rgba(255,255,255,0.5) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3) !important;
}

/* Result pages */
.result-water {
    background: linear-gradient(135deg, #0077b6, #00b4d8, #90e0ef, #caf0f8) !important;
}
.result-grass {
    background: linear-gradient(135deg, #1b4332, #2d6a4f, #52b788, #95d5b2) !important;
}
.result-fire {
    background: linear-gradient(135deg, #7f1d1d, #dc2626, #f97316, #fbbf24) !important;
}
.result-electric {
    background: linear-gradient(135deg, #713f12, #ca8a04, #eab308, #fef08a) !important;
}

.result-card {
    border-radius: 32px;
    padding: 3rem 2rem;
    text-align: center;
    animation: slideIn 0.8s ease-out;
    position: relative;
    overflow: hidden;
}
.result-title {
    font-size: 3rem;
    font-weight: 900;
    color: #fff;
    text-shadow: 0 2px 20px rgba(0,0,0,0.3);
    margin-bottom: 0.5rem;
}
.result-subtitle {
    font-size: 1.3rem;
    color: rgba(255,255,255,0.9);
    margin-bottom: 1rem;
    font-weight: 700;
}
.result-emoji-big {
    font-size: 5rem;
    display: block;
    margin: 1rem 0;
}
.trait-list {
    text-align: left;
    margin: 1.5rem 0;
    padding: 0;
    list-style: none;
}
.trait-list li {
    padding: 0.5rem 0;
    font-size: 1.05rem;
    color: rgba(255,255,255,0.95);
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

/* Water animations */
@keyframes waveBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.water-bubble {
    display: inline-block;
    animation: float var(--dur) ease-in-out infinite var(--delay);
}
.fire-flicker {
    display: inline-block;
    animation: fireFlicker 0.8s ease-in-out infinite;
}
.leaf-sway {
    display: inline-block;
    animation: leafSway 2s ease-in-out infinite;
}
.electric-zap {
    display: inline-block;
    animation: electricZap 1.5s ease-in-out infinite;
}

/* Decorative circles on result card */
.deco-circle {
    position: absolute;
    border-radius: 50%;
    opacity: 0.15;
    animation: spin var(--dur) linear infinite;
}

.restart-btn > button {
    background: rgba(255,255,255,0.25) !important;
    border: 2px solid rgba(255,255,255,0.6) !important;
    border-radius: 50px !important;
    font-size: 1.1rem !important;
    padding: 0.8rem 2.5rem !important;
}
.restart-btn > button:hover {
    background: rgba(255,255,255,0.4) !important;
}

/* Pokemon silhouette */
.pokemon-silhouette {
    font-size: 6rem;
    filter: drop-shadow(0 0 20px rgba(255,255,255,0.5));
    display: inline-block;
}
.water-pokemon { animation: waterWave 2s ease-in-out infinite; }
.fire-pokemon { animation: fireFlicker 0.8s ease-in-out infinite; }
.grass-pokemon { animation: leafSway 2s ease-in-out infinite; }
.electric-pokemon { animation: electricZap 1.5s ease-in-out infinite; }

/* Particle effects */
.particles-container {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    pointer-events: none;
    overflow: hidden;
}
.particle {
    position: absolute;
    border-radius: 50%;
    animation: particleFly 3s ease-out infinite var(--delay);
}
</style>
""", unsafe_allow_html=True)

# Floating stars
stars_html = '<div class="stars-container">'
import random
random.seed(42)
star_chars = ["★", "✦", "✧", "⊹", "✩", "⋆"]
for i in range(25):
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    size = random.uniform(0.7, 1.5)
    dur = random.uniform(2, 5)
    delay = random.uniform(0, 3)
    char = random.choice(star_chars)
    stars_html += f'<div class="star" style="left:{x}%;top:{y}%;font-size:{size}rem;--dur:{dur}s;--delay:{delay}s;">{char}</div>'
stars_html += '</div>'
st.markdown(stars_html, unsafe_allow_html=True)

# Questions
questions = [
    {
        "emoji": "🌅",
        "text": "주말 오전, 나는 보통...",
        "options": [
            ("☕ 조용히 커피 한잔 하며 책을 읽어요", "water"),
            ("🌿 가벼운 산책이나 피크닉을 즐겨요", "grass"),
            ("🎉 친구들과 신나는 약속을 잡아요", "fire"),
            ("💡 새로운 프로젝트 아이디어를 구상해요", "electric"),
        ]
    },
    {
        "emoji": "💭",
        "text": "친구가 고민을 털어놓을 때, 나는...",
        "options": [
            ("🤗 말없이 옆에서 들어주며 공감해줘요", "water"),
            ("🌱 천천히 해결책을 함께 찾아줘요", "grass"),
            ("🔥 열정적으로 조언하고 함께 행동해요", "fire"),
            ("⚡ 빠르게 핵심을 파악하고 해결책을 제시해요", "electric"),
        ]
    },
    {
        "emoji": "🎨",
        "text": "나에게 가장 잘 어울리는 색깔은?",
        "options": [
            ("💙 깊고 차분한 블루 계열이요", "water"),
            ("💚 싱그럽고 자연스러운 그린 계열이요", "grass"),
            ("❤️ 강렬하고 열정적인 레드/오렌지요", "fire"),
            ("💛 밝고 생기넘치는 옐로우 계열이요", "electric"),
        ]
    },
    {
        "emoji": "🏖️",
        "text": "이상적인 여행지는?",
        "options": [
            ("🌊 파도 소리 들리는 조용한 해변", "water"),
            ("🏕️ 공기 맑은 숲 속 캠핑장", "grass"),
            ("🗺️ 활기찬 도시, 새로운 문화 탐험", "fire"),
            ("🌃 네온사인 반짝이는 야경 도시", "electric"),
        ]
    },
    {
        "emoji": "😤",
        "text": "스트레스를 받을 때 나는...",
        "options": [
            ("🛁 목욕이나 명상으로 마음을 비워요", "water"),
            ("🌿 자연 속에서 혼자만의 시간을 가져요", "grass"),
            ("🏃 운동하거나 친구를 만나 발산해요", "fire"),
            ("🎮 게임이나 문제 풀기로 집중해요", "electric"),
        ]
    },
    {
        "emoji": "🍽️",
        "text": "내가 좋아하는 음식 스타일은?",
        "options": [
            ("🍣 신선하고 담백한 해산물 요리", "water"),
            ("🥗 건강하고 자연적인 샐러드/채소", "grass"),
            ("🌶️ 맵고 강렬한 풍미의 요리", "fire"),
            ("⚡ 빠르게 먹을 수 있는 간편식", "electric"),
        ]
    },
    {
        "emoji": "🌙",
        "text": "밤에 잠들기 전 나는...",
        "options": [
            ("📖 잔잔한 음악 들으며 독서해요", "water"),
            ("🌿 내일 할 일을 차분하게 계획해요", "grass"),
            ("📱 SNS나 유튜브를 신나게 봐요", "fire"),
            ("💡 번뜩이는 아이디어를 메모해요", "electric"),
        ]
    },
    {
        "emoji": "🦁",
        "text": "나의 가장 큰 강점은?",
        "options": [
            ("💙 깊은 공감 능력과 감수성", "water"),
            ("💚 꾸준함과 안정감", "grass"),
            ("❤️ 뜨거운 열정과 추진력", "fire"),
            ("💛 빠른 두뇌와 호기심", "electric"),
        ]
    },
    {
        "emoji": "🎵",
        "text": "내가 자주 듣는 음악 장르는?",
        "options": [
            ("🎶 잔잔한 Lo-fi나 재즈", "water"),
            ("🌿 어쿠스틱이나 인디 팝", "grass"),
            ("🔥 신나는 팝, 힙합, EDM", "fire"),
            ("⚡ 일렉트로닉이나 실험적 음악", "electric"),
        ]
    },
    {
        "emoji": "🌟",
        "text": "나에게 가장 중요한 가치는?",
        "options": [
            ("💙 마음의 평화와 진정한 연결", "water"),
            ("💚 자연과 조화, 지속 가능한 삶", "grass"),
            ("❤️ 도전과 열정, 변화를 만드는 삶", "fire"),
            ("💛 지식과 혁신, 세상을 놀라게 하는 삶", "electric"),
        ]
    },
]

results = {
    "water": {
        "name": "물 타입 🌊",
        "subtitle": "깊고 투명한 바다처럼",
        "color_class": "result-water",
        "bg_color": "linear-gradient(135deg, #0077b6, #00b4d8, #90e0ef)",
        "text_color": "#ffffff",
        "pokemon": ["🐬", "💧", "🐋", "🦈", "🐙"],
        "main_pokemon": "🐳",
        "pokemon_class": "water-pokemon",
        "traits": [
            "💙 깊은 공감 능력을 가진 따뜻한 사람이에요",
            "🌊 감수성이 풍부하고 섬세한 감정의 소유자",
            "💎 신뢰할 수 있고 진실된 관계를 소중히 여겨요",
            "🔮 직관이 뛰어나고 상황을 잘 파악해요",
            "💙 조용하지만 강인한 내면의 힘이 있어요",
        ],
        "compatible": "풀 타입과 잘 맞아요 🌿",
        "pokemon_examples": "잠만보, 갸라도스, 물범이",
        "particles": "💧🌊💙🫧",
        "anim_class": "water-bubble",
        "particle_color": "#00b4d8",
    },
    "grass": {
        "name": "풀 타입 🌿",
        "subtitle": "싱그러운 자연처럼",
        "color_class": "result-grass",
        "bg_color": "linear-gradient(135deg, #1b4332, #2d6a4f, #52b788, #95d5b2)",
        "text_color": "#ffffff",
        "pokemon": ["🌱", "🍃", "🌸", "🌻", "🍀"],
        "main_pokemon": "🌿",
        "pokemon_class": "grass-pokemon",
        "traits": [
            "🌿 차분하고 꾸준한 성격의 소유자예요",
            "🌸 자연과 환경을 사랑하는 마음이 커요",
            "💚 모두를 포용하는 넉넉한 마음을 가졌어요",
            "🍃 인내심이 강하고 성실하게 목표를 이뤄요",
            "🌱 주변 사람들에게 힘이 되어주는 존재예요",
        ],
        "compatible": "물 타입과 잘 맞아요 💙",
        "pokemon_examples": "이상해씨, 치코리타, 나뭇짱",
        "particles": "🌿🍃🌱💚",
        "anim_class": "leaf-sway",
        "particle_color": "#52b788",
    },
    "fire": {
        "name": "불 타입 🔥",
        "subtitle": "뜨겁게 타오르는 불꽃처럼",
        "color_class": "result-fire",
        "bg_color": "linear-gradient(135deg, #7f1d1d, #dc2626, #f97316, #fbbf24)",
        "text_color": "#ffffff",
        "pokemon": ["🔥", "⚡", "💥", "🌟", "✨"],
        "main_pokemon": "🔥",
        "pokemon_class": "fire-pokemon",
        "traits": [
            "🔥 넘치는 열정과 에너지를 가졌어요",
            "💪 어떤 도전도 두려워하지 않는 용기의 소유자",
            "❤️ 리더십이 강하고 사람들을 이끄는 힘이 있어요",
            "🌟 주변 사람들에게 활력과 긍정을 전파해요",
            "🏆 목표를 향해 끝없이 돌진하는 불굴의 의지",
        ],
        "compatible": "전기 타입과 잘 맞아요 ⚡",
        "pokemon_examples": "파이리, 마그마, 부스터",
        "particles": "🔥💥✨❤️",
        "anim_class": "fire-flicker",
        "particle_color": "#f97316",
    },
    "electric": {
        "name": "전기 타입 ⚡",
        "subtitle": "번개처럼 빠르고 밝게",
        "color_class": "result-electric",
        "bg_color": "linear-gradient(135deg, #713f12, #ca8a04, #eab308, #fef08a)",
        "text_color": "#1a1a00",
        "pokemon": ["⚡", "💡", "✨", "🌟", "💛"],
        "main_pokemon": "⚡",
        "pokemon_class": "electric-pokemon",
        "traits": [
            "⚡ 빠른 두뇌 회전으로 문제를 척척 해결해요",
            "💡 창의적인 아이디어가 끊임없이 샘솟아요",
            "🌟 밝은 에너지로 주변을 환하게 밝혀줘요",
            "🔬 호기심이 넘치고 새로운 것을 배우는 걸 좋아해요",
            "💛 유머 감각이 넘치고 분위기를 띄워줘요",
        ],
        "compatible": "불 타입과 잘 맞아요 🔥",
        "pokemon_examples": "피카츄, 썬더, 에레키블",
        "particles": "⚡💡✨💛",
        "anim_class": "electric-zap",
        "particle_color": "#eab308",
    }
}

# Session state
if 'page' not in st.session_state:
    st.session_state.page = 'intro'
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
if 'scores' not in st.session_state:
    st.session_state.scores = {"water": 0, "grass": 0, "fire": 0, "electric": 0}
if 'answers' not in st.session_state:
    st.session_state.answers = []

def reset():
    st.session_state.page = 'intro'
    st.session_state.current_q = 0
    st.session_state.scores = {"water": 0, "grass": 0, "fire": 0, "electric": 0}
    st.session_state.answers = []

# ---- INTRO PAGE ----
if st.session_state.page == 'intro':
    st.markdown("""
    <div class="hero-section">
        <div class="pokeball-anim">🔮</div>
        <h1 class="hero-title">포켓몬 속성<br>심리테스트</h1>
        <p class="hero-sub">당신은 어떤 타입의 트레이너인가요?<br>10가지 질문으로 나의 속성을 알아보세요! ✨</p>
    </div>
    """, unsafe_allow_html=True)

    # Type preview cards
    st.markdown("""
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1.5rem 0;">
        <div style="background:linear-gradient(135deg,#0077b6,#00b4d8);border-radius:20px;padding:1.2rem;text-align:center;animation:float 3s ease-in-out infinite;">
            <div style="font-size:2rem;" class="water-bubble">🌊</div>
            <div style="color:#fff;font-weight:800;font-size:1.1rem;">물 타입</div>
            <div style="color:rgba(255,255,255,0.8);font-size:0.85rem;">깊고 감성적인</div>
        </div>
        <div style="background:linear-gradient(135deg,#2d6a4f,#52b788);border-radius:20px;padding:1.2rem;text-align:center;animation:float 3s ease-in-out infinite 0.5s;">
            <div style="font-size:2rem;" class="leaf-sway">🌿</div>
            <div style="color:#fff;font-weight:800;font-size:1.1rem;">풀 타입</div>
            <div style="color:rgba(255,255,255,0.8);font-size:0.85rem;">차분하고 꾸준한</div>
        </div>
        <div style="background:linear-gradient(135deg,#dc2626,#f97316);border-radius:20px;padding:1.2rem;text-align:center;animation:float 3s ease-in-out infinite 1s;">
            <div style="font-size:2rem;" class="fire-flicker">🔥</div>
            <div style="color:#fff;font-weight:800;font-size:1.1rem;">불 타입</div>
            <div style="color:rgba(255,255,255,0.8);font-size:0.85rem;">열정 넘치는</div>
        </div>
        <div style="background:linear-gradient(135deg,#ca8a04,#eab308);border-radius:20px;padding:1.2rem;text-align:center;animation:float 3s ease-in-out infinite 1.5s;">
            <div style="font-size:2rem;" class="electric-zap">⚡</div>
            <div style="color:#fff;font-weight:800;font-size:1.1rem;">전기 타입</div>
            <div style="color:rgba(255,255,255,0.8);font-size:0.85rem;">빠르고 창의적인</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✨ 테스트 시작하기!", key="start"):
            st.session_state.page = 'quiz'
            st.rerun()

# ---- QUIZ PAGE ----
elif st.session_state.page == 'quiz':
    q_idx = st.session_state.current_q
    q = questions[q_idx]
    total = len(questions)
    progress_pct = int((q_idx / total) * 100)

    st.markdown(f"""
    <div style="margin:0.5rem 0;">
        <div style="display:flex;justify-content:space-between;color:#aac4ff;font-weight:700;font-size:0.9rem;margin-bottom:0.3rem;">
            <span>질문 {q_idx+1} / {total}</span>
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

    for opt_text, opt_type in q['options']:
        if st.button(opt_text, key=f"opt_{q_idx}_{opt_type}"):
            st.session_state.scores[opt_type] += 1
            st.session_state.answers.append(opt_type)
            if q_idx + 1 < total:
                st.session_state.current_q += 1
                st.rerun()
            else:
                st.session_state.page = 'result'
                st.rerun()

# ---- RESULT PAGE ----
elif st.session_state.page == 'result':
    winner = max(st.session_state.scores, key=st.session_state.scores.get)
    r = results[winner]

    # Animated particles for result
    particles_html = f"""
    <style>
    .stApp {{
        background: {r['bg_color']} !important;
        background-size: 400% 400% !important;
        animation: waveBG 5s ease infinite !important;
    }}
    </style>
    """
    st.markdown(particles_html, unsafe_allow_html=True)

    # Floating decorative emojis
    deco_emojis = r['particles']
    deco_html = '<div style="position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;overflow:hidden;z-index:0;">'
    import random as rnd
    for i in range(15):
        emoji = deco_emojis[i % len(deco_emojis)]
        x = rnd.randint(0, 100)
        y = rnd.randint(0, 100)
        size = rnd.uniform(1.2, 2.5)
        dur = rnd.uniform(2, 5)
        delay = rnd.uniform(0, 3)
        deco_html += f'<div style="position:absolute;left:{x}%;top:{y}%;font-size:{size}rem;opacity:0.3;animation:float {dur}s ease-in-out infinite {delay}s;">{emoji}</div>'
    deco_html += '</div>'
    st.markdown(deco_html, unsafe_allow_html=True)

    # Score bar
    total_answers = sum(st.session_state.scores.values())
    score_pct = int((st.session_state.scores[winner] / total_answers) * 100)

    # Main pokemon animation class
    main_anim = r['anim_class']

    st.markdown(f"""
    <div class="result-card {r['color_class']}" style="background:{r['bg_color']};">
        <div style="font-size:4.5rem;display:inline-block;" class="{main_anim}">{r['main_pokemon']}</div>
        <div style="font-size:0.9rem;letter-spacing:3px;font-weight:800;color:rgba(255,255,255,0.8);text-transform:uppercase;margin:0.5rem 0;">당신의 속성은</div>
        <div class="result-title">{r['name']}</div>
        <div class="result-subtitle">{r['subtitle']}</div>
        
        <div style="background:rgba(255,255,255,0.2);border-radius:50px;padding:0.8rem 1.5rem;margin:1rem 0;font-size:1rem;font-weight:700;color:rgba(255,255,255,0.95);">
            {r['name']} 성향 {score_pct}%
        </div>
        
        <ul class="trait-list">
    """, unsafe_allow_html=True)

    traits_html = ""
    for trait in r['traits']:
        traits_html += f'<li>{trait}</li>'

    st.markdown(traits_html + f"""
        </ul>
        
        <div style="background:rgba(255,255,255,0.2);border-radius:16px;padding:1rem 1.5rem;margin:1rem 0;text-align:left;">
            <div style="font-weight:800;font-size:1rem;color:rgba(255,255,255,0.95);margin-bottom:0.3rem;">🎮 나의 포켓몬 파트너</div>
            <div style="color:rgba(255,255,255,0.9);font-size:0.95rem;">{r['pokemon_examples']}</div>
        </div>
        
        <div style="background:rgba(255,255,255,0.15);border-radius:16px;padding:0.8rem 1.5rem;margin:0.5rem 0;font-size:0.95rem;color:rgba(255,255,255,0.9);font-weight:700;">
            💕 {r['compatible']}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Score breakdown
    st.markdown("""
    <div style="background:rgba(0,0,0,0.2);border-radius:20px;padding:1.5rem;margin:1rem 0;backdrop-filter:blur(10px);">
        <div style="font-size:1.1rem;font-weight:800;margin-bottom:1rem;text-align:center;">📊 속성별 점수</div>
    """, unsafe_allow_html=True)

    type_info = [
        ("water", "🌊 물", "#00b4d8"),
        ("grass", "🌿 풀", "#52b788"),
        ("fire", "🔥 불", "#f97316"),
        ("electric", "⚡ 전기", "#eab308"),
    ]
    for t, label, color in type_info:
        pct = int((st.session_state.scores[t] / total_answers) * 100)
        st.markdown(f"""
        <div style="margin:0.5rem 0;">
            <div style="display:flex;justify-content:space-between;margin-bottom:0.3rem;font-size:0.9rem;font-weight:700;">
                <span>{label}</span><span>{pct}%</span>
            </div>
            <div style="background:rgba(255,255,255,0.1);border-radius:20px;height:8px;">
                <div style="width:{pct}%;height:100%;border-radius:20px;background:{color};box-shadow:0 0 10px {color};transition:width 1s ease;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="restart-btn">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄 다시 테스트하기", key="restart"):
            reset()
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
