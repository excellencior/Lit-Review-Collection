How different methods of Model Compression impact the **fairness/bias** of a model?

### Datasets Used
- COMPAS Recidivism Racial Bias Dataset

### Impact Factors
- Type of Compression
- Amount of compression

### Fairness Metrics Used
- Equalized Odds \
  Considers a model to be fair if the subgroups have equal sensitivity (TPR) and specificity (1 - FPR).
- Bias Function \
  ![bias_function](assets/bias_function.png)

