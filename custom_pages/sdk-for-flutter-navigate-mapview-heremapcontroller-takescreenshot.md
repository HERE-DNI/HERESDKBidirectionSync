---
title: "takeScreenshot method - HereMapController class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-heremapcontroller-takescreenshot"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/HereMapController-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">takeScreenshot</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">takeScreenshot</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-takeScreenshot-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-takescreenshotcallback">TakeScreenshotCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Asynchronously retrieves a screenshot of the map view.

Note that on Android devices this may not work when the map view is currently not visible, for example, when an application is running in background and onPause() was called. On iOS devices the GPU cannot be used when running in background and taking a screenshot is therefore not possible when the map view is not visible.

The image is returned in a Dart ImageInfo object. The image itself can be accessed from the ImageInfo.image member and its dimensions from the ImageInfo.image.width and the ImageInfo.image.height members. These are represented as physical pixels, not device independent pixels.

If a Flutter Image widget is desired, it can be created thus:

final ByteData byteData = await imageInfo.image.toByteData(format: ui.ImageByteFormat.png); Image widget = Image.memory(byteData.buffer.asUint8List());

`callback` Completion handler called when the screenshot is completed

</div>

## Implementation

``` dart
void takeScreenshot(TakeScreenshotCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

