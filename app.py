# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import os
from copy import deepcopy
import pandas as pd
import time
import http.client
import json
import matplotlib.font_manager as font_manager
from matplotlib import rcParams
from scipy.interpolate import pchip_interpolate
import datetime
import matplotlib.pyplot as plt
import matplotlib.image as img
import matplotlib.patheffects as path_effects
import matplotlib
import threading
import numpy as np
from PIL import Image
from os import listdir
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
import math


headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key':"903a0d7149864011a7b81adaa2c060d9"

    }


def run():
    for i in range(40):
        st.write("# Bienvenido a NanoTeam! 👋⚽")

        conn = http.client.HTTPSConnection("v3.football.api-sports.io")
        conn.request("GET", "/fixtures?live=all", headers=headers)
        res = conn.getresponse()
        data = res.read()    
        zz = deepcopy(json.loads(data)) 
    

if __name__ == "__main__":
        st.set_page_config(
        page_title="NT ⚽🔮",
        page_icon="👋",
        layout="wide"
        )
        run()
