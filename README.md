# House Price Prediction Model

This project is a machine learning pipeline that predicts house prices based on specific input features such as size, number of bedrooms, and number of bathrooms. The application uses a Flask API to serve the predictions.

## **How It Works**

### **1. Data Preprocessing**
- The dataset (e.g., `housing.csv`) contains historical data, including:
  - Size of the house (e.g., square footage)
  - Number of bedrooms
  - Number of bathrooms
  - House price (target variable)
- Preprocessing steps:
  - Remove missing values.
  - Split the dataset into training and testing sets.

### **2. Model Training**
- **Algorithm**: Linear Regression
  - The model learns the relationship between the input features (e.g., size, rooms) and the target variable (house price).
- **Output**: A trained model (`trained_model.pkl`) saved for deployment.

### **3. Model Prediction**
- The trained model takes new input data, such as:
  ```json
  {
    "features": [1200, 3, 2]
  }


# CSV vs Excel for Machine Learning Training

When preparing data for training machine learning models, choosing the right file format is important. Below is a comparison of **CSV (Comma-Separated Values)** and **Excel (XLSX)** formats to help you decide which is better for your workflow.

---

## **Why CSV is Better for Machine Learning**

### **1. Lightweight and Efficient**
- CSV files are plain text, making them much smaller in size compared to Excel files.
- They are faster to read, write, and process, which is critical for large datasets.

### **2. Universal Compatibility**
- CSV files are supported by nearly all programming libraries, such as:
  - **Python**: Libraries like `pandas`, `numpy`, `Dask`, etc.
  - **Machine Learning Frameworks**: TensorFlow, PyTorch, Scikit-learn.
- CSVs are universally compatible with tools and workflows across various platforms.

### **3. No Overhead**
- Unlike Excel, CSV files store only raw data without:
  - Styling
  - Charts
  - Embedded formulas
- This ensures faster processing and avoids errors caused by additional formatting.

### **4. Ease of Version Control**
- CSV files work better with version control systems like Git because:
  - They are plain text files.
  - They allow for line-by-line diffs to track changes over time.

### **5. Scalability**
- CSV files are easier to process in chunks for large datasets using tools like:
  - **Dask**
  - **PySpark**
  - **SQL engines**
- Excel files may encounter performance issues or require conversion for similar workflows.

---

## **When to Use Excel**

Although CSV is usually the better choice, there are some scenarios where Excel might be preferable:

### **1. Manual Data Entry**
- Excel provides a user-friendly interface for manually entering or editing data.

### **2. Embedded Metadata**
- Excel files can store additional metadata, formulas, and multiple sheets, which can be useful during data exploration.

### **3. Collaborative Data Editing**
- Excel allows for easy collaboration, especially among non-technical users.

### **4. Pre-Existing Data in Excel Format**
- If your dataset is already in Excel format, it might save time to work with it directly during the initial stages.

---

## **Best Practices**
- **If using Excel**, convert it to CSV during preprocessing:
  - Python example:
    ```python
    import pandas as pd
    df = pd.read_excel("data/housing.xlsx")
    df.to_csv("data/housing.csv", index=False)
    ```
- Always validate the data after conversion to ensure no data loss or formatting errors.

---

## **Summary**
| Feature                | CSV                          | Excel (XLSX)                  |
|------------------------|------------------------------|--------------------------------|
| **File Size**          | Smaller, plain text          | Larger, includes formatting   |
| **Speed**              | Faster to process            | Slower due to overhead        |
| **Compatibility**      | Universally supported        | Requires specific software    |
| **Version Control**    | Easy with Git                | Difficult to diff             |
| **Scalability**        | Handles large datasets well  | Limited scalability           |
| **Usability**          | Plain text, less user-friendly | Rich UI, better for manual editing |

For most machine learning workflows, **CSV is the recommended format** due to its simplicity, efficiency, and compatibility. Use Excel only if the scenario requires features like metadata, collaboration, or manual data entry.

---
# Techniques to Save Resources on a Powerful VM

## 1. Use Containers for Isolation
- Use Docker or Podman to containerize training jobs.
- Pre-build Docker images with dependencies to reduce setup time during training.
- This ensures clean environments for each run and avoids resource conflicts.

---

## 2. Preload Data and Models
- Cache frequently used datasets, models, and intermediate files locally on the VM.
- Use tools like `dvc` (Data Version Control) or shared storage for versioning and sharing across jobs.

---

## 3. Enable GPU Utilization (if available)
- Ensure CUDA, cuDNN, and other GPU drivers are installed for frameworks like TensorFlow or PyTorch.
- Use mixed precision training to maximize GPU memory usage (supported in PyTorch and TensorFlow).

---

## 4. Optimize Model Training
- Techniques for efficiency:
  - Distributed training for large-scale models.
  - Gradient checkpointing to save memory.
  - Reduce batch sizes when GPU memory is limited.

---

## 5. Schedule Jobs Smartly
- Use job schedulers (e.g., cron, Kubernetes, or SLURM) to avoid resource contention.
- Configure the GitHub runner to limit the number of concurrent jobs.

---

## 6. Monitor Resource Usage
- Install monitoring tools like:
  - Prometheus + Grafana
  - `htop` or `nvidia-smi` for GPU usage
- Track CPU, GPU, and memory usage to identify bottlenecks.

---

## 7. Run Jobs in Parallel
- Use multi-core processors efficiently with tools like Ray or Dask.
- Distribute tasks across available CPU cores for parallel execution.

---

## 8. Set Idle Shutdown
- Automate VM shutdown when idle to save costs.
- Use scripts or tools like:
  - AWS Lambda
  - Azure Automation
  - GCP Cloud Functions

---

## 9. Use Preemptible or Spot Instances (Optional for Cloud)
- If using a cloud-based VM, opt for preemptible or spot instances to save costs.
- Run non-critical training jobs on these instances.

---

## 10. Use Lightweight Frameworks and Libraries
- Prefer optimized libraries (e.g., TensorFlow Lite or ONNX) when possible.
- Reduce overhead by using only the necessary dependencies.

---

By implementing these techniques, you can effectively utilize your VM resources for optimal performance and cost-efficiency.
---
