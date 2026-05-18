# 🗒️ Histórico de Engenharia de Prompt (GitHub Copilot)

Este arquivo documenta as estratégias de comunicação e os prompts utilizados com o GitHub Copilot para o desenvolvimento, otimização e correção dos algoritmos deste projeto.

---

## 1. Geração de Código do Zero (Contextualização)
Para evitar que a IA gerasse códigos genéricos, utilizei a técnica de dar um papel (role) e restrições claras para o Copilot.

*   **Prompt Utilizado:**
    > "Atue como um desenvolvedor Python especialista. Preciso de uma função que verifique se uma string é um palíndromo (ignoring espaços, maiúsculas/minúsculas e pontuação). Escreva um código limpo, performático e utilize type hints."
*   **Resultado esperado:** O Copilot sugeriu o uso de tratamento de string com `.lower()` combinado com expressões regulares (`re`) ou manipulação de strings para remover caracteres inválidos, entregando a lógica pronta.

---

## 2. Refatoração e Otimização de Performance
Aqui, o objetivo foi transformar um código funcional em algo mais eficiente ou legível ("pythônico").

*   **Prompt Utilizado:**
    > "Analise esta função de cálculo de fatorial com loop `while`. Como posso refatorá-la usando recursão ou uma abordagem mais performática nativa do Python? Explique a complexidade de tempo de ambas."
*   **Resultado esperado:** A IA apresentou a abordagem com recursão e sugeriu a utilização da biblioteca padrão `math.factorial()`, explicando a complexidade $O(n)$.

---

## 3. Tratamento de Erros e Debugging (Resolução de Bugs)
Simulei falhas comuns para testar a capacidade de diagnóstico da ferramenta.

*   **Prompt Utilizado (no Copilot Chat):**
    > "Estou recebendo um `ZeroDivisionError` e `ValueError` quando o usuário insere dados inválidos nesta função de média. Como posso implementar um bloco try-except robusto para capturar essas exceções e retornar uma mensagem amigável?"
*   **Resultado esperado:** O Copilot gerou a estrutura de captura de exceções adequada, separando os tipos de erro e tratando entradas vazias.

---

## 4. Criação de Testes Unitários
Automação de testes utilizando comandos rápidos do Copilot Chat.

*   **Prompt Utilizado:**
    > `/tests Crie 5 cenários de testes unitários utilizando a biblioteca padrão 'unittest' para a função de validação de CPF, incluindo casos válidos, inválidos, strings vazias e tipos incorretos.`
*   **Resultado esperado:** Criação automática de uma classe de teste isolada com asserts específicos para cobrir todas as arestas do código.

---

## 5. Documentação de Código
Uso da IA para manter o projeto legível para outros desenvolvedores.

*   **Prompt Utilizado:**
    > "Gere docstrings no padrão Google Style para todas as funções deste arquivo, explicando detalhadamente os parâmetros de entrada, os tipos e o retorno."

---

## 💡 Lições Aprendidas em Engenharia de Prompt
*   **Contexto é tudo:** Quanto mais detalhes sobre as restrições (ex: "use a biblioteca padrão", "retorne um booleano"), melhor a primeira resposta da IA.
*   **Iteração:** O primeiro código raramente é o final. Usar o chat para pedir "mude a abordagem X para Y" traz resultados muito mais refinados.