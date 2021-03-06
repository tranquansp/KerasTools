#!/usr/bin/env python
# -*- coding: utf-8 -*-

import keras
import KerasTools as KT
import numpy as np

grid_size = 10
nb_frames = 5

model = keras.models.Sequential()
model.add(keras.layers.Permute((2,3,1), input_shape=(nb_frames, grid_size, grid_size)))
model.add(keras.layers.Conv2D(16, (3, 3), activation='relu'))
model.add(keras.layers.Conv2D(32, (3, 3), activation='relu'))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(16, activation='relu', kernel_regularizer=keras.regularizers.l2(0.01)))
model.add(keras.layers.Dense(3, activation='linear'))
model.compile(keras.optimizers.rmsprop(), "logcosh")
model.summary()

game = KT.qlearn.snake.Snake(grid_size, max_turn=64)
agent = KT.qlearn.agent.Agent(model=model, memory_size=65536, nb_frames = nb_frames)

agent.train(game, batch_size=256, epochs=100, train_interval=128,
            epsilon=[0.5, 0.0], epsilon_rate=0.1, gamma=0.8, reset_memory=False)

