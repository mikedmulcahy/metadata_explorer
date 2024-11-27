import streamlit as st
import pandas as pd
from streamlit_extras.grid import grid
from streamlit_extras.tags import tagger_component

import constants
from pages.common.common_components import CommonComponents
from services.metadata_service import MetadataService
from services.storage_service import StorageService

import ui_constants
import utils

CommonComponents.init_app()

metadata_service = MetadataService(collection_name = 'article-demo')
storage_service = st.session_state[ui_constants.SERVICE_STORAGE]


@st.dialog("Article Detail", width="large")



build_list_page()
