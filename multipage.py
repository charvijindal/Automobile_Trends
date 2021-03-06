import streamlit as st

# To manage multiple pages 
class MultiPage: 

    def __init__(self) -> None:
        self.pages = []
    
    def add_page(self, title, func) -> None: 
        #add pages to the app

        self.pages.append(
            {
                "title": title, 
                "function": func
            }
        )

    def run(self):
        # Drodown to select the page to run  
        page = st.sidebar.selectbox(
            'App Navigation', 
            self.pages, 
            format_func=lambda page: page['title']
        )

        # run the app function 
        page['function']()