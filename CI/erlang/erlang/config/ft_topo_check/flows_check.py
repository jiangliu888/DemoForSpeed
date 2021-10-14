CR8550_ER8022_CPE16192_CR8566_ER8038_CPE16208_POP_TO_CPE_Flows = \
    [{'local': 8550, 'route': [{'target': 16192, 'next': 8022}, {'target': 16208, 'next': 8566}]},
     {'local': 8566, 'route': [{'target': 16192, 'next': 8550}, {'target': 16208, 'next': 8038}]},
     {'local': 8022, 'route': [{'target': 16208, 'next': 8550}]},
     {'local': 8038, 'route': [{'target': 16192, 'next': 8566}]}]

Add_CPE16224_IN_ER8566_POP_Flows = \
    [{'local': 8550, 'route': [{'target': 16224, 'next': 8566}]}]

CR8550_CR8566_CPE16192_CPE16208_POP_TO_CPE_Flows = \
    [{'local': 8550, 'route': [{'target': 16208, 'next': 8566}]},
     {'local': 8566, 'route': [{'target': 16192, 'next': 8550}]}]

CR8550_CR8566_CPE16192_change16224_CPE16208_POP_TO_CPE_Flows = \
    [{'local': 8550, 'route': [{'target': 16208, 'next': 8566}]},
     {'local': 8566, 'route': [{'target': 16224, 'next': 8550}]}]

CR8550_CR8566_CPE16192_CPE17009_CPE17026_CPE17043_POP_TO_CPE_Flows = \
    [{'local': 8550, 'route': [{'target': 17026, 'next': 8566}, {'target': 17043, 'next': 8566}]},
     {'local': 8566, 'route': [{'target': 16192, 'next': 8550}, {'target': 17009, 'next': 8550}]}]

CR8550_CR8566_CPE17009_CPE17026_CPE17043_POP_TO_CPE_Flows = \
    [{'local': 8550, 'route': [{'target': 17026, 'next': 8566}, {'target': 17043, 'next': 8566}]},
     {'local': 8566, 'route': [{'target': 17009, 'next': 8550}]}]

CR8550_CR8566_CPE17026_CPE17043_POP_TO_CPE_Flows = \
    [{'local': 8550, 'route': [{'target': 17043, 'next': 8566}]},
     {'local': 8566, 'route': [{'target': 17026, 'next': 8550}]}]

CR8550_CR8566_ER8038_CPE16192_POP_TO_CPE_Flows = \
    [{'local': 8550, 'route': [{'target': 16192, 'next': 8566}]},
     {'local': 8566, 'route': [{'target': 16192, 'next': 8038}]}]

CR8550_CR8566_CPE16192_POP_TO_CPE_Flows = \
    [{'local': 8550, 'route': [{'target': 16192, 'next': 8566}]}]

CR8550_CR8566_ER8038_CPE16192_Prefer_5_1_POP_TO_CPE_Flows = \
    [{'local': 8550, 'route': [{'target': 16192, 'next': 8566}]},
     {'local': 8038, 'route': [{'target': 16192, 'next': 8566}]}]

CR8550_CR8566_ER8038_CPE16192_Prefer_5_1_addCPE16208_POP_TO_CPE_Flows = \
    [{'local': 8550, 'route': [{'target': 16192, 'next': 8566}, {'target': 16208, 'next': 8566}]},
     {'local': 8566, 'route': [{'target': 16208, 'next': 8038}]},
     {'local': 8038, 'route': [{'target': 16192, 'next': 8566}]}]

CR8550_CR8566_ER8038_Maintain_CPE16192_POP_TO_CPE_Flows = \
    [{'local': 8550, 'route': [{'target': 16192, 'next': 8566}]},
     {'local': 8566, 'route': [{'target': 16192, 'next': 16192}]}]

CR8550_CR8566_ER8038_CPE16192_Prefer_4_1_POP_TO_CPE_Flows = \
    [{'local': 8566, 'route': [{'target': 16192, 'next': 8550}]},
     {'local': 8038, 'route': [{'target': 16192, 'next': 8566}]}]

CR8550_CR8566_ER8038_CPE16192_CPE16208_CR8582_POP_TO_CPE_Flows = \
    [{'local': 8550, 'route': [{'target': 16192, 'next': 8566}, {'target': 16208, 'next': 8566}]},
     {'local': 8566, 'route': [{'target': 16192, 'next': 8038}, {'target': 16208, 'next': 8038}]},
     {'local': 8582, 'route': [{'target': 16192, 'next': 8566}, {'target': 16208, 'next': 8566}]}]

CR8550_ER8022_CPE16192_CR8566_CPE16208_POP_TO_CPE_Flows = \
    [{'local': 8550, 'route': [{'target': 16192, 'next': 8022}, {'target': 16208, 'next': 8566}]},
     {'local': 8566, 'route': [{'target': 16192, 'next': 8550}]},
     {'local': 8022, 'route': [{'target': 16208, 'next': 8550}]}]

CR8550_ER8022_ER8038_CPE16192_POP_TO_CPE_Flows = \
    [{'local': 8550, 'route': [{'target': 16192, 'next': 8038}]},
     {'local': 8022, 'route': [{'target': 16192, 'next': 8038}]}]

CR13350_CR13366_ER12838_CPE20992_with_group_POP_TO_CPE_Flows = \
    [{'local': 13350, 'route': [{'target': 20992, 'next': 12838}]},
     {'local': 13366, 'route': [{'target': 20992, 'next': 12838}]}]

CR13350_CR13366_grp1_4_ER12838_grp1_2_3_CPE20992_POP_TO_CPE_Flows = \
    [{'local': 13350, 'route': [{'target': 20992, 'next': 12838}]},
     {'local': 13366, 'route': [{'target': 20992, 'next': 12838}]}]

CR13350_CR13366_grp1_4_ER12838_grp1_2_3_CPE20992_grp4_POP_TO_CPE_Flows = \
    [{'local': 13350, 'route': [{'target': 20992, 'next': 13366}]},
     {'local': 12838, 'route': [{'target': 20992, 'next': 13366}]}]

CR13350_CR13366_grp1_2_ER12838_grp1_2_3_CPE20992_grp4_POP_TO_CPE_Flows = \
    [{'local': 13366, 'route': [{'target': 20992, 'next': 13350}]},
     {'local': 12838, 'route': [{'target': 20992, 'next': 13350}]}]

CR8550_ER8022_ADD_ER8038_CPE16192_CPE16208_POP_TO_CPE_Flows = \
    [{'local': 8550, 'route': [{'target': 16192, 'next': 8022}, {'target': 16208, 'next': 8038}]},
     {'local': 8022, 'route': [{'target': 16208, 'next': 8038}]},
     {'local': 8038, 'route': [{'target': 16192, 'next': 8022}]}]

CR8550_ER8022_CPE16192_POP_TO_CPE_Flows = \
    [{'local': 8550, 'route': [{'target': 16192, 'next': 8022}]}]

CR8550_CR8566_ER8038_CPE16192_ADD_CR8582_POP_TO_CPE_Flows = \
    [{'local': 8582, 'route': [{'target': 16192, 'next': 8566}]}]

CR8550_CPE16192_CPE16208_POP_TO_CPE_Flows = \
    []

UN16192_16208_CPE_Flows = \
    [{'local': 16192, 'route': [{'target': 16208, 'target_ip': '10.5.22.1'}]},
     {'local': 16208, 'route': [{'target': 16192, 'target_ip': '10.4.21.1'}]}]

UN16192_change16224_16208_CPE_Flows = \
    [{'local': 16224, 'route': [{'target': 16208, 'target_ip': '10.5.22.1'}]},
     {'local': 16208, 'route': [{'target': 16224, 'target_ip': '10.4.20.1'}]}]

UN16192_17009_UN16192_17026_UN16192_17043_CPE_Flows = \
    [{'local': 16192, 'route': [{'target': 17009, 'target_ip': '10.50.3.0/24'}, {'target': 17026, 'target_ip': '10.50.5.0/24'}, {'target': 17043, 'target_ip': '10.50.6.0/24'}]},
     {'local': 17009, 'route': [{'target': 16192, 'target_ip': '10.50.1.0/24'}]},
     {'local': 17026, 'route': [{'target': 16192, 'target_ip': '10.50.1.0/24'}]},
     {'local': 17043, 'route': [{'target': 16192, 'target_ip': '10.50.1.0/24'}]}]

UN17009_17026_UN17009_17043_CPE_Flows = \
    [{'local': 17009, 'route': [{'target': 17026, 'target_ip': '10.50.5.0/24'}, {'target': 17043, 'target_ip': '10.50.6.0/24'}]},
     {'local': 17026, 'route': [{'target': 17009, 'target_ip': '10.50.3.0/24'}]},
     {'local': 17043, 'route': [{'target': 17009, 'target_ip': '10.50.3.0/24'}]}]

UN17009_17026_UN17009_17043_Add_route_CPE_Flows = \
    [{'local': 17009, 'route': [{'target': 17026, 'target_ip': '10.50.5.0/24'}, {'target': 17043, 'target_ip': '10.50.6.0/24'}]},
     {'local': 17026, 'route': [{'target': 17009, 'target_ip': '10.50.3.0/24'}, {'target': 17009, 'target_ip': '1.1.1.0/24', 'src': '10.50.0.0/16'}]},
     {'local': 17043, 'route': [{'target': 17009, 'target_ip': '10.50.3.0/24'}]}]

UN17009_17026_UN17009_17043_Add_17026_17043_route_CPE_Flows = \
    [{'local': 17009, 'route': [{'target': 17026, 'target_ip': '10.50.5.0/24'}, {'target': 17043, 'target_ip': '10.50.6.0/24'}]},
     {'local': 17026, 'route': [{'target': 17009, 'target_ip': '10.50.3.0/24'}, {'target': 17009, 'target_ip': '10.50.6.0/24', 'src': '10.50.5.0/24'}]},
     {'local': 17043, 'route': [{'target': 17009, 'target_ip': '10.50.3.0/24'}]}]

UN17026_17043_CPE_Flows = \
    [{'local': 17026, 'route': [{'target': 17043, 'target_ip': '10.50.6.0/24'}]},
     {'local': 17043, 'route': [{'target': 17026, 'target_ip': '10.50.5.0/24'}]}]

UN17009_17026_CPE_Flows = \
    [{'local': 17026, 'route': [{'target': 17009, 'target_ip': '10.50.3.0/24'}, {'target': 17009, 'target_ip': '1.1.1.0/24', 'src': '10.50.0.0/16'}]}]

UN16192_16208_UN16192_16224_CPE_Flows = \
    [{'local': 16208, 'route': [{'target': 16192, 'target_ip': '10.4.21.1'}]},
     {'local': 16192, 'route': [{'target': 16208, 'target_ip': '10.5.22.1'}, {'target': 16224, 'target_ip': '10.5.23.1'}]},
     {'local': 16224, 'route': [{'target': 16192, 'target_ip': '10.4.21.1'}]}]

CR10150_CPE17792_CR10166_CR10182_CPE17808_POP_TO_CPE_Flows = \
    [{'local': 10150, 'route': [{'target': 17808, 'next': 10182}]},
     {'local': 10166, 'route': [{'target': 17792, 'next': 10150}, {'target': 17808, 'next': 10182}]},
     {'local': 10182, 'route': [{'target': 17792, 'next': 10150}]}]

UN17792_17808_CPE_Flows = \
    [{'local': 17792, 'route': [{'target': 17808, 'target_ip': '10.6.22.1'}]},
     {'local': 17808, 'route': [{'target': 17792, 'target_ip': '10.4.21.1'}]}]

CR10150_CPE17792_CR10166_CR10182_loss_CPE17808_POP_TO_CPE_Flows = \
    [{'local': 10150, 'route': [{'target': 17808, 'next': 10166}]},
     {'local': 10166, 'route': [{'target': 17792, 'next': 10150}, {'target': 17808, 'next': 10182}]},
     {'local': 10182, 'route': [{'target': 17792, 'next': 10166}]}]

CR10150_CPE17792_CR10166_CR10182_Abnormal_CPE17808_POP_TO_CPE_Flows = \
    [{'local': 10150, 'route': [{'target': 17792, 'next': 17792}, {'target': 17808, 'next': 10166}]},
     {'local': 10166, 'route': [{'target': 17792, 'next': 10150}, {'target': 17808, 'next': 17808}]}]

CR8550_CR8566_POP_Flows = \
    [{'local': 8550, 'route': [{'target': 8566, 'next': 8566}]},
     {'local': 8566, 'route': [{'target': 8550, 'next': 8550}]}]

CR10150_ER9622_POP_Flows_NoPath_Change = \
    [{'local': 9622, 'target': 10150, 'port_pairs': [(1, 2), (2, 2)]},
     {'local': 10150, 'target': 9622, 'port_pairs': [(1, 2), (2, 2)]}]

CR8550_CR8566_CR8582_POP_Flows = \
    [{'local': 8550, 'route': [{'target': 8566, 'next': 8566}, {'target': 8582, 'next': 8582}]},
     {'local': 8566, 'route': [{'target': 8550, 'next': 8550}, {'target': 8582, 'next': 8582}]},
     {'local': 8582, 'route': [{'target': 8566, 'next': 8566}, {'target': 8550, 'next': 8550}]}]

CR10150_ER9622_POP_Flows = \
    [{'local': 10150, 'route': [{'target': 9622, 'next': 9622}]},
     {'local': 9622, 'route': [{'target': 10150, 'next': 10150}]}]

CR8550_CR8566_ER8038_CPE16192_CPE16208_POP_TO_CPE_Flows = \
    [{'local': 8550, 'route': [{'target': 16192, 'next': 8566}, {'target': 16208, 'next': 8566}]},
     {'local': 8566, 'route': [{'target': 16192, 'next': 8038}, {'target': 16208, 'next': 8038}]}]

CR8550_ER8038_CPE16192_POP_TO_CPE_Flows = \
    [{'local': 8550, 'route': [{'target': 16192, 'next': 8038}]}]

CR8550_ER8022_ER8038_CR8566_POP_Flows = \
    [{'local': 8550, 'route': [{'target': 8566, 'next': 8566}, {'target': 8022, 'next': 8022}, {'target': 8038, 'next': 8038}]},
     {'local': 8022, 'route': [{'target': 8550, 'next': 8550}, {'target': 8566, 'next': 8550}, {'target': 8038, 'next': 8038}]},
     {'local': 8566, 'route': [{'target': 8550, 'next': 8550}, {'target': 8022, 'next': 8550}, {'target': 8038, 'next': 8550}]},
     {'local': 8038, 'route': [{'target': 8550, 'next': 8550}, {'target': 8566, 'next': 8550}, {'target': 8022, 'next': 8022}]}]

CR8550_ER8038_CR8566_POP_Flows = \
    [{'local': 8550, 'route': [{'target': 8566, 'next': 8566}, {'target': 8038, 'next': 8038}]},
     {'local': 8566, 'route': [{'target': 8550, 'next': 8550}, {'target': 8038, 'next': 8550}]},
     {'local': 8038, 'route': [{'target': 8550, 'next': 8550}, {'target': 8566, 'next': 8550}]}]

CR8550_ER8022_ER8038_ER8054_POP_Flows = \
    [{'local': 8550, 'route': [{'target': 8022, 'next': 8022}, {'target': 8038, 'next': 8038}, {'target': 8054, 'next': 8054}]},
     {'local': 8022, 'route': [{'target': 8550, 'next': 8550}, {'target': 8038, 'next': 8550}, {'target': 8054, 'next': 8550}]},
     {'local': 8038, 'route': [{'target': 8550, 'next': 8550}, {'target': 8022, 'next': 8022}, {'target': 8054, 'next': 8054}]},
     {'local': 8054, 'route': [{'target': 8550, 'next': 8550}, {'target': 8022, 'next': 8022}, {'target': 8038, 'next': 8038}]}]

CR8550_ER8022_POP_Flows = \
    [{'local': 8550, 'route': [{'target': 8022, 'next': 8022}]},
     {'local': 8022, 'route': [{'target': 8550, 'next': 8550}]}]

CR13350_ER12838_CR13366_POP_Flows = \
    [{'local': 13350, 'route': [{'target': 13366, 'next': 13366}, {'target': 12838, 'next': 12838}]},
     {'local': 13366, 'route': [{'target': 13350, 'next': 13350}, {'target': 12838, 'next': 12838}]},
     {'local': 12838, 'route': [{'target': 13350, 'next': 13350}, {'target': 13366, 'next': 13366}]}]

CR8550_SAAS8584_POP_TO_Service_Flows = \
    [{'local': 8550, 'route': [{'target': 8584, 'next': 8584}]}]

CR8550_CR8566_SAAS8584_POP_TO_Service_Flows = \
    [{'local': 8566, 'route': [{'target': 8584, 'next': 8584}]},
     {'local': 8550, 'route': []}]

CR8550_SAAS8584_CR8566_SAAS8600_POP_TO_Service_Flows = \
    [{'local': 8566, 'route': [{'target': 8600, 'next': 8600}]},
     {'local': 8550, 'route': [{'target': 8584, 'next': 8584}]}]

CR8550_ANY8535_POP_TO_Service_Flows = \
    [{'local': 8550, 'route': [{'target': 8535, 'next': 8535}]}]

CR8550_CR8566_ANY8535_POP_TO_Service_Flows = \
    [{'local': 8566, 'route': [{'target': 8535, 'next': 8535}]},
     {'local': 8550, 'route': []}]

CR8550_ANY8535_CR8566_ANY8583_POP_TO_Service_Flows = \
    [{'local': 8566, 'route': [{'target': 8583, 'next': 8583}]},
     {'local': 8550, 'route': [{'target': 8535, 'next': 8535}]}]

CR_5_POP_Flows = \
    [{'local': 10150, 'route': [{'target': 10182, 'next': 10198}]},
     {'local': 10198, 'route': [{'target': 10182, 'next': 10214}]},
     {'local': 10214, 'route': [{'target': 10182, 'next': 10182}]}]

CR_5_POP_Weight_5_Flows = \
    [{'local': 10150, 'route': [{'target': 10182, 'next': 10166}]},
     {'local': 10166, 'route': [{'target': 10182, 'next': 10182}]}]
