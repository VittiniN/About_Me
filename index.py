import streamlit as st

#https://www.//www.webfx.com/tools/emoji-cheat-sheet/



st.set_page_config(page_title="my first python page", page_icon=":cactus:", layout="wide" )

# header 
with st.container():
    st.subheader("Hello my name Is Natalie :cactus:")
    st.image('flowerpic .jpeg', caption="Flower wall in Peru", width=400)
    st.balloons()

    st.title("I am a self-taught software developer :wave:")
    st.write("When I am not coding, I am either reading or playing my nientendo switch. Feel free to connect with  me on linkedin or twitter.")

    st.write("[Linkedin](https://www.linkedin.com/in/natalie-vittini-a60604242/)", "[GitHub >](https://github.com/VittiniN)") 




#what i do 


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
   
    with left_column:
        st.header("what I do")
        st.write("##")
        st.write(" - I am a self-taught software developer :computer:")
        st.write(" - I am a yogi ")
        st.write(" - I run a book club")
        st.write(" - I am a cat mom :cat:")


    with right_column:
        st.header("I love:")
        st.write("##")
        st.write(" - Javascript & React")
        st.write(" - HTML")
        st.write(" - CSS")
        st.write(" - Python")
      

    with st.container():
        st.write("---")
    