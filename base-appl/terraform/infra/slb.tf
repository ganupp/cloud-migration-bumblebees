# Subnet for the Load Balancer
data "cloudplatform_slb_subnet" "slb_subnet" {
  network_name      = var.network
  availability_zone = var.availability_zone
}

# Load Balancer configuration
data "cloudplatform_slb_load_balancer" "default" {
  availability_zone = var.availability_zone
  name              = "default"
}

# SSL Profile for Load Balancer
data "cloudplatform_slb_ssl_profile" "high" {
  name = "sg-high-2019-november"
}

# VIP Resource for the Service
resource "cloudplatform_slb_vip_v1" "service_vip" {
  name            = "${var.app_name}-${var.availability_zone}-vip-${var.app_environment}"
  loadbalancer_id = data.cloudplatform_slb_load_balancer.default.id
  subnet_id       = data.cloudplatform_slb_subnet.slb_subnet.id
}

# Health Check Configuration for the Service
resource "cloudplatform_slb_healthcheck_v1" "service_healthcheck" {
  name              = "${var.app_name}-${var.availability_zone}-health-${var.app_environment}"
  loadbalancer_id   = data.cloudplatform_slb_load_balancer.default.id
  health_check_type = "STANDARD"
  protocol          = "TCP"
  port              = 9000
}

# Pool Configuration
resource "cloudplatform_slh_pool_vi" "service_pool" {
  name              = "${var.app_name}-${var.availability_zone}-pool-${var.app_environment}"
  loadbalancer_id   = data.cloudplatform_slb_load_balancer.default.id
  persistence       = "COOKIE"
  healthcheck_id    = cloudplatform_slb_healthcheck_v1.service_healthcheck.id
  ssl_profile_id    = data.cloudplatform_slb_ssl_profile.high.id
  real_server_ids   = cloudplatform_compute_instance.vm.id
}

# Listener for the Load Balancer
resource "cloudplatform_slb_listener_v1" "service_listener" {
  name             = "${var.app_name}-${var.availability_zone}-listener-${var.app_environment}"
  loadbalancer_id  = data.cloudplatform_slb_load_balancer.default.id
  vip_id           = cloudplatform_slb_vip_v1.service_vip.id
  pool_id          = cloudplatform_slh_pool_vi.service_pool.id
  port             = 443
  protocol         = "HTTPS"
  xff              = true
  ssl_profile_id   = data.cloudplatform_slb_ssl_profile.high.id
  certificate_id   = cloudplatform_slb_certificate_vi.certificate.id
}

# Secret for the SSL Certificate
data "cloudplatform_secret_generic_secret" "path_to_certificate" {
  path = "${var.account_id}/private/CRS/${var.app_environment}/path_to_certificate"
}

data "cloudplatform_secret_generic_secret" "certificate" {
  path = element(split("/secret/data/", data.cloudplatform_secret_generic_secret.path_to_certificate.data.vault_path), 1)
}

# SSL Certificate Resource
resource "cloudplatform_slb_certificate_vi" "certificate" {
  name         = "${var.app_name}-${var.app_environment}"
  certificate  = data.cloudplatform_secret_generic_secret.certificate.data.certificate_pem
  private_key  = data.cloudplatform_secret_generic_secret.certificate.data.private_key
  passphrase   = data.cloudplatform_secret_generic_secret.certificate.data.passphrase
  loadbalancer_id = data.cloudplatform_slb_load_balancer.default.id
}
