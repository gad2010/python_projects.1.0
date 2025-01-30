import boto3

def lambda_handler(event, context):
    # Create an S3 client
    s3 = boto3.client('s3')

    # List all buckets
    try:
        response = s3.list_buckets()

        # Check if there are any buckets and return them
        if 'Buckets' in response:
            bucket_names = [bucket['Name'] for bucket in response['Buckets']]
            return {
                'statusCode': 200,
                'body': {
                    'message': 'List of S3 Buckets',
                    'buckets': bucket_names
                }
            }
        else:
            return {
                'statusCode': 404,
                'body': 'No S3 buckets found.'
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error retrieving S3 buckets: {str(e)}"
        }
