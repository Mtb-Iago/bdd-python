Feature: permissao para entrar em Zion


Scenario: Um personagem chega a zion e deve ser reconhecido pela foto
    Given reconhecer personagem
    When a foto ./faces/neo1.jpeg de um personagem visitante for capturada
    Then o personagem ./faces/neo1.jpeg deve ser reconhecido para prosseguir