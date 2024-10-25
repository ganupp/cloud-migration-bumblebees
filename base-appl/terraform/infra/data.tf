# Data resource for compute flavor
data "cloudplatform_compute_flavor" "flavor" {
  name = lookup(var.flavor, "${var.app_environment}")
}

# Data resource for compute image
data "cloudplatform_compute_image" "infra_image" {
  name   = "${var.app_name}_image_${var.app_environment}"
  latest = true
}

# Data resource for network
data "cloudplatform_compute_network" "network_name" {
  name = var.network
}

# Data resource for DNS zone
data "cloudplatform_dns_zone" "fr-world-socgen" {
  name = "fr.world.socgen"
}
