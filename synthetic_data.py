import pandas as pd 
import numpy as np 

# VB-V2 beginner/foundational 
# V3-V5 intermediate/dynamic/strength
# V6-V10 advanced precision/footwork 

def generate_synthetic_climbing_data(n_samples: 500):
    np.random.seed(42)
    grades = np.random.choice(
        range(0, 11),
        size=n_samples,
        # Grade distribution  EDIT 
        p=[0.15, 0.15, 0.12, 0.12, 0.10, 0.10, 0.09, 0.08, 0.05, 0.03, 0.01]
    )
    
    data = pd.DataFrame({
        'grade': grades,
        
        # Route features
        'wall_angle': np.where(
            grades < 4,
            np.random.normal(70, 10, n_samples),  # slab/vertical
            np.random.normal(110, 15, n_samples)   # overhang
        ).clip(60, 160),
        
        # ADD
        'num_holds': np.random.normal( , n_samples).clip(5, 25).astype(int),
        
        'hold_types': np.random.choice(
            ['jug', 'crimp', 'sloper', 'pinch'], n_samples
        ), 
        
        'route_height_m': np.random.normal(10, 5, n_samples),
        
        'crux_position': np.random.choice(
            ['bottom', 'middle', 'top'], n_samples
        ),
        
        # Climbing styles focusing on strength, height, and weight distribution/precision and flexibility 
        'style': np.random.choice(
            ['power', 'dynamic', 'technical', 'flexible', 'bold'], n_samples
        ),
        
        # User biomechanics ADD MORE 
        'user_height_cm': np.random.normal(170, 10, n_samples),
        
        # Attempt data EDIT  
        'attempts_to_send': (grades + np.random.normal(0, 2, n_samples)
        ).clip(1, 20).astype(int),

        'completed': np.random.binomial(1, 
                        np.exp(-grades/10), n_samples)
    })
    
    return data

df = generate_synthetic_climbing_data()
print(df.describe())
print("\nGrade distribution:")
print(df['grade'].value_counts().sort_index())

