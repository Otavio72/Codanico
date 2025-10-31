import os
from pathlib import Path
import gzip
import random
import io

OUT_DIR = Path("tests_corrupt_files")
OUT_DIR.mkdir(exist_ok=True)

def write_bytes(name, data: bytes):
    p = OUT_DIR / name
    p.write_bytes(data)
    print(f"[OK] Gerado: {p}")

# 1️⃣ Arquivo truncado — pedaço de código cortado no meio
write_bytes("truncado.py", b"print('Inicio de arquivo...')\nprint('Mas foi cortado no meio")

# 2️⃣ Arquivo com bytes ilegais pra UTF-8 (quebra de decodificação)
write_bytes("utf8_invalido.py", b"\xff\xfe\xfa\x00\xff\x00\xab\xacprint('codigo ilegivel')\n")

# 3️⃣ Arquivo com mistura de texto e binário aleatório
mixed = b"print('Comeco legivel')\n" + os.urandom(40) + b"\nprint('Fim legivel')"
write_bytes("misturado_binario.py", mixed)

# 4️⃣ Arquivo de 1 byte (incompleto)
write_bytes("um_byte.py", b"p")

# 5️⃣ Arquivo com cabeçalho de outro formato (gzip)
buf = io.BytesIO()
with gzip.GzipFile(fileobj=buf, mode="wb") as f:
    f.write(b"print('isso esta compactado, nao texto')")
write_bytes("gzip_fake.py", buf.getvalue())

# 6️⃣ Arquivo que é só NULL bytes
write_bytes("zeros.py", b"\x00" * 200)

# 7️⃣ Arquivo cheio de caracteres randômicos não imprimíveis
noise = bytes(random.randint(0, 255) for _ in range(300))
write_bytes("ruido_total.py", noise)

# 8️⃣ Arquivo grande mas truncado (simula download quebrado)
big_partial = b"print('inicio ok')\n" + b"A" * 1024 * 10 + b"\x00\xff"
write_bytes("arquivo_truncado_grande.py", big_partial)

# 9️⃣ Arquivo corrompido por encoding alternado (latin1 misturado)
write_bytes("latin1_misturado.py", "print('Olá')\nçãõ\n".encode("latin1") + b"\xff\xff\xff")

# 🔟 Arquivo ilegível (nome estranho + binário)
nome_ruim = OUT_DIR / "ilegal_\x00_nome.py"
try:
    nome_ruim.write_bytes(b"print('nome bizarro')\n")
except Exception:
    print(f"[INFO] Nome {nome_ruim} não pôde ser criado (sistema não permite).")

# 🧠 README explicando os testes
(OUT_DIR / "README_CORRUPTOS.txt").write_text(
    "Arquivos de teste realmente corrompidos (nível de bytes):\n"
    "- truncado.py → arquivo cortado no meio (EOF inesperado)\n"
    "- utf8_invalido.py → bytes ilegais pra UTF-8\n"
    "- misturado_binario.py → mistura de texto e binário\n"
    "- um_byte.py → arquivo incompleto\n"
    "- gzip_fake.py → arquivo GZIP disfarçado de .py\n"
    "- zeros.py → apenas NULL bytes\n"
    "- ruido_total.py → bytes aleatórios (não UTF-8)\n"
    "- arquivo_truncado_grande.py → arquivo parcialmente escrito\n"
    "- latin1_misturado.py → encoding híbrido latin1 + bytes inválidos\n"
    "- ilegal_\\x00_nome.py → nome impossível (se suportado)\n\n"
    "Esses arquivos causam erros no open/read, não no parse do Python.\n"
    "Use-os pra testar tratamento de exceções ao abrir ou ler arquivos.\n",
    encoding="utf-8"
)

print(f"\nTodos os arquivos criados em: {OUT_DIR.resolve()}")
print("Pronto pra usar no Codanico — ele deve disparar exceções ao tentar abrir qualquer um deles!")
