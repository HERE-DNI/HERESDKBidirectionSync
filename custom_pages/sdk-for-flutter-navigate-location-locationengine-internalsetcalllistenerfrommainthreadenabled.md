---
title: "internalsetCallListenerFromMainThreadEnabled method"
slug: "sdk-for-flutter-navigate-location-locationengine-internalsetcalllistenerfrommainthreadenabled"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- internalsetCallListenerFromMainThreadEnabled.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-location-locationengine-class</li>
<li class="self-crumb">internalsetCallListenerFromMainThreadEnabled method</li>
</ol>
<div class="self-name">internalsetCallListenerFromMainThreadEnabled</div>
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
<h1>internalsetCallListenerFromMainThreadEnabled method</h1></div>
<section class="multi-line-signature">
void
internalsetCallListenerFromMainThreadEnabled(<wbr/><ol class="parameter-list single-line"> <li>bool enabled</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Enables or disables forcing listener calls to originate from main thread.</p>
<p>When disabled listener calls can originate from any thread.
Defaults to false .</p>
<p>For internal use only.</p>
<ul>
<li><code>enabled</code> The enabled flag.</li>
</ul>
<p>@nodoc</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void internalsetCallListenerFromMainThreadEnabled(bool enabled) =&gt;
    _location.internalsetCallListenerFromMainThreadEnabled(enabled);</code></pre>
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
<li class="self-crumb">internalsetCallListenerFromMainThreadEnabled method</li>
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
