def processar_features_categoricas(df: pd.DataFrame, colunas: list) -> pd.DataFrame:
    """
    Converte colunas categóricas em colunas numéricas (one-hot encoding).

    Args:
        df (pd.DataFrame): O DataFrame de entrada.
        colunas (list): Uma lista com os nomes das colunas categóricas a serem processadas.

    Returns:
        pd.DataFrame: Um novo DataFrame com as colunas categóricas transformadas.
    """
    df_copy = df.copy()
    
    # pd.get_dummies é a função perfeita para essa tarefa
    df_com_dummies = pd.get_dummies(df_copy, columns=colunas, prefix_sep='_')
    
    return df_com_dummies
