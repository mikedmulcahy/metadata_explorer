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

import os

def print_volume_contents(volume_path):
  """Prints the contents of a Linux volume using os.walk.

  Args:
    volume_path: The path to the volume.
  """
  try:
    for root, dirs, files in os.walk(volume_path):
      print(f"Directory: {root}")
      for dir in dirs:
        print(f"  Subdirectory: {dir}")
      for file in files:
        print(f"  File: {file}")

  except FileNotFoundError:
    print(f"Error: Volume not found at {volume_path}")

if __name__ == "__main__":
  volume_path = "/secrets/"  # Replace with the actual path
  print_volume_contents(volume_path)
  print("MIKE")



CommonComponents.init_app()

metadata_service = MetadataService(collection_name = 'article-demo')
storage_service = st.session_state[ui_constants.SERVICE_STORAGE]


#@st.dialog("Article Detail", width="large")
#build_list_page()
