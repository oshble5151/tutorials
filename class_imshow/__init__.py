import numpy as np
from .imshow_for import *
np.ma.masked_array.imshow=np.ma.core.MaskedArray.imshow = imshow
