import boto3, response

#AWS Credentials and region
aws_access_key_id = 'AKIAUJRYN7IHD7ODEYPH'
aws_secret_access_key = 'secret access key'
region = 'ap-south-1'

def check_asg_activity(asg_name):
    client = boto3.client('autoscaling', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region)
    response = client.describe_scaling_activities(AutoScalingGroupName=asg_name)
    
    for activity in response['Activities']:
        print(f"Activity ID: {activity['ActivityId']}")
        print(f"Description: {activity['Description']}")
        print(f"Cause: {activity['Cause']}")
        print(f"Start Time: {activity['StartTime']}")
        print(f"End Time: {activity['EndTime']}")
        print(f"Status Code: {activity['StatusCode']}")
        print("------")

# Replace 'my-asg' with your Auto Scaling Group name
check_asg_activity('Gpr11ASG')
