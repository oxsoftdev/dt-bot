class ws:

    def __init__(self, cnxn):
        self.cnxn = cnxn

    def insert_stream_update(self, o):
        tsql = '''
            ; DECLARE @id bigint
            ; EXEC [Bitso].[ws].[usp_InsertStreamUpdate] ?,?,?,?,?, @id OUTPUT
            ; SELECT @id
        '''
        params = (
            o._timestamp,
            o._datetime,
            #
            getattr(o, 'type', None),
            getattr(o, 'book', None),
            getattr(o, 'sequence_no', None)
        )
        cursor = self.cnxn.cursor()
        with cursor.execute(tsql, params):
            return cursor.fetchone()[0]

    def insert_order_update(self, StreamUpdate_id, o):
        tsql = '''
            ; DECLARE @id bigint
            ; EXEC [Bitso].[ws].[usp_InsertOrderUpdate] ?,?,?,?,?,?,?,?,?,?, @id OUTPUT
            ; SELECT @id
        '''
        params = (
            o._timestamp,
            o._datetime,
            StreamUpdate_id,
            #
            getattr(o, 'book', None),
            getattr(o, 'rate', None),
            getattr(o, 'amount', None),
            getattr(o, 'value', None),
            getattr(o, 'type', None),
            getattr(o, 'timestamp', None),
            getattr(o, 'datetime', None)
        )
        cursor = self.cnxn.cursor()
        with cursor.execute(tsql, params):
            return cursor.fetchone()[0]

    def insert_trade_update(self, StreamUpdate_id, o):
        tsql = '''
            ; DECLARE @id bigint
            ; EXEC [Bitso].[ws].[usp_InsertTradeUpdate] ?,?,?,?,?,?,?,?,?,?,?, @id OUTPUT
            ; SELECT @id
        '''
        params = (
            o._timestamp,
            o._datetime,
            StreamUpdate_id,
            #
            getattr(o, 'book', None),
            getattr(o, 'tid', None),
            getattr(o, 'rate', None),
            getattr(o, 'amount', None),
            getattr(o, 'value', None),
            getattr(o, 'type', None),
            getattr(o, 'maker_order_id', None),
            getattr(o, 'taker_order_id', None)
        )
        cursor = self.cnxn.cursor()
        with cursor.execute(tsql, params):
            return cursor.fetchone()[0]
