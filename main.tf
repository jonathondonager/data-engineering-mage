terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "5.14.0"
    }
  }
}
 
provider "google" {
  credentials = file(var.credential)
  project     = var.project
  region      = var.region
}

resource "google_storage_bucket" "demo-bucket" {
  name          = var.gcs_bucket_name
  location      = var.location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_service_account" "sa" {
  account_id   = var.service-account-id
  display_name = var.service-account-display
}

resource "google_bigquery_dataset" "demo_dataset" {
  dataset_id                  = "demo_dataset"
  friendly_name               = "demo"
  description                 = "This is a test description"
  location                    = var.location
  delete_contents_on_destroy  = true
  project                     = var.project

}
