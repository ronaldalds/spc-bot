from process.cancelamento import cancelamento

cancelamento(
        mk = "test",
        cod_pessoa = "152628",
        contrato = "189726",
        detalhes_cancelamento = """Cancelamento em razão de inadimplência superior a 75 dias, em conformidade com os artigos 90 a 100 da resolução nº 632/2014 da Anatel.
        MAC: 00:E0:4C:CF:95:8B | Serial ONU: ITBS:E8A2D273 | Caixa: ARD AC.5.3.13 | Porta: 1 |
        Multa: R$ 0,00""",
        tipo_da_os = "Cancelamento - Fibra",
        grupo_atendimento_os = "ARARENDÁ",
        relato_do_problema = """Cancelamento em razão de inadimplência superior a 75 dias, em conformidade com os artigos 90 a 100 da resolução nº 632/2014 da Anatel

        Observação1: Multa por quebra de contrato de R$ 0,00. Para negociar seu débito, basta entrar em contato pelo 0800-088-1111
        Observação2: MAC - 00:E0:4C:CF:95:8B | Serial ONU - ITBS:E8A2D273 | Caixa - ARD AC.5.3.13 | Porta - 1
        Observação3: Encerramento da OS de recolhimento de equipamentos deste contrato = Retirada Concluída""",
        incidencia_multa = True,
        valor_multa = '100,75',
        vencimento_multa = '10062023',
        planos_contas = "01.02.07 Cliente - Pessoa Física"
    )
