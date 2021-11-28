# a set of functions to save code cell space in the python foundations 
# textbook

import matplotlib.pyplot as _plt
import numpy as _np
import scipy.stats as _stats
import pandas as _pd

def r_ify(fig_size = (7,6)):
    "Make plots look like R!"
    _plt.style.use('ggplot')
    _plt.rc('axes', facecolor='white', edgecolor='black',
       axisbelow=True, grid=False)
    _plt.rcParams['figure.figsize'] = fig_size
    
def data_gen_trial(seed = 1000):

    '''
    A function to generate the data for the clinical trial
    example on the first page.
    '''

    _np.random.seed(1000)
    n1 = 50
    n2 = 50

    placebo_change = _np.random.choice(['+', '-'], p = [0.3, 0.7], size = n1 )

    drug_change =  _np.random.choice(['+', '-'], p = [0.5, 0.5], size = n2)   
    
    trial_df = _pd.DataFrame({'group': _np.append(_np.repeat('placebo', len(placebo_change)), 
                                            _np.repeat('adirudin', len(drug_change))),
                        'change': _np.append(placebo_change, drug_change)})

    return placebo_change, drug_change, trial_df


def trial_pop_plot(placebo_change, drug_change, seed = 300, pop_size = 1000):
    
    '''
    This function generates a plot of a population consistent with the null hypothesis,
    for the trial example. The code is very messy at the moment. It needs tidying up!
    '''
    _np.random.seed(seed)
    
    # generating a population consistent with the null hypothesis
    pop_scores = _np.random.choice(['+', '-'],p = [0.2, 0.8],  size = pop_size)
    x_coord = _np.random.choice(_np.linspace(-18.6, 13.3, 1000 ), replace = False, size = pop_size)
    y_coord = _np.random.choice(_np.linspace(-14.2, 8.9, 1000), replace = False, size = pop_size)
    pop_df = _pd.DataFrame({'change': pop_scores,
                          'x': x_coord,
                          'y': y_coord})
    
    # half of the population receive placebo, half receive the drug
    placebo = pop_df.iloc[:int(len(pop_df)/2)]
    
    drug = pop_df.iloc[int(len(pop_df)/2):]
    
    # show the '+' or '-' change of every member of the hypothetical population
    _plt.figure(figsize = (16, 8))
    _plt.subplot(1,2,1)
    _plt.suptitle('Hypothetical Population', y = .93)
    _plt.scatter(placebo[placebo['change'] == '+']['x'] , placebo[placebo['change'] == '+']['y'], 
                marker = '+', color = 'darkgreen', label = 'placebo positive change')
    _plt.scatter(placebo[placebo['change'] == '-']['x'] , placebo[placebo ['change'] == '-']['y'] , 
                marker = "_", color = 'darkgreen', label = 'placebo negative change')
    _plt.scatter(drug[drug['change'] == '+']['x'] , drug[drug['change'] == '+']['y'], 
                marker = '+', color = 'darkred', label = 'drug positive change')
    _plt.scatter(drug[drug['change'] == '-']['x'] , drug[drug['change'] == '-']['y'] , 
                marker = "_", color = 'darkred', label = 'drug negative change')
    _plt.xticks([])
    _plt.yticks([])
    _plt.legend( bbox_to_anchor=(0.7, -0.03))
    
    # show the proportion of positive changes placebo vs drug
    _plt.subplot(1,2,2)
    _plt.bar(['placebo', 'drug'], 
            [_np.sum(placebo['change'] == '+')/len(placebo)*100, _np.sum(drug['change'] == '+')/len(drug)*100 ],
           color = ['darkgreen', 'darkred'])
    _plt.ylabel('% improved')
    _plt.show()
    
    return pop_df, placebo, drug

def trial_sample_plot(pop_df, placebo, drug, placebo_change, drug_change, seed = 300):
    
    '''
    This function takes the output of trial_pop_plot() and then draws a sample with a pattern of 
    results inconsistent with the population pattern. The code is very messy at the moment. 
    It needs tidying up!
    '''
    
    # create a sample from the population which is unreflective of the general patter
    placebo_sample = placebo.iloc[_np.random.choice(_np.arange(len(placebo)), len(placebo_change))]
    drug_sample = drug[drug['change'] == '+'].iloc[_np.random.choice(_np.arange(len(drug[drug['change'] == '+'])), int(len(drug_change)*.75))]
    drug_sample_negatives = drug[drug['change'] == '-'].iloc[_np.random.choice(_np.arange(len(drug[drug['change'] == '-'])), int(len(drug_change)-  int(len(drug_change)*.75)))]
    drug_sample = drug_sample.append(drug_sample_negatives)
    
    # show the sample, and the proportion of positive changes in the sample (drug vs placebo)
    _plt.figure(figsize = (16, 8))
    _plt.subplot(1,2,1)
    _plt.suptitle('Hypothetical Sample', y = .93)
    _plt.scatter(placebo_sample[placebo_sample['change'] == '+']['x'] , placebo_sample[placebo_sample['change'] == '+']['y'], 
                marker = '+', color = 'darkgreen', label = 'placebo positive change')
    _plt.scatter(placebo_sample[placebo_sample['change'] == '-']['x'] , placebo_sample[placebo_sample['change'] == '-']['y'] , 
                marker = "_", color = 'darkgreen', label = 'placebo negative change')
    _plt.scatter(drug_sample[drug_sample['change'] == '+']['x'] , drug_sample[drug_sample['change'] == '+']['y'], 
                marker = '+', color = 'darkred', label = 'drug positive change')
    _plt.scatter(drug_sample[drug_sample['change'] == '-']['x'] , drug_sample[drug_sample['change'] == '-']['y'] , 
                marker = "_", color = 'darkred', label = 'drug negative change')
    _plt.xticks([])
    _plt.yticks([])
    _plt.legend(bbox_to_anchor=(0.7, -0.03))
    _plt.scatter(placebo[placebo['change'] == '+']['x'] , placebo[placebo['change'] == '+']['y'], 
                marker = '+', color = 'black', alpha = 0.1)
    _plt.scatter(placebo[placebo['change'] == '-']['x'] , placebo[placebo ['change'] == '-']['y'] , 
                marker = "_", color = 'black', alpha = 0.1)
    _plt.scatter(drug[drug['change'] == '+']['x'] , drug[drug['change'] == '+']['y'], 
                marker = '+', color = 'black', alpha = 0.1)
    _plt.scatter(drug[drug['change'] == '-']['x'] , drug[drug['change'] == '-']['y'] , 
                marker = "_", color = 'black', alpha = 0.1)
    
    _plt.scatter(pop_df['x'] , pop_df['y'], 
                alpha = 0)
    _plt.subplot(1,2,2)
    _plt.bar(['placebo', 'drug'], 
            [_np.sum(placebo_sample['change'] == '+')/len(placebo_sample)*100, _np.sum(drug_sample['change'] == '+')/len(drug_sample)*100 ],
           color = ['darkgreen', 'darkred'])
    _plt.ylabel('% improved')
    _plt.show()


   
def data_gen_pollution(seed = 1000, pop_size = 1000, samp_size = 100):
    
    """A function to generate the population/sample data for the first page.
    Generates a null and alternate population of 
    `cognitive impairment ~ pollutant exposure` scores. Takes a sample from the
    alternate population. Arguments set population size, sample size and seed
    value (to ensure reproducibility)."""
    
    _np.random.seed(seed)
    
    # generating an alternate hypothesis population
    pollutant_exposure_pop = _np.random.normal(15, 3, size = pop_size)
    pollutant_exposure_pop = _np.round(pollutant_exposure_pop,2)
    
    cognitive_impairment_pop = 3 * pollutant_exposure_pop + _np.random.normal(0, 5, size = pop_size)
    cognitive_impairment_pop = cognitive_impairment_pop.astype('int')
    
    # null population
    cognitive_impairment_pop_null = _np.random.normal(_np.mean(cognitive_impairment_pop), 12, size = pop_size)
    cognitive_impairment_pop_null = cognitive_impairment_pop_null.astype('int')
    
    # get values to ensure same axes on all plots (for easy comparison)
    min_y = _np.min(cognitive_impairment_pop_null) - 2
    max_y = _np.max(cognitive_impairment_pop_null) + 2
    
    min_x = _np.min(pollutant_exposure_pop) - 2
    max_x = _np.max(pollutant_exposure_pop) + 2
    
    # get a random sample from the alternate population    
    sample_indexes = _np.random.choice(_np.arange(pop_size), size = samp_size)

    pollutant_exposure = pollutant_exposure_pop[sample_indexes]

    cognitive_impairment = cognitive_impairment_pop[sample_indexes]

    
    return pollutant_exposure_pop, cognitive_impairment_pop, cognitive_impairment_pop_null, min_x, max_x, min_y, max_y, pollutant_exposure, cognitive_impairment


def plot_sample(pollutant_exposure, cognitive_impairment, min_x, max_x, min_y, max_y):
    "Plots the sample from the alternate population only."
    
    _plt.scatter(pollutant_exposure, cognitive_impairment)
    _plt.xlim([min_x, max_x])
    _plt.ylim([min_y, max_y])
    _plt.xlabel('Pollutant Exposure \n (μg/m^3)')
    _plt.ylabel('Cognitive Impairment \n (Questionairre Score)')
    _plt.show()
    
def plot_populations(pollutant_exposure_pop, cognitive_impairment_pop, cognitive_impairment_pop_null, pollutant_exposure, cognitive_impairment, min_x, max_x, min_y, max_y, fig_size = (15,6)):
    """Plots the sample data against the alternate and null population, to provoke
    the questions 'which population did they come from?' """
    
    _plt.figure(figsize = fig_size)
    _plt.subplot(1,2,1)
    _plt.scatter(pollutant_exposure_pop, cognitive_impairment_pop, color = 'darkblue', label = 'hypothetical population data')
    _plt.scatter(pollutant_exposure, cognitive_impairment, label = 'actual sample data')
    _plt.xlim([min_x, max_x])
    _plt.ylim([min_y, max_y])
    _plt.legend(loc = 'upper right')
    _plt.title('Scenario 1: Strong Linear Relationship')
    _plt.xlabel('Pollutant Exposure \n (μg/m^3)')
    _plt.ylabel('Cognitive Impairment \n (Questionairre Score)')
    
    _plt.subplot(1,2,2)
    _plt.scatter(pollutant_exposure_pop, cognitive_impairment_pop_null, color = 'darkblue', label = 'hypothetical population data')
    _plt.scatter(pollutant_exposure, cognitive_impairment, label = 'actual sample data')
    _plt.xlim([min_x, max_x])
    _plt.ylim([min_y, max_y])
    _plt.legend(loc = 'upper right')
    _plt.title('Scenario 2: No Linear Relationship')
    _plt.xlabel('Pollutant Exposure \n (μg/m^3)')
    _plt.ylabel('Cognitive Impairment \n (Questionairre Score)')
    
    
def plot_sample_shuffle(pollutant_exposure, cognitive_impairment,  min_x, max_x, min_y, max_y, fig_size = (13, 8)):
    "Creates a set of subplots showing the effect of the shuffling process on the sample."
    
    n_iters = 6
    
    _plt.figure(figsize = fig_size)
    for i in _np.arange(n_iters):
        _plt.subplot(2, 3, i+1)
        _plt.scatter(pollutant_exposure, _np.random.permutation(cognitive_impairment))
        if i == 0 or i == 3:
            _plt.ylabel('Cognitive Impairment \n (Questionairre Score)')
        _plt.xlim([min_x, max_x])
        _plt.ylim([min_y, max_y])
        _plt.xlabel('Pollutant Exposure \n (μg/m^3)')
        _plt.title('Shuffle Number '+str(i+1))
    _plt.tight_layout()
    
    
def plot_sample_shuffle_with_pop(pollutant_exposure, cognitive_impairment, pollutant_exposure_pop, cognitive_impairment_pop_null, min_x, max_x, min_y, max_y, fig_size = (13, 8)):
    "Creates a set of subplots showing the effect of the shuffling process on the sample."
    
    n_iters = 6
    
    _plt.figure(figsize = fig_size)
    for i in _np.arange(n_iters):
        _plt.subplot(2, 3, i+1)
        _plt.scatter(pollutant_exposure_pop, cognitive_impairment_pop_null, color = 'darkblue')
        _plt.scatter(pollutant_exposure, _np.random.permutation(cognitive_impairment))
        _plt.xlim([min_x, max_x])
        _plt.ylim([min_y, max_y])
        if i == 0 or i == 3:
            _plt.ylabel('Cognitive Impairment \n (Questionairre Score)')
        _plt.xlabel('Pollutant Exposure \n (μg/m^3)')
        _plt.title('Shuffle Number '+str(i+1))
    _plt.tight_layout()
    
def pearson_plot(pollutant_exposure):
    """Generates an illustration of the meaning of Pearson's r"""
    
    _plt.figure(figsize = (18,4))
    _plt.subplot(1,5, 1)
    _plt.scatter(pollutant_exposure, -pollutant_exposure)
    _plt.title("Pearson's r = "+str(_np.round(_stats.pearsonr(pollutant_exposure, -pollutant_exposure)[0],2)))
    _plt.xticks([])
    _plt.yticks([])
    _plt.xlabel('Perfect Negative \n Linear Relationship')
    
    _plt.subplot(1,5, 2)
    y_strong_neg = -0.6 * pollutant_exposure + _np.random.normal(0, 2, size = len(pollutant_exposure))
    _plt.scatter(pollutant_exposure, y_strong_neg)
    _plt.title("Pearson's r = "+str(_np.round(_stats.pearsonr(pollutant_exposure, y_strong_neg)[0], 2)))
    _plt.xticks([])
    _plt.yticks([])
    _plt.xlabel('Strong Negative \n Linear Relationship')
    
    _plt.subplot(1,5, 3)
    y_rand = _np.random.normal(_np.mean(pollutant_exposure), 2, size = len(pollutant_exposure))
    _plt.scatter(pollutant_exposure, y_rand)
    _plt.title("Pearson's r = "+str(_np.round(_stats.pearsonr(pollutant_exposure, y_rand)[0], 2)))
    _plt.xticks([])
    _plt.yticks([])
    _plt.xlabel('No Linear Relationship \n (Random Association)')
    
    _plt.subplot(1,5, 4)
    y_strong_pos = pollutant_exposure + _np.random.normal(0, 2, size = len(pollutant_exposure))
    _plt.scatter(pollutant_exposure, y_strong_pos )
    _plt.title("Pearson's r = "+str(_np.round(_stats.pearsonr(pollutant_exposure,y_strong_pos)[0], 2)))
    _plt.xticks([])
    _plt.yticks([])
    _plt.xlabel('Strong Positive \n Linear Relationship')
    
    _plt.subplot(1,5, 5)
    _plt.scatter(pollutant_exposure, pollutant_exposure)
    _plt.title("Pearson's r = "+str(_np.round(_stats.pearsonr(pollutant_exposure,pollutant_exposure)[0], 2)))
    _plt.xticks([])
    _plt.yticks([])
    _plt.xlabel('Perfect Positive \n Linear Relationship')
    
    _plt.show()