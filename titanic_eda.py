import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filepath):
    """Load Titanic dataset from CSV file."""
    return pd.read_csv(filepath)

def clean_data(df):
    """Perform data cleaning on the Titanic dataset."""
    # Fill missing Age values with median age
    df.loc[:, 'Age'] = df['Age'].fillna(df['Age'].median())
    # Fill missing Embarked values with mode
    df.loc[:, 'Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    # Fill missing Fare values with median fare
    df.loc[:, 'Fare'] = df['Fare'].fillna(df['Fare'].median())
    # Fill missing Cabin values with 'Unknown'
    df.loc[:, 'Cabin'] = df['Cabin'].fillna('Unknown')
    # Extract Title from Name
    df['Title'] = df['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)
    # Simplify titles
    df['Title'] = df['Title'].replace(['Lady', 'Countess','Capt', 'Col',
        'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
    df['Title'] = df['Title'].replace('Mlle', 'Miss')
    df['Title'] = df['Title'].replace('Ms', 'Miss')
    df['Title'] = df['Title'].replace('Mme', 'Mrs')
    # Convert categorical columns to category dtype
    categorical_cols = ['Sex', 'Embarked', 'Title', 'Pclass']
    for col in categorical_cols:
        df[col] = df[col].astype('category')
    return df

def eda(df):
    """Perform exploratory data analysis and generate plots."""
    sns.set(style="whitegrid")

    # Summary statistics
    print("Summary statistics:")
    print(df.describe(include='all'))

    # Survival count plot
    plt.figure(figsize=(6,4))
    sns.countplot(x='Survived', data=df)
    plt.title('Survival Count')
    plt.savefig('survival_count.png')
    plt.close()

    # Survival by Sex
    plt.figure(figsize=(6,4))
    sns.countplot(x='Survived', hue='Sex', data=df)
    plt.title('Survival by Sex')
    plt.savefig('survival_by_sex.png')
    plt.close()

    # Survival by Pclass
    plt.figure(figsize=(6,4))
    sns.countplot(x='Survived', hue='Pclass', data=df)
    plt.title('Survival by Passenger Class')
    plt.savefig('survival_by_pclass.png')
    plt.close()

    # Age distribution by Survival
    plt.figure(figsize=(8,6))
    sns.histplot(data=df, x='Age', hue='Survived', multiple='stack', bins=30)
    plt.title('Age Distribution by Survival')
    plt.savefig('age_distribution_by_survival.png')
    plt.close()

    # Fare distribution by Survival
    plt.figure(figsize=(8,6))
    sns.histplot(data=df, x='Fare', hue='Survived', multiple='stack', bins=30)
    plt.title('Fare Distribution by Survival')
    plt.savefig('fare_distribution_by_survival.png')
    plt.close()

    # Correlation heatmap
    plt.figure(figsize=(10,8))
    corr = df.select_dtypes(include=['number']).corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap')
    plt.savefig('correlation_heatmap.png')
    plt.close()

    # Pairplot of selected features colored by Survival
    features = ['Age', 'Fare', 'Parch', 'SibSp', 'Pclass']
    sns.pairplot(df[features + ['Survived']], hue='Survived', diag_kind='kde')
    plt.savefig('pairplot_survival.png')
    plt.close()

    # Survival rate by Title
    plt.figure(figsize=(8,6))
    title_survival = df.groupby('Title')['Survived'].mean().sort_values()
    title_survival.plot(kind='bar')
    plt.title('Survival Rate by Title')
    plt.ylabel('Survival Rate')
    plt.savefig('survival_rate_by_title.png')
    plt.close()

    # Survival rate by Embarked
    plt.figure(figsize=(8,6))
    embarked_survival = df.groupby('Embarked')['Survived'].mean().sort_values()
    embarked_survival.plot(kind='bar')
    plt.title('Survival Rate by Embarked')
    plt.ylabel('Survival Rate')
    plt.savefig('survival_rate_by_embarked.png')
    plt.close()

    # Survival rate by Sex and Pclass
    plt.figure(figsize=(10,6))
    sns.barplot(x='Pclass', y='Survived', hue='Sex', data=df)
    plt.title('Survival Rate by Sex and Passenger Class')
    plt.savefig('survival_rate_by_sex_pclass.png')
    plt.close()

    print("EDA plots saved as PNG files.")

def main():
    filepath = 'train.csv'
    df = load_data(filepath)
    df = clean_data(df)
    eda(df)

if __name__ == "__main__":
    main()
