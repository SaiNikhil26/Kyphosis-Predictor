import streamlit as st
import pickle
pickle_in = open("kyphosis.pkl","rb")
clf = pickle.load(pickle_in)

def prediction(Age,Number,Start):
    predict=clf.predict([[Age,Number,Start]])
    print(predict)
    return predict

def main():
    st.title("Kyphosis Preidctor")
    Age = st.number_input("Age")
    Number = st.number_input("Number")
    Start = st.number_input("Start")
    result = "";
    if st.button("Predict"):
        result = prediction(Age,Number,Start)
    st.success(result)

if __name__=='__main__':
    main()