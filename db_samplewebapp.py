import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title = 'BOOK RECOMMEDER',
    layout = 'centered'
)

head_page = st.columns([0.3, 0.7])
with head_page[0]:
    st.image('https://insightasia.com/wp-content/uploads/2019/05/logo.png')
with head_page[1]:
    st.header(':green[DASHBOARD] :orange[SAMPLE]')
with st.expander(label = 'NAVIGATION'):
            options = option_menu(
                menu_title = 'MENU',
                options = ['MG Dashboard', 'The Loop Dashboard', 'Muji Dashboard'],
                icons = ['robot','book','wrench'],
                menu_icon = 'window-dock',
                orientation = 'horizontal',
                styles = {
                    'container': {'background-color': 'cornsilk', 'opacity': 0.8},
                    'nav-link': {'text-align': 'center',
                                'font-family': "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif"},
                    "nav-link-selected": {"background-color": "green"}
                })
                
if options == 'MG Dashboard':
    st.markdown(
        '<iframe title="mg_db2" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiOTFjMGVhYzUtZWNhYi00NzVlLTljMTctMzQxYWQwY2FmNDRjIiwidCI6IjNjOTM1YzBjLTZmMjktNGYxMC1iMmIxLTExYTMwYmZmNjZlYyIsImMiOjEwfQ%3D%3D" frameborder="0" allowFullScreen="true"></iframe>',
        unsafe_allow_html = True
    )
elif options == 'The Loop Dashboard':
    st.markdown(
        '<iframe title="db_theloop" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiMDM0ZjU4ZDItNzg3NS00ODY5LWEzOTktNDVlYTliMjIwMWYyIiwidCI6IjNjOTM1YzBjLTZmMjktNGYxMC1iMmIxLTExYTMwYmZmNjZlYyIsImMiOjEwfQ%3D%3D" frameborder="0" allowFullScreen="true"></iframe>',
        unsafe_allow_html = True
    )
elif options == 'Muji Dashboard':
    st.markdown(
        '<iframe title="MUJI x IA_CSS Dashboard_202404" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiNzVlYjc2NjItNDE4YS00OGZiLTk0NWQtOGZhMTUzZTg0NTZlIiwidCI6IjNjOTM1YzBjLTZmMjktNGYxMC1iMmIxLTExYTMwYmZmNjZlYyIsImMiOjEwfQ%3D%3D" frameborder="0" allowFullScreen="true"></iframe>',
        unsafe_allow_html = True
    )