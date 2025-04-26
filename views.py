from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import ProfileForm, UserRegistrationForm
import numpy as np
import pickle
import matplotlib
import base64
from io import BytesIO
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from accounts.models import ProfileData
from .blockchain import blockchain
from .models import ProfileData, Report
from django.contrib.auth.decorators import login_required
# Load models
matplotlib.use('Agg') 

# Load the trained models
with open('rf_model.pkl', 'rb') as f:
        rf_model = pickle.load(f)
with open('svm_model.pkl', 'rb') as f:
        svm_model = pickle.load(f)
with open('ann_model.pkl', 'rb') as f:
        ann_model = pickle.load(f)
with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)

# Generate pie chart
def generate_pie_chart(predictions):
    labels = ['Fake', 'Real']
    counts = [predictions.count('Fake'), predictions.count('Real')]

    fig, ax = plt.subplots()
    ax.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#ff9999', '#66b3ff'])
    ax.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    pie_chart = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()
    plt.close(fig)
    return pie_chart

def generate_bar_chart(predictions):
    labels = ['Fake', 'Real']
    counts = [predictions.count('Fake'), predictions.count('Real')]

    fig, ax = plt.subplots()
    ax.bar(labels, counts, color=['#ff9999', '#66b3ff'])
    ax.set_ylabel('Count')
    ax.set_title('Prediction Counts')

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    bar_chart = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()
    plt.close(fig)
    return bar_chart

# Chat view function to handle user input and prediction
from sklearn.preprocessing import StandardScaler

def chat_view(request):
    rf_prediction, svm_prediction, ann_prediction, consensus = None, None, None, None
    pie_chart, bar_chart = None, None

    # Load the saved models and scaler
    with open('rf_model.pkl', 'rb') as f:
        rf_model = pickle.load(f)
    with open('svm_model.pkl', 'rb') as f:
        svm_model = pickle.load(f)
    with open('ann_model.pkl', 'rb') as f:
        ann_model = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)

    if request.method == 'POST':
        try:
            # Get input features from the POST request
            followers = int(request.POST.get('followers', 0))
            following = int(request.POST.get('following', 0))
            bio_length = int(request.POST.get('bio_length', 0))
            profile_photo = int(request.POST.get('profile_photo', 0))  # 1 if photo exists, else 0
            is_private = int(request.POST.get('is_private', 0))  # 1 if private, else 0

            # Prepare the feature vector
            features = [followers, following, bio_length, profile_photo, is_private]

            # Scale the input features using the loaded scaler
            features_scaled = scaler.transform([features])

            # Make predictions
            rf_prediction = 'Fake' if rf_model.predict(features_scaled)[0] == 1 else 'Real'
            svm_prediction = 'Fake' if svm_model.predict(features_scaled)[0] == 1 else 'Real'
            ann_prediction = 'Fake' if ann_model.predict(features_scaled)[0] == 1 else 'Real'

            # Calculate consensus
            predictions = [rf_prediction, svm_prediction, ann_prediction]
            consensus = max(set(predictions), key=predictions.count)
            print("RF raw prediction:", rf_model.predict(features_scaled))
            print("SVM raw prediction:", svm_model.predict(features_scaled))
            print("ANN raw prediction:", ann_model.predict(features_scaled))

            # Generate charts
            pie_chart = generate_pie_chart(predictions)
            bar_chart = generate_bar_chart(predictions)

        except Exception as e:
            print(f"Error during prediction: {e}")
            rf_prediction, svm_prediction, ann_prediction, consensus = "Error", "Error", "Error", "Error"

    return render(request, 'chat.html', {
        'rf_prediction': rf_prediction,
        'svm_prediction': svm_prediction,
        'ann_prediction': ann_prediction,
        'consensus': consensus,
        'pie_chart': pie_chart,
        'bar_chart': bar_chart,
    })

# Registration view (homepage)
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('form')
    return render(request, 'login.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')

# Form for prediction
def input_form(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            data = {
                'followers': form.cleaned_data['followers'],
                'following': form.cleaned_data['following'],
                'bio': form.cleaned_data['bio'],
                'has_profile_photo': form.cleaned_data['has_profile_photo'],
                'is_private': form.cleaned_data['is_private'],
            }
            predictions = predict_fake_profile(data)
            return render(request, 'result.html', {'predictions': predictions})
    else:
        form = ProfileForm()
    return render(request, 'form.html', {'form': form})

# Prediction logic for fake profile
def predict_fake_profile(data):
    features = np.array([
        data['followers'],
        data['following'],
        len(data['bio']),
        int(data['has_profile_photo']),
        int(data['is_private']),
    ]).reshape(1, -1)

    return {
        "RF Prediction": "Fake" if rf_model.predict(features)[0] == 1 else "Real",
        "SVM Prediction": "Fake" if svm_model.predict(features)[0] == 1 else "Real",
        "ANN Prediction": "Fake" if ann_model.predict(features)[0] == 1 else "Real",
    }

@login_required
def report_fake_profile(request):
    """Handles reporting of fake profiles with blockchain integration."""
    if request.method == 'POST':
        reported_profile = request.POST.get('reported_profile')
        reason = request.POST.get('reason')

        # Create a report
        report = Report(user=request.user, reported_profile=reported_profile, reason=reason)
        report.save()  # Save to generate a timestamp

        # Store in Blockchain
        report_hash = blockchain.create_block({
            'reported_profile': reported_profile,
            'reason': reason,
            'timestamp': str(report.timestamp)
        })
        report.blockchain_tx_hash = report_hash
        report.save()

        return redirect('home')

    return render(request, 'report.html')

