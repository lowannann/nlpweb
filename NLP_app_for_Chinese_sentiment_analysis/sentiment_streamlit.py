import streamlit as st
from snownlp import SnowNLP

def main():

    st.title("NLP app for Chinese sentiment analysis")
    st.write("這是一個中文情緒分析app, 請輸入想分析的語句🔎")
    st.image("nlp_cloud.jpeg", width=350)

    menu = ["Text","Sentences"]
    choice = st.sidebar.selectbox("Menu",menu) 

    if choice=="Text":
        st.subheader("Text")
        with st.form(key="nlpForm"):
            raw_text=st.text_area("Enter your text here✏️")
            submit_button=st.form_submit_button(label="Analyze")
        
        col1,col2=st.columns(2)
        if submit_button:
            with col1:
                st.info("sentiment")
                sentiment=SnowNLP(SnowNLP(raw_text).han) #轉簡體
                sentiment_han=sentiment.sentiments
                st.write(sentiment_han)

                #emoji
                if sentiment_han>0:
                    st.markdown("Sentiment:: Positive :smiley: ")
                elif sentiment_han<0:
                    st.markdown("Sentiment:: Negative :angry: ")
                else:
                    st.markdown("Sentiment:: Neutral :neutral: ")



            with col2:
                st.info("category")
                category=SnowNLP(SnowNLP(raw_text).han) #轉簡體
                category_han=list(category.tags)
                st.write(category_han)


    else:
        st.subheader("Sentences")
        with st.form(key="nlpForm"):
            raw_text=st.text_area("Enter your text here✏️ (Traditional / Simplified Chinese)")
            submit_button=st.form_submit_button(label="Analyze")
        
        col1,col2=st.columns(2)
        if submit_button:
            with col1:
                st.info("sentiment")
                sentiment=SnowNLP(SnowNLP(raw_text).han) #轉簡體
                sentiment_han=sentiment.sentences
                for s in sentiment_han:
                    sentiment_slices=SnowNLP(s).sentiments
                    st.write(sentiment_slices)

                #emoji
                    if sentiment_slices>0:
                        st.markdown("Sentiment:: Positive :smiley: ")
                    elif sentiment_slices<0:
                        st.markdown("Sentiment:: Negative :angry: ")
                    else:
                        st.markdown("Sentiment:: Neutral :neutral: ")



            with col2:
                st.info("category")
                category=SnowNLP(SnowNLP(raw_text).han) #轉簡體
                category_han=list(category.tags)
                st.write(category_han)


if __name__=='__main__':
    main()   




