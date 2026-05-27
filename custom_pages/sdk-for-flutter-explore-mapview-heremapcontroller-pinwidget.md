---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-heremapcontroller-pinwidget"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- pinWidget.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/HereMapController-class.html">/sdk-for-flutter-explore-mapview-heremapcontroller-class</a></li>
<li class="self-crumb">pinWidget abstract method</li>
</ol>
<div class="self-name">pinWidget</div>
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
<h1>pinWidget abstract method</h1></div>
<section class="multi-line-signature">
<a href="../../mapview/WidgetPin-class.html">/sdk-for-flutter-explore-mapview-widgetpin-class</a>?
pinWidget(<wbr/><ol class="parameter-list"> <li>Widget widget, </li>
<li><a href="../../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> coordinates, {</li>
<li><a href="../../core/Anchor2D-class.html">/sdk-for-flutter-explore-core-anchor2d-class</a>? anchor, </li>
</ol>})

      

    </section>
<section class="desc markdown">
<p>Pins a <code>Widget</code> to the MapView and returns a proxy object that can be used to
control the pinning.</p>
<p>The altitude component of the coordinates, if set, is interpreted as above sea level.
When not set, the coordinates are interpreted as at ground level.</p>
<p><code>widget</code> Widget to pin</p>
<p><code>coordinates</code> GeoCoordinates to pin the widget at</p>
<p><code>anchor</code> The anchor point for the widget which specifies the position offset relative to the widget's coordinates.</p>
<p>Returns <a href="../../mapview/WidgetPin-class.html">/sdk-for-flutter-explore-mapview-widgetpin-class</a> a pin proxy object</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">WidgetPin? pinWidget(Widget widget, GeoCoordinates coordinates, {Anchor2D? anchor});</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/HereMapController-class.html">/sdk-for-flutter-explore-mapview-heremapcontroller-class</a></li>
<li class="self-crumb">pinWidget abstract method</li>
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
</HTMLBlock>
