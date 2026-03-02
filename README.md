# ❄️ NEUROFOOD - Controle de Gelo

O **Neurofood - Controle de Gelo** é uma aplicação de inteligência térmica desenvolvida para otimizar sessões de crioterapia desportiva. O sistema utiliza princípios da termodinâmica para calcular com precisão a carga de gelo necessária para a preparação e manutenção de banheiras de gelo.

## 🚀 Funcionalidades

- **Cálculo de Carga de Choque:** Determina a massa exata de gelo para arrefecer a água da torneira até a temperatura alvo.
- **Manutenção Biotérmica:** Considera a termogénese dos atletas (calor corporal) e a troca térmica com o ambiente.
- **Cronograma Operacional:** Gera uma tabela de reposição de gelo minuto a minuto.
- **Interface Otimizada:** Design em Dark Mode (Verde/Preto) para alta visibilidade em ambientes de treino.

## 🧪 Fundamentos Físicos

O algoritmo baseia-se na **Primeira Lei da Termodinâmica** e no equilíbrio de fases:

1. **Calor Sensível ($Q = m \cdot c \cdot \Delta T$):** Calculamos a energia que deve ser removida da água.
2. **Calor Latente ($Q = m \cdot L$):** Utilizamos o calor de fusão do gelo ($334 \text{ kJ/kg}$) como o agente de extração térmica.
3. **Carga Térmica Humana:** O modelo assume uma dissipação média de **250W (~15 kJ/min)** por atleta submerso, garantindo a estabilidade da janela terapêutica (10°C - 15°C).

## 🛠️ Como Instalar

1. Clone o repositório:
   ```bash
   git clone [https://github.com/teu-usuario/neurofood-app.git](https://github.com/teu-usuario/neurofood-app.git)
