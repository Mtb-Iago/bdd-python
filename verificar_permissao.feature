Feature: permissao para entrar em Zion

Scenario: liberar entrada de personagem em Zion
    Given verificar permissao
    When a foto ./faces/neo1.jpeg do personagem visitante for capturada
    Then o personagem ./faces/neo1.jpeg deve ser reconhecido
    When verificar permissao do ./faces/neo1.jpeg
    Then permitir a entrada do personagem em Zion


Scenario: o personagem não tem permissão para entrar em zion
    Given verificar permissao
    When a foto ./faces/smith1.jpeg do personagem visitante for capturada
    Then o personagem ./faces/smith1.jpeg deve ser reconhecido
    When verificar permissao do ./faces/smith1.jpeg
    Then não permitir a entrada do personagem em Zion

