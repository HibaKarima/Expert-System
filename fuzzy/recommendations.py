def get_recommendations(results):

    recommendations = []

    if results.get("overheating_risk", 0) > 0.75:

        recommendations.extend([
            "Clean cooling fan",
            "Reduce heavy applications",
            "Improve laptop ventilation"
        ])

    return recommendations