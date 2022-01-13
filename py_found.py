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
                                            _np.repeat('drug', len(drug_change))),
                        'change': _np.append(placebo_change, drug_change)})

    return placebo_change, drug_change, trial_df


def trial_pop_plot(seed = 300, pop_size = 1000):
    
    '''
    This function generates a plot of a population consistent with the null hypothesis,
    for the trial example. The code is very messy at the moment. It needs tidying up!
    '''
    _np.random.seed(seed)
    
    # generating a population consistent with the null hypothesis
    # equal number of +/- in placebo and intervention group (proportion in both groups 
    # is the same as the placebo positive proportion in the acutal sample
    positive_group_size = 180
    negative_group_size = int(500 - positive_group_size)
    placebo_plus = _np.repeat('+', positive_group_size)
    placebo_minus= _np.repeat('-', negative_group_size)
    drug_plus = _np.repeat('+', positive_group_size)
    drug_minus= _np.repeat('-', negative_group_size)
    all_scores = _np.concatenate([placebo_plus, placebo_minus, drug_plus, drug_minus])
    group_labels = _np.repeat('placebo', 500)
    group_labels = _np.append(group_labels, _np.repeat('drug', 500))
    x_coord = _np.random.choice(_np.linspace(-18.6, 13.3, 1000 ), replace = False, size = pop_size)
    y_coord = _np.random.choice(_np.linspace(-14.2, 8.9, 1000), replace = False, size = pop_size)
    pop_df = _pd.DataFrame({'change': all_scores,
                           'group': group_labels,
                          'x': x_coord,
                          'y': y_coord})
    
    placebo = pop_df[pop_df['group'] == 'placebo']
    drug = pop_df[pop_df['group'] == 'drug']
    
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
    
def get_x_y_sample(trial_df):
    '''
    A function to get x y coordinates for a raw data plot of the sample in the clinical trial example.
    '''
    
    _np.random.seed(300)
    # getting x y coordinates for the raw data plot
    x_coord = _np.random.choice(_np.linspace(-18.6, 13.3, 1000 ), replace = False, size = len(trial_df))
    y_coord = _np.random.choice(_np.linspace(-14.2, 8.9, 1000), replace = False, size = len(trial_df))
    
    return x_coord, y_coord
    
def raw_sample_plot(trial_df, figsize = (10,5)):

    '''
    This function plots the raw data from the actual trial, alongside the bar plot.
    '''
    
    # get the x y coordinates for the raw data plot
    x_coord, y_coord = get_x_y_sample(trial_df)
    
    function_trial_df = trial_df.copy()
        
    function_trial_df['x'] = x_coord
    function_trial_df['y'] = y_coord
        
        
    placebo_sample = function_trial_df[function_trial_df['group'] == 'placebo']
    drug_sample = function_trial_df[function_trial_df['group'] == 'drug']
        
        
    # show the sample, and the proportion of positive changes in the sample (drug vs placebo)
    _plt.figure(figsize = figsize)
    _plt.subplot(1,2,1)
    _plt.suptitle('Actual Sample Data', y = 1)
    _plt.scatter(placebo_sample[placebo_sample['change'] == '+']['x'] , placebo_sample[placebo_sample['change'] == '+']['y'], 
                    marker = '+', color = 'green', label = 'placebo positive change')
    _plt.scatter(placebo_sample[placebo_sample['change'] == '-']['x'] , placebo_sample[placebo_sample['change'] == '-']['y'] , 
                    marker = "_", color = 'green', label = 'placebo negative change')
    _plt.scatter(drug_sample[drug_sample['change'] == '+']['x'] , drug_sample[drug_sample['change'] == '+']['y'], 
                    marker = '+', color = 'red', label = 'drug positive change')
    _plt.scatter(drug_sample[drug_sample['change'] == '-']['x'] , drug_sample[drug_sample['change'] == '-']['y'] , 
                    marker = "_", color = 'red', label = 'drug negative change')
    _plt.xticks([])
    _plt.yticks([])
    _plt.legend(bbox_to_anchor=(0.7, -0.03))

    _plt.scatter(function_trial_df['x'] , function_trial_df['y'], 
                    alpha = 0)
    _plt.subplot(1,2,2)
    _plt.bar(['placebo', 'drug'], 
                [_np.sum(placebo_sample['change'] == '+')/len(placebo_sample)*100, _np.sum(drug_sample['change'] == '+')/len(drug_sample)*100 ],
               color = ['green', 'red'])
    _plt.ylabel('% improved')
    _plt.show()
    
    
def actual_sample_plot_repeated(trial_df, seed = 300, figsize = (10,5), num_repeats = 5):
    '''
    This function shows the shuffling process the actual sample.'''
    
    # get the x y coordinates for the raw data plot
    x_coord, y_coord = get_x_y_sample(trial_df)
    
    function_trial_df = trial_df.copy()
    
    for i in _np.arange(num_repeats):
    
        _np.random.seed()
    
        function_trial_df['x'] = x_coord
        function_trial_df['y'] = y_coord
        
        # shuffling the group labels, under the null
        function_trial_df['group'] = _np.random.permutation(function_trial_df['group'])
        
        placebo_sample = function_trial_df[function_trial_df['group'] == 'placebo']
        drug_sample = function_trial_df[function_trial_df['group'] == 'drug']
        
        
        # show the sample, and the proportion of positive changes in the sample (drug vs placebo)
        _plt.figure(figsize = figsize)
        _plt.subplot(1,2,1)
        _plt.suptitle('Shuffling the Actual Sample\nRepeat Number:'+str(i+1), y = 1)
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

        _plt.scatter(function_trial_df['x'] , function_trial_df['y'], 
                    alpha = 0)
        _plt.subplot(1,2,2)
        _plt.bar(['placebo', 'drug'], 
                [_np.sum(placebo_sample['change'] == '+')/len(placebo_sample)*100, _np.sum(drug_sample['change'] == '+')/len(drug_sample)*100 ],
               color = ['darkgreen', 'darkred'])
        _plt.ylabel('% improved')
        _plt.show()
        

   
def data_gen_pollution(seed = 1500, pop_size = 1000, samp_size = 100):
    
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
    
def function_plot_page_setup():
        
        '''
        Sets up the data etc. needed for the 'functions and plotting' page.
        '''
        # getting the lists used on the 'lists_indexing' page
        psychosis_status_observations = ['psychotic', 'not_psychotic', 'not_psychotic', 'not_psychotic', 'psychotic']
        observations_sex = ['male', 'male', 'female', 'female', 'female']
        psychosis_scores = [80, 20, 14, 13, 91]
        names = ['roy', 'david','lucy', 'aiesha', 'amelia']

        # some new data we need for the current exercise
        _np.random.seed(1000)
        psychosis_score_200_patients = _np.random.normal(78, 2, size = 200)
        psychosis_score_200_patients = psychosis_score_200_patients.astype('int')
        psychosis_score_200_patients[psychosis_score_200_patients > _np.quantile(psychosis_score_200_patients, .8)] = psychosis_score_200_patients[psychosis_score_200_patients >_np.quantile(psychosis_score_200_patients, .8)] + _np.random.normal(6, 3, size = len(psychosis_score_200_patients[psychosis_score_200_patients > _np.quantile(psychosis_score_200_patients, .8)]))
        num_hospitalisations = -30 + _np.round(0.5 * psychosis_score_200_patients) + _np.round(_np.random.normal(0, 1, size = 200))
        
        return psychosis_status_observations, observations_sex, psychosis_scores, names, psychosis_score_200_patients, num_hospitalisations
    
def another_trial_gen():
    
    '''
    Generates and plots the trial data for the Fentacriptine question.
    '''
    _np.random.seed(2000)
    
    placebo = _np.random.normal(80, 2, 100).astype('int')

    drug = _np.random.normal(77, 2, 100).astype('int')
    
    _plt.hist(placebo, label = 'placebo group')
    _plt.hist(drug, alpha = 0.5, label = 'drug group')
    _plt.xlabel('Psychosis Score')
    _plt.ylabel('Frequency')
    _plt.legend(bbox_to_anchor=(1,1))
    _plt.show()
    
    return placebo, drug

def another_trial_pop_illustration(placebo, drug):
    
    population =  _np.random.normal(_np.mean([placebo.mean(),drug.mean()]), 1, 100000)

    population_placebo = _np.random.normal(_np.mean(placebo), 0.9, 50000)
    population_drug = _np.random.normal(_np.mean(drug), 0.9, 50000)
    
    placebo_samp =_np.random.choice(population_placebo, size =10000)
    drug_samp =_np.random.choice(population_drug, size = 10000)
    
    _plt.figure(figsize = (16, 6)) 
    _plt.subplot(1,2,1)
    _plt.hist(population,color = 'black', label = 'underlying population')
    _plt.hist(placebo_samp, label = 'placebo group')
    _plt.hist(drug_samp, alpha = 0.5, label = 'drug group')
    _plt.yticks([])
    _plt.xlabel('Psychosis Score')
    _plt.ylabel('Number of Scores')
    _plt.legend(bbox_to_anchor = (1,1))
    _plt.title('The Null World')
    
    
    
    _plt.subplot(1,2,2)
    _plt.hist(population_placebo,color = 'darkred', label = 'underlying placebo population')
    _plt.hist(population_drug,color = 'darkblue', label = 'underlying drug population')
    _plt.hist(placebo_samp, label = 'placebo group')
    _plt.hist(drug_samp, alpha = 0.5, label = 'drug group')
    _plt.xlabel('Psychosis Score')
    _plt.ylabel('Number of Scores')
    _plt.yticks([])
    _plt.legend(bbox_to_anchor = (1,1))
    _plt.title('The Alternate World')
    _plt.show()
    
def another_trial_pop_resample(placebo, drug):
    
    population =  _np.random.normal(_np.mean([placebo.mean(),drug.mean()]), 1, 100000)
    
    population_placebo = _np.random.normal(_np.mean(placebo), 0.9, 50000)
    population_drug = _np.random.normal(_np.mean(drug), 0.9, 50000)

    sample = _np.random.choice(population, size = 20000)
    placebo = sample[:10000]
    drug  = sample[10000:]
        
    _plt.figure(figsize = (16, 6)) 
    _plt.subplot(1,2,1)
    _plt.hist(population,color = 'black', label = 'underlying population')
    _plt.hist(placebo, label = 'placebo group')
    _plt.hist(drug, alpha = 0.5, label = 'drug group')
    _plt.xlabel('Psychosis Score')
    _plt.ylabel('Number of Scores')
    _plt.yticks([])
    _plt.legend(bbox_to_anchor = (1,1))
    _plt.title('The Null World')
        
        

    placebo =  _np.random.choice(population_placebo, size = 10000)
    drug  = _np.random.choice(population_drug, size = 10000)
        
    _plt.subplot(1,2,2)
    _plt.hist(population_placebo,color = 'darkred', label = 'underlying placebo population')
    _plt.hist(population_drug,color = 'darkblue', label = 'underlying drug population')
    _plt.hist(placebo, label = 'placebo group')
    _plt.hist(drug, alpha = 0.5, label = 'drug group')
    _plt.xlabel('Psychosis Score')
    _plt.ylabel('Number of Scores')
    _plt.yticks([])
    _plt.legend(bbox_to_anchor = (1,1))
    _plt.title('The Alternate World')
    _plt.show()
    
def another_trial_pop_resample_with_medians(placebo, drug):
    
    population =  _np.random.normal(_np.mean([placebo.mean(),drug.mean()]), 1, 100000)
    
    population_placebo = _np.random.normal(_np.mean(placebo), 0.9, 50000)
    population_drug = _np.random.normal(_np.mean(drug), 0.9, 50000)

    sample = _np.random.choice(population, size = 20000)
    placebo = sample[:10000]
    drug  = sample[10000:]
    
    together = _np.append(placebo, drug)
        
    _plt.figure(figsize = (16, 6)) 
    _plt.subplot(1,2,1)
    _plt.hist(population,color = 'black', label = 'underlying population')
    _plt.hist(placebo, label = 'placebo group')
    _plt.hist(drug, alpha = 0.5, label = 'drug group')
    _plt.xlabel('Psychosis Score')
    _plt.ylabel('Number of Scores')
    _plt.yticks([])
    _plt.axvline(_np.median(placebo), color = 'cyan', label = 'placebo median')
    _plt.axvline(_np.median(drug), color = 'crimson', label = 'drug median')
    _plt.axvline(_np.median(together), color = 'yellow', label = 'median of both groups combined')
    _plt.title('The Null World')
        
        

    placebo =  _np.random.choice(population_placebo, size = 10000)
    drug  = _np.random.choice(population_drug, size = 10000)
    
    together = _np.append(placebo, drug)
        
    _plt.subplot(1,2,2)
    _plt.hist(population_placebo,color = 'darkred', label = 'underlying placebo population')
    _plt.hist(population_drug,color = 'darkblue', label = 'underlying drug population')
    _plt.hist(placebo, label = 'placebo group')
    _plt.hist(drug, alpha = 0.5, label = 'drug group')
    _plt.xlabel('Psychosis Score')
    _plt.ylabel('Number of Scores')
    _plt.yticks([])
    _plt.title('The Alternate World')
    _plt.axvline(_np.median(placebo), color = 'cyan', label = 'placebo median')
    _plt.axvline(_np.median(drug), color = 'crimson', label = 'drug median')
    _plt.axvline(_np.median(together), color = 'yellow', label = 'median of both groups combined')
    _plt.legend(bbox_to_anchor = (1,1))
    _plt.show()