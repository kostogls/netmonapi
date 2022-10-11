import pandas as pd
import numpy as np

# FOR PRECALCULATED
# ripe_ris_plus_rcc = '../.././use_cases/bias_in_monitoring_infrastructure/data/bias_values_per_rrc.csv'
# ripe_atlas_views_ris_wviews = '../.././use_cases/bias_in_monitoring_infrastructure/data/precalculated_bias_4.csv'
# saved_df_name = '../.././use_cases/bias_in_monitoring_infrastructure/data/precalculated_bias.csv'
# df2 = pd.read_csv(ripe_ris_plus_rcc, header=0, index_col=0)
# df1 = pd.read_csv(ripe_atlas_views_ris_wviews, header=0, index_col=0)
#
# f_df = pd.concat([df1, df2], axis=1)
# tr_df = f_df.T
# print(tr_df)
# tr_df['list_name'] = tr_df.index
# print(tr_df)
# tr_df.to_csv(saved_df_name, header=True, index=True)

# FOR DIFFERENCE

diff_Atlas = '../.././use_cases/ripe_ris_extension/data/bias_df__no_stubs_Atlas_groups.csv'
diff_RIS = '../.././use_cases/ripe_ris_extension/data/bias_df__no_stubs_RIS_groups.csv'

saved_diff_df_name_atlas = '../.././use_cases/ripe_ris_extension/data/diff_in_bias_Atlas.csv'
saved_diff_df_name_ris = '../.././use_cases/ripe_ris_extension/data/diff_in_bias_RIS.csv'
diff_Atlas_df = pd.read_csv(diff_Atlas, header=0, index_col=0)
diff_RIS_df = pd.read_csv(diff_RIS, header=0, index_col=0)
diff_Atlas_df['Improvement proximity'] = np.nan
diff_Atlas_df['kind'] = 'Atlas'

diff_RIS_df['kind'] = 'RIS'

# rename column
diff_Atlas_df.columns = ['Location_bias','Network_size_bias','Topology_bias', 'IXP_related_bias', 'Network_type_bias','RIR_region','Customer_cone_num_ASNs','Customer_cone_num_prefixes', 'Location_country','num_neighbors_total', 'Scope_PeeringDB', 'Network_type_PeeringDB', 'Peering_policy_PeeringDB','IXPs_PeeringDB','num_facilities_PeeringDB','is_in_peeringDB','nb_atlas_probes_v4','nb_atlas_probes_v6','is_routeviews_peer','Improvement_proximity','kind']
diff_RIS_df.columns = ['Location_bias','Network_size_bias','Topology_bias', 'IXP_related_bias', 'Network_type_bias','RIR_region','Customer_cone_num_ASNs','Customer_cone_num_prefixes', 'Location_country','num_neighbors_total', 'Scope_PeeringDB', 'Network_type_PeeringDB', 'Peering_policy_PeeringDB','IXPs_PeeringDB','num_facilities_PeeringDB','is_in_peeringDB','nb_atlas_probes_v4','nb_atlas_probes_v6','is_routeviews_peer','Improvement_proximity','kind']

# f_df_diff = pd.concat([diff_Atlas_df, diff_RIS_df], axis=1)
print(diff_Atlas_df)
diff_Atlas_df.to_csv(saved_diff_df_name_atlas, header=True, index=True)
diff_RIS_df.to_csv(saved_diff_df_name_ris, header=True, index=True)
