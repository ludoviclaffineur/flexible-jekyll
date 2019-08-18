---
layout: post
title: Granular Synthesiser
date: 2019-08-17 9:21:20 +0200
img: granular_synth.png # Add image post (optional)
description: "Granular synthesis how mine works"
tags: [audio, synthesis, granular, grain, audio source]
---
## How it works

When I worked for [Laras](http://laras.be), I had the opportunity for my sonification project to model and code my own granular synthesiser.

> Granular synthesis is a basic sound synthesis method that operates on the microsound time scale.
> It is based on the same principle as sampling. However, the samples are not played back conventionally, but are instead split into small pieces of around 1 to 50 ms. These small pieces are called grains. Multiple grains may be layered on top of each other, and may play at different speeds, phases, volume, and frequency, among other parameters.

*[Source wikipedia](https://en.wikipedia.org/wiki/Granular_synthesis)*

## Creation of grains
We first have to load a wave form in order to pick some samples to create our grains. Those grain are randomly selected within a window (subset) of the whole waveform as you can see on the figure 1. Having a window can be convenient if you want to select only certain parts of the waveform and move this window to modify the generated grains.

<p align="center">
<img src="/assets/img/sample_selection.png" alt="Grain selection"/>
</p>
<p align="center">
Figure 1: Sample selection
</p>

A grain is composed of Selected sample and some silence at the end of the grain to temporise the succession of grains. Reducing the blank will accelerate the succession of grains and accelerate the production of grains.

Grain = Selected sample + Blank


```cpp
class Grain{
public:
    Grain(
      float* audioFile,
      int duration,
      int blank,
      int initPos,
      int channels,
      int musicSize
    );
    samples getSample();

    int mEnvelope;
    int mDuration;
    int mCurrentPostion;
    int mInitPostion;

    float* mAudioFile;
    bool isDone(){
        return done;
    }
    bool done;
    int mBlank;
    int mWindowSize;
    int mChannels;
    int mMusicSize;
};
```
