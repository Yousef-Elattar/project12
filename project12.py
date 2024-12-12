
import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff

st.set_page_config(
    layout='wide',
    page_title='Financial Analysis',
    page_icon= '📈'
)
with st.container():
    st.subheader("Financial Analysis")
    st.title("Defacto Store")
    st.write("in this dashboard we will discover some statistics that will help us discover some of the problems we face in the company and ways to solve these problems by making the right decisions from Stockholders to improve the company's sales and thus increase profits.")
df = pd.read_csv("Defacto.csv")
orders = pd.read_csv("orders.csv")
customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")
sales = pd.read_csv("sales.csv")
df_merged = pd.read_csv("df_merged.csv")
df_merged_1 = pd.read_csv("df_merged_1.csv")
df.drop('Unnamed: 0', axis=1, inplace= True)
num= df.describe()
cat= df.describe(include='O')
revenue_state=pd.read_csv("revenue_state.csv")
revenue_gender=pd.read_csv("revenue_gender.csv")
quantity_state=pd.read_csv("quantity_state.csv")
quantity_gender=pd.read_csv("quantity_gender.csv")




tab1,tab2,tab3= st.tabs(['🏠 Home','🧶 Orders','💁‍♂️ Customer'])

with tab1:
    st.markdown('<div class="title"> Defacto Store </div>', unsafe_allow_html=True)

    st.write('')
    
    col1,col2 = st.columns(2)
    
    with col1:
        st.markdown(f'''
            <div class="myMetric">
                <h3>Total Orders</h3>
                <p cl>{len(df_merged)}</p>
            </div>
            
        ''', unsafe_allow_html=True)
        
        st.write(" ")
        
        st.markdown(f'''
            <div class="myMetric">
                <h3>Quantity per piece</h3>
                <p >{df['quantity_sold'].sum()}</p>
            </div>
        ''', unsafe_allow_html=True)
        st.write(" ")
        st.write("##")
        st.subheader('Categorical Describtive Statistics')
        st.dataframe(cat.T)
    with col2:
        st.markdown(f'''
            <div class="myMetric">
                <h3>Total Revenue</h3>
                <p>{df['revenue'].sum()}</p>
            </div>
        ''', unsafe_allow_html=True)
        st.markdown(" ")
        state = df.groupby('state')['revenue'].sum().reset_index().sort_values(by='revenue', ascending=False)
    
        top_state = state[['state']].head(1)
        top_state = top_state.iloc[0]['state']
    
        st.markdown(f'''
            <div class="myMetric">
                <h3>Top State</h3>
                <p>{top_state}</p>
            </div>
        ''', unsafe_allow_html=True)
        st.write(" ")
        st.write("##")
        
        st.subheader('Numerical Describtive Statistics')
        st.dataframe(num.T)
        
        ##-----------------------------##
with tab2:
    st.header("Insghts for our Orders")
    col1, col2, col3 = st.columns([6,0.5,6])
    with col1:
        order_by_month = df_merged.groupby("order_month").agg({
            "order_id" : "count"
        }).reset_index().sort_values(by = "order_month")
        fig1 = px.bar(order_by_month,x="order_month",y = order_by_month.columns[1:],color_discrete_sequence=px.colors.qualitative.Pastel,title="Total Orders by Month")
        fig1.update_layout(
        xaxis_title="Month",
        yaxis_title="Orders",
        title_x=0.5,
        template="presentation"
        )
        st.plotly_chart(fig1,use_container_width=True)
        fig3 = px.histogram(
            df,
            x="MoM_change",
            nbins=10,  # Number of bins
            title="Month-over-Month Change Histogram",
            labels={"MoM Change": "Month-over-Month Change (%)"},
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
    
        fig3.add_vline(
            x=df["MoM_change"].mean(),
            line_dash="dash",
            line_color="red",
            annotation_text="Mean",
            annotation_position="top"),
        fig3.update_layout(
            xaxis_title="Month-over-Month Change (%)",
            yaxis_title="Frequency",
            title_x=0.5,
            template="presentation"
        )
        


    with col3:
        
        order_by_quarter = df_merged.groupby("order_quarter").agg({
            "order_id" : "count"
        }).reset_index().sort_values(by = "order_quarter")
        fig2= px.line (order_by_quarter,x="order_quarter",y= order_by_quarter.columns[1:],color_discrete_sequence=px.colors.qualitative.Pastel,title="Total Orders by Quarter")
        fig2.update_layout(
            xaxis_title="Quarter",
            yaxis_title="Orders",
            title_x=0.5,
            template="presentation",
        )
        
        st.plotly_chart(fig2,use_container_width=True)
        fig3= px.bar (df,x="order_day_name",y= "revenue",color_discrete_sequence=px.colors.qualitative.Pastel,title="Revenue by DayName")
        fig3.update_layout(
            xaxis_title="Day",
            yaxis_title="Revenue",
            title_x=0.5,
            template="presentation"
        )
        st.plotly_chart(fig3,use_container_width=True)

##--------------------------------------------##
with tab3:
    st.header("Our Customers")
    col1, col2, col3 = st.columns([6,0.5,6])
    with col1:
        fig5 = px.bar(
        revenue_state,
        x="state",
        y="revenue",
        title="State with total price",
        color_discrete_sequence=px.colors.qualitative.Pastel
        ,text = "revenue"
    )
        
        fig5.update_layout(
        xaxis_title="State",
        yaxis_title="Revenue",
        title_x=0.5,
        template="presentation"
        )

        st.plotly_chart(fig5,use_container_width=True)

        fig7 = px.line(
            revenue_gender,
            x="gender",
            y="revenue",
            title="Gender with total price",
            color_discrete_sequence=px.colors.qualitative.Pastel,
            text="revenue"
        )
        
        fig7.update_layout(
            xaxis_title="Gender",
            yaxis_title="Revenue",
            title_x=0.5,
            template="presentation"
            
        )
        st.plotly_chart(fig7,use_container_width=True)

    with col3:
        fig8 = px.bar(
           quantity_state,
            y="state",
            x="quantity_sold",
            title="Gender with total quantity",
            color_discrete_sequence=px.colors.qualitative.Pastel,
            text= "quantity_sold"
        )
        
        fig8.update_layout(
            yaxis_title="State",
            xaxis_title="Quantity",
            title_x=0.5,
            template="presentation"
        )
        st.plotly_chart(fig8,use_container_width=True)
        fig9 = px.bar(
           quantity_gender,
            x="gender",
            y="quantity_sold",
            title="Gender with total quantity",
            color_discrete_sequence=px.colors.qualitative.Pastel,
            text= "quantity_sold"
        )
        
        fig9.update_layout(
            xaxis_title="Gender",
            yaxis_title="Quantity",
            title_x=0.5,
            template="presentation"
        )
        st.plotly_chart(fig9,use_container_width=True)
