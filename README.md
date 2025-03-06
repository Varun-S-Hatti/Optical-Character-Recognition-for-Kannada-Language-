# Optical-Character-Recognition-for-Kannada-Language-
Kannada OCR recognizes and extracts Kannada text from images and documents using deep learning for accurate text detection and conversion.

## Outline 
Kannada OCR is an advanced Optical Character Recognition (OCR) system powered by Machine Learning (ML) and Deep Learning. It is designed to accurately extract and convert Kannada text from images and documents into a machine-readable format, making digitization easier and more efficient.

The platform enhances text recognition accuracy by utilizing Convolutional Neural Networks (CNNs) and image preprocessing techniques to handle challenges such as diverse fonts, skewed text, and document noise. Key features include real-time text extraction, multi-font support, noise reduction, and high-accuracy recognition, making it a powerful tool for digitizing Kannada-language content.

---

## Features  

 **1. Kannada Text Recognition:** Accurately extracts and converts Kannada text from images into a machine-readable format.  
 **2. Dataset Utilization:** Uses an 80:20 training-to-testing dataset split to optimize model performance.  
 **3. Image Preprocessing:** Enhances image quality by removing noise, correcting skewness, and improving text clarity.  
 **4. CNN-Based Training:** Employs Convolutional Neural Networks (CNNs) to train the model for high-accuracy text recognition.  
 **5. User Image Upload:** Allows users to upload scanned documents or images containing Kannada text for recognition.  
 **6. Real-Time Text Extraction:** Processes and extracts Kannada text efficiently with minimal latency.  
 **7. Text Copying and Export:** Enables users to copy extracted text and use it in documents, applications, or further processing. 

 ---

 ## Dependencies  

The following libraries and frameworks are required to run the Kannada OCR system:  

  **1. joblib** == 0.16.0  
  **2. Keras** == 2.4.3  
  **3. matplotlib** == 3.3.0  
  **4. numpy** == 1.19.1  
  **5. opencv-python** == 4.3.0.36  
  **6. scikit-image** == 0.17.2  
  **7. tensorboard** == 2.2.2  
  **8. tensorflow** == 2.2.1  

  ---
  ## Technology Used  

  **1. Frontend:** HTML, CSS (for UI, if applicable)  
  **2. Backend:** Python (Flask/Django) for handling OCR requests  
  **3. Machine Learning:** TensorFlow/Keras for CNN-based text recognition  
  **4. Image Processing:** OpenCV and scikit-image for preprocessing and feature extraction  
  **5. OCR Libraries:** EasyOCR, PyTesseract for text extraction  

  ---

  ## Installation and Setup  

### Prerequisites  
* **Python 3.10+**  
* **Virtual Environment** (optional but recommended)  

### Steps  

#### 1. Clone the repository:  
```bash
git clone <repository-url>  
cd Kannada-OCR
``` 
#### 2.Set Up Virtual Environment:
   ```bash
python -m venv env  
source env/bin/activate   # For Linux/Mac  
env\Scripts\activate      # For Windows
 ```
#### 3.Install dependencies:
   ```bash
pip install -r requirements.txt
 ```
#### 4.Set up environment variables:  
- Configure the .env file with necessary keys if required.
#### 5.Run the application:
   ```bash
python app.py
 ```
#### 5.Access the application:
Open http://127.0.0.1:5000 in your browser to use the Kannada OCR system.

 ## How to Use  

* **1. The platform is free and open-source**; no login is required to use the OCR system.  
* **2. Upload an Image:**  
   - On the homepage, users can upload an image containing Kannada text.  
   - The system will process the image and extract the text.  
* **3. Text Recognition Process:**  
   - The uploaded image undergoes preprocessing to enhance text clarity.  
   - The OCR model detects and extracts Kannada text using deep learning techniques.  
   - The extracted text is displayed on the screen.  
* **4. Copy or Download Extracted Text:**  
   - Users can copy the recognized Kannada text for further use.  
   - Option to download the extracted text for offline access.  
  ---
