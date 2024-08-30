
def calculate_investment_summary(clients, bonds_investments, stocks_investments):
        investment_summary = []
            for client in clients:
                      total_bonds = sum(bi['invested_amount'] for bi in bonds_investments if bi['client_id'] == client['id'])
                              total_stocks = sum(si['invested_amount'] for si in stocks_investments if si['client_id'] == client['id'])
                              if total_bonds > 5000:
                                          summary = {
                                                                  'client_name': client['name'],
                                                                                  'total_invested_in_bonds': round(total_bonds, 2),
                                                                                                  'total_invested_in_stocks': round(total_stocks, 2)
                                          }
                                                      investment_summary.append(summary)
                                              return sorted(investment_summary, key=lambda x: x['total_invested_in_bonds'], reverse=True)
                      
                                          }