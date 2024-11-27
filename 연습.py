# 필요한 라이브러리 임포트
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score

# 데이터 로드
data_region = pd.read_csv("경찰청_범죄 발생 지역별 통계_20221231.csv", encoding="cp949")
data_location = pd.read_csv("경찰청_범죄 발생 장소별 통계_20231231.csv", encoding="cp949")
data_time = pd.read_csv("경찰청_범죄 발생 시간대 및 요일_20191231.csv", encoding="cp949")

# 데이터 병합
merged_data = pd.merge(data_region, data_location, on=["범죄대분류", "범죄중분류"], how="inner")
merged_full_data = pd.merge(merged_data, data_time, on=["범죄대분류", "범죄중분류"], how="inner")

# 시간대 범주화
time_categories = {
    "0시00분-02시59분": "심야",
    "03시00분-05시59분": "심야",
    "06시00분-08시59분": "오전",
    "09시00분-11시59분": "오전",
    "12시00분-14시59분": "오후",
    "15시00분-17시59분": "오후",
    "18시00분-20시59분": "저녁",
    "21시00분-23시59분": "저녁",
}
for col, category in time_categories.items():
    merged_full_data[category] = merged_full_data.get(category, 0) + merged_full_data[col]
merged_full_data = merged_full_data.drop(columns=list(time_categories.keys()))

# 요일 데이터 인코딩
day_columns = ["일", "월", "화", "수", "목", "금", "토"]
merged_full_data["Weekday"] = merged_full_data[day_columns].idxmax(axis=1)
merged_full_data = merged_full_data.drop(columns=day_columns)

# 타깃 변수 생성
merged_full_data["CrimeOccurred"] = (merged_full_data["심야"] > 100).astype(int)

# 최종 데이터 준비
columns_needed = ["서울", "부산", "대구", "광주", "대전", "울산", "세종", "Weekday", "심야", "오전", "오후", "저녁", "CrimeOccurred"]
final_data = merged_full_data[columns_needed]
final_data = pd.get_dummies(final_data, columns=["Weekday"], drop_first=True)

# 독립 변수(X)와 종속 변수(y) 분리
X_final = final_data.drop(columns=["CrimeOccurred"])
y_final = final_data["CrimeOccurred"]

# 데이터 분할
X_train_final, X_test_final, y_train_final, y_test_final = train_test_split(
    X_final, y_final, test_size=0.2, random_state=42, stratify=y_final
)

# 모델 학습
final_model = RandomForestClassifier(random_state=42, class_weight="balanced")
final_model.fit(X_train_final, y_train_final)

# 모델 평가
y_pred_final = final_model.predict(X_test_final)
y_pred_proba_final = final_model.predict_proba(X_test_final)[:, 1]

accuracy_final = accuracy_score(y_test_final, y_pred_final)
roc_auc_final = roc_auc_score(y_test_final, y_pred_proba_final)
classification_rep_final = classification_report(y_test_final, y_pred_final)

print(f"Accuracy: {accuracy_final:.2f}")
print(f"ROC-AUC Score: {roc_auc_final:.2f}")
print(classification_rep_final)

# 교차 검증
cv_scores = cross_val_score(final_model, X_final, y_final, cv=5, scoring="accuracy")
cv_mean = cv_scores.mean()
cv_std = cv_scores.std()
print(f"Cross-Validation Accuracy: {cv_mean:.2f} ± {cv_std:.2f}")

# 시나리오 테스트 (저녁, 부산, 목요일)
input_data = pd.DataFrame({
    "서울": [0], "부산": [1], "대구": [0], "광주": [0], "대전": [0], "울산": [0], "세종": [0],
    "심야": [0], "오전": [0], "오후": [0], "저녁": [1],
    "Weekday_월": [0], "Weekday_화": [0], "Weekday_수": [0],
    "Weekday_목": [1], "Weekday_금": [0], "Weekday_토": [0]
})
input_data = input_data.reindex(columns=X_final.columns, fill_value=0)
predicted_probability_final = final_model.predict_proba(input_data)[:, 1][0]
print(f"Predicted Probability for scenario: {predicted_probability_final:.2f}")
