from locust import HttpUser, task
class WebsiteUser(HttpUser): 
    
    @task 
    def hello_world(self): 
        self.client.get(url='/')
    # @task 
    # def square_numbers(self): 
    #     self.client.get(url='/add') 
    
    # @task 
    # def cube_numbers(self): 
    #     self.client.get(url='/update')

    # @task 
    # def cube_numbers(self): 
    #     self.client.get(url='/update')