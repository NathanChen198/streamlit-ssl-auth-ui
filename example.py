import streamlit as st
from streamlit_rsa_auth_ui import Encryptor, SigninEvent, SignoutEvent, getEvent, signinForm, signoutForm, changePasswordForm
ss = st.session_state

st.set_page_config(layout='wide')

encryptor = Encryptor.load('rsa', 'key')
with st.sidebar:
    signoutForm(encryptor.publicKeyPem, configs={
        'align': 'right',
        'title': {
            'text': 'Welcome Chen, Nathan',
            'size': 'smaller'
        },
        # 'cancel': {}
    })

signinForm(encryptor.publicKeyPem, configs={
    'type': 'inline',
    'title': {},
    'cancel': {},
    'forgot': {},
    'title': {}
})

changePasswordForm(encryptor.publicKeyPem, configs={
    'type': 'inline',
    'title': {},
    'cancel': {},
})

# def checkAuth(username: str, password: str):
#     return username == 'test' and password == 'New.Prog'

# def login():
#     if 'event' in ss and type(ss.event) is SigninEvent: return True
#     result = signinForm(encryptor.publicKeyPem, default={'remember': True}, configs={
#         'title': {
#             'text': 'Login',
#             'align': 'left'
#         },
#         # 'cancel': {},
#         'username': {
#             # 'label': 'Username',
#             'patterns': [{ 'pattern': '^.*@illumina.com$', 'message': 'Must be illumina email' }],
#             # 'width': 200,
#         },
#         'password': {
#             # 'label': 'Password'
#         },
#         # 'labelSpan': 10,
#         # 'remember': {},
#         # 'forgot': {},
#         # 'size': 'small',
#         # 'maxWidth': 500,
#         'type': 'inline',
#         # 'align': 'center',
#         # 'style': {
#         #     'margin': 'auto',
#         #     # 'maxWidth': 400
#         # }
#     })
#     if result is None: return False
#     if 'result' in ss and ss['result'] == result: return False

#     ss['result'] = result
#     _dict = encryptor.decrypt(result)
#     event = getEvent(_dict)
#     if type(event) is not SigninEvent or not checkAuth(event.username, event.password): return False
#     ss['event'] = event
#     del ss['result']
#     st.rerun()

# def logout():
#     result = signoutForm(encryptor.publicKeyPem, configs={'cancel': {}})
#     if result is None: return False
#     _dict = encryptor.decrypt(result)
#     event = getEvent(_dict)
#     if type(event) is SignoutEvent:
#         del ss['event']
#         return True
#     return False

# if not login(): st.stop()
# if logout(): st.rerun()

# st.title('Streamlit Rsa Auth UI Test')
# st.button('test')