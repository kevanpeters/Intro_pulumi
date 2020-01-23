# Pulumi Tutorial on AWS for Python

[Check out the video](https://youtu.be/60LYNRnmM5M)


[Link to post](https://kevanpeters.com/post/Intro_pulumi/
)

## Setup
---

### AWS CLI setup 

[Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)

    pip3 install awscli 

[Setup AWS Creds](https://cloudacademy.com/blog/how-to-use-aws-cli/)

    aws configure


### Installing Pulumi

[install-pulumi](https://www.pulumi.com/docs/get-started/aws/install-pulumi/)

macOS

    brew install pulumi

Lunix 

    curl -fsSL https://get.pulumi.com | sh


Windows 

    @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; iex ((New-Object System.Net.WebClient).DownloadString('https://get.pulumi.com/install.ps1'))" && SET "PATH=%PATH%;%USERPROFILE%\.pulumi\bin"
