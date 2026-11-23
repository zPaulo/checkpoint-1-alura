# Checkpoint 1 Alura — Café e qualidade do sono

Projeto de ciência de dados para a Health&Life Analytics. A análise explora como o consumo de café e outros hábitos se associam à qualidade do sono e compara dois classificadores para prever `Sleep_Quality` em uma base sintética de 10.000 participantes.

## Executar no Jupyter Notebook

Use Python 3.8 ou superior. A execução e a recarga do modelo distribuído foram verificadas em Python 3.12 com scikit-learn 1.8.0. Em versões anteriores, rode todas as células para gerar um modelo compatível com o ambiente.

```bash
python -m pip install -r requirements.txt
python -m notebook checkpoint_1_alura.ipynb
```

Na interface, execute todas as células em ordem. As dependências incluem pandas, NumPy, Matplotlib, seaborn, scikit-learn e joblib.

## Executar no Google Colab

Abra `checkpoint_1_alura.ipynb` no Colab. Depois, em uma célula antes da primeira célula do projeto, clone o repositório e entre na pasta para disponibilizar `features.py` e os arquivos de dados. Substitua a URL se estiver usando uma cópia do repositório.

```python
!git clone https://github.com/zPaulo/checkpoint-1-alura.git
%cd checkpoint-1-alura
%pip install -r requirements.txt
```

Se o Colab solicitar, reinicie a sessão após instalar as dependências, volte à pasta com `%cd /content/checkpoint-1-alura` e execute todas as células do projeto.

## Arquivos

| Caminho | Conteúdo |
| --- | --- |
| `checkpoint_1_alura.ipynb` | EDA, visualizações por grupo, principais descobertas, avaliação e recomendações |
| `data/coffee.csv` | Base sintética original fornecida pela Alura |
| `data/coffee_processed.csv` | Features numéricas e codificadas, variável alvo e partição de cada registro |
| `models/sleep_quality.joblib` | Pipeline da floresta aleatória, incluindo transformação e pré-processamento |
| `features.py` | Função de criação de variáveis utilizada pelo pipeline |

A base original também pode ser obtida no [CSV da Alura](https://cdn3.gnarususercontent.com.br/5209-projeto-cientista-dados-nivel-1/synthetic_coffee_health_10000%28in%29.csv) ou na [fonte indicada no Kaggle](https://www.kaggle.com/datasets/uom190346a/global-coffee-health-dataset).

## Resultados

- O grupo com cafeína acima de 332,0 mg/dia dormiu, em média, **0,59 hora a menos por noite** que o grupo com até 138,8 mg/dia.
- Na base sintética, 100% dos registros com estresse alto tiveram qualidade de sono *Poor*, frente a 0% com estresse baixo. O modelo exclui estresse e horas de sono para reduzir o risco de aprender diretamente regras que possam ter gerado o alvo.
- A floresta aleatória obteve **60,1% de acurácia** e **0,504 de F1 macro** no teste. A diferença de F1 macro entre treino e validação sugere sobreajuste.

As associações observadas descrevem a base sintética. Use-as para formular hipóteses a investigar com dados reais.

## Tópicos do checkpoint

[Projeto](https://cursos.alura.com.br/app/forum/topic/new?courseCode=checkpoint-cientista-dados-nivel-1&kind=task&taskId=236517) · [Ambiente](https://cursos.alura.com.br/app/forum/topic/new?courseCode=checkpoint-cientista-dados-nivel-1&kind=task&taskId=211806) · [EDA](https://cursos.alura.com.br/app/forum/topic/new?courseCode=checkpoint-cientista-dados-nivel-1&kind=task&taskId=211807) · [Visualização](https://cursos.alura.com.br/app/forum/topic/new?courseCode=checkpoint-cientista-dados-nivel-1&kind=task&taskId=211808) · [Modelo](https://cursos.alura.com.br/app/forum/topic/new?courseCode=checkpoint-cientista-dados-nivel-1&kind=task&taskId=211809) · [Revisão](https://cursos.alura.com.br/app/forum/topic/new?courseCode=checkpoint-cientista-dados-nivel-1&kind=task&taskId=211810)
