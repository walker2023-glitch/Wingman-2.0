resource "aws_security_group" "wingman_sg_v2" {  # Changed name here
  name        = "wingman-security-group-v2"      # Changed name here
  description = "Allow web traffic to Wingman App"

  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
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
  # Update this reference to match the new name above
  vpc_security_group_ids = [aws_security_group.wingman_sg_v2.id]

  user_data = <<-EOF
              #!/bin/bash
              sudo apt-get update -y
              sudo apt-get install -y docker.io
              sudo systemctl start docker
              sudo systemctl enable docker
              sudo docker pull walkedal006/rexburg-wingman:latest
              sudo docker run -d -p 8000:8000 walkedal006/rexburg-wingman:latest
              EOF

  tags = {
    Name = "RexburgWingman-Production"
  }
}
