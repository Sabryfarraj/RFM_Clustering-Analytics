# RFM Clustering Analytics Dashboard 📊

An interactive analytics dashboard built with Streamlit that performs RFM (Recency, Frequency, Monetary) analysis and customer segmentation. The application provides visual insights into customer behavior and segments.

## 🚀 Quick Start

You have two options to access the application:

### Option 1: Web Browser (No Installation Required)
Visit the live application at:
```
https://rfmclustering-analytics-bysabryfarraj.streamlit.app/
```
This option requires no setup - just click and use!

### Option 2: Run using Docker

If you prefer to run the application locally:

```bash
# Pull the image from Docker Hub
docker pull sabryfarraj/rfm-analytics:latest

# Run the container
docker run -p 8501:8501 sabryfarraj/rfm-analytics:latest
```

After running these commands, open your browser and visit:
```
http://localhost:8501
```

## 🛠️ Project Structure
```
RFM_Clustering-Analytics/
├── rfm_app.py         # Main Streamlit application
├── Data/              # Directory containing dataset
└── requirements.txt   # Python dependencies
```

## 📋 Prerequisites
For Docker option only:
- Docker installed on your machine ([Install Docker](https://docs.docker.com/get-docker/))

## 🔧 Local Development

If you want to build the Docker image locally:

```bash
# Clone the repository
git clone https://github.com/Sabryfarraj/RFM_Clustering-Analytics.git

# Navigate to project directory
cd RFM_Clustering-Analytics

# Build Docker image
docker build -t rfm-analytics .

# Run container
docker run -p 8501:8501 rfm-analytics
```

## 📊 Features
- Interactive RFM Analysis Dashboard
- Customer Segmentation Visualization
- Key Performance Metrics
- Data Exploration Tools
- Plotly-powered Interactive Charts
- Features include:
  - RFM Score Calculation
  - Customer Segmentation
  - Segment Distribution Analysis
  - Temporal Trends
  - Customer Value Analysis

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Authors
- Sabry Farraj

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## 🙏 Acknowledgments
- Built with Streamlit
- Interactive visualizations powered by Plotly
- Hosted on Streamlit Cloud
