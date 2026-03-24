def get_pricing():
    """
    Sample pricing assumptions for v1 of the forecasting engine.
    These are simplified placeholder rates for modeling purposes.
    """

    return {
        "lambda_cost_per_million_requests": 2.20,
        "dynamodb_cost_per_million_transactions": 16.30,
        "s3_cost_per_gb": 0.023,
        "other_fixed_cost": 10000
    }
