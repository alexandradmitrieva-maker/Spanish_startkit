import streamlit as st
from streamlit_mic_recorder import mic_recorder
import os

st.set_page_config(page_title="Испанский с Сашей", page_icon="🇪🇸")

st.title("🇪🇸 Твой старт в испанском")
st.write("### Привет! Спасибо, что записались на курс!")

# Список фраз с точными именами файлов, которые ты загружала
phrases = [
    {"es": "Hola! ¿Qué tal?", "ru": "Привет, как дела?", "file": "Que tal.m4a"},
    {"es": "Bien, ¿y tú?", "ru": "Хорошо, а у тебя?", "file": "Bien, y tu.m4a"},
    {"es": "¿Как тебя зовут?", "ru": "Как тебя зовут?", "file": "Como te llamas.m4a"},
    {"es": "Me llamo...", "ru": "Меня зовут...", "file": "Me llamo.m4a"},
    {"es": "Perdona, ¿me traes una caña, por favor?", "ru": "Извини, принесешь пива?", "file": "Perdona, me traes una caña, por favor_.m4a"},
    {"es": "Un café sólo, por favor!", "ru": "Черный кофе, пожалуйста", "file": "Un café solo, por favor.m4a"},
    {"es": "¿Me podrías traer la carta, por favor?", "ru": "Принесешь меню?", "file": "Me podrias traer la carta, por favor_.m4a"},
    {"es": "¿Me cobras, por favor?", "ru": "Посчитай меня, пожалуйста", "file": "Me cobras, por favor.m4a"},
    {"es": "Voy a pagar con tarjeta", "ru": "Я оплачу картой", "file": "Voy a pagar con tarjeta.m4a"},
    {"es": "Voy a pagar en efectivo", "ru": "Я оплачу наличными", "file": "Voy a pagar en efectivo.m4a"},
    {"es": "Cómo se dice en Español…", "ru": "Как сказать по-испански?", "file": "Como se dice en Eapanol.m4a"},
    {"es": "¿Подри́ас говорить медленнее?", "ru": "Можешь говорить медленнее?", "file": "Podrías hablar más despacio, por favor.m4a"},
    {"es": "Perdona, no te entiendo!", "ru": "Извини, я не понимаю", "file": "Perdona, no te entiendo.m4a"},
    {"es": "¿Me podrías помогать?", "ru": "Ты не мог бы мне помочь?", "file": "Me podrías ayudar, por favor.m4a"},
    {"es": "¿Hablas inglés?", "ru": "Ты говоришь по-английски?", "file": "Hablas inglés_.m4a"}
]

for i, item in enumerate(phrases):
    with st.expander(f"{item['es']} — {item['ru']}"):
        # Проверяем, существует ли файл физически
        if os.path.exists(item['file']):
            col1, col2 = st.columns([1, 1])
            with col1:
                st.audio(item['file'])
            with col2:
                mic_recorder(start_prompt="Записать", stop_prompt="Стоп", key=f"rec_{i}")
        else:
            st.warning(f"Файл {item['file']} загружается или не найден. Проверь название на GitHub!")

st.divider()

if st.button("Я прошел все фразы!"):
    st.balloons()
    st.success("Ого! Поздравляю, похоже, первый барьер вы преодолели! 🎉")
    st.write("Теперь ваш испанский — это не просто буквы в учебнике, а ваш собственный голос. На курсе мы превратим эти простые фразы в связную речь! Жду вас 26 мая, будем зажигать!")