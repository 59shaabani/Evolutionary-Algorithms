#MSH-59shaabani
import sys, os, json
import numpy as np


def get_parameters(input):
    with open(input) as data_file:
        source = json.load(data_file)
    return source
    # return dict(
    #     assimilation_rate= source.get('mpi-nodes',1),
    #     cluster_size= source['cluster-size'],
    #     initial_cutoff = source['initial-cutoff']
    # )

#{
#"assimilation_rate": 0.4,
#"revolution_rate": 0.1,
#"alpha_rate": 0.8,	
#"revolution_probability": 0.2,	
#"neighbourhood_radius": 0.1,	
#"constant_gravitation": 6.672,	
#"number_of_items": 9,	
#"number_of_choices": 2,	
#"number_of_iterations": 30,	
#"number_of_countries": 300,	
#"number_of_empires": 20
#}

def read_parameters(list):
    # result = get_parameters(list)
    # for i in list:
    # result.append(get_parameters(i))

    # return result
    return get_parameters(list)


elements_value  = [1, 3, 1, 2, 5, 6, 1, 4, 5]  # $
elements_weight = [2, 2, 1, 4, 10, 8, 3, 3, 5]  # kg

weight_limit = 10
