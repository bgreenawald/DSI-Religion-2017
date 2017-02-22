#THE FULL SETUP, compacted
model = Sequential(); model.add(Convolution1D(64, 11, border_mode='same', input_shape=(X.shape[1],X.shape[2]))); model.add(BatchNormalization()); model.add(Activation('relu')); model.add(MaxPooling1D(pool_length=3)); model.add(Convolution1D(128, 7, border_mode='same')); model.add(BatchNormalization()); model.add(Activation('relu')); model.add(MaxPooling1D(pool_length=3)); model.add(Convolution1D(192, 3, border_mode='same')); model.add(BatchNormalization()); model.add(Activation('relu')); model.add(MaxPooling1D(pool_length=3)); model.add(Convolution1D(256, 3, border_mode='same')); model.add(BatchNormalization()); model.add(Activation('relu')); model.add(MaxPooling1D(pool_length=3))
model.add(Flatten()); model.add(Dense(4096, init='normal')); model.add(BatchNormalization()); model.add(Activation('relu')); model.add(Dropout(.5)); model.add(Dense(1000, init='normal')); model.add(BatchNormalization()); model.add(Activation('relu')); model.add(Dropout(.25)); model.add(Dense(200, init='normal')); model.add(BatchNormalization()); model.add(Activation('relu'))
#
model.add(Dense(9, activation='softmax')) # for categorical_cross_entropy, below (classification)
#model.add(Dense(1)) # for mse, below (regression)