from typing import List, Union

import uvicorn
from fastapi import FastAPI, HTTPException, Query
from fastapi_pagination import Page, add_pagination, paginate

from .api.db_connection import connect_db
from .api.response_model import AsnData, DiffInBias, PrecalcBias
from .project_files.calculate_bias_for_list import calc_bias

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/asns", response_model=Page[AsnData])
async def get_asns():
    db = connect_db()
    aggregated_dataframe = db.get_collection("aggregated_dataframe")
    return paginate(list(aggregated_dataframe.find()))


@app.get("/asn/{ASN}", response_model=AsnData)
def get_asn(ASN: int):
    db = connect_db()
    aggregated_dataframe = db.get_collection("aggregated_dataframe")
    result = aggregated_dataframe.find_one({"ASN": ASN})
    if result is None:
        raise HTTPException(status_code=404, detail='Item not found.')
    return result


@app.get("/bias/")
async def get_bias(asn: Union[List[int], None] = Query(default=None)):
    bias_list, non_exist_asns = calc_bias(asn)
    if not non_exist_asns[1]:
        return bias_list
    else:
        return bias_list, non_exist_asns


@app.get("/bias/{imp}", response_model=PrecalcBias)
def get_precalc_bias(imp: str):
    db = connect_db()
    precalc_df = db.get_collection("precalc")
    result = precalc_df.find_one({"list_name": imp})
    if result is None:
        raise HTTPException(status_code=404, detail='Item not found.')
    return result


@app.get("/bias_diff/{set}", response_model=Page[DiffInBias])
def get_diff_bias(set: str):
    db = connect_db()
    diff_df = db.get_collection("biasdiff")
    result = list(diff_df.find({"kind": set}))
    if result is None:
        raise HTTPException(status_code=404, detail='Item not found.')
    return paginate(result)


add_pagination(app)


# if __name__ == '__main__':
#     uvicorn.run("main:app", reload=True)

