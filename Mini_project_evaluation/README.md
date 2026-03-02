(Evaluators)
- YASHWANTH ASHOK
- VISHNU R NAIR
- MANAV MAHESH

  Observations Made:
- Presence of too many rare location categories.
- Unrealistic house entries (e.g., less than 100 sqft).
- Data noise affecting regression performance.

 Suggestions:
- Limit location feature to the top 50 most frequent locations.
- Group less frequent locations into an "Other" category.
- Remove unrealistic square footage values below 100 sqft.
- Improve overall data cleaning before training.

 Outcome After Implementation:
After applying the suggested modifications:
- R² score improved.
- Model accuracy increased.
- Predictions became more stable and realistic.
