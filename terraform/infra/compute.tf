# KEY CREATION
resource "cloudplatform_compute_keypair" "key" {
  name = "vm_key_${var.app_environment}"
  public_key = var.ocs_compute_ssh_public_key
}

# VMs
resource "cloudplatform_compute_instance" "vm" {
  name              = "${var.app_name}-vm-${var.app_environment}"
  description       = "${var.app_name}-compute-instance"
  availability_zone = var.availability_zone
  flavor_ref        = data.cloudplatform_compute_flavor.flavor.id
  network           = data.cloudplatform_compute_network.network_name.id
  image_ref         = data.cloudplatform_compute_image.infra_image.id
  key_name          = cloudplatform_compute_keypair.key.id
  metadata = {}

  lifecycle {
    create_before_destroy = true
  }
}

# DNS CNAME Record
resource "cloudplatform_dns_cname_record_v2" "dns-alias" {
  name    = var.dns_name
  target  = cloudplatform_slb_vip_v1.service_vip.fqdn
  zone_id = data.cloudplatform_dns_zone.fr_world_socgen.id
}

# Output IP Address
output "ip" {
  value = cloudplatform_compute_instance.vm.ipv4
}
