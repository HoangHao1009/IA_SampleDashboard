import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title = 'BOOK RECOMMEDER',
    layout = 'centered'
)

head_page = st.columns([0.3, 0.7])
with head_page[0]:
    st.image('https://insightasia.com/wp-content/uploads/2024/06/insightasia-logo-edited.png')
with head_page[1]:
    st.header(':green[DASHBOARD] :orange[SAMPLE]')
with st.expander(label = 'NAVIGATION'):
            options = option_menu(
                menu_title = 'MENU',
                options = ['MVV Main Dashboard', 'MMV Progress','ACB Dashboard', 'MG Dashboard', 'The Loop Dashboard', 'Muji Dashboard'],
                icons = ['robot','book','wrench'],
                menu_icon = 'window-dock',
                orientation = 'horizontal',
                styles = {
                    'container': {'background-color': 'cornsilk', 'opacity': 0.8},
                    'nav-link': {'text-align': 'center',
                                'font-family': "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif"},
                    "nav-link-selected": {"background-color": "green"}
                })

if options == 'ACB Dashboard':
    st.markdown(
        '<iframe title="Bank_Dashboard_V2" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiZjg5YzdhZjUtZjc4OC00NzhjLWI0MjgtZTYzNDIyZjU3NWRjIiwidCI6IjNjOTM1YzBjLTZmMjktNGYxMC1iMmIxLTExYTMwYmZmNjZlYyIsImMiOjEwfQ%3D%3D" frameborder="0" allowFullScreen="true"></iframe>',
        unsafe_allow_html = True
    )        
elif options == 'MG Dashboard':
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
elif options == 'MMV Progress':
    st.markdown(
        '<iframe title="MMV_FW_UpdateGGDrive" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiNjBlZjBmOTQtYmRlZS00ZTI4LWIyOWItMThhYzE0ZWRjMTkzIiwidCI6IjNjOTM1YzBjLTZmMjktNGYxMC1iMmIxLTExYTMwYmZmNjZlYyIsImMiOjEwfQ%3D%3D" frameborder="0" allowFullScreen="true"></iframe>',
        unsafe_allow_html = True
    )
elif options == 'MVV Main Dashboard':
    st.markdown(
        '<iframe title="MMV_Dashboard" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiNmE2ZDVhMjItZjAyNi00YzYwLTgxYjEtYWZhYzU1ZjgyZTBkIiwidCI6IjNjOTM1YzBjLTZmMjktNGYxMC1iMmIxLTExYTMwYmZmNjZlYyIsImMiOjEwfQ%3D%3D" frameborder="0" allowFullScreen="true"></iframe>',
        unsafe_allow_html = True
    )
