class InputView:
    @staticmethod
    def get_order_details(last_order_id):
        return {
            'orderid': last_order_id + 1,
            'customerid': 'ALFKI',
            'employeeid': 1,
            'orderdate': '2023-06-01',
            'requireddate': '2023-06-15',
            'shipperid': 1,
            'freight': 100.00,
            'shipname': 'Ship Name',
            'shipaddress': 'Ship Address',
            'shipcity': 'Ship City',
            'shipregion': 'Ship Region',
            'shippostalcode': '12345',
            'shipcountry': 'Country'
        }