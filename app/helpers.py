import os
from dotenv import load_dotenv

load_dotenv()

def env(key, default=None):
    """
    Mengambil nilai dari .env berdasarkan key yang diberikan.
    Jika key tidak ditemukan, akan mengembalikan nilai default (default: None).
    """
    return os.getenv(key, default)
