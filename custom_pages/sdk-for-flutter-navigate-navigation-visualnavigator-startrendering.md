---
title: "startRendering abstract method"
slug: "sdk-for-flutter-navigate-navigation-visualnavigator-startrendering"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startRendering.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-visualnavigator-class</li>
<li class="self-crumb">startRendering abstract method</li>
</ol>
<div class="self-name">startRendering</div>
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
<div class="main-content" data-above-sidebar="navigation/VisualNavigator-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>startRendering abstract method</h1></div>
<section class="multi-line-signature">
void
startRendering(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-mapview-mapviewbase-class mapView</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Starts visual navigation rendering.</p>
<p>A preconfigured current location marker is shown as soon as a location is received.
The marker is chosen according to the transport mode specified in the route. If no route is
present, the marker is chosen based on the /sdk-for-flutter-navigate-navigation-navigatorinterface-trackingtransportspecification property.
Calling startRendering() changes the /sdk-for-flutter-navigate-mapview-mapcamera-principalpoint property so that the current
position indicator is equal to the value from /sdk-for-flutter-navigate-navigation-camerabehavior-normalizedprincipalpoint,
in which by default places the principal point slightly at the bottom of the mapview. It is
restored to its original value when stopRendering() is called.
<strong>Note:</strong> When rendering is started again for a new map view instance, rendering
is automatically stopped on the previous map view instance. Also note that
the /sdk-for-flutter-navigate-mapview-mapviewbase-framerate can be lowered to reduce CPU usage, to adjust for tradeoffs
between rendering smoothness versus battery consumption.</p>
<ul>
<li><code>mapView</code> The map view on which visual navigation will take place.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void startRendering(MapViewBase mapView);</code></pre>
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
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-visualnavigator-class</li>
<li class="self-crumb">startRendering abstract method</li>
</ol>
<h5>VisualNavigator class</h5>
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
