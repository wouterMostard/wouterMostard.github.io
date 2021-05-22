import torch.nn as nn


class Classifier(nn.Module):
    def __init__(self, input_shape, n_classes, hidden_size):
        super().__init__()
        self.input_shape = input_shape
        self.n_classes = n_classes
        self.hidden_size = hidden_size

        self.mlp = nn.Sequential(
            nn.Linear(self.input_shape, self.hidden_size),
            nn.ReLU(),
            nn.Linear(self.hidden_size, self.n_classes)
        )

    def forward(self, x):
        return self.mlp(x)


