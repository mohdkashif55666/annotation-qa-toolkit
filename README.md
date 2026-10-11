# Annotation QA Toolkit

A lightweight, dependency-free Python toolkit for **quality-checking human-labelled datasets**, the core job in AI training and data annotation workflows.

Give it a CSV with one label column per annotator and it reports:

- **Inter-annotator agreement**: Fleiss' kappa (all raters) and Cohen's kappa (each pair), with Landis & Koch interpretation
- **Label distribution per annotator** to spot bias (e.g. an annotator over-using "positive")
- **Adjudication queue**: items with no majority, which need guideline review or expert tie-break

## Quick start

```bash
git clone https://github.com/<your-username>/annotation-qa-toolkit.git
cd annotation-qa-toolkit
python -m annotation_qa.cli data/sample_sentiment_labels.csv -o data/sample_report.md
pip install -r requirements.txt && pytest
```

## Input format

```csv
item_id,text,annotator_1,annotator_2,annotator_3
1,The delivery was fast,positive,positive,positive
```

## Sample output

See [`data/sample_report.md`](data/sample_report.md). On the included 12-item sentiment sample, Fleiss' kappa is 0.532 (moderate) and item #7 is flagged because all three annotators disagree.

## Why it matters

Low agreement usually means unclear guidelines, not bad annotators. Measuring it early lets teams fix label definitions, retrain annotators and keep training data reliable before it reaches a model.

## Project structure

```
annotation_qa/metrics.py   agreement metrics + majority vote
annotation_qa/report.py    CSV loading + markdown report
annotation_qa/cli.py       command-line entry point
tests/                     pytest unit tests
data/                      sample labels and generated report
```

## Roadmap

- Gold-standard accuracy per annotator
- Krippendorff's alpha for missing labels
- Confusion matrix between annotator pairs

## License
MIT
