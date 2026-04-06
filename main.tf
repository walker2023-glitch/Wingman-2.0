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
  vpc_security_group_ids = [aws_security_group.wingman_sg.id]

  # THIS IS THE MISSING PIECE: It installs Docker and runs your app
  user_data = <<-EOF
              #!/bin/bash
              sudo apt-get update -y
              sudo apt-get install -y docker.io
              sudo systemctl start docker
              sudo systemctl enable docker
              # Pull your specific image from Docker Hub
              sudo docker pull walkedal006/rexburg-wingman:latest
              # Run it on Port 8000
              sudo docker run -d -p 8000:8000 walkedal006/rexburg-wingman:latest
              EOF

  tags = {
    Name = "RexburgWingman-Production"
  }
}

  tags = {
    Name = "RexburgWingman-Production"
  }
}

output "instance_public_ip" {
  value = aws_instance.wingman_app_server.public_ip
}
