import numpy as np
import random
import json

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

from konlp_utils import bag_of_words, tokenize, stem
from model import NeuralNet

with open('intents.json', 'r') as f:
    intents = json.load(f)

all_words = []
tags = []
xy = []
# intents 파일에서 각 입력(pattern) 문장에 대해 순환 
for intent in intents['intents']:
    tag = intent['tag']
    # 태그를 태그 리스트에 추가 
    tags.append(tag)
    for pattern in intent['patterns']:
        # 각 문장의 단어들에 대해 토큰화 
        w = tokenize(pattern)
        # 토큰화된 단어를 단어 리스트에 추가 
        all_words.extend(w)
        # 단어와 태그 쌍을 xy 리스트에 추가 
        xy.append((w, tag))

# 불용 표현 제거 및 각 단어의 표제어 추출 
ignore_words = ['?', '.', '!']
all_words = [stem(w) for w in all_words if w not in ignore_words]
# 중복 제거 및 정렬 
all_words = sorted(set(all_words))
tags = sorted(set(tags))

print(len(xy), "입력(patterns)")
print(len(tags), "태그(tag):", tags)
print(len(all_words), "표제어(표제어 분류 불가 단어 포함):", all_words)

# 학습용 데이터 생성 
X_train = []
y_train = []
for (pattern_sentence, tag) in xy:
    # X: 입력 문장에 대한 bag of words 
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)
    # y: PyTorch CrossEntropyLoss 계산을 위한 클래스 라벨 
    label = tags.index(tag)
    y_train.append(label)

X_train = np.array(X_train)
y_train = np.array(y_train)

# 하이퍼 파라미터 설정 
num_epochs = 1000
batch_size = 8
learning_rate = 0.001
input_size = len(X_train[0])
hidden_size = 8
output_size = len(tags)
print(input_size, output_size)

# 데이터셋 클래스 선언
class ChatDataset(Dataset):

    def __init__(self):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.n_samples

dataset = ChatDataset()
train_loader = DataLoader(dataset = dataset,
                          batch_size = batch_size,
                          shuffle = True,
                          num_workers = 0)

# GPU 활용 여부 설정 
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# 모델 선언 
model = NeuralNet(input_size, hidden_size, output_size).to(device)

# 손실 및 최적화
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr = learning_rate)

# 모델 학습 
for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype = torch.long).to(device)
        
        # 순전파 
        outputs = model(words)
        loss = criterion(outputs, labels)
        
        # 역전파 및 최적화 
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
    if (epoch+1) % 100 == 0:
        print (f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# 최종 손실 출력 
print(f'final loss: {loss.item():.4f}')

# 모델 저장 
data = {
"model_state": model.state_dict(),
"input_size": input_size,
"hidden_size": hidden_size,
"output_size": output_size,
"all_words": all_words,
"tags": tags
}

FILE = "data.pth"
torch.save(data, FILE)

print(f'학습이 완료되었습니다. 모델은 {FILE} 파일로 저장되었습니다.')
