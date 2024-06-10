class InputView:
    @staticmethod
    def get_order_details(last_order_id):
        print("Insira os detalhes do pedido.")
        
        orderid = last_order_id + 1
        customerid = input("ID do Cliente: ")
        employeeid = int(input("ID do Funcionário: "))
        orderdate = input("Data do Pedido (YYYY-MM-DD): ") + " 00:00:00"
        requireddate = input("Data Necessária (YYYY-MM-DD): ") + " 00:00:00"
        shipperid = int(input("ID do Transportador: "))
        freight = float(input("Frete: "))
        shipname = input("Nome do Destinatário: ")
        shipaddress = input("Endereço do Destinatário: ")
        shipcity = input("Cidade do Destinatário: ")
        shipregion = input("Região do Destinatário: ")
        shippostalcode = input("CEP do Destinatário: ")
        shipcountry = input("País do Destinatário: ")
        
        return {
           'orderid': orderid,
            'customerid': customerid,
            'employeeid': employeeid,
            'orderdate': orderdate,
            'requireddate': requireddate,
            'shipperid': shipperid,
            'freight': freight,
            'shipname': shipname,
            'shipaddress': shipaddress,
            'shipcity': shipcity,
            'shipregion': shipregion,
            'shippostalcode': shippostalcode,
            'shipcountry': shipcountry
        }
