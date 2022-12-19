import time, random
from multiprocessing.dummy import Process, Queue


class TwapExec():

    def __init__(self):
        self.period = 5
        self.cnt = 1
        self.pair = None
        self.side = None
        self.tolvol = None
        self.queue = None
        self.last_oid = None
        self.c_vol = 0
        self.Done = False

    def place_order(self, vol):
        self.last_oid = 1

    def cancel_order(self, oid):
        pass

    def get_order_c_vol(self, oid):
        return 1

    def on_order_cancel(self):
        if self.last_oid is not None:
            self.cancel_order(self.last_oid)
            c_vol = self.get_order_c_vol(self.last_oid)
            self.c_vol += c_vol

    def on_order(self):
        if self.c_vol < self.tolvol:
            self.place_order(self.cnt)

    def put_pair(self, pair, side, vol, queue):
        self.pair = pair
        self.side = side
        self.tolvol = vol
        self.queue = queue
        while not self.Done:
            self.monitor_thr()
            if self.Done: break
            self.on_order_cancel()
            self.on_order()
            time.sleep(self.period * (1.2 - 0.4 * random.random()))

    def monitor_thr(self):
        if self.task_terminate():
            self.Done = True
            return
        if self.c_vol >= self.tolvol:
            self.Done = True
            return

    def task_terminate(self):
        if self.queue.qsize() > 0:
            status = self.queue.get()
            if status.lower() == 'cancel':
                return True
        return False


def twap_order_put(pair, side, vol):
    twap_exec = TwapExec()
    q = Queue()
    order_process = Process(target=twap_exec.put_pair, args=(pair, side, vol, q, ))
    order_process.start()
    return {"order_process":order_process, "queue":q}


def twap_order_cancel(order):
    if order["order_process"].is_alive():
        order["queue"].put("cancel")
        # Wait For worker to finish
        order["order_process"].join()


if __name__ == '__main__':
    order = twap_order_put('GBTC', 'BUY', 10)
    time.sleep(30)
    twap_order_cancel(order)
    time.sleep(300)