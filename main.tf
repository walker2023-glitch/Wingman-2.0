provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "wingman_app_server" {
  ami           = "ami-04b70fa74e45c3917" # Ubuntu 24.04 (Verified for us-east-1)
  instance_type = "t2.micro"

  tags = {
    Name = "RexburgWingman-Production"
  }
}

output "instance_public_ip" {
  value = aws_instance.wingman_app_server.public_ip
}
