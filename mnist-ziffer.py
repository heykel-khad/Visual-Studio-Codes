# Importieren der notwendigen Bibliotheken
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

# Laden des MNIST-Datensatzes
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Normalisieren der Daten (Werte zwischen 0 und 1)
X_train = X_train / 255.0
X_test = X_test / 255.0

# Neuronales Netz aufbauen
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Wandelt 28x28 Bild in flaches Array um
    layers.Dense(128, activation='relu'),  # Erste versteckte Schicht mit 128 Neuronen
    layers.Dense(10, activation='softmax') # Ausgabeschicht für 10 Ziffern
])

# Kompilieren des Modells
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Trainieren des Modells
model.fit(X_train, y_train, epochs=5)

# Modell auf Testdaten bewerten
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f'Testgenauigkeit: {test_acc * 100:.2f}%')

# Vorhersage auf einer Beispielziffer
plt.imshow(X_test[0], cmap='gray')  # Ziffer darstellen
plt.show()

# Vorhersagen auf Testdaten machen
predictions = model.predict(X_test)

# Ausgabe der vorhergesagten Ziffer
print(f'Vorhergesagte Ziffer: {predictions[0].argmax()}')
