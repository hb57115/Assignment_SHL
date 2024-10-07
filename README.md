# Synthetic Data Generation for AI Systems

## Overview

Welcome to the Synthetic Data Generation project! This initiative aims to tackle the common challenge of limited datasets in training AI models, particularly in the realm of **Supplements/Vitamins**. Our goal is to generate realistic synthetic reviews that can help improve model training, evaluation, and design.

## Table of Contents

- [Project Goals](#project-goals)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [How to Use](#how-to-use)
- [Challenges Faced](#challenges-faced)
- [Contributions](#contributions)
- [Contact](#contact)

## Project Goals

In the fast-evolving field of AI, having a robust dataset is crucial. However, acquiring sufficient quality data can often be challenging. This project focuses on generating synthetic datasets that mimic realistic human-written reviews while allowing for controlled variations in factors like:

- **Dialogue Length**: Adjusting the length of reviews to represent different customer experiences.
- **Topic Diversity**: Covering a wide range of supplement types and consumer sentiments.
- **Language Complexity**: Varying the complexity of the language used to appeal to different audiences.

## Dataset

We are using a subset of the [Amazon reviews dataset](https://amazon-reviews-2023.github.io/main.html) specifically tailored for the **Supplements/Vitamins** category. This dataset serves as the foundation for generating our synthetic reviews.

## Methodology

To generate our synthetic reviews, we utilized a pre-trained language model (GPT-2) for text generation. The process involves:

1. **Data Preparation**: Cleaning and pre-processing the Amazon reviews dataset.
2. **Text Generation**: Using the model to generate reviews based on specific prompts.
3. **Evaluation**: Assessing the quality of the generated reviews for relevance and diversity.

### Key Considerations

- **Model Selection**: GPT-2 was chosen due to its ability to generate coherent and contextually relevant text based on input prompts.
- **Factors for Review Generation**: We considered length, topic diversity, and language complexity when generating the dataset.
- **Efficacy Measurement**: We assess the effectiveness of our synthetic dataset by comparing its quality and variety to the original dataset.

## How to Use

1. Clone this repository to your local machine.
2. Install the required libraries by running:
   ```bash
   pip install -r requirements.txt
