# Parent: MediaPlayer
#   - attributes: device_name
#   - method: play() -> "Playing media..."
#   - method: stop() -> "Stopped"
#   - method: display()
#
# Child: MP3Player
#   - extra: storage_gb
#   - override play() -> "Playing MP3: {song}"
#   - extra method: shuffle() -> "Shuffle ON"
#
# Child: CDPlayer
#   - extra: cd_count
#   - override play() -> "Playing CD #{num}"
#   - extra method: eject() -> "CD ejected"
#
# Child: StreamingPlayer
#   - extra: subscription, quality
#   - override play() -> "Streaming on {subscription} at {quality}"
#   - extra method: download(song) -> "Downloaded {song}"
#
# List banao sab players ki
# Loop chalao aur sabko play() karwao — POLYMORPHISM!

class MediaPlayer:
    def __init__(self, device_name):
        self.device_name = device_name

    def play(self):
        print("▶️  Playing media...")

    def stop(self):
        print("⏹️  Stopped")

    def display(self):
        print(f"--- Device: {self.device_name} ---")
        print(f"Type       : {type(self).__name__}")

    def __str__(self):
        return f"{self.device_name} ({type(self).__name__})"


class MP3Player(MediaPlayer):
    def __init__(self, device_name, storage_gb):
        super().__init__(device_name)
        self.storage_gb = storage_gb

    def play(self, song="Shape of You"):
        print(f"▶️  Playing MP3: {song}")

    def shuffle(self):                          
        print("🔀 Shuffle ON")

    def display(self):                          
        super().display()
        print(f"Storage    : {self.storage_gb} GB")


class CDPlayer(MediaPlayer):
    def __init__(self, device_name, cd_count):
        super().__init__(device_name)
        self.cd_count = cd_count

    def play(self, cd_num=1):
        print(f"▶️  Playing CD #{cd_num}")

    def eject(self):
        print("📀 CD ejected")

    def display(self):                          
        super().display()
        print(f"CDs        : {self.cd_count}")


class StreamingPlayer(MediaPlayer):
    def __init__(self, device_name, subscription, quality):
        super().__init__(device_name)
        self.subscription = subscription
        self.quality = quality

    def play(self):
        print(f"▶️  Streaming on {self.subscription} at {self.quality}")

    def download(self, song):
        print(f"⬇️  Downloaded: {song}")

    def display(self):                          
        super().display()
        print(f"Plan       : {self.subscription}")
        print(f"Quality    : {self.quality}")


# ===== MAIN =====
players = [
    MP3Player("iPod", 64),
    CDPlayer("Sony CD Player", 5),
    StreamingPlayer("Spotify", "Premium", "320 kbps"),
]

print("=" * 30)
print("🎵 MUSIC PLAYER SYSTEM")
print("=" * 30)

for p in players:
    p.display()
    p.play()
    p.stop()
    
    # Unique methods bhi call karo
    if isinstance(p, MP3Player):
        p.shuffle()
    elif isinstance(p, CDPlayer):
        p.eject()
    elif isinstance(p, StreamingPlayer):
        p.download("Blinding Lights")
    
    print("-" * 30)