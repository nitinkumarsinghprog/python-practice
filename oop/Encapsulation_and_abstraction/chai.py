from abc import ABC, abstractmethod

# ===== ABSTRACT CLASS =====
class ChaiMachine(ABC):
    
    @abstractmethod
    def make_chai(self):
        pass
    
    def on_button(self):              # Concrete method
        print("🔘 Button dabaya...")
        self.make_chai()              # Andar ka kaam child karega


# ===== CHILD CLASS 1 =====
class ElaichiChai(ChaiMachine):
    def make_chai(self):
        print("🫖 Elaichi chai ban rahi hai...")
        print("   (paani garam + patti + elaichi + doodh)")
        print("☕ Chai ready!")


# ===== CHILD CLASS 2 =====
class AdrakChai(ChaiMachine):
    def make_chai(self):
        print("🫖 Adrak chai ban rahi hai...")
        print("   (paani garam + patti + adrak + doodh)")
        print("☕ Chai ready!")


# ===== MAIN =====
# machine = ChaiMachine()    # ❌ ERROR! Abstract class ka object nahi banta

chai1 = ElaichiChai()
chai1.on_button()              # ✅ Button dabaya → chai bani

print()

chai2 = AdrakChai()
chai2.on_button()