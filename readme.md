# 🏥 Medical Symptom Checker - Bayesian Network

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A web application that uses **Bayesian Networks** to diagnose common illnesses based on symptoms. Built with Python, Flask, and pgmpy for educational purposes.

![Demo Screenshot](https://via.placeholder.com/800x400?text=Add+Your+Screenshot+Here)

## 🎯 Features

- **5 Diseases**: Cold, Flu, Allergy, COVID-19, Strep Throat
- **8 Symptoms**: Fever, Cough, Fatigue, Runny Nose, Body Aches, Sneezing, Sore Throat, Headache
- **Real-time Inference**: Uses Bayesian Network probabilistic reasoning
- **Interactive UI**: Modern, responsive design with visual probability bars
- **Docker Support**: Easy deployment with Docker and Docker Compose
- **RESTful API**: JSON API for integration with other applications

## 🚀 Quick Start

### Option 1: Docker (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/medical-symptom-checker.git
cd medical-symptom-checker

# Start with Docker Compose
docker-compose up -d

# Access at http://localhost:5000
```

### Option 2: Local Python

```bash
# Clone the repository
git clone https://github.com/yourusername/medical-symptom-checker.git
cd medical-symptom-checker

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

# Access at http://localhost:5000
```

### Option 3: Using Makefile (Linux/Mac)

```bash
# Start the app
make up

# View logs
make logs

# Stop the app
make down
```

## 📋 Prerequisites

- Python 3.8+ or Docker
- pip (Python package manager)
- Docker & Docker Compose (for Docker deployment)

## 🏗️ Project Structure

```
medical-symptom-checker/
├── app.py                  # Flask application
├── bayesian_model.py       # Bayesian Network implementation
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose configuration
├── Makefile              # Command shortcuts
├── setup.sh              # Setup script
├── templates/
│   └── index.html        # Frontend UI
├── README.md             # This file
└── DOCKER_SETUP.md       # Docker documentation
```

## 🧠 How It Works

### Bayesian Network Structure

```
Disease (Prior Probabilities)
   ├── Fever
   ├── Cough
   ├── Fatigue
   ├── Runny Nose
   ├── Body Aches
   ├── Sneezing
   ├── Sore Throat
   └── Headache
```

The application uses a **Bayesian Network** to model the probabilistic relationships between diseases and symptoms. Each disease has different conditional probabilities for each symptom:

- **COVID-19**: High cough (90%), high fever (80%), high fatigue (85%)
- **Flu**: High fever (90%), high body aches (95%), high headache (80%)
- **Strep Throat**: Very high sore throat (95%), high fever (70%)
- **Cold**: High runny nose (80%), high cough (80%), moderate symptoms
- **Allergy**: High sneezing (95%), high runny nose (90%), low fever (5%)

### Inference Algorithm

The system uses **Variable Elimination** to calculate posterior probabilities:

1. User selects observed symptoms
2. Evidence is fed into the Bayesian Network
3. Posterior probabilities are calculated for each disease
4. Results are ranked and displayed with confidence scores

## 🧪 Example Use Cases

### Case 1: COVID-19 Symptoms
**Input**: Fever + Cough + Body Aches + Fatigue + Headache  
**Output**: ~75-85% COVID-19 probability

### Case 2: Strep Throat
**Input**: Severe Sore Throat + Fever  
**Output**: ~70-85% Strep Throat probability

### Case 3: Seasonal Allergy
**Input**: Sneezing + Runny Nose (no fever)  
**Output**: ~80-90% Allergy probability

## 📡 API Documentation

### POST `/diagnose`

Diagnose diseases based on symptoms.

**Request**:
```json
{
  "Fever": "Yes",
  "Cough": "Yes",
  "Fatigue": "Yes",
  "RunnyNose": "No",
  "BodyAches": "Yes",
  "Sneezing": "No",
  "SoreThroat": "No",
  "Headache": "Yes"
}
```

**Response**:
```json
{
  "success": true,
  "most_likely_disease": "COVID-19",
  "probability": 78.45,
  "all_probabilities": {
    "COVID-19": 78.45,
    "Flu": 15.23,
    "Cold": 4.12,
    "Allergy": 1.20,
    "StrepThroat": 1.00
  }
}
```

### GET `/api/info`

Get model information.

**Response**:
```json
{
  "diseases": ["Cold", "Flu", "Allergy", "COVID-19", "StrepThroat"],
  "symptoms": ["Fever", "Cough", "Fatigue", "RunnyNose", "BodyAches", "Sneezing", "SoreThroat", "Headache"],
  "description": "A Bayesian Network for medical symptom diagnosis"
}
```

## 🛠️ Development

### Running Tests

```bash
# Test the Bayesian model
python bayesian_model.py

# With Docker
make test
```

### Adding New Diseases

1. Update `bayesian_model.py`:
```python
cpd_disease = TabularCPD(
    variable='Disease',
    variable_card=6,  # Increase count
    values=[[0.20], [0.20], [0.20], [0.20], [0.10], [0.10]],
    state_names={'Disease': ['Cold', 'Flu', 'Allergy', 'COVID-19', 'StrepThroat', 'NewDisease']}
)
```

2. Update all CPD tables with new probabilities
3. Update `templates/index.html` with new symptom cards

### Customizing Probabilities

Edit the CPD values in `bayesian_model.py` to match real medical data or your specific use case.

## 🐳 Docker Commands

```bash
# Build and start
docker-compose up -d --build

# View logs
docker-compose logs -f

# Stop
docker-compose down

# Restart
docker-compose restart

# Access shell
docker exec -it medical-symptom-checker bash
```

## 📊 Tech Stack

- **Backend**: Python 3.11, Flask 3.0
- **Bayesian Network**: pgmpy 0.1.25
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Containerization**: Docker, Docker Compose
- **Data Processing**: pandas, numpy, scipy

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Add comments for complex logic
- Update documentation for new features
- Test your changes before submitting PR

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

**This application is for educational purposes only.** It should **NOT** be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.

## 🎓 Educational Use

This project demonstrates:
- Bayesian Network implementation in Python
- Probabilistic inference algorithms
- Web application development with Flask
- Docker containerization
- RESTful API design
- Interactive data visualization

Perfect for:
- Machine Learning students
- Data Science projects
- AI/ML course assignments
- Probabilistic reasoning demonstrations

## 📚 Resources

- [pgmpy Documentation](https://pgmpy.org/)
- [Bayesian Networks Tutorial](https://www.bayesserver.com/docs/introduction/bayesian-networks)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Documentation](https://docs.docker.com/)

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Built with [pgmpy](https://pgmpy.org/) - Probabilistic Graphical Models in Python
- UI inspired by modern medical applications
- Thanks to the open-source community

## 📈 Future Enhancements

- [ ] Add more diseases (Pneumonia, Bronchitis, etc.)
- [ ] Implement user authentication
- [ ] Add symptom severity levels
- [ ] Machine learning to improve probabilities
- [ ] Mobile app version
- [ ] Multi-language support
- [ ] Export diagnosis history
- [ ] Integration with health APIs

## 🐛 Known Issues

See the [Issues](https://github.com/yourusername/medical-symptom-checker/issues) page for known bugs and planned features.

## 📞 Support

If you have any questions or need help:
- Open an [Issue](https://github.com/yourusername/medical-symptom-checker/issues)
- Check the [Documentation](DOCKER_SETUP.md)
- Contact: your.email@example.com

---

⭐ If you find this project useful, please consider giving it a star!

Made with ❤️ using Python and Bayesian Networks
