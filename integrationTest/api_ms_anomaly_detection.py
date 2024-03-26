from playwright.async_api import APIRequestContext


async def test_historicalPricingByIdItem(api_request_context: APIRequestContext, \
                                item_id: str):
    return await api_request_context.get(
        "/historicalPricingByIdItem/" + str(item_id),
        headers={
            "Accept": "*/*",
        }
    )

async def test_detectAnomaly(api_request_context: APIRequestContext, \
                                item_id: str, price: float):
    return await api_request_context.post(
        "/detectAnomaly",
        headers={
            "Accept": "*/*",
        },
        data={"price": price, "item_id": item_id},
    )

async def test_cargarCsvHistorico(api_request_context: APIRequestContext, \
                                path_csv: str, tag_file:str):
    
    with open(path_csv, 'rb') as file:
        csv_content = file.read()

    return await api_request_context.post(
        "/cargarCsvHistorico",
        headers={
            "Accept": "*/*",
        },
       multipart={
            tag_file: {
                'name': tag_file,
                'buffer': csv_content,
                'mimeType': 'text/csv'  # Define el tipo MIME explicitamente
            }
        }
    )