provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "wingman_app_server" {
  ami           = "ami-0c55b159cbfafe1f0" # Amazon Linux 2
  instance_type = "t2.micro"             # Free Tier

  tags = {
    Name = "RexburgWingman-Production"
  }
}
