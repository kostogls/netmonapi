from pydantic import BaseModel


class AsnData(BaseModel):
    ASN: int
    AS_rank_rank: str
    AS_rank_source: str
    AS_rank_longitude: str
    AS_rank_latitude: str
    AS_rank_numberAsns: str
    AS_rank_numberPrefixes: str
    AS_rank_numberAddresses: str
    AS_rank_total: str
    AS_rank_customer: str
    AS_rank_peer: str
    AS_rank_provider: str
    AS_rank_iso: str
    AS_rank_continent: str
    is_personal_AS: str
    peeringDB_info_ratio: str
    peeringDB_info_traffic: str
    peeringDB_info_scope: str
    peeringDB_info_type: str
    peeringDB_info_prefixes4: str
    peeringDB_info_prefixes6: str
    peeringDB_policy_general: str
    peeringDB_ix_count: str
    peeringDB_fac_count: str
    peeringDB_created: str
    is_in_peeringDB: str
    AS_hegemony: str
    nb_atlas_probes_v4: str
    nb_atlas_probes_v6: str
    nb_atlas_anchors: str
    is_ris_peer_v4: str
    is_ris_peer_v6: str
    is_routeviews_peer: str
    AS_rel_degree: str
    cti_top: str
    cti_origin: str
    ASDB_C1L1: str
    ASDB_C1L2: str


class PrecalcBias(BaseModel):
    AS_rank_source: str
    AS_rank_iso: str
    AS_rank_continent: str
    AS_rank_numberAsns: str
    AS_rank_numberPrefixes: str
    AS_rank_numberAddresses: str
    AS_hegemony: str
    AS_rank_total: str
    AS_rank_peer: str
    AS_rank_customer: str
    AS_rank_provider: str
    peeringDB_ix_count: str
    peeringDB_fac_count: str
    peeringDB_policy_general: str
    peeringDB_info_type: str
    peeringDB_info_ratio: str
    peeringDB_info_traffic: str
    peeringDB_info_scope: str
    is_personal_AS: str
    list_name: str


class DiffInBias(BaseModel):
    Location_bias: str
    Network_size_bias: str
    Topology_bias: str
    IXP_related_bias: str
    Network_type_bias: str
    RIR_region: str
    Customer_cone_num_ASNs: str
    Customer_cone_num_prefixes: str
    Location_country: str
    num_neighbors_total: str
    Scope_PeeringDB: str
    Network_type_PeeringDB: str
    Peering_policy_PeeringDB: str
    IXPs_PeeringDB: str
    num_facilities_PeeringDB: str
    is_in_peeringDB: str
    nb_atlas_probes_v4: str
    nb_atlas_probes_v6: str
    is_routeviews_peer: str
    kind: str





