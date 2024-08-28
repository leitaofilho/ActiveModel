# ActiveModel

## Descrição

Bem-vindo ao repositório oficial do **ActiveModel**, um modelo de inteligência artificial desenvolvido pela Active Ware para suporte ao diagnóstico odontológico. A Active Ware é reconhecida no mercado pela comercialização da **IntraCam**, uma câmera intraoral concebida especialmente para o ramo da odontologia, e do **AWBook**, um software odontológico baseado em nuvem. O AWBook armazena imagens capturadas pela IntraCam, bem como exames clínicos, possibilitando que profissionais odontólogos façam anotações e detecções visuais durante o tratamento bucal de seus pacientes.

O projeto **ActiveModel** é uma prova de conceito no âmbito do processo FAPESP 2024/10567-2, intitulado "Desenvolvimento de software baseado em IA para apoio diagnóstico preventivo e corretivo de doenças odontológicas comuns". A proposta deste projeto é integrar inteligência artificial ao AWBook, proporcionando suporte automático na classificação e interpretação de sintomas e causas de doenças odontológicas, além de gerar recomendações para diagnósticos clínicos corretivos e preventivos.

## Funcionalidades

O modelo **Active v1.0** foi desenvolvido para realizar as seguintes tarefas:

- **Detecção e Classificação Automática**: Identificação de estruturas anatômicas bucais, incluindo dentes, gengivas, língua e tecidos moles.
- **Identificação de Anomalias**: Detecção de problemas de saúde bucal, como cáries, lesões, inflamações gengivais, desalinhamento dentário, sinais precoces de doenças periodontais e implantes dentários.

## Arquitetura

O **Active v1.0** é baseado na arquitetura **YOLO (You Only Look Once)**, conhecida por sua eficiência em tarefas de visão computacional. O modelo foi treinado em um dataset de 1202 imagens rotuladas, obtidas a partir da IntraCam e armazenadas no AWBook.

### Detalhes do Treinamento

- **Dataset**:
  - 1202 imagens rotuladas.
  - Divisão dos dados: 70% para treinamento, 15% para validação, e 15% para teste.
  
- **Hiperparâmetros**:
  - **Épocas**: 60
  - **Otimização**: AdamW
  - **Taxa de Aprendizagem**: 0.001429
  - **Momentum**: 0.9
  
- **Infraestrutura**:
  - Treinamento realizado em uma GPU (Graphical Processing Unit) para otimização de desempenho.

- **Desempenho**:
  - **Precisão Global**: 60%

## Como Fazer a Inferência

Para testar o modelo **Active v1.0**, você pode utilizar o diretório `inference`, que contém imagens no formato PNG para inferência. O arquivo `main.py` do repositório inclui o código necessário para carregar o modelo e realizar a inferência em uma imagem de exemplo.

### Exemplo de Código:

```python
from ultralytics import YOLO

# Carregar modelo
model = YOLO('model/activeModel_v1.0.pt')

# Inferência do modelo
results = model(source='inference/img02.png', conf=0.75, save=True)
```

Neste exemplo, o modelo carrega a imagem img02.png do diretório `inference` e executa a inferência com uma confiança mínima de 0.75, salvando os resultados.

## Propostas Futuras
Os próximos passos incluem o aperfeiçoamento do **Active v1.0**, envolvendo a incorporação de novos dados e ajustes nos hiperparâmetros, além de utilização de técnicas avançadas de regularização.
