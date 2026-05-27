---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-heremapcontroller-unpinwidget"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- unpinWidget.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/HereMapController-class.html">/sdk-for-flutter-explore-mapview-heremapcontroller-class</a></li>
<li class="self-crumb">unpinWidget abstract method</li>
</ol>
<div class="self-name">unpinWidget</div>
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
<h1>unpinWidget abstract method</h1></div>
<section class="multi-line-signature">
void
unpinWidget(<wbr/><ol class="parameter-list single-line"> <li>Widget widget</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Removes a <a href="../../mapview/WidgetPin-class.html">/sdk-for-flutter-explore-mapview-widgetpin-class</a> from the MapView by specifying the corresponding <code>Widget</code>.
Trying to unpin a widget that was not pinned or has been unpinned before has no effect.
All pinned widgets equal to <code>widget</code> will be removed.</p>
<p><code>widget</code> corresponding to the <a href="../../mapview/WidgetPin-class.html">/sdk-for-flutter-explore-mapview-widgetpin-class</a> to remove.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void unpinWidget(Widget widget);</code></pre>
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
<li class="self-crumb">unpinWidget abstract method</li>
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
