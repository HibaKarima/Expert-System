def _extend_unique(recommendations, items):
    for item in items:
        if item not in recommendations:
            recommendations.append(item)


def get_recommendations(results, context_config=None):
    recommendations = []

    context = (context_config or {}).get("context", {})
    usage_type = context.get("usage_type", "diagnosis")
    path_map = (context_config or {}).get("recommendation_path", {})

    overheating_risk = results.get("overheating_risk", 0)
    performance = results.get("performance", 100)
    stability = results.get("stability", 100)
    storage_issue = results.get("storage_issue", 0)
    battery_issue = results.get("battery_issue", 0)
    boot_issue = results.get("boot_issue", 0)

    if overheating_risk >= 75:
        if usage_type == "gaming":
            _extend_unique(
                recommendations,
                [
                    "Reduce graphics settings",
                    "Use cooling pad",
                    "Clean cooling fan",
                ],
            )
        elif usage_type == "office":
            _extend_unique(
                recommendations,
                [
                    "Close background applications",
                    "Restart system",
                    "Improve laptop ventilation",
                ],
            )
        else:
            _extend_unique(
                recommendations,
                path_map.get("overheating", [
                    "Clean cooling fan",
                    "Improve laptop ventilation",
                ]),
            )

    if performance <= 45:
        if usage_type == "gaming":
            _extend_unique(
                recommendations,
                [
                    "Reduce graphics settings",
                    "Close background applications",
                ],
            )
        elif usage_type == "office":
            _extend_unique(
                recommendations,
                [
                    "Close background applications",
                    "Restart system",
                ],
            )
        else:
            _extend_unique(
                recommendations,
                path_map.get("performance", [
                    "Close background applications",
                    "Restart system",
                ]),
            )

    if storage_issue >= 60:
        _extend_unique(
            recommendations,
            path_map.get("storage", [
                "Free up disk space",
                "Backup important files",
            ]),
        )

    if battery_issue >= 60:
        _extend_unique(
            recommendations,
            path_map.get("battery", [
                "Check charger and power settings",
                "Reduce brightness and background load",
            ]),
        )

    if boot_issue >= 60:
        _extend_unique(
            recommendations,
            path_map.get("boot", [
                "Run startup repair",
                "Check drive detection in BIOS",
            ]),
        )

    if stability <= 45 and not recommendations:
        _extend_unique(
            recommendations,
            [
                "Restart system",
                "Check background processes",
            ],
        )

    return recommendations