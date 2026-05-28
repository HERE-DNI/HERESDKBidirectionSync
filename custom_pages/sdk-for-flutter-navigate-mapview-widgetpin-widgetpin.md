---
title: "WidgetPin constructor"
slug: "sdk-for-flutter-navigate-mapview-widgetpin-widgetpin"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- WidgetPin.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-widgetpin-class</li>
<li class="self-crumb">WidgetPin factory constructor</li>
</ol>
<div class="self-name">WidgetPin</div>
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
<div class="main-content" data-above-sidebar="mapview/WidgetPin-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>WidgetPin constructor</h1></div>
<section class="multi-line-signature">
WidgetPin(<wbr/>{<ol class="parameter-list"> <li>required Widget child, </li>
<li>required /sdk-for-flutter-navigate-core-geocoordinates-class coordinates, </li>
<li>/sdk-for-flutter-navigate-core-anchor2d-class? anchor, </li>
<li>dynamic onChange()?, </li>
<li>dynamic onUnpin(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-mapview-widgetpin-class</li>
</ol>)?, </li>
</ol>})
    </section>
<section class="desc markdown">
<p>Creates a /sdk-for-flutter-navigate-mapview-widgetpin-class displaying child <code>Widget</code> at coordinates location on the map
Don't use this constructor directly. Instead use /sdk-for-flutter-navigate-mapview-heremapcontroller-pinwidget to create a /sdk-for-flutter-navigate-mapview-widgetpin-class.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory WidgetPin({
  required Widget child,
  required GeoCoordinates coordinates,
  Anchor2D? anchor,
  Function()? onChange,
  Function(WidgetPin)? onUnpin,
}) =&gt;
    $prototype.make(
      child: child,
      coordinates: coordinates,
      anchor: anchor,
      onChange: onChange,
      onUnpin: onUnpin,
    );</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-widgetpin-class</li>
<li class="self-crumb">WidgetPin factory constructor</li>
</ol>
<h5>WidgetPin class</h5>
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
