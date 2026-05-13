from locust import HttpUser, task, between
from random import randint


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task(2)
    def view_products(self):
        print('View property')
        collection_id = randint(2, 6)
        self.client.get(
            f'/estate/properties /?collection_id={collection_id}', name='/home/properties')

    @task(4)
    def view_property(self):
        print('View property details')
        property_id = randint(1, 1000)
        self.client.get(f'/estate/property/{property_id}',
                        name='/estate/properties/:id')

    @task(1)
    def add_to_cart(self):
        print('Add to cart')
        property_id = randint(1, 10)
        self.client.post(
            f'/estate/carts/{self.cart_id}/items',
            name='/estate/carts/items',
            json={'property_id': property_id, 'quantity': 1}
        )

    def on_start(self):
        response = self.client.post('/estate/carts')
        result = response.json()
        self.cart_id = result['id']
