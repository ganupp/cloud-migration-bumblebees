# Disk monitoring rule
resource "cloudplatform_monitoring_rule_ve" "disk_rule" {
  description   = "disk_rule"
  metric_family = "disk"
  metric_name   = "used_percent"
  operator      = ">"
  resource_id   = cloudplatform_compute_instance.vm.id
  severity      = "CRITICAL"
  threshold     = "70"
}

# Disk monitoring subscription
resource "cloudplatform_monitoring_subscription_ve" "my_subscription" {
  email         = ["praveen.gaddam@socgen.com"]
  metric_family = cloudplatform_monitoring_rule_ve.disk_rule.metric_family
  metric_name   = cloudplatform_monitoring_rule_ve.disk_rule.metric_name
  resource_id   = cloudplatform_monitoring_rule_ve.disk_rule.resource_id
  severities    = [cloudplatform_monitoring_rule_ve.disk_rule.severity]
}

# CPU monitoring rule
resource "cloudplatform_monitoring_rule_ve" "cpu_rule" {
  description   = "cpu_rule"
  metric_family = "cpu"
  metric_name   = "usage_idle"
  operator      = "<"
  resource_id   = cloudplatform_compute_instance.vm.id
  severity      = "CRITICAL"
  threshold     = "15"
}

# CPU monitoring subscription
resource "cloudplatform_monitoring_subscription_ve" "cpu_subscription" {
  email         = ["praveen.gaddam@socgen.com"]
  metric_family = cloudplatform_monitoring_rule_ve.cpu_rule.metric_family
  metric_name   = cloudplatform_monitoring_rule_ve.cpu_rule.metric_name
  resource_id   = cloudplatform_monitoring_rule_ve.cpu_rule.resource_id
  severities    = [cloudplatform_monitoring_rule_ve.cpu_rule.severity]
}
