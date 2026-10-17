# Parent 1: Camera
#   - method: take_photo() -> "📸 Photo clicked"
#   - method: record_video() -> "🎥 Video recording..."
#
# Parent 2: Phone
#   - method: call(number) -> "📞 Calling {number}..."
#   - method: send_message(number, msg) -> "💬 Message sent to {number}"
#
# Parent 3: MusicPlayer
#   - method: play_music() -> "🎵 Music playing..."
#   - method: pause_music() -> "⏸️  Music paused"
#
# Child: Smartphone(Camera, Phone, MusicPlayer)
#   - Sab features access kare
#   - extra: method: browse_internet() -> "🌐 Browsing internet..."
#
# Test karo: Smartphone object banao, sab methods call karo

class Camera:
    def take_photo(self):
        return "📸 Photo clicked"
    def record_video(self):
        return "🎥 Video recording..."

class Phone:
    def call(self, number):
        return f"📞 Calling {number}..."
    def send_message(self, number, msg):
        return f"💬 Message {msg} sent to {number}"

class MusicPlayer:
    def play_music(self):
        return "🎵 Music playing..."
    def pause_music(self):
        return "⏸️  Music paused"

class Smartphone(Camera, Phone, MusicPlayer):
    def browse_internet(self):
        return "🌐 Browsing internet..."

sp = Smartphone()

print(sp.take_photo())
print(sp.record_video())
print(sp.call(9988776655))
print(sp.send_message( 9988776655, "hello dost"))
print(sp.play_music())
print(sp.pause_music())
print(sp.browse_internet())
print(Smartphone.__mro__)