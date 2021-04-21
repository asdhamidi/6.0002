total_pop, resistant_pop = simulation_with_antibiotic(num_bacteria=100,
                                                      max_pop=1000,
                                                      birth_prob=0.17,
                                                      death_prob=0.2,
                                                      resistant=False,
                                                      mut_prob=0.8,
                                                      num_trials=50)

make_two_curve_plot([k for k in range(150+250)],
                        [calc_pop_avg(total_pop, n) for n in range (len(total_pop[0]))],
                        [calc_pop_avg(resistant_pop, n) for n in range (len(resistant_pop[0]))],
                        'average population',
                        'avere resistant population',
                        'time',
                        'average population size',
                        'with treament')