---
title: "onInterpolatedLocationUpdated abstract method"
slug: "sdk-for-flutter-navigate-navigation-interpolatedlocationlistener-oninterpolatedlocationupdated"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onInterpolatedLocationUpdated.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-interpolatedlocationlistener-class</li>
<li class="self-crumb">onInterpolatedLocationUpdated abstract method</li>
</ol>
<div class="self-name">onInterpolatedLocationUpdated</div>
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
<div class="main-content" data-above-sidebar="navigation/InterpolatedLocationListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>onInterpolatedLocationUpdated abstract method</h1></div>
<section class="multi-line-signature">
void
onInterpolatedLocationUpdated(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-location-class location</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Called whenever a new interpolated location is calculated, usually several times per second.</p>
<p>The interpolated locations are only provided between /sdk-for-flutter-navigate-navigation-visualnavigator-startrendering and
/sdk-for-flutter-navigate-navigation-visualnavigator-stoprendering calls and the application is not running in the background.</p>
<ul>
<li><code>location</code> The interpolated location.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onInterpolatedLocationUpdated(Location location);</code></pre>
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
<li>/sdk-for-flutter-navigate-navigation-interpolatedlocationlistener-class</li>
<li class="self-crumb">onInterpolatedLocationUpdated abstract method</li>
</ol>
<h5>InterpolatedLocationListener class</h5>
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
