---
author: Aquiles Carattino
slug: python-tip-ready-publish-matplotlib-figures
date: 2020-05-18
description: Learn how to make figures with proper font size and resolution, ready to be published
image: '/images/Tips_02_Python-Tips-Matplotlib-Saving.width-800.png'
subtitle: Learn how to make figures with proper font size and resolution, ready to be published
tags: [matplotlib, resolution, figure, plot, saving] 
title: "Python Tip: Ready to Publish Matplotlib Figures"
---

Saving figures for publications, presentations, books, or websites can be a cumbersome task but doesn't need to be. In this **Python Tip**, we will see how to create images using Matplotlib that are ready to be embedded. We will take care of the most important aspects: shape, font sizes, and resolution. You won't have to tinker ever again with random parameters until the result is right. 

Once you understand the options that Matplotlib offers, and what they mean, you will realize that generating publication-ready figures can be a breeze. We will focus mostly on plots for papers, but once you get the gist, you can extrapolate to other formats such as posters, books, or websites.  

## Size 
First, we need to discuss size and resolution, two independent, but related magnitudes. Size is the physical dimensions of an image. If we were preparing a plot for a paper, for example, we should first check the column width. [Science uses a width](https://www.sciencemag.org/sites/default/files/Figure_prep_guide.pdf) of 9cm, or 3.54 inches. The height of the image will depend on the content we are displaying. For simplicity, I will assume a square image, so we have 3.54x3.54 inches. 

With matplotlib, defining the size of a figure is straightforward:

```python
fig = plt.figure(figsize=(3.54,3.54))
plt.plot(x, y)
```

However, knowing the size is only half the problem. We can make a plot of the same size, but with different *resolution*, which is the second parameter we need to discuss. 

## DPI
The resolution of an image can be calculated, counting the total number of pixels it contains or defining the dots per inch: **DPI**. We can calculate the dots per inch if we know the total number of pixels and the physical size we expect for the image. The other way around, if we know the final size of an image and the **dpi**, we can calculate the number of pixels we need. The terminology comes from the printer process of making *dots* of ink. If we are looking at the image on a screen instead of printing, the *dots* become *pixels*. 

If we are preparing a paper, the *dpi* is fixed by the printer. Therefore, we must match that value when we prepare our images, or they would look terrible. A typical *dpi* value for printing is **600dpi**. We can specify this directly on matplotlib:

```python
fig = plt.figure(figsize=(3.54,3.54), dpi=600)
plt.plot(x, y)
```

If we make the math, this means the final figure has 2124 pixels on each axis. 

## Font Size
At some point, you must wonder why we are specifying both the figure size and the *dpi*. If we used bigger image sizes, we would get more pixels. However, font size and thickness is related to the size of the figure, not to the number of pixels. Therefore, if we do the following:

```python
fig = plt.figure(figsize=(3.54,3.54), dpi=300)
plt.plot(x, y, linewidth=2)
plt.xlabel('X label (s)', fontsize=20)
plt.ylabel('Y label (V)', fontsize=10)
```

We will get a figure that, when set to the proper size of 3.54inx3.54in will have axes with fonts of 20pt and 10pt. Matplotlib allows us to set the font size to the exact value we want. For example, if our main text uses a font size of 12pt, we can make the labels slightly larger than the text, and the ticks slightly smaller:

```python
import matplotlib 
matplotlib.rc('xtick', labelsize=10) 
matplotlib.rc('ytick', labelsize=10) 

fig = plt.figure(figsize=(3.54,3.54), dpi=300)
plt.plot(x, y, linewidth=2)
plt.xlabel('X label (s)', fontsize=15)
plt.ylabel('Y label (V)', fontsize=15)
```

Remember, setting the font size implies knowing the final size of the figure. We can try to change the *dpi* parameter. We will see that even if the figure shrinks on the screen (because of fewer pixels), the relative size of the fonts to the total image area is always the same. If you stretch the images to occupy the same space on the screen, the axes labels will have the same size.  

You can download [this document]https://www.pythonforthelab.com/documents/1/image_sizes.pdf) to see how the dpi affects the overall image quality. There are figures at 72dpi, 150dpi, 300dpi, and 600dpi. I've also included one figure with double-column width but keeping all the other parameters the same, including the data.

If you are preparing figures for a poster, for example, you would likely have a larger figure size, bigger font sizes, but keeping a *dpi* of 600 for printing. 

## Saving
Once we have the figures we want, the last step is to save them. We must decide the format we want to use to save them. I tend to default to *png* because it is a lossless compression format. It means that the quality is as good as what I've defined it. In Matplotlib, it becomes:

```python
plt.savefig('figure.png', bbox_inches='tight')
```

The extra argument, ``bbox_inches`` is needed to be sure Matplotlib figures out the entire canvas before saving. If we don't add it, the axes will likely be cropped out of the picture. PNG images can be embedded in documents, websites, and presentations. Almost all paper journals also accept them if you provide them with the proper resolution. 

Other alternatives are saving as vector formats. You can choose to save as *SVG* if you plan to further edit the images in programs such as Inkscape or Adobe Illustrator. If you are writing in TeX, prefer vector over raster, you can save the figures as *pdf*. My note: avoid *eps* (encapsulated postscript), unless you have a legitimate reason to do it. They are just harder to share, and they don't provide a real gain.  

## For Presentations
If we are preparing figures for a presentation, we must consider two things. People will be looking at the slides from afar, and we don't want to have PowerPoint files of hundreds of megabytes. Generally speaking, font sizes in presentations are larger than in a paper, or people won't be able to see the axes. The other aspect is that figures should have a reasonable amount of pixels. Higher resolutions would generate heavy figures without any gain. 

PowerPoint specifies some default slide dimensions. For a wide-screen presentation, they are 13.33inx7.5in. Let's assume we will use a Full-HD projector, which has a width of 1920px and a height of 1080px. It gives a *dpi* of 144. However, PowerPoint works with a [default resolution](https://docs.microsoft.com/en-us/office/troubleshoot/powerpoint/change-export-slide-resolution) of **96dpi**. 

**Note**: other programs may use different default resolutions, or newer versions of PowerPoint may default to higher resolutions. In any case, the only thing you have to do is changing the *dpi* parameter of the figure. 

With the information we have, we can create the figures: 

```python
import matplotlib 
matplotlib.rc('xtick', labelsize=16) 
matplotlib.rc('ytick', labelsize=16) 

fig = plt.figure(figsize=(13.33,7.5), dpi=96)
plt.plot(x, y, linewidth=2)
plt.xlabel('X label (s)', fontsize=18)
plt.ylabel('Y label (V)', fontsize=18)
```

We have selected font sizes of **16** and **18**. These are reasonable values, but you may prefer to make them larger if you are presenting to large auditoriums.  In most presentations, however, we won't show figures at full-screen. If we use two images side-by-side, we can have something like this:

```python
fig = plt.figure(figsize=(5,3), dpi=96)
```

If we don't scale the image after we embed it into PowerPoint, we will have consistent figures. Perhaps they are full-screen, maybe they are displayed side-by-side, but all the axes and line thicknesses will be precisely the same. 

## Figures for the Web
If you are preparing figures for the web, then the discussion becomes much more complicated. Screens change in shape and resolution. Someone behind an iPad with a retina display will have as many pixels as someone behind a desktop screen. Still, the physical size of the figure is dramatically different. There is no blanket advice on how to prepare images for the web that work across all possible situations. Most websites make separate images for different situations, at various resolutions, and with different content. 

However, the best you can do when preparing images for the web is to save them as **SVG**, which is a vector format. These images can be scaled without losing resolution. In Matplotlib, it is trivial:

```python
plt.savefig('my_figure.svg', bbox_inches='tight')
```

You can go ahead and try changing the *dpi* of the image before saving, and try to notice if there are any differences. 

## Conclusions
If you are preparing figures for a publication, the best you can do is finding out the size figures should have. Most journals give you the dimensions of the columns. If you can't find them, you can always default to the size of [Science](https://www.sciencemag.org/sites/default/files/Figure_prep_guide.pdf). Once you know the size of your figures, fix the *dpi*. If it is for a paper, a thesis, or a poster, **600dpi** should be good enough. Then, set the font size of the labels and the axes to match the font size of the text around them. You can make labels and ticks slightly bigger or smaller than the text, depending on your style preferences. 

In [this PDF](https://www.pythonforthelab.com/documents/1/image_sizes.pdf), I have included figures generated at different *dpi* but scaled to the sizes recommended by Science.