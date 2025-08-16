def positive_feedback_percentage(ratings):
    if not ratings:
        return "No ratings available."
    
    positive_count = sum(1 for r in ratings if r >= 4)
    percentage = (positive_count / len(ratings)) * 100
    return f"Positive Feedback: {percentage:.1f}%"

# Input example
ratings = [5, 4, 3, 5, 2, 4, 1, 5]

# Calculate and print
print(positive_feedback_percentage(ratings))
