---
title: "startWithLocationOptions method"
slug: "sdk-for-flutter-navigate-location-locationengine-startwithlocationoptions"
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
<li>/sdk-for-flutter-navigate-location-locationengine-class</li>
<li class="self-crumb">startWithLocationOptions method</li>
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
<div class="main-content" data-above-sidebar="location/LocationEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>startWithLocationOptions method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-location-locationenginestatus
startWithLocationOptions(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-location-locationoptions-class locationOptions</li>
</ol>)

      <div class="features">override</div>
</section>
<section class="desc markdown">
<p>On Android devices starts the location engine with desired /sdk-for-flutter-navigate-location-locationoptions-class.
Make sure to call either /sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeinclusion or
/sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeexception beforehand.
Returns /sdk-for-flutter-navigate-location-locationenginestatus if /sdk-for-flutter-navigate-location-locationengine-startwithlocationaccuracy or
/sdk-for-flutter-navigate-location-locationengine-startwithlocationoptions is called again without calling /sdk-for-flutter-navigate-location-locationengine-stop in between.
See /sdk-for-flutter-navigate-location-locationenginestatus for other possible return values.</p>
<p>On iOS devices this is not supported and /sdk-for-flutter-navigate-location-locationenginestatus is returned.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LocationEngineStatus startWithLocationOptions(LocationOptions locationOptions) =&gt;
    _location.startWithLocationOptions(locationOptions);</code></pre>
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
<li>/sdk-for-flutter-navigate-location-locationengine-class</li>
<li class="self-crumb">startWithLocationOptions method</li>
</ol>
<h5>LocationEngine class</h5>
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
