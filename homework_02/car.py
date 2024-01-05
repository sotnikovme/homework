from homework_02.engine import Engine
from homework_02.base import Vehicle


class Car(Vehicle):
    engine: Engine
    # type = Engine
    def set_engine(self, a:Engine):
        self.engine = a
        # self.volume
        # self.pistons