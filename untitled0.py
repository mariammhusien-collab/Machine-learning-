# ==== problem 1 ===
import numpy as np

M = np.array([[4, -2, 7, 0],
              [1, 9, 3, -5],
              [8, 6, -1, 2]])

print("Matrix M:\n", M)
print("1. Dimensions:", M.shape) # m x n
print("2. m_1,3 =", M[0, 2]) # الصف الأول العمود الثالث
print(" m_2,4 =", M[1, 3]) # الصف الثاني العمود الرابع
print(" m_3,2 =", M[2, 1]) # الصف الثالث العمود الثاني

# ==== problem 2 ===
import numpy as np

A = np.array([[3, 5], [-1, 4]])
B = np.array([[0, -2], [7, 1]])
C = np.array([[1, 2, 3], [4, 5, 6]])

print("A:\n", A)
print("B:\n", B)
print("C:\n", C)
print("1. A + B =\n", A + B)
print("2. A - B =\n", A - B)

# ==== problem 3 ===
import numpy as np

X = np.array([[2, -1], [3, 0]])
Y = np.array([[1, 4], [-2, 5]])
print("X:\n", X)
print("Y:\n", Y)
print("1. 3X =\n", 3 * X)
print("2. Element-wise X ⊙ Y =\n", X * Y)
print("3. Matrix product X · Y =\n", X @ Y) 

# ==== problem 4 ===
import numpy as np
K = np.array([[5, 2], [3, 4]])
print("K:\n", K)
print("1. K^T =\n", K.T)
print("2. det(K) =", np.linalg.det(K))
print("3. K^-1 =\n", np.linalg.inv(K))

# ==== problem 5 ===
import numpy as np
# 2x + 3y = 13
# 4x - y = 5
A = np.array([[2, 3], [4, -1]])
b = np.array([13, 5])
solution = np.linalg.solve(A, b)
print("A * X = b")
print("A =\n", A)
print("b =", b)
print("Solution: x =", solution[0], ", y =", solution[1])

# ==== problem 6 ===
import numpy as np
data = np.array([120, 150, 130, 180, 150, 200, 110, 160])
print("Data:", data)
print("1. Mean =", np.mean(data))
print("2. Median =", np.median(data))

# ==== problem 7 ===
import numpy as np
data = np.array([2, 4, 6, 8, 10])
print("Data:", data)
print("1. Sample Standard Deviation =", np.std(data, ddof=1))
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
print("2. Q1 =", q1, ", Q3 =", q3)
print(" IQR =", q3 - q1)

# ==== problem 8 ===
import pandas as pd
import numpy as np
df = pd.DataFrame({
    "Area": [1200, np.nan, 1800],
    "Bedrooms": [2, 3, 4],
    "Price": [200000, 250000, 350000]
})
print("Original Data:\n", df)
# 1. Impute missing with mean
df["Area"] = df["Area"].fillna(df["Area"].mean())
print("\nAfter Imputation:\n", df)
# 2. Min-Max Scaling
min_val = df["Area"].min()
max_val = df["Area"].max()
df["Area_scaled"] = (df["Area"] - min_val) / (max_val - min_val)
print("\nAfter Min-Max Scaling:\n", df[["Area", "Area_scaled"]])

# ==== problem 10 ===
def predict_price(age):
    return -2000 * age + 25000

age = 4
predicted = predict_price(age)
actual = 16000
residual = actual - predicted

print("Equation: Price = -2000 * Age + 25000")
print("1. Predicted price for", age, "years old car: $", predicted)
print("2. Actual price: $", actual)
print(" Residual =", residual)
print(" Negative residual means model overestimated by $", abs(residual))











