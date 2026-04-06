provider "aws" {
  region = "us-east-1" 
}

resource "aws_instance" "wingman_app_server" {
  ami = "ami-0e2c8ccd4e0370c72"
  instance_type = "t2.micro"             # Free Tier

  tags = {
    Name = "RexburgWingman-Production"
  }
}
