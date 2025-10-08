# 🧠 1-Week Model Quantization + Knowledge Distillation Roadmap

## ✅ Day 1 – Concepts & Foundations
- [ ] Read: [MIT EfficientML – Model Compression Overview](https://efficientml.ai)
- [ ] Watch: *AI Coffee Break – “Quantization Explained”* on YouTube
- [ ] Learn key ideas:
  - [ ] PTQ vs QAT  
  - [ ] Bit precision trade-offs (INT8, FP16, etc.)  
  - [ ] Knowledge Distillation basics (teacher–student concept)

---

## ✅ Day 2 – Post-Training Quantization (PTQ)
- [ ] Follow: [PyTorch PTQ Official Guide](https://pytorch.org/docs/stable/quantization.html#post-training-quantization)
- [ ] Practice:
  - [ ] Quantize pretrained `ResNet18`
  - [ ] Compare FP32 vs INT8 accuracy and inference time
- [ ] Record:
  - [ ] Latency improvement (%)  
  - [ ] Accuracy drop (%)

---

## ✅ Day 3 – Quantization-Aware Training (QAT)
- [ ] Follow: [TensorFlow QAT Tutorial](https://www.tensorflow.org/model_optimization/guide/quantization/training)
- [ ] Practice:
  - [ ] Train a small CNN (MNIST/CIFAR-10) with QAT  
  - [ ] Compare with PTQ model performance
- [ ] Optional:
  - [ ] Try PyTorch FX Graph Mode QAT

---

## ✅ Day 4 – Knowledge Distillation (KD)
- [ ] Read paper: [Distilling the Knowledge in a Neural Network (Hinton, 2015)](https://arxiv.org/abs/1503.02531)
- [ ] Follow: [PyTorch KD Tutorial](https://pytorch.org/tutorials/beginner/knowledge_distillation_tutorial.html)
- [ ] Practice:
  - [ ] Train a smaller “student” CNN from a pretrained “teacher” on CIFAR-10  
  - [ ] Tune temperature and distillation loss weights

---

## ✅ Day 5 – Combine KD + Quantization
- [ ] Concept: KD helps quantized models recover accuracy loss
- [ ] Practice:
  - [ ] Train student with KD  
  - [ ] Apply QAT to the KD student model  
  - [ ] Compare:
    - [ ] FP32 Teacher  
    - [ ] FP32 Student (KD only)  
    - [ ] INT8 Student (KD + QAT)

---

## ✅ Day 6 – Framework Exploration
- [ ] Explore:
  - [ ] [Intel Neural Compressor (INC)](https://github.com/intel/neural-compressor)
  - [ ] [ONNX Runtime Quantization](https://onnxruntime.ai/docs/performance/quantization.html)
- [ ] Practice:
  - [ ] Export PyTorch → ONNX  
  - [ ] Quantize & benchmark on CPU and GPU  
  - [ ] Measure inference time and model size

---

## ✅ Day 7 – Wrap-Up & Evaluation
- [ ] Compare:
  - [ ] Accuracy  
  - [ ] Latency  
  - [ ] Model size
- [ ] Summarize insights:
  - [ ] Best trade-off found  
  - [ ] Challenges faced  
- [ ] (Optional) Publish:
  - [ ] Push quantized KD model to Hugging Face Hub  
  - [ ] Share a short report/notebook

---

💡 **Tip:** Keep a notebook of latency, accuracy, and compression ratio for every experiment.
