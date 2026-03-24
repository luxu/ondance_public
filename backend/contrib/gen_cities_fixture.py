"""
Gera user/fixtures/cities.json com todos os municípios brasileiros
buscados da API pública do IBGE.

Uso:
    python contrib/gen_cities_fixture.py

Requer apenas bibliotecas da stdlib (urllib + json).
Os UUIDs das cidades são determinísticos (uuid5) — rodar o script
duas vezes produz o mesmo arquivo.
"""

import gzip
import json
import sys
import uuid
from pathlib import Path
from urllib.request import urlopen

IBGE_URL = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios?orderBy=nome"
STATES_FIXTURE = Path(__file__).parent.parent / "user" / "fixtures" / "states.json"
OUTPUT = Path(__file__).parent.parent / "user" / "fixtures" / "cities.json"

# Namespace fixo para geração determinística de UUIDs das cidades
CITY_NAMESPACE = uuid.UUID("d3e5f700-0000-0000-0000-000000000000")


def load_state_map() -> dict[str, str]:
    """Retorna { 'SP': 'uuid-do-estado', ... } lendo states.json."""
    with STATES_FIXTURE.open(encoding="utf-8") as f:
        states = json.load(f)
    return {entry["fields"]["abbreviation"]: str(entry["pk"]) for entry in states}


def fetch_municipalities() -> list[dict]:
    print(f"Buscando municípios em {IBGE_URL} ...")
    with urlopen(IBGE_URL, timeout=30) as resp:  # noqa: S310
        raw = resp.read()
        if resp.info().get("Content-Encoding") == "gzip" or raw[:2] == b"\x1f\x8b":
            raw = gzip.decompress(raw)
        data = json.loads(raw.decode("utf-8"))
    print(f"  {len(data)} municípios recebidos.")
    return data


def build_fixture(municipalities: list[dict], state_map: dict[str, str]) -> list[dict]:
    fixture = []
    missing_states: set[str] = set()

    for mun in municipalities:
        try:
            sigla = mun["microrregiao"]["mesorregiao"]["UF"]["sigla"]
        except (KeyError, TypeError):
            sigla = mun["regiao-imediata"]["regiao-intermediaria"]["UF"]["sigla"]
        state_uuid = state_map.get(sigla)
        if not state_uuid:
            missing_states.add(sigla)
            continue

        city_uuid = str(uuid.uuid5(CITY_NAMESPACE, str(mun["id"])))
        fixture.append(
            {
                "model": "user.city",
                "pk": city_uuid,
                "fields": {
                    "name": mun["nome"],
                    "state": state_uuid,
                },
            }
        )

    if missing_states:
        print(f"AVISO: estados não encontrados no mapa: {sorted(missing_states)}", file=sys.stderr)

    return fixture


def main() -> None:
    state_map = load_state_map()
    municipalities = fetch_municipalities()
    fixture = build_fixture(municipalities, state_map)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8") as f:
        json.dump(fixture, f, ensure_ascii=False, indent=2)

    print(f"Fixture salva em {OUTPUT} ({len(fixture)} cidades).")


if __name__ == "__main__":
    main()
