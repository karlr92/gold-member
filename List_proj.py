# Create a list of services using Python

aws_list = []

# Populate the list using append or insert.

aws_list.append("S3")
aws_list.append("Lambda")
aws_list.append("EC2")
aws_list.append("VPC")
aws_list.append("RDS")
aws_list.append("SNS")

# Print the list and the length of the list.

print(aws_list)
print(len(aws_list))

# Remove two specific services from the list by name or by index.

aws_list.remove("SNS")
aws_list.remove("RDS")

# Print the new list and the new length of the list.

print(aws_list)
print(len(aws_list))