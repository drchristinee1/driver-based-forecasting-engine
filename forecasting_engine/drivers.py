def project_demand(data):
    """
    Apply growth assumptions to business demand drivers.
    """
    growth = data.get("growth_rate", 0)

    projected = {
        "transactions": int(data["transactions"] * (1 + growth)),
        "api_requests": int(data["api_requests"] * (1 + growth)),
        "storage_gb": int(data["storage_gb"] * (1 + growth))
    }

    return projected


def map_to_infrastructure_usage(projected):
    """
    Map business demand to infrastructure usage drivers.
    """

    # Assumptions (simple for v1)
    # These can evolve into more realistic models later

    usage = {
        # Lambda usage driven by API requests
        "lambda_requests_millions": projected["api_requests"] / 1_000_000,

        # DynamoDB usage driven by transactions
        "dynamodb_transactions_millions": projected["transactions"] / 1_000_000,

        # S3 usage driven by storage growth
        "s3_storage_gb": projected["storage_gb"]
    }

    return usage
