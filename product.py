{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "6ff5fd02-8054-464b-b36e-10fdf79dc732",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Initialize a new product with a product name, product ID, and premium amount\n",
    "class Product:\n",
    "    def __init__(self, product_name, product_id, premium):        \n",
    "        self.product_name = product_name\n",
    "        self.product_id = product_id\n",
    "        self.premium = premium\n",
    "        self.is_available = True  # The product is available by default\n",
    "    \n",
    "    # Method to create a new product\n",
    "    def create_product(self):        \n",
    "        print(f\"Product {self.product_name} with ID {self.product_id} has been created.\")\n",
    "    \n",
    "    # Method to update the product's name and premium amount\n",
    "    def update_product(self, new_name=None, new_premium=None):        \n",
    "        if new_name:\n",
    "            self.product_name = new_name\n",
    "        if new_premium:\n",
    "            self.premium = new_premium\n",
    "        print(f\"Product {self.product_name} with ID {self.product_id} has been updated.\")\n",
    "    \n",
    "    # Method to suspend a product. This makes it unavailable\n",
    "    def suspend_product(self):        \n",
    "        self.is_available = False\n",
    "        print(f\"Product {self.product_name} with ID {self.product_id} has been suspended.\")\n",
    "    \n",
    "    # Method to get the details of the product\n",
    "    def get_details(self):        \n",
    "        status = \"Available\" if self.is_available else \"Suspended\"\n",
    "        return f\"Product Name: {self.product_name}, Product ID: {self.product_id}, Premium: ${self.premium}, Status: {status}\""
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
