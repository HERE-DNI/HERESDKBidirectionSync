---
title: "takeScreenshot abstract method"
slug: "sdk-for-flutter-explore-mapview-heremapcontroller-takescreenshot"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- takeScreenshot.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-heremapcontroller-class</li>
<li class="self-crumb">takeScreenshot abstract method</li>
</ol>
<div class="self-name">takeScreenshot</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="mapview/HereMapController-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>takeScreenshot abstract method</h1></div>
<section class="multi-line-signature">
void
takeScreenshot(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-explore-mapview-takescreenshotcallback callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Asynchronously retrieves a screenshot of the map view.</p>
<p>Note that on Android devices this may not work when the map view is currently not visible,
for example, when an application is running in background and onPause() was called. On iOS
devices the GPU cannot be used when running in background and taking a screenshot is
therefore not possible when the map view is not visible.</p>
<p>The image is returned in a Dart ImageInfo object. The image itself can be accessed from
the ImageInfo.image member and its dimensions from the ImageInfo.image.width and the
ImageInfo.image.height members. These are represented as physical pixels, not device
independent pixels.</p>
<p>If a Flutter Image widget is desired, it can be created thus:</p>
<p>final ByteData byteData = await imageInfo.image.toByteData(format: ui.ImageByteFormat.png);
Image widget = Image.memory(byteData.buffer.asUint8List());</p>
<p><code>callback</code> Completion handler called when the screenshot is completed</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void takeScreenshot(TakeScreenshotCallback callback);</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-heremapcontroller-class</li>
<li class="self-crumb">takeScreenshot abstract method</li>
</ol>
<h5>HereMapController class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
