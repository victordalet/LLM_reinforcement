# LLM_reinforcement

## Run scrapper

```bash
export PYTHONPATH=$(pwd)/src:$(pwd)
uv run tools/scrapper/scrapper_sport_passion.py
uv run tools/scrapper/scrapper_musculaction.py
uv run tools/scrapper/scrapper_coach_hunter.py 
```

## Run app

```bash
export PYTHONPATH=$(pwd)/src:$(pwd)
streamlit run src/app/app.py
```

# Run train text

```bash
export PYTHONPATH=$(pwd)/src:$(pwd)
uv run tools/train_text_model.py
```

# Run train img

```bash
export PYTHONPATH=$(pwd)/src:$(pwd)
uv run tools/train_image_model.py
```