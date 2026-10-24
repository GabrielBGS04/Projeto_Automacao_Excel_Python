
#Biblioteca da automação
import pandas as pd
from plyer import notification


def verifica_contas():
    try:
        df = pd.read_excel('contas.xlsx', parse_dates=['VENCIMENTO'])

        hoje = pd.Timestamp.now().normalize()

        pendentes = df[(df['VENCIMENTO'] <= hoje) & (df['STATUS'].str.upper() != "PAGO")]

        for _, linha in pendentes.iterrows():
            nome_da_conta = linha["CONTA"]
            data_vencimento = linha["VENCIMENTO"].strftime('%d/%m/%Y')

            notification.notify(
                title="Lembrete de Pagamento",
                message=f"A conta {nome_da_conta} está proxima ou passou do limite ({data_vencimento})",
                app_name="Aviso Pagamentos",
                timeout=15,
            )
    except Exception as e:
        print(f"Erro interno: {e}")
        notification.notify(
            title="Erro na Planilha",
            message="Verificar se o Excel está fechado e preenchido corretamente",
            timeout=15,
        )

if __name__ == "__main__":
    verifica_contas()