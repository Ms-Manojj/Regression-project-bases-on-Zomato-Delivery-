import pandas as pd
import plotly.graph_objects as go
import plotly.express as ex
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns


st.set_page_config(layout='wide')


df=pd.read_csv('Clean_data.csv')

st.sidebar.title('EDA \ Model on Zomato data')

option=st.sidebar.selectbox('Select Box',['Overall Analysis','Order_Type','City','Weather_Conditions'])

if option == 'Overall Analysis':
    st.title('Overall Analysis')

    c1,c2,c3,c4 = st.columns(4)
    with c1:
        avg_age=round(df['Delivery_person_Age'].mean(),2)
        st.metric('Avg Age',avg_age)
        st.markdown("<style>div#centered_col04 { text-align: center; }</style>", unsafe_allow_html=True)
    with c2:
        rating=round(df['Delivery_person_Ratings'].mean(),2)
        st.metric('Avg Rating',rating)
        st.markdown("<style>div#centered_col04 { text-align: center; }</style>", unsafe_allow_html=True)
    with c3:
        time_taken=int(round(df['Time_taken'].mean(),0))
        st.metric('Avg Time taken',str(time_taken) + 'Min')
        st.markdown("<style>div#centered_col04 { text-align: center; }</style>", unsafe_allow_html=True)
    
    with c4:
        time_taken=int(round(df['Distance_km'].mean(),0))
        st.metric('Avg Distance',str(time_taken) + 'Km')
        st.markdown("<style>div#centered_col04 { text-align: center; }</style>", unsafe_allow_html=True)


    col1, col2 = st.columns(2)
    with col1:
        mean_time_taken = df['Delivery_person_Age'].mean()
        fig = px.histogram(df, x='Delivery_person_Age', nbins=30, marginal='violin', histnorm='density', opacity=0.6)
        fig.update_layout(
            title='Age Distribution',
            xaxis_title='Delivery Person Age',
            yaxis_title='Density',
            showlegend=False,
            template='plotly_white'
        )

        fig.add_vline(x=mean_time_taken, line_dash="dash", line_color="red", annotation_text="Mean", annotation_position="top left")

        # Show the plot in Streamlit
        st.plotly_chart(fig)

        with col2:
            mean_time_taken = df['Delivery_person_Ratings'].mean()
            fig = px.histogram(df, x='Delivery_person_Ratings', nbins=30, marginal='violin', histnorm='density', opacity=0.6)
            fig.update_layout(
                title='Rating Distribution',
                xaxis_title='Delivery_person_Ratings',
                yaxis_title='Density',
                showlegend=False,
                template='plotly_white'
            )
            fig.add_vline(x=mean_time_taken, line_dash="dash", line_color="red", annotation_text="Mean", annotation_position="top left")
            st.plotly_chart(fig)


    col1, col2 = st.columns(2)
    with col1:
        mean_time_taken = df['Time_taken'].mean()
        fig = px.histogram(df, x='Time_taken', nbins=30, marginal='violin', histnorm='density', opacity=0.6)
        fig.update_layout(
            title='Total Time Taken in overall order',
            xaxis_title='Time taken',
            yaxis_title='Density',
            showlegend=False,
            template='plotly_white'
        )
        fig.add_vline(x=mean_time_taken, line_dash="dash", line_color="red", annotation_text="Mean", annotation_position="top left")

            # Show the plot in Streamlit
        st.plotly_chart(fig)

        with col2:
            mean_distance = df['Distance_km'].mean()
            fig = px.histogram(df, x='Distance_km', nbins=30, marginal='violin', histnorm='density', opacity=0.6)
            fig.update_layout(
                title='Distance_km Distribution',
                xaxis_title='Distance Km',
                yaxis_title='Density',
                showlegend=False,
                template='plotly_white'
                )
            fig.add_vline(x=mean_distance, line_dash="dash", line_color="red", annotation_text="Mean", annotation_position="top left")

            # Show the plot in Streamlit
            st.plotly_chart(fig)





  
elif option=='Order_Type':
    pass
elif option =='City':
    pass
elif option=='Weather_Conditions':
    pass
else:
    pass



option=st.sidebar.selectbox('Select Box',['Model'])
                            