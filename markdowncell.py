
import pandas as pd
import os
import matplotlib.pyplot as plt

# Load chatbot conversation history
history_file = "dataset/chat_history.csv"

if not os.path.exists(history_file):
    print("Chat history file not found:", history_file)

else:
    history = pd.read_csv(history_file)

    print("Chat history loaded successfully!")
    print("\nDataset shape:", history.shape)

    print("\nMissing values:")
    print(history.isnull().sum())

    print("\nFirst five conversations:")
    print(history.head())

    # Analyze response lengths
    if "Bot_Response" in history.columns:
        history["Response_Length"] = (
            history["Bot_Response"].fillna("").astype(str).str.len()
        )

        print("\nResponse Length Analysis:")
        print(history[["User_Question", "Response_Length"]])

        print(
            "\nAverage response length:",
            round(history["Response_Length"].mean(), 2)
        )

        # Save analysis
        history.to_csv(
            "dataset/response_analysis.csv",
            index=False
        )
        print("\nAnalysis saved successfully!")

        # Create chart
        plt.figure(figsize=(10, 5))
        plt.bar(
            history["User_Question"],
            history["Response_Length"]
        )
        plt.title("Chatbot Response Length Analysis")
        plt.xlabel("User Questions")
        plt.ylabel("Response Length (characters)")
        plt.xticks(rotation=15, ha="right")
        plt.tight_layout()

        # Save and display chart
        plt.savefig("dataset/response_length_chart.png")
        print("Chart saved to dataset/response_length_chart.png")
        plt.show()

    else:
        print("Bot_Response column not found in the CSV.")
