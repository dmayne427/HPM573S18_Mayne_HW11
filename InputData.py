
# simulation settings
POP_SIZE = 1000     # cohort population size
SIM_LENGTH = 15    # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DISCOUNT = 0.03     # annual discount rate

ADD_BACKGROUND_MORT = True  # if background mortality should be added
DELTA_T = 1/4      # years

# transition matrix
TRANS_MATRIX = [
    [0, 0.0136, 0.0, 0.00151],  # Well
    [0, 0.0, 52, 0.0],  # Stroke
    [0, 0.0298, 0, 0.00746],  # Post-Stroke
    [0.0, 0.0, 0.0, 0.0],  # Dead
]

# annual cost of each health state
ANNUAL_STATE_COST = [
    0.0,   # Well
    260000,   # Stroke
    200,    # Post-Stroke
    0.0      # Dead
    ]

# annual health utility of each health state
ANNUAL_STATE_UTILITY = [
    1.0,   # Well
    0.2,   # Stroke
    0.9,   # Post-Stroke
    0.0     # Dead
    ]

# annual drug costs
Zidovudine_COST = 550 #Anticoagulation = Zido
Lamivudine_COST = 0 # NoDrug = Lami

# treatment relative risk
TREATMENT_RR = 1
TREATMENT_RR_CI = 1, 1  # lower 95% CI, upper 95% CI

# annual probability of background mortality (number per year per 1,000 population)
ANNUAL_PROB_BACKGROUND_MORT = 17.638 / 1000

