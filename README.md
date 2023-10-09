# wab-cviceni
Webove aplikace: backend

## Vytvoreni simple service
- Vytvoreni pracovni testovaci service

## Notes
### Pyproject.toml
- obsahuje informace k projektu
- extension -- stahnout ext pro Python a pro toml

### FastAPI
- (znovu pustit terminal pro nacteni virtualniho prostredi) -- NEFUNGUJE!
- psat do cmd v adresari, kde pdm existuje
- pdm venv activate
- pdm add fastapi
- pdm add uvicorn[standard]


### SPUSTENI
- `uvicorn main:app --reload (soubory musi byt ulozeny!!!)`
- instalace, pres pdm: pdm add 
- docs: http://localhost:8000/docs -- vygenerovane api
- start = "uvicorn main:app --reload" -> pustit mimo slozku jako `pdm run start`
- v ramci slozky primo "uvicorn..."

*ERRORS*

`(wab-cviceni-3.11) PS C:\Users\xpacako1\Downloads> pdm`

`Traceback (most recent call last):`

  `File "<frozen runpy>", line 88, in _run_code`

  `File "C:\Users\xpacako1\AppData\Roaming\Python\Python311\Scripts\pdm.exe\__main__.py", line 4, in <module>`

`ModuleNotFoundError: No module named 'pdm'`

*RESENI:*
- deactivate
- pdm venv activate
- pdm run start
- ... uz jede bez problemu