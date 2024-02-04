// Define the resource group
resource "azurerm_resource_group" "example" {
  name     = "example-resource-group"
  location = "West Europe"
}

// Define the resource
resource "azurerm_resource" "resource1" {
  name                  = "resource1"
  resource_group_name   = azurerm_resource_group.example.name
  location              = azurerm_resource_group.example.location
  // Add more configuration options for the resource here
}
