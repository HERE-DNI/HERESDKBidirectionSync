---
title: "startWithLocationOptions abstract method"
slug: "sdk-for-flutter-navigate-location-locationenginebase-startwithlocationoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startWithLocationOptions.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-location-locationenginebase-class</li>
<li class="self-crumb">startWithLocationOptions abstract method</li>
</ol>
<div class="self-name">startWithLocationOptions</div>
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
<div class="main-content" data-above-sidebar="location/LocationEngineBase-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>startWithLocationOptions abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-location-locationenginestatus
startWithLocationOptions(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-location-locationoptions-class locationOptions</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Starts the location engine with desired /sdk-for-flutter-navigate-location-locationoptions-class.</p>
<p>Returns
/sdk-for-flutter-navigate-location-locationenginestatus, if /sdk-for-flutter-navigate-location-locationenginebase-startwithlocationoptions is called again without /sdk-for-flutter-navigate-location-locationenginebase-stop in between.
Make sure to call either /sdk-for-flutter-navigate-location-locationenginebase-confirmhereprivacynoticeinclusion or /sdk-for-flutter-navigate-location-locationenginebase-confirmhereprivacynoticeexception beforehand.
This method variant is not currently supported on iOS platforms. Returns /sdk-for-flutter-navigate-location-locationenginestatus on platforms which this method variant is not supported.</p>
<ul>
<li><code>locationOptions</code> Desired location options.</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-location-locationenginestatus. Engine status. Valid values are defined in /sdk-for-flutter-navigate-location-locationenginestatus</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LocationEngineStatus startWithLocationOptions(LocationOptions locationOptions);</code></pre>
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
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-location-locationenginebase-class</li>
<li class="self-crumb">startWithLocationOptions abstract method</li>
</ol>
<h5>LocationEngineBase class</h5>
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
