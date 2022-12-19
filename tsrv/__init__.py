# -*- coding: utf-8 -*-
import os
from urllib.parse import quote_plus
from flask import Flask


app = Flask(__name__)

from tsrv import views