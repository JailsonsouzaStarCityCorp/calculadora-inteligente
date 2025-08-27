#!/bin/bash
# Calculadora Jailson Souza

echo "===== CALCULADORA DO JAILSON SOUZA ====="
echo "Digite o primeiro número: "
read num1
echo "Digite o segundo número: "
read num2

echo "Escolha a operação:"
echo "1 - Soma"
echo "2 - Subtração"
echo "3 - Multiplicação"
echo "4 - Divisão"
read opcao

case $opcao in
  1) resultado=$((num1 + num2))
     echo "Resultado: $resultado" ;;
  2) resultado=$((num1 - num2))
     echo "Resultado: $resultado" ;;
  3) resultado=$((num1 * num2))
     echo "Resultado: $resultado" ;;
  4) 
     if [ $num2 -ne 0 ]; then
       resultado=$((num1 / num2))
       echo "Resultado: $resultado"
     else
       echo "Erro: divisão por zero!"
     fi ;;
  *) echo "Opção inválida!" ;;
esac

echo "========================================="
echo "Obrigado por usar a Calculadora de Jailson Souza!"
echo "Finalizando o programa..."
echo "========================================="
