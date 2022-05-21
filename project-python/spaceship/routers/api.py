from fastapi import APIRouter
import numpy as np

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}


@router.get('/matrices')
def create_matrices() -> dict:
    first_matrix = np.random.rand(10, 10)
    second_matrix = np.random.rand(10, 10)
    product = np.matmul(first_matrix, second_matrix)
    
    return {
        'matrix_a': first_matrix.tolist(),
        'matrix_b': second_matrix.tolist(),
        'product': product.tolist()
        }
