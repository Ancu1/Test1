import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

def generate_sample_data(n_samples=1000):
    """Generate sample data from different distributions"""
    # Generate data from different distributions
    normal_data = np.random.normal(loc=0, scale=1, size=n_samples)
    uniform_data = np.random.uniform(low=-3, high=3, size=n_samples)
    exponential_data = np.random.exponential(scale=1, size=n_samples)
    binomial_data = np.random.binomial(n=10, p=0.5, size=n_samples)
    poisson_data = np.random.poisson(lam=2, size=n_samples)
    
    return {
        'Normal': normal_data,
        'Uniform': uniform_data,
        'Exponential': exponential_data,
        'Binomial': binomial_data,
        'Poisson': poisson_data
    }

def plot_distributions(data_dict):
    """Plot histograms and theoretical PDFs for each distribution"""
    plt.figure(figsize=(15, 10))
    
    for i, (dist_name, data) in enumerate(data_dict.items(), 1):
        plt.subplot(2, 3, i)
        
        # Plot histogram
        sns.histplot(data=data, stat='density', alpha=0.5, label='Histogram')
        
        # Plot theoretical PDF
        x = np.linspace(min(data), max(data), 100)
        if dist_name == 'Normal':
            pdf = stats.norm.pdf(x, loc=np.mean(data), scale=np.std(data))
        elif dist_name == 'Uniform':
            pdf = stats.uniform.pdf(x, loc=min(data), scale=max(data)-min(data))
        elif dist_name == 'Exponential':
            pdf = stats.expon.pdf(x, scale=1/np.mean(data))
        elif dist_name == 'Binomial':
            pdf = stats.binom.pmf(x, n=10, p=0.5)
        elif dist_name == 'Poisson':
            pdf = stats.poisson.pmf(x, mu=np.mean(data))
            
        plt.plot(x, pdf, 'r-', label='Theoretical PDF')
        plt.title(f'{dist_name} Distribution')
        plt.xlabel('Value')
        plt.ylabel('Density')
        plt.legend()
    
    plt.tight_layout()
    plt.savefig('probability_distributions.png')
    plt.close()

def calculate_statistics(data_dict):
    """Calculate and print basic statistics for each distribution"""
    print("\nStatistical Summary:")
    print("-" * 50)
    
    for dist_name, data in data_dict.items():
        print(f"\n{dist_name} Distribution:")
        print(f"Mean: {np.mean(data):.4f}")
        print(f"Median: {np.median(data):.4f}")
        print(f"Standard Deviation: {np.std(data):.4f}")
        print(f"Skewness: {stats.skew(data):.4f}")
        print(f"Kurtosis: {stats.kurtosis(data):.4f}")

def perform_ks_test(data_dict):
    """Perform Kolmogorov-Smirnov test for each distribution"""
    print("\nKolmogorov-Smirnov Test Results:")
    print("-" * 50)
    
    for dist_name, data in data_dict.items():
        if dist_name == 'Normal':
            _, p_value = stats.kstest(data, 'norm')
        elif dist_name == 'Uniform':
            _, p_value = stats.kstest(data, 'uniform')
        elif dist_name == 'Exponential':
            _, p_value = stats.kstest(data, 'expon')
        elif dist_name == 'Binomial':
            _, p_value = stats.kstest(data, 'binom', args=(10, 0.5))
        elif dist_name == 'Poisson':
            _, p_value = stats.kstest(data, 'poisson', args=(np.mean(data),))
            
        print(f"\n{dist_name} Distribution:")
        print(f"P-value: {p_value:.4f}")
        print(f"Follows theoretical distribution: {'Yes' if p_value > 0.05 else 'No'}")

def main():
    # Generate sample data
    data_dict = generate_sample_data()
    
    # Plot distributions
    plot_distributions(data_dict)
    
    # Calculate and print statistics
    calculate_statistics(data_dict)
    
    # Perform KS test
    perform_ks_test(data_dict)
    
    print("\nPlots have been saved as 'probability_distributions.png'")

if __name__ == "__main__":
    main() 