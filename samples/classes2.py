from samples.classes import Base

class Classes2(Base):
    def run(self):
        print(self.value)


if __name__ == "__main__":
    Classes2().run()
