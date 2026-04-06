provider "aws" {
  region = "us-east-1"
}

# This creates the "Firewall Rule"
resource "aws_security_group" "wingman_sg" {
  name        = "wingman-security-group"
  description = "Allow web traffic to Wingman App"

  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Allows anyone to see the site
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "wingman_app_server" {
  ami                    = "ami-04b70fa74e45c3917"
  instance_type          = "t2.micro"
  # This line connects the firewall to the server
  vpc_security_group_ids = [aws_security_group.wingman_sg.id]

  tags = {
    Name = "RexburgWingman-Production"
  }
}

output "instance_public_ip" {
  value = aws_instance.wingman_app_server.public_ip
}
