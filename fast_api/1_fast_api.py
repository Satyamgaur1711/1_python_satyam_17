from fastapi import FastAPI
from pydantic import BaseModel

class product(BaseModel):
    name : str
    price : float


app = FastAPI()

@app.post("/add-product/")
def create_product(item: Product):
    # 'item: Product' likhne se FastAPI samajh gaya ki Request Body 'Product' class jaisi hogi.
    
    # Ab 'item' ke andar wo saara data aa gaya hai jo user ne bheja tha.
    # Hum use easily access kar sakte hain:
    final_price = item.price + 50.0  # Maan lijiye 50 rs delivery charge hai
    
    # API ke end mein hum response return karte hain
    return {
        "message": f"Success! {item.name} add ho gaya hai.",
        "total_cost": final_price
    }

