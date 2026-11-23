def derivar_features(frame):
    """Cria variáveis de atividade diária e cafeína por unidade de IMC."""
    return frame.assign(
        Atividade_Diaria_Horas=frame.Physical_Activity_Hours / 7,
        Cafeina_por_IMC=frame.Caffeine_mg / frame.BMI.where(frame.BMI > 0),
    ).drop(columns="Physical_Activity_Hours")
