variable "region" {
  type        = string
  description = "A region is an isolated set of resources, with a dedicated control plane and resource plane."
  default     = "eu-fr-paris"
}

variable "availability_zone" {
  type        = string
  description = "Availability zone (AZ) is an isolated location within data center regions from which cloud services operate."
  default     = "eu-fr-paris-1"
}

variable "app_name" {
  type        = string
  description = "Name of the application."
  default     = "my-app"
}

variable "flavor" {
  type    = map(any)
  default = {
    dev  = "XLarge 12vCPU-16GB"
    suat = "XLarge 8vCPU-16GB"
    prd  = "XLarge 8vCPU-16GB"
  }
}

variable "network" {
  type        = string
  description = "The network zone of the compute instance."
  default     = "SSA UAT 2"
}

variable "account_id" {
  type    = string
  default = "your-account-id"
}

variable "client_id" {
  type    = string
  default = "your-client-id"
}

variable "client_s" {
  type    = string
  default = "your-client-secret"
}

variable "app_environment" {
  type    = string
  default = "dev"
}

variable "compute_ssh_public_key" {
  type    = string
  default = "ssh-rsa AAAAB3RzC3yZEAAAADAQABAAABgQ0h8xL8f622vJHOOLLNIsBI8dWle18P6rRgFH9EvYZGFB"
}

variable "dns_name" {
  type    = string
  default = "my-dns-name"
}
