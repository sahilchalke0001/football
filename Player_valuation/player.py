import streamlit as st
import pickle
import numpy as np
import plotly.graph_objects as go


class Player:
    def __init__(self, name, age, dribbling_reflexes, passing_kicking, shooting_handling,
                 total_mentality, shot_power, total_power, ball_control, finishing):
        self.name = name
        self.age = age
        self.dribbling_reflexes = dribbling_reflexes
        self.passing_kicking = passing_kicking
        self.shooting_handling = shooting_handling
        self.total_mentality = total_mentality
        self.shot_power = shot_power
        self.total_power = total_power
        self.ball_control = ball_control
        self.finishing = finishing

        # Load the model when the Player is initialized
        self.model = self.load_model()

    def load_model(self):
        try:
            with open('Player_valuation/forest.pkl', 'rb') as f:
                model = pickle.load(f)
            return model
        except FileNotFoundError:
            st.error("Model file 'forest.pkl' not found.")
            return None

    def preprocess_input(self):
        """Preprocess the input features into a format that can be used by the model."""
        input_features = np.array([[self.age, self.dribbling_reflexes, self.passing_kicking, 
                                    self.shooting_handling, self.total_mentality, self.shot_power, 
                                    self.total_power, self.ball_control, self.finishing]])
        return input_features

    def predict_market_value(self):
        """Predict the market value of the player."""
        if self.model is not None:
            features = self.preprocess_input()
            try:
                log_market_value = self.model.predict(features)[0]
                predicted_market_value = np.exp(log_market_value) / 1_000_000  # Convert to millions
                return predicted_market_value
            except ValueError as e:
                st.error(f"Prediction error: {e}")
                return None
        return None

    def generate_report(self):
        """Generate a report with the player details and predicted market value."""
        predicted_market_value = self.predict_market_value()
        if predicted_market_value is not None:
            report_data = f"""
            Player's name: {self.name}
            Age: {self.age}
            Dribbling Reflexes: {self.dribbling_reflexes} 
            Passing Kicking: {self.passing_kicking} 
            Shooting Handling: {self.shooting_handling}
            Total Mentality: {self.total_mentality}
            Shot Power: {self.shot_power}
            Total Power: {self.total_power}
            Ball Control: {self.ball_control}
            Finishing: {self.finishing}
            Predicted Market Value: €{predicted_market_value:.2f} million
            """
            return report_data
        return None

    def get_radar_chart(self):
        """Generate a radar chart based on the player's attributes."""
        input_data = {
            'age': self.age,
            'dribbling_reflexes': self.dribbling_reflexes,
            'passing_kicking': self.passing_kicking,
            'shooting_handling': self.shooting_handling,
            'total_mentality': self.total_mentality,
            'shot_power': self.shot_power,
            'total_power': self.total_power,
            'ball_control': self.ball_control,
            'finishing': self.finishing
        }

        categories = ['Age', 'Dribbling / Reflexes', 'Passing / Kicking', 'Shooting / Handling', 
                      'Total Mentality', 'Shot Power', 'Total Power', 'Ball Control', 'Finishing']

        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            r=[input_data['age'], input_data['dribbling_reflexes'], input_data['passing_kicking'],
              input_data['shooting_handling'], input_data['total_mentality'], input_data['shot_power'],
              input_data['total_power'], input_data['ball_control'], input_data['finishing']],
            theta=categories,
            fill='toself',
            name='Player Attributes'
        ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]  # Adjust this range if needed based on data
                )
            ),
            showlegend=True,
            template="plotly_dark"
        )
        return fig


# This method can be called directly in app.py as you wanted
def player():
    # Assuming the form in your main app to collect player details
    player_name = st.text_input("Enter the player's name:")
    age = st.number_input("Enter the Age (min value=16, max value=45):", min_value=16, max_value=45, step=1)
    dribbling_reflexes = st.number_input("Enter Dribbling / Reflexes (max value=100):", min_value=0, max_value=100, step=1)
    passing_kicking = st.number_input("Enter Passing / Kicking (max value=100):", min_value=0, max_value=100, step=1)
    shooting_handling = st.number_input("Enter Shooting / Handling (max value=100):", min_value=0, max_value=100, step=1)
    total_mentality = st.number_input("Enter Total Mentality (max value=500):", min_value=0, max_value=500, step=1)
    shot_power = st.number_input("Enter Shot Power (max value=100):", min_value=0, max_value=100, step=1)
    total_power = st.number_input("Enter Total Power (max value=500):", min_value=0, max_value=500, step=1)
    ball_control = st.number_input("Enter Ball Control (max value=100):", min_value=0, max_value=100, step=1)
    finishing = st.number_input("Enter Finishing (max value=100):", min_value=0, max_value=100, step=1)

    submit_button = st.button("Predict Market Value")

    if submit_button:
        if player_name == "":
            st.warning("Player name cannot be empty.")
        else:
            # Create player object
            p = Player(player_name, age, dribbling_reflexes, passing_kicking, shooting_handling,
                       total_mentality, shot_power, total_power, ball_control, finishing)
            
            # Get the report data and display it
            report_data = p.generate_report()
            if report_data:
                st.success(f"Predicted Market Value for {player_name}: €{p.predict_market_value():.2f} million")
        

            # Display radar chart
            radar_chart = p.get_radar_chart()
            st.plotly_chart(radar_chart)

            # Option to download report
            st.download_button(
                label="Download Report",
                data=report_data,
                file_name=f"{player_name}_report.txt",
                mime="text/plain"
            )
