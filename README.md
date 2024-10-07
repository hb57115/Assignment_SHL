Synthetic Data Generation for AI Systems
Overview
Welcome to the Synthetic Data Generation project! This initiative aims to tackle the common challenge of limited datasets in training AI models, particularly in the realm of Supplements/Vitamins. Our goal is to generate realistic synthetic reviews that can help improve model training, evaluation, and design.

Table of Contents
Project Goals
Dataset
Methodology
How to Use
Challenges Faced
Contributions
Contact
Project Goals
In the fast-evolving field of AI, having a robust dataset is crucial. However, acquiring sufficient quality data can often be challenging. This project focuses on generating synthetic datasets that mimic realistic human-written reviews while allowing for controlled variations in factors like:

Dialogue Length: Adjusting the length of reviews to represent different customer experiences.
Topic Diversity: Covering a wide range of supplement types and consumer sentiments.
Language Complexity: Varying the complexity of the language used to appeal to different audiences.
Dataset
We are using a subset of the Amazon reviews dataset specifically tailored for the Supplements/Vitamins category. This dataset serves as the foundation for generating our synthetic reviews.

Methodology
To generate our synthetic reviews, we utilized a pre-trained language model (GPT-2) for text generation. The process involves:

Data Preparation: Cleaning and pre-processing the Amazon reviews dataset.
Text Generation: Using the model to generate reviews based on specific prompts.
Evaluation: Assessing the quality of the generated reviews for relevance and diversity.
Key Considerations
Model Selection: GPT-2 was chosen due to its ability to generate coherent and contextually relevant text based on input prompts.
Factors for Review Generation: We considered length, topic diversity, and language complexity when generating the dataset.
Efficacy Measurement: We assess the effectiveness of our synthetic dataset by comparing its quality and variety to the original dataset.
How to Use
Clone this repository to your local machine.

Install the required libraries by running:

bash
Copy code
pip install -r requirements.txt
Run the main script to generate synthetic reviews:

bash
Copy code
python generate_reviews.py
The generated reviews will be saved in a CSV file.

Challenges Faced
While working on this project, we encountered several challenges, including:

Maintaining Realism: Striking the right balance between generating realistic reviews and introducing variations.
Quality Control: Ensuring that the synthetic reviews were diverse and meaningful, avoiding repetitive patterns.
Contributions
Feel free to contribute to this project by sharing your insights or suggesting improvements. Whether you have ideas on enhancing the methodology or feedback on the generated data, your input is welcome!

Contact
For any questions or inquiries, please reach out:

Name: Harsh Bhardwaj
Email: hb57115@gmail.com
Thank you for your interest in this project! Together, let's advance the field of AI by creating better datasets for training.
