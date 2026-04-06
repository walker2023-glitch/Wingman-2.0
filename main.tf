provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "wingman_app_server" {
  ami           = "ami-0533af068ccd7af1f" # Amazon Linux 2023 (us-east-1)
  instance_type = "t2.micro"

  tags = {
    Name = "RexburgWingman-Production"
  }
}

output "instance_public_ip" {
  value = aws_instance.wingman_app_server.public_ip
}
