import streamlit as st
st.title('이승연의 첫번째 앱!')
st.subheader('오늘 저녁 뭐먹지?')
st.write('하하하! 오늘 석식 고구마튀김...')
st.write('https://www.naver.com/')
st.link_button('네이버 바로가기','https://www.naver.com/')

name=st.text_input('이름을 입력하세요:')
if st.button('환영인사'):
    st.write(name+'님 안녕하세요!')
    st.balloons()
    st.image('https://i.namu.wiki/i/XUmuonckB2a5Q7wVgQn3bvOYgN-CeqEKBTDGXCoQnySsLLb5esdQZdxMmBXOcNxhUtjYJ5VaBH9sk3WHxiMHiQ.webp')

st.success('성공!')
st.warning('경고!')
st.error('오류!')
st.info('안내문')
