import pulumi
import pulumi_aws as aws

sg = aws.ec2.SecurityGroup(
    "web-sg",
    description="Web sg for HTTP",
    ingress = [
        {
            'protocol': 'tcp',
            'from_port': 80,
            'to_port': 80,
            'cidr_blocks': ['0.0.0.0/0']
        }
    ]
)

ami = aws.get_ami(
    most_recent="true",
    owners=['amazon'],
    filters=[{'name': 'name', 'values': ['amzn-ami-hvm-*']}]
)

user_data = """
#!/bin/bash
uname -n > index.html
nohup python -m SimpleHTTPServer 80 &
"""

instance = aws.ec2.Instance(
    "pulumi-webapp",
    instance_type="t2.micro",
    security_groups=[sg.name],
    ami=ami.id,
    user_data=user_data,
)
pulumi.export("web-app-ip", instance.public_ip)