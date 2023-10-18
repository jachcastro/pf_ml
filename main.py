import inicio, usuarios, usuarios2, negocios, negocios2, inversionistas, inversionistas2, acercade
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
        page_title="JL3",
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='JL3 ',
                options=['inicio','usuarios 1','usuarios 2','negocios 1','negocios 2','inversionistas 1','inversionistas 2', 'acerca de'],
                icons=['house-fill','person-circle','person-circle','kanban', 'kanban', 'graph-up-arrow', 'graph-up-arrow', 'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "inicio":
            inicio.app()
        if app == "negocios 1":
            negocios.app()    
        if app == "negocios 2":
            negocios2.app()    
        if app == "usuarios 1":
            usuarios.app()        
        if app == "usuarios 2":
            usuarios2.app()        
        if app == 'inversionistas 1':
            inversionistas.app()
        if app == 'inversionistas 2':
            inversionistas2.app()
        if app == 'acerca de':
            acercade.app()                
    run()            
         