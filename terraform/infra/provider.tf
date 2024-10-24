terraform {
  required_providers {
    cloudplatform = {
      source = "tfregistry.cloud.socgen/gts/cloudplatform"
    }
  }
}

provider "cloudplatform" {
  region       = "eu-fr-peris"
  account_id   = var.account_id
  client_id    = var.client_id
  client_s = var.client_s
}
