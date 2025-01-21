# **MPDL-Base-Station-Sleep-Control-Algorithm**

## **Project Overview**
This project implements an algorithm to control the sleep time of base stations in a mobile network. The goal is to optimize power consumption while maintaining quality of service (QoS) for users.

# Transformer Implementation Roadmap

**Prepared by:** Mohammad Hasan Bayatiany

## Reference 36 of the Paper:
For this section, we need to use the Google Places API and make the API call in the specified format. Additionally, we need to discuss the types of places from which we want to retrieve data. It seems the document doesn't provide comprehensive information about the entire dataset; it only focuses on making the API call.

## Italian Telecom Data:
I reviewed this dataset and downloaded it for easier access. You can find it in my drive (with the main link filtered). The dataset includes the following labels:

- **CellId**
- **Datetime**
- **Countrycode**
- **SMSin**
- **SMSout**
- **Callin**
- **Callout**
- **Internet**

## Model Implementation:
1. First, the dataset should be loaded.
2. Then, the hyperparameters should be defined. I have identified the following hyperparameters for the code:

| Hyperparameter       | Value       | Note about Usage Reason                                              |
|----------------------|-------------|----------------------------------------------------------------------|
| **sequence_length**   | 24          | The number of past time steps used to predict future values.          |
| **batch_size**        | 64          |                                                                      |
| **epochs**            | 50          |                                                                      |
| **learning_rate**     | 0.001       |                                                                      |
| **model_dim**         | 128         | The size of the embedding vectors for each input feature (dimensionality of the model space). |
| **num_heads**         | 8           | The number of parallel attention mechanisms in the Transformer’s multi-head attention block. |
| **ff_dim**            | 256         | The size of the hidden layer in the feed-forward network within each Transformer block. |
| **num_layers**        | 4           |                                                                      |
| **dropout**           | 0.1         |                                                                      |

Additionally, using **ReLU** activation function and **ADAM** optimizer (should be discussed).


If you encounter any issues or need assistance, feel free to contact me at:

**Email:** mowhby2004@gmail.com
