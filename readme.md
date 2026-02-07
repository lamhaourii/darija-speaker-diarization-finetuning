# darija-speaker-diarization-finetuning

Fine-tuned pyannote speaker diarization model for Darija (Moroccan Arabic) with 0.12 DER.

## Overview

This project improves speaker diarization for Darija by fine-tuning `pyannote/segmentation-3.0` on a synthetic dataset of 2-person conversations, achieving a Diarization Error Rate (DER) of **0.12** on Darija audio.

## Pipeline

1. **Data Collection**: Downloaded videos from Moroccan YouTubers
2. **Clip Extraction**: Chunked videos into small speaker clips → [darija-speakers-clips](https://huggingface.co/datasets/igitsml/darija-speakers-clips)
3. **Synthetic Call Generation**: Created realistic 2-person calls with controlled overlap and silence → [darija-synthetic-calls](https://huggingface.co/datasets/igitsml/darija-synthetic-calls)
4. **Model Fine-tuning**: Fine-tuned pyannote segmentation model → [speaker-segmentation-darija2](https://huggingface.co/igitsml/speaker-segmentation-darija2)

## Model

- **Base Model**: `pyannote/segmentation-3.0`
- **Fine-tuned Model**: [igitsml/speaker-segmentation-darija2](https://huggingface.co/igitsml/speaker-segmentation-darija2)
- **Performance**: DER = 0.12 on Darija conversations



## Application

We used this model to create an efficient Darija transcription system by accurately segmenting speakers before transcription.

## Datasets

- [Darija Speaker Clips](https://huggingface.co/datasets/igitsml/darija-speakers-clips)
- [Darija Synthetic Calls](https://huggingface.co/datasets/igitsml/darija-synthetic-calls)

