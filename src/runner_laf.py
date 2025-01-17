import numpy as np
from poggers.io import read_fill
from typing import Any
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from pathlib import Path
#from data.data_getter import LocalFileExplorer
from model.preprocessor import DifferencePreprocessor
#from model.detectors import EnsambleDetector
from model.figure_of_merit import Processor

path = "pylaf/laf/src/example_8880"


searcher = Processor()
searcher("/eos/user/t/tatehort/pylaf/laf/src/example_8880", 8880)