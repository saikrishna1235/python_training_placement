
# ============================================================
# DEEP LEARNING MODEL: COMPLETE TRAINING & EVALUATION PIPELINE
# Framework: TensorFlow / Keras
# Tasks supported: Classification and Regression
# ============================================================

# STEP 1: Import required libraries
import os
import random
import joblib
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import (
    StandardScaler, OneHotEncoder, LabelEncoder
)
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.metrics import (
    accuracy_score, classification_report,
    confusion_matrix, mean_absolute_error,
    mean_squared_error, r2_score
)

# Make results more reproducible
SEED = 42
random.seed(SEED)
np.random.seed(SEED)
tf.random.set_seed(SEED)


# ============================================================
# STEP 2: Configure and load your dataset
# ============================================================

DATA_PATH = "data.csv"    # Change to your CSV file
TARGET = "target"         # Change to your target column
TASK = "classification"   # Use "classification" or "regression"

# Read the dataset
df = pd.read_csv(DATA_PATH)

# Remove duplicate rows and rows without a target value
df = df.drop_duplicates()
df = df.dropna(subset=[TARGET])

# Separate input features (X) and target labels (y)
X = df.drop(columns=[TARGET])
y = df[TARGET]

print("Dataset shape:", df.shape)
print("Input features:", X.shape[1])
print(df.head())


# ============================================================
# STEP 3: Split data into training, validation, and test sets
# ============================================================

# Classification uses stratification to preserve class proportions.
# Regression uses a random split.
stratify_values = y if TASK == "classification" else None

# First, reserve 20% for the final test set.
X_train_val, X_test, y_train_val, y_test = train_test_split(
    X, y,
    test_size=0.20,
    random_state=SEED,
    stratify=stratify_values
)

# Next, reserve 20% of the remaining data for validation.
# This gives approximately 64% train, 16% validation, 20% test.
stratify_values = (
    y_train_val if TASK == "classification" else None
)

X_train, X_val, y_train, y_val = train_test_split(
    X_train_val, y_train_val,
    test_size=0.20,
    random_state=SEED,
    stratify=stratify_values
)

print("Training samples:", len(X_train))
print("Validation samples:", len(X_val))
print("Test samples:", len(X_test))


# ============================================================
# STEP 4: Preprocess numerical and categorical features
# ============================================================

# Identify numerical and categorical columns.
numeric_cols = X_train.select_dtypes(
    include=["number"]
).columns.tolist()

categorical_cols = X_train.select_dtypes(
    exclude=["number"]
).columns.tolist()

# Numerical data:
# - Fill missing values with the training-set median.
# - Standardize features to improve neural network training.
numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

# Categorical data:
# - Fill missing values with the most frequent category.
# - Convert categories into numeric one-hot encoded features.
categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

# Apply the appropriate preprocessing to each column type.
preprocessor = ColumnTransformer([
    ("numeric", numeric_pipeline, numeric_cols),
    ("categorical", categorical_pipeline, categorical_cols)
])

# Fit preprocessing ONLY on training data to prevent leakage.
X_train_processed = preprocessor.fit_transform(X_train)
X_val_processed = preprocessor.transform(X_val)
X_test_processed = preprocessor.transform(X_test)

# Convert sparse matrices to dense arrays for Keras.
X_train_processed = np.asarray(
    X_train_processed.toarray()
    if hasattr(X_train_processed, "toarray")
    else X_train_processed,
    dtype=np.float32
)
X_val_processed = np.asarray(
    X_val_processed.toarray()
    if hasattr(X_val_processed, "toarray")
    else X_val_processed,
    dtype=np.float32
)
X_test_processed = np.asarray(
    X_test_processed.toarray()
    if hasattr(X_test_processed, "toarray")
    else X_test_processed,
    dtype=np.float32
)

input_dim = X_train_processed.shape[1]

print("Features after preprocessing:", input_dim)


# ============================================================
# STEP 5: Prepare target labels
# ============================================================

if TASK == "classification":
    # Convert text labels into integer class IDs.
    label_encoder = LabelEncoder()

    y_train_processed = label_encoder.fit_transform(y_train)
    y_val_processed = label_encoder.transform(y_val)
    y_test_processed = label_encoder.transform(y_test)

    num_classes = len(label_encoder.classes_)

    if num_classes < 2:
        raise ValueError("Classification requires at least 2 classes.")

elif TASK == "regression":
    # Regression targets must be numeric.
    y_train_processed = np.asarray(y_train, dtype=np.float32)
    y_val_processed = np.asarray(y_val, dtype=np.float32)
    y_test_processed = np.asarray(y_test, dtype=np.float32)

    if not (
        np.isfinite(y_train_processed).all()
        and np.isfinite(y_val_processed).all()
        and np.isfinite(y_test_processed).all()
    ):
        raise ValueError("Target values must be finite numeric values.")

else:
    raise ValueError(
        "TASK must be 'classification' or 'regression'."
    )


# ============================================================
# STEP 6: Build the deep learning model
# ============================================================

# Define a feed-forward neural network.
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(input_dim,)),

    # Hidden layer 1 learns patterns from the input features.
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dropout(0.30),

    # Hidden layer 2 learns more complex relationships.
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dropout(0.20)
])

# Select output layer, loss function, and metrics by task.
if TASK == "classification":
    # Softmax predicts probabilities for each class.
    model.add(
        tf.keras.layers.Dense(num_classes, activation="softmax")
    )

    loss_function = "sparse_categorical_crossentropy"
    metrics = ["accuracy"]

else:
    # One continuous numeric output for regression.
    model.add(tf.keras.layers.Dense(1))

    loss_function = "mse"
    metrics = ["mae"]

# Configure the optimizer and learning objective.
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss=loss_function,
    metrics=metrics
)

# Display the model architecture.
model.summary()


# ============================================================
# STEP 7: Train the model and validate each epoch
# ============================================================

# Stop training if validation loss stops improving.
early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor="val_loss",
    patience=10,
    restore_best_weights=True
)

# Reduce the learning rate if validation loss plateaus.
reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(
    monitor="val_loss",
    factor=0.5,
    patience=4,
    min_lr=1e-6
)

# Train using training data and monitor validation data.
history = model.fit(
    X_train_processed,
    y_train_processed,
    validation_data=(X_val_processed, y_val_processed),
    epochs=100,
    batch_size=32,
    callbacks=[early_stopping, reduce_lr],
    verbose=1
)


# ============================================================
# STEP 8: Plot training and validation performance
# ============================================================

# Plot loss curves to check for overfitting or underfitting.
plt.figure(figsize=(8, 5))
plt.plot(history.history["loss"], label="Training loss")
plt.plot(history.history["val_loss"], label="Validation loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training vs Validation Loss")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# ============================================================
# STEP 9: Evaluate on the independent test dataset
# ============================================================

# This dataset was not used for fitting or tuning.
test_results = model.evaluate(
    X_test_processed,
    y_test_processed,
    verbose=0,
    return_dict=True
)

print("\nTest evaluation:")
for metric_name, value in test_results.items():
    print(f"{metric_name}: {value:.4f}")

# Generate model predictions.
predictions = model.predict(X_test_processed, verbose=0)


# ============================================================
# STEP 10: Calculate task-specific evaluation metrics
# ============================================================

if TASK == "classification":

    # Convert predicted probabilities into class IDs.
    y_pred = np.argmax(predictions, axis=1)

    # Accuracy measures the fraction of correct predictions.
    print("\nTest Accuracy:",
          accuracy_score(y_test_processed, y_pred))

    # Precision, recall, and F1-score for every class.
    print("\nClassification Report:")
    print(classification_report(
        y_test_processed,
        y_pred,
        labels=np.arange(num_classes),
        target_names=[
            str(c) for c in label_encoder.classes_
        ],
        zero_division=0
    ))

    # Confusion matrix shows correct and incorrect predictions.
    cm = confusion_matrix(
        y_test_processed,
        y_pred,
        labels=np.arange(num_classes)
    )

    print("Confusion Matrix:\n", cm)

    plt.figure(figsize=(6, 5))
    plt.imshow(cm, interpolation="nearest")
    plt.title("Test Confusion Matrix")
    plt.xlabel("Predicted class")
    plt.ylabel("Actual class")
    plt.xticks(range(num_classes), label_encoder.classes_,
               rotation=45, ha="right")
    plt.yticks(range(num_classes), label_encoder.classes_)
    plt.colorbar()
    plt.tight_layout()
    plt.show()

else:
    # Convert model output into one-dimensional predictions.
    y_pred = predictions.reshape(-1)

    # MAE: average absolute prediction error.
    mae = mean_absolute_error(y_test_processed, y_pred)

    # RMSE: square root of average squared prediction error.
    rmse = np.sqrt(
        mean_squared_error(y_test_processed, y_pred)
    )

    # R²: goodness of fit relative to a mean-value baseline.
    r2 = r2_score(y_test_processed, y_pred)

    print("\nTest MAE:", mae)
    print("Test RMSE:", rmse)
    print("Test R²:", r2)


# ============================================================
# STEP 11: Save the model and preprocessing objects
# ============================================================

# Save the neural network in Keras format.
model.save("deep_learning_model.keras")

# Save preprocessing so future inputs use the same transformations.
joblib.dump(preprocessor, "preprocessor.joblib")

# Save the label encoder for classification tasks.
if TASK == "classification":
    joblib.dump(label_encoder, "label_encoder.joblib")

print("\nModel and preprocessing artifacts saved.")


# ============================================================
# STEP 12: Example inference on new data
# ============================================================

# Supply a dictionary containing the original feature columns.
# Replace these example values with real values from your dataset.
#
# new_data = pd.DataFrame([{
#     column_name: example_value
#     for column_name, example_value in ...
# }])
#
# For example, if your dataset has columns "age" and "salary":
# new_data = pd.DataFrame([{"age": 30, "salary": 50000}])
#
# Ensure all required feature columns are present in the same schema.

# Example inference function for reuse with new records.
def predict_new_data(new_data):
    """Predict labels or numeric values from a pandas DataFrame."""
    # Enforce the same feature order as during training.
    new_data = new_data[X_train.columns]

    # Apply the saved preprocessing transformation.
    processed = preprocessor.transform(new_data)

    # Keras accepts dense arrays in this example.
    if hasattr(processed, "toarray"):
        processed = processed.toarray()

    processed = np.asarray(processed, dtype=np.float32)

    # Make predictions.
    output = model.predict(processed, verbose=0)

    if TASK == "classification":
        class_ids = np.argmax(output, axis=1)
        predicted_labels = label_encoder.inverse_transform(class_ids)

        # Return labels and their predicted probabilities.
        return pd.DataFrame({
            "predicted_label": predicted_labels,
            "confidence": np.max(output, axis=1)
        })

    return pd.DataFrame({
        "predicted_value": output.reshape(-1)
    })

# Example usage:
# new_data = pd.DataFrame([{
#     "feature_1": 10,
#     "feature_2": 25
# }])
# print(predict_new_data(new_data))

print("\nPipeline completed successfully.")
