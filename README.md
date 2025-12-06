# LLM_reinforcement

## Run scrapper

```bash
export PYTHONPATH=$(pwd)/src:$(pwd)
uv run tools/scrapper/scrapper_sport_passion.py
```

## Run app

```bash
streamlit run src/app/app.py
```

# Run train text

```bash
uv run tools/train_txt_model.py
```

# Run train img

```bash
uv run tools/train_image_model.py
```