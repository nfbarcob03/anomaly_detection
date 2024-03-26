from playwright.async_api import APIRequestContext, async_playwright
import pytest
import api_ms_anomaly_detection as api_encpoints
@pytest.fixture()
async def api_request_context():
    async with async_playwright() as p:
        request_context = await p.request.new_context(base_url=\
        "http://localhost:8000")
        yield request_context
        request_context.dispose()

##async def test_full_flow_scenario(api_request_context: APIRequestContext):
async def test_get_HistoricalPricingByIdItem(api_request_context: APIRequestContext):
    # Create a new repository

    response = await api_encpoints.test_historicalPricingByIdItem( \
                                api_request_context=api_request_context,
                                item_id='MLB4432316952'
                                )
    assert response.status == 200
    respose_boyd = await response.body()
    respose_boyd = str(respose_boyd)
    assert 'item_id' in respose_boyd
    assert 'ord_closed_dt' in respose_boyd
    assert 'price' in respose_boyd

async def test_post_DetectAnomaly(api_request_context: APIRequestContext):
    # Update name and description of the repository
    response = await api_encpoints.test_detectAnomaly(\
                                api_request_context=api_request_context,
                                item_id='MLB4432316952', price = 200
                                )
    assert response.status == 200
    

async def test_post_DetectAnomaly_not_found(api_request_context: APIRequestContext):
    # Update name and description of the repository
    response = await api_encpoints.test_detectAnomaly(\
                                api_request_context=api_request_context,
                                item_id='111', price = 200
                                )
    assert response.status == 404
    response_body = await response.body()
    print(response_body)
    assert 'No existe el item_id en el historico de precios' in str(response_body)

async def test_post_cargarCsvHistorico(api_request_context: APIRequestContext):
    # Update name and description of the repository
    response = await api_encpoints.test_cargarCsvHistorico(\
                                api_request_context=api_request_context,
                                path_csv = 'data.csv',
                                tag_file = 'archivo_csv'
                                )
    assert response.status == 201
    response_body = await response.body()
    print(response_body)
    assert 'Datos insertados correctamente' in str(response_body)

async def test_post_cargarCsvHistorico_notfile(api_request_context: APIRequestContext):
    # Update name and description of the repository
    response = await api_encpoints.test_cargarCsvHistorico(\
                                api_request_context=api_request_context,
                                path_csv = 'data.csv',
                                tag_file = 'archivo_csvvv'
                                )
    assert response.status == 400
    response_body = await response.body()
    print(response_body)
    assert 'Se requiere un archivo CSV' in str(response_body)
