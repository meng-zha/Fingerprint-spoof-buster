import numpy as np
import cv2
import torch
import torch.nn as nn
from torch.utils.data import Dataset


class DataPatch(Dataset):
    def __init__(self, fake_path, live_path, list_path, size):
        # 正负样本轮流训练
        self.fake_path = fake_path
        self.live_path = live_path
        self.list_path = list_path
        self.size = size
        self.image_id = [i_id.strip() for i_id in open(list_path)]

    def __len__(self):
        return len(self.image_id)

    def __getitem__(self, index):
        image = cv2.imread(self.image_id[index], cv2.IMREAD_GRAYSCALE)
        image = cv2.resize(image, self.size)
        image = np.expand_dims(image, axis=0)
        label = (self.image_id[index][0] == '1')
        sample={"image":image,"label":label}
        return sample
