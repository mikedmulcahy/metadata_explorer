import streamlit as st
import constants


from services.storage_service import StorageService
import ui_constants
from utils import add_logo


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


my_logo = add_logo(logo_path="media/logo.jpeg", width=240, height=240)

logo_row = st.columns(3)
logo_row[1].image(my_logo)
# st.image(my_logo)

if ui_constants.SERVICE_STORAGE not in st.session_state:
    with st.spinner('Getting your experience ready...'):
        # Services initialization
        st.session_state[ui_constants.SERVICE_STORAGE] = StorageService([constants.INPUT_BUCKET, constants.OUTPUT_BUCKET], constants.SERVICE_ACCOUNT_KEY_FILE)

header_row = st.columns([6,1], vertical_alignment="center")
header_row[0].title("Editorial Solaris - A metadata explorer")

# Page definition
st.write("Editorial Solaris, powered by Google's Gemini, leverages its multimodal capabilities to revolutionize digital content management. By seamlessly combining information from audio and video, Gemini generates rich metadata that allows users to effortlessly search, organize, and explore their digital libraries with unprecedented ease and efficiency.  This means you can use the metadata to quickly and easily find the files you're looking for, even if you have a huge collection of audio and video content.")
st.write("All the code can be found in this github rep [https://github.com/pedroccorreia/metadata_explorer/](rhttps://github.com/pedroccorreia/metadata_explorer/)")

