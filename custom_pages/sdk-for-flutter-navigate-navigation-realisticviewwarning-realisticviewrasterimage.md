---
title: "realisticViewRasterImage property - RealisticViewWarning class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-realisticviewwarning-realisticviewrasterimage"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/RealisticViewWarning-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">realisticViewRasterImage</span> property

</div>

<div class="section multi-line-signature">

<a href="sdk-for-flutter-navigate-navigation-realisticviewrasterimage-class">RealisticViewRasterImage</a>? <span class="name">realisticViewRasterImage</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

The realistic view object for which the warning is given. Image resources are stored as raster graphics. Within <a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-class">RealisticViewWarning</a>, only one type of image, either raster or vector, will be provided. If this property is not `null`, then <a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-realisticviewvectorimage">RealisticViewWarning.realisticViewVectorImage</a> will be `null`. **Note:** Certain countries support only raster images as realistic views. Currently, this is the case only for Japan, but in the future, more countries might support this type of realistic views.

</div>

## Implementation

``` dart
RealisticViewRasterImage? realisticViewRasterImage;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

